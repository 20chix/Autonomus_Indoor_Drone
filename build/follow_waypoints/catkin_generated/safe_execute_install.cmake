execute_process(COMMAND "/home/hadi/catkin_ws/build/follow_waypoints/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/hadi/catkin_ws/build/follow_waypoints/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
