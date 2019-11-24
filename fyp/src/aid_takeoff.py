#!/usr/bin/env python
import rospy
from mavros_msgs.srv import SetMode
from mavros_msgs.srv import CommandBool
from mavros_msgs.srv import CommandTOL
import time

rospy.loginfo("Setting up ros node")
rospy.init_node('mavros_takeoff_python')
rospy.loginfo("Setting up rate")
rate = rospy.Rate(10)


def start():
    setMode()
    arming()
    takeoff()
    #landing()


def setMode():
    # Set Mode
    rospy.loginfo("Setting Mode")
    rospy.wait_for_service('/mavros/set_mode')
    try:
        change_mode = rospy.ServiceProxy('/mavros/set_mode', SetMode)
        response = change_mode(custom_mode="GUIDED")
        rospy.loginfo(response)
    except rospy.ServiceException as e:
        rospy.loginfo("Set mode failed: %s" %e)

def arming():
    # Arm
    rospy.loginfo("Arming")
    rospy.wait_for_service('/mavros/cmd/arming')
    try:
        arming_cl = rospy.ServiceProxy('/mavros/cmd/arming', CommandBool)
        response = arming_cl(value = True)
        rospy.loginfo("my presonal response "+ str(response))
    except rospy.ServiceException as e:
       rospy.loginfo("Arming failed: %s" %e)


def takeoff():
    # Takeoff
    rospy.loginfo("Taking off")
    rospy.wait_for_service('/mavros/cmd/takeoff')
    try:
        takeoff_cl = rospy.ServiceProxy('/mavros/cmd/takeoff', CommandTOL)
        response = takeoff_cl(altitude=10, latitude=0, longitude=0, min_pitch=0, yaw=0)
        rospy.loginfo(response)
    except rospy.ServiceException as e:
        rospy.loginfo("Takeoff failed: %s" %e)

    rospy.loginfo("Hovering...")
    time.sleep(5)


def landing():

    # Land
    rospy.loginfo("Landing")
    rospy.wait_for_service('/mavros/cmd/land')
    try:
        takeoff_cl = rospy.ServiceProxy('/mavros/cmd/land', CommandTOL)
        response = takeoff_cl(altitude=10, latitude=0, longitude=0, min_pitch=0, yaw=0)
        rospy.loginfo(response)
    except rospy.ServiceException as e:
        rospy.loginfo("Landing failed: %s" %e)

    # Disarm
    rospy.loginfo("Disarming")
    rospy.wait_for_service('/mavros/cmd/arming')
    try:
        arming_cl = rospy.ServiceProxy('/mavros/cmd/arming', CommandBool)
        response = arming_cl(value = False)
        rospy.loginfo(response)
    except rospy.ServiceException as e:
        rospy.loginfo("Disarming failed: %s" %e)



if __name__ == '__main__':
    try:
        start()
    except rospy.ROSInterruptException:
        pass
