# Launch ardupilot simulation only gazebo world
gazebo --verbose ~/catkin_ws/src/ardupilot_gazebo/worlds/iris_arducopter_runway.world

# Launch sim vehicle so ros topics can appear on terminal
/home/hadi/ardupilot/Tools/autotest/sim_vehicle.py --map --console  -v ArduCopter -f gazebo-iris

# roslaunch mavros
roslaunch ardupilotMavros apm.launch