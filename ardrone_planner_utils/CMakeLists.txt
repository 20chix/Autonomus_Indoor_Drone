cmake_minimum_required(VERSION 2.8.3)
project(ardrone_planner_utils)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS_RELEASE} -std=c++0x -O3")
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS_DEBUG} -std=c++0x")#for debug


find_package(catkin REQUIRED COMPONENTS 
             roslib 
             roscpp 
             std_msgs 
             geometry_msgs 
             sensor_msgs
             tf
             )

include_directories(
    ${catkin_INCLUDE_DIRS} 
    include 
    include/kdtree
    )

catkin_package(
  INCLUDE_DIRS include 
  CATKIN_DEPENDS roscpp std_msgs
  )
  
add_executable(collision_detection_node src/collision_detection.cpp)

target_link_libraries(collision_detection_node ${catkin_LIBRARIES})
