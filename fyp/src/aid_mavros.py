#!/usr/bin/env python
import rospy
import numpy as np
import math
import mavros_msgs

from geometry_msgs.msg import PoseStamped, TwistStamped
from mavros_msgs import srv
from mavros_msgs.msg import State

#=================Parameter Initializaiton========================
goal_pose = PoseStamped()
current_pose = PoseStamped()
set_velocity = TwistStamped()
current_state = State()


def altitude_hold():
    global goal_pose
    goal_pose.pose.position.z = 2

#==============Call Back Functions=====================
def pos_sub_callback(pose_sub_data):
    global current_pose
    current_pose = pose_sub_data

def state_callback(state_data):
    global current_state
    current_state = state_data

#============Intialize Node, Publishers and Subscribers=================
rospy.init_node('Vel_Control_Node', anonymous = True)
rate = rospy.Rate(10) #publish at 10 Hz
local_position_subscribe = rospy.Subscriber('/mavros/local_position/pose', PoseStamped, pos_sub_callback)
local_position_pub = rospy.Publisher('/mavros/setpoint_position/local', PoseStamped, queue_size = 10)
setpoint_velocity_pub = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel',TwistStamped, queue_size = 10)
state_status_subscribe = rospy.Subscriber('/mavros/state',State,state_callback)
altitude_hold()


#============Define Velocity==============================================
set_velocity.twist.linear.x = +1 #moving 1m/s at x direction


while not rospy.is_shutdown():
    local_position_pub.publish(goal_pose)

    if current_state.mode != "OFFBOARD" or not current_state.armed:
        clear_mission =  rospy.ServiceProxy('/mavros/mission/clear', mavros_msgs.srv.CommandBool)
        clear_mission(True)
        arm = rospy.ServiceProxy('/mavros/cmd/arming', mavros_msgs.srv.CommandBool)
        arm(True)
        set_mode = rospy.ServiceProxy('/mavros/set_mode',mavros_msgs.srv.SetMode)
        mode = set_mode(custom_mode = 'OFFBOARD')
        rospy.loginfo(mode)
        if mode:
            rospy.loginfo('Switched to OFFBOARD mode!')

    setpoint_velocity_pub.publish(set_velocity)


    rate.sleep()