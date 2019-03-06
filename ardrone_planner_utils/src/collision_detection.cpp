/*
 * Copyright 2017 Brian Paden
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */


#include <ros/ros.h>
#include <sensor_msgs/PointCloud.h>
#include <kdtree.h>
#include <time.h>

typedef std::valarray<double> vctr;

class Trajectory{
  std::vector<vctr> states;
  std::vector<double> time;
public:
  
  void clear(){
    states.clear();
    time.clear();
  }
  
  void resize(int n){
    states.resize(n);
    time.resize(n);
  }
  
  void reserve(int n){
    states.reserve(n);
    time.reserve(n);
  }
  
  void push(const Trajectory& tail){
    //states.reserve(states.size()+tail.states.size());
    states.insert(states.end(), tail.states.begin(), tail.states.end() );
    //time.reserve(time.size()+tail.time.size());
    time.insert(time.end(), tail.time.begin(), tail.time.end() );
  }
  
  void pop_back(){
    states.pop_back();
    time.pop_back();
    //return;
  }
  
  //get last element
  void back(vctr& x, double& t) {
    x=states.back();
    t=time.back();
  }
  
  int size() const{
    return time.size();
  }
  
  void get(int index, vctr& x, double& t) const{
    x=states[index];
    t=time[index];
  }
  const vctr& getState(int index) const{
    return states[index];
  }
  
  void set(int index, const vctr& x, double t) {
    states[index]=x;
    time[index]=t;
  }
  
  void push_back(const vctr& x, const double t){
    states.push_back(x);
    time.push_back(t);
  }
  const double& getTime(int index) const{
    return time[index];
  }
  
  double getDuration() const {
    return time.back() - time.front();
  }
  
  double getEndTime() const {
    return time.back();
  }
  
  double getDurationFrom(int index) const {
    return time.back() - time.at(index);
  }
};


class Obstacles{
public:
  int collision_counter=0;
  //check pointwise for collision    
  virtual bool collisionFree(const Trajectory& x, int* last=NULL){ 
    for(int i=0;i<x.size();i++) {
      if(not collisionFree(x.getState(i), x.getTime(i))){
        if(last)
          *last = i;
        return false;
      }
    }
    return true;
  }
  
  virtual bool collisionFree(const vctr& x, const double& t)=0;
};

class PointCloudEnvironment : public Obstacles
{
    kdtree::Kdtree* kdtree;
    const int dimension = 3;
    const double radius  = 0.2;//20cm radius around quadrotor
    
public:
    //The pointcloud is 3D 
    void updatePointCloud(const sensor_msgs::PointCloud& new_point_cloud){
        std::cout << "Received new point cloud of size " << new_point_cloud.points.size() << " from ORB-SLAM" << std::endl;
        //rebuild kdtree for each new point cloud
        if(kdtree!=nullptr)
            delete kdtree;
        kdtree = new kdtree::Kdtree(3);
        //incremental build of kdtree
        clock_t t = clock();
        
        std::vector<kdtree::vertexPtr> data;
        for(int i=0;i<new_point_cloud.points.size();i++)
        {
            
            kdtree::point p({new_point_cloud.points[i].x,
                new_point_cloud.points[i].y,
                new_point_cloud.points[i].z});
            kdtree::vertexPtr vtx(new kdtree::Vertex(p));
            data.push_back(vtx);
        }
            kdtree->batchBuild(data);
        
        std::cout << " Built kdtree in " << ((float)(clock()-t))/CLOCKS_PER_SEC << " seconds " << std::endl;
    }
    bool collisionFree(const vctr& state, const double& t)//TODO state will not have the same dimension as kdtree points
    {
        kdtree::point query_state = state;//TODO this is really inefficient
        query_state.resize(kdtree->dimension());//TODO ... this too
        //Don't query an empty tree
        if(kdtree!=nullptr){
          if(not kdtree->isEmpty()){
                kdtree::query_results<kdtree::vertexPtr, kdtree::numT> nearest = kdtree->query(query_state,1);
                if(kdtree::norm2(nearest.BPQ.queue.top().vtx_ptr->coord - query_state)<radius)
                    return false;
            }
        }
        return true;
    }
    
    bool collisionFree(const Trajectory& x, int* last=NULL){ 
      if(kdtree==nullptr){return true;}
        for(int i=0;i<x.size();i++) {
            if(not collisionFree(x.getState(i), x.getTime(i))){
                if(last)
                    *last = i;
                return false;
            }
        }
        return true;
    }
    
};

int main(int argc, char **argv)
{
    PointCloudEnvironment obstacles;

    ros::init(argc, argv, "collision_detection");
    ros::start();

    ros::NodeHandle node_handle;
    ros::Subscriber point_cloud_sub = node_handle.subscribe("orb/point_cloud", 2, &PointCloudEnvironment::updatePointCloud, &obstacles);

    ros::Rate loop_rate(1.0);
    while(ros::ok()){
      
        ros::spinOnce();
      
        //Time 1,000 collision checking queries
        Trajectory traj;
        vctr x1(3);
        for(int i=1;i<1000;i++){
            x1[0]=fmod(x1[0]+1,8);
            x1[1]=fmod(x1[1]+1,2.73569);
            x1[2]=fmod(x1[2]+1,3.14159);
            traj.push_back(x1,0.0);
        }

        clock_t t=clock();
        
        std::cout << "Collision Free? " << obstacles.collisionFree(traj) << std::endl;
        std::cout << "Checked 1,000 points for collision in " << ((float)(clock()-t))/CLOCKS_PER_SEC << std::endl;

        loop_rate.sleep();
    }
    return 0;
}
