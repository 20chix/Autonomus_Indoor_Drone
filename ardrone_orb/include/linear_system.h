/*
Copyright 2017 Brian Paden

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

#ifndef LINEAR_SYSTEM_H
#define LINEAR_SYSTEM_H
#include<cmath>
#include<stdio.h>
#include<iostream>
#include<vector>
#include<valarray>
#include<deque>

namespace LTI{
  typedef std::valarray<double> array;
  
  //Simple polynomial object over reals
  class Polynomial{
  public:
    array coeffs;
    
    //p(s)=coeffs[0]+coeffs[1]s+coeffs[2]s^2+...+coeffs[n]s^n
    Polynomial(){}
    Polynomial(const array& _coeffs):coeffs(_coeffs){}
    Polynomial(const int& degree):coeffs(degree){}
    
    int degree(){return coeffs.size();}
    
    //Evaluate polynomial at real number s
    double operator()(const double& s){
      double out(0);
      for(int i=0;i<coeffs.size();i++){
        out+= coeffs[i]*pow(s,i);
      }
      return out;
    }
  };  
  
  Polynomial operator*(const Polynomial& p, const Polynomial& q){
    Polynomial out( p.coeffs.size()+q.coeffs.size()-1);
    for(int i=0;i<q.coeffs.size();i++){
      for(int j=0;j<p.coeffs.size();j++){
        out.coeffs[(i+j)] += (q.coeffs[i])*(p.coeffs[j]);
      }
    }
    return out;
  }
  
  Polynomial operator*(const double& c, const Polynomial& p){
    Polynomial out=p;
    for(int i=0;i<p.coeffs.size();i++){
      out.coeffs[i]*=c;
    }
    return out;
  }
  
  Polynomial operator+(const Polynomial& p, const Polynomial& q){
    Polynomial out(std::max(p.coeffs.size(),q.coeffs.size()));
    for(int i=0;i<std::min(p.coeffs.size(),q.coeffs.size());i++){
      out.coeffs[i]=p.coeffs[i]+q.coeffs[i];
    }
    return out;
  }
  
  Polynomial operator-(const Polynomial& q, const Polynomial& p){
    Polynomial out(std::max(p.coeffs.size(),q.coeffs.size()));
    for(int i=0;i<p.coeffs.size();i++){
      if(i<=q.coeffs.size()){out.coeffs[i] = q.coeffs[i]-p.coeffs[i];}
      else{out.coeffs[i] = -(double)(p.coeffs[i]);}
    }
    return out;
  }
  
  void printPolynomial(const Polynomial& p){
    std::cout << "Polynomial: ";
    for(int i=0;i<p.coeffs.size();i++){ std::cout << p.coeffs[i] << ","; }
    std::cout << std::endl;
    
  }
  
  //CT-LTI-SISO system that is updated based on (input,time) pairs. zero order hold.
  //denominator[0]y(s)+denominator[1]y'(s)+...+denominator[k]y^(k)(s) = numerator[0]u(x)+...
  class SisoSystem{
  public:
    Polynomial num;
    Polynomial den;
    array state;//Controllable canonical form realization
    double input;
    double output;
    double time=0;
    double max_time_step;
    
    
    /* Provide the numerator and denominator of the transfer function and the time of the first time time 
     *  y(s)/u(s) = (num[0]+num[1]s+...+num[m]s^m)/(den[0]+den[1]s+...+den[n]s^n) */
    SisoSystem(){}
    SisoSystem(const array& _num, const array& _den, const double& t_0, const double& _max_time_step) : num(_num), den(_den), state(0.0,_den.size()-1), time(t_0),output(0.0),max_time_step(_max_time_step),input(0.0){
      
      //Put into canonical form
      if(_den.size()<2){
        printf ("\n ERROR: Trying to create a static system\n");
        exit (EXIT_FAILURE);
      }
      if(_den.size()<=_num.size())
      {
        printf ("\n ERROR: Trying to create an non-strictly proper transfer function\n");
        exit (EXIT_FAILURE);
      }
      
      num = (1.0/(den.coeffs[_den.size()-1]))*num;
      den = (1.0/(den.coeffs[_den.size()-1]))*den;
      
    }
    
    //This updates the system when a new input is recieved
    void timeStep(const double& t_now, const double& u_now){
      
      if(t_now < time){printf("WARNING: time request is in the past \n");}
      if(t_now==time){return;}
      
      //stuff for numerical integration
      double num_steps=ceil((t_now-time)/max_time_step);
      double dt=(t_now-time)/num_steps;
      //Euler integration on controllable canonical form with first order hold
      for(int j=0;j<num_steps;j++){
        //x[k+1] = x[k] + (A*dt)x[k]
        for(int i=0;i<(state.size()-1);i++){
          state[i] += dt*state[i+1];
        }
        for(int i=0;i<state.size();i++){
          state[state.size()-1] = state[state.size()-1] - dt*( (state[i])*(den.coeffs[i])); 
        }
        state[state.size()-1] += dt*(u_now*j+(num_steps-j)*input)/num_steps;
      }
      output=0;
      for(int i=0;i<state.size();i++){
        output+=num.coeffs[i]*state[i];
      }
      
      time=t_now;
      input = u_now;
    }
    
    //Steps the system up to q_time from internal state time assuming last input
    double getOutput(const double& q_time){
      timeStep(q_time, input);
      return output;
    }
    
    double getTime(){return time;}
    
    void printState(){
      std::cout << "State: (";
      for(int i=0;i<state.size();i++){
        std::cout << state[i] << ",";
      }
      std::cout << ")" << std::endl;
      std::cout << "Time: " << time << std::endl;
    }  
    void printOutput(){
      std::cout << "output " << output << std::endl;
    }
    
  };
  
  SisoSystem operator*(const SisoSystem& sys1, const SisoSystem& sys2){
    Polynomial num = sys1.num*sys2.num;
    Polynomial den = sys1.den*sys2.den;
    return SisoSystem(num.coeffs, den.coeffs, sys1.time, std::min(sys1.max_time_step,sys2.max_time_step));
  }
  
  SisoSystem operator*(const double& c, const SisoSystem& sys){
    return SisoSystem(c*sys.num.coeffs, sys.den.coeffs, sys.time, sys.max_time_step);
  }
  
  SisoSystem operator/(const SisoSystem& sys1, const SisoSystem& sys2){
    Polynomial num = sys1.num*sys2.den;
    Polynomial den = sys1.num*sys2.den;
    return SisoSystem(num.coeffs, den.coeffs, sys1.time, std::min(sys1.max_time_step,sys2.max_time_step));
  }
  
}

#endif
