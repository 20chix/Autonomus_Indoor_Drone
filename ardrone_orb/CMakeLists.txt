cmake_minimum_required(VERSION 2.8.3)
project(ardrone_orb)

#Compiler options
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS_RELEASE} -std=c++0x -O3")
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS_DEBUG} -std=c++0x")#for debug

#Set a variable for the orb_slam path
set(ORB_DIR ${PROJECT_SOURCE_DIR}/../ORB_SLAM2)

########### Normal catkin stuff #################
find_package(catkin REQUIRED COMPONENTS
  roslib
  roscpp
  std_msgs
  geometry_msgs
  tf
  message_generation
  cv_bridge
  image_transport
)

find_package(Pangolin REQUIRED)
find_package(${ORB_SLAM} REQUIRED)

find_package(OpenCV 3.2)
if(NOT OpenCV_FOUND)
  message("Open CV 3 not found")
   find_package(OpenCV 2.4.3)
   if(NOT OpenCV_FOUND)
      message(FATAL_ERROR "OpenCV > 2.4.3 not found.")
   endif()
endif()

catkin_package(
  CATKIN_DEPENDS roscpp
  roslib
  std_msgs
  geometry_msgs
  tf
  cv_bridge
  image_transport
  message_runtime
)

include_directories(
${catkin_INCLUDE_DIRS}
${ORB_DIR}
${ORB_DIR}/include
${Pangolin_INCLUDE_DIRS}
)

set(LIBS
${OpenCV_LIBS}
${EIGEN3_LIBS}
${Pangolin_LIBRARIES}
${ORB_SLAM}
${ORB_DIR}/Thirdparty/DBoW2/lib/libDBoW2.so
${ORB_DIR}/Thirdparty/g2o/lib/libg2o.so
${ORB_DIR}/lib/libORB_SLAM2.so
)
###########################################################


get_property(dirs DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY INCLUDE_DIRECTORIES)
foreach(dir ${dirs})
  message(STATUS "dir='${dir}'")
endforeach()

message(STATUS "====================MY_VAR={${ORB_DIR}}==============")

add_executable(ros_orb_node src/ardrone_orb_adapter.cpp)

target_link_libraries(ros_orb_node ${LIBS})
target_link_libraries(ros_orb_node ${catkin_LIBRARIES} )


