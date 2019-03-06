//This is an adaptation of a kdtree implementation written by Valerio Varricchio

#ifndef KDTREE_H_
#define KDTREE_H_

#include <memory>
#include <utility>
#include <vector>
#include <chrono>
#include <algorithm>
#include <set>
#include <queue>
#include <cstdio>
#include <unistd.h>
#include <ostream>
#include "kdtree_utils.h"

static int x = 0;
void test()
{
  x++;
  std::cout << "test " << x << std::endl;
}

namespace kdtree{
  
  class Vertex
  {
  public:
    
    point coord;
    point normal;
    
    size_t depth;
    size_t id;
    
    // Tree pointers
    std::shared_ptr<Vertex> parent;
    std::shared_ptr<Vertex> children[2];
    
    Vertex(const point& _coord):coord(_coord),normal(coord.size()){}
    Vertex(const point& _coord, const point& _normal):coord(_coord),normal(_normal){}
    ~Vertex(){}
    
    bool isLeaf(){
      return !(children[0].get() || children[1].get());
    }
    
    bool isRoot(){
      return !parent.get();
    }
    
    bool operator<(const Vertex& b) const{
      return std::lexicographical_compare(std::begin(coord),std::end(coord),std::begin(b.coord),std::end(b.coord));
    }
  };
  typedef std::shared_ptr<Vertex> vertexPtr;
  
  template <class vertexPtr, class numT>
  struct query_node
  {
    numT score;
    vertexPtr vtx_ptr;
    
    query_node(){return;}
    query_node(const numT& _score, const vertexPtr& _vtx_ptr):score(_score),vtx_ptr(_vtx_ptr){}
    
    bool operator<(const query_node& b) const{
      return  b.score > score;//Other way?
    }
  };
  
  template <class vertexPtr, class numT>
  class query_queue
  {
    numT queue_score;
  public:
    int query_size;
    std::priority_queue< query_node<vertexPtr,numT> > queue;
    
    query_queue():query_size(1),queue_score(0.0){}
    
    void set_size(int size){
      query_size=size;
    }
    
    numT get_score()
    {
      if(queue.size()<query_size)
      {
        return std::numeric_limits<numT>::max();
      }
      return queue_score;            
    }
    void insert(numT score, vertexPtr v)
    {
      query_node<vertexPtr,numT> newnode(score, v);
      queue.push(newnode);
      if(queue.size()>query_size)
      {
        queue.pop();
      }
      queue_score = queue.top().score;
      return;
    }
    void clear()
    {
      queue=std::priority_queue< query_node<vertexPtr,numT> >();
    }
    
  };
  
  template <class vertexPtr, class numT>
  struct query_results {
    point querypoint;
    query_queue<vertexPtr,numT> BPQ;
    int depth;
  };
  
  class Kdtree{
    
    bool inPositiveHalfspace(const point& center, const point &pivot, const point& n) const{
      return innerProduct(center-pivot, n)>0;
    }
    bool ballHyperplane(const point& center, const numT& radius, const point& pivot, const point& n){
      d_count++;
      return fabs( innerProduct(center-pivot, n) )<=radius;
    }
    void addChild(vertexPtr parent, vertexPtr child, bool which){
      parent->children[which] = child;
      child->parent = parent;
      child->depth = parent->depth+1;
      tree_depth=std::max((int)tree_depth,(int)child->depth);
    }
    void descend(point& coord, vertexPtr& parent_o, bool& side_o) const {
      descend(coord, root, parent_o, side_o);
    }
    void descend(point& x, const vertexPtr& node, vertexPtr& parent_o, bool& side_o) const {
      bool which = inPositiveHalfspace(x, node->coord, node->normal);
      if(!node->children[which].get()){
        parent_o = node;
        side_o = which;
        return;
      }
      descend(x, node->children[which], parent_o, side_o);
    }
    
    vertexPtr root;
    unsigned int tree_dimension, tree_size, tree_depth;
    unsigned int d_count;
  public:
    
    //         Kdtree():d_count(0),tree_size(0),tree_depth(0){}
    Kdtree(const int& _dimension):d_count(0),tree_size(0),tree_depth(0),tree_dimension(_dimension){}
    bool isEmpty(){
      if (!root.get())
        return true;
      return false;
    }
    void insert(vertexPtr& v){
      //If root is null 
      if(!root.get()){
        point node_normal(0.0,tree_dimension);
        node_normal[0]=1.0;
        v->normal=node_normal;
        root = v; 
        assert(v->coord.size() == tree_dimension);
        tree_size++;
      }
      else{
        vertexPtr parent; bool side;
        descend(v->coord, parent, side);
        point node_normal(0.0,tree_dimension);
        node_normal[(parent->depth+1)%tree_dimension]=1.0;
        v->normal=node_normal;
        
        vertexPtr child = v;
        addChild(parent, child, side);
        tree_size++;
      }
    }
    query_results<vertexPtr,numT> query(const point& qp, size_t k){
      query_results<vertexPtr,numT> R;
      
      if(!root.get()){return R;}
      
      R.depth=0;
      //R.querypoint = qp;//TODO necessary?
      R.BPQ.clear();
      R.BPQ.set_size(k);
      query(qp, root, R);      
      return R;
    }
    void query(const point& qp, vertexPtr& current, query_results<vertexPtr,numT>& R){ 
      if(not root.get())
        return;
      
      bool side = inPositiveHalfspace(qp, current->coord, current->normal);
      
      if(current->children[side].get())
      {
        R.depth++;
        query(qp, current->children[side], R);
      }
      
      numT point_score = norm2(qp-current->coord);
      R.BPQ.insert(point_score, current);
      
      if(ballHyperplane(qp, R.BPQ.get_score(), current->coord, current->normal)){
        if(current->children[1-side].get()){
          query(qp, current->children[1-side], R);
        }
      }
    }
    
    struct BucketRef{
      unsigned int start,end,depth;
      BucketRef(int _start, int _end, int _depth):start(_start),end(_end),depth(_depth){}
      bool operator<(const BucketRef& half_data){
        return depth > half_data.depth;//Check order
      }
    };
    typedef std::shared_ptr<BucketRef> bucketPtr;
    
    void batchBuild(std::vector<vertexPtr>& data){
      //If dataset is empty, build is done
      if(data.size()==0){return;}
      //Stack for recursive build
      std::deque<bucketPtr> bucketRefs;
      bucketPtr rootData(new BucketRef(0,data.size()-1,0));
      bucketRefs.push_back(rootData);
      while(bucketRefs.size()>0){
        bucketPtr current = bucketRefs.front();
        bucketRefs.pop_front();
        int d = (current->depth)%tree_dimension;
        std::sort(data.begin()+current->start, data.begin()+current->end, [d](vertexPtr a, vertexPtr b) {return a->coord[d] < b->coord[d];});
        if(current->end - current->start<2){
          insert(data[current->start]);
          if(current->start<current->end){
            insert(data[current->end]);
          }
        }
        else{
          int median = current->start + (current->end - current->start)/2;
          insert(data[median]);
          bucketPtr left_children(new BucketRef(current->start,median - 1,current->depth+1));//add the right child
          bucketPtr right_children(new BucketRef(median+1,current->end,current->depth+1));//add the right child
          
          bucketRefs.push_back(left_children);
          bucketRefs.push_back(right_children);
        }
      } 
    }
    unsigned int size(){return tree_size;}
    unsigned int dimension()
    {
      assert(tree_dimension == 3 );//TODO remove later -- debugging line
      return tree_dimension;
      
    }
    unsigned int depth(){return tree_depth;}
  };
}


#endif