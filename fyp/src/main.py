#!/usr/bin/env python


import roslib
import rospy
# Import the joystick message
from sensor_msgs.msg import Joy
import time
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
# An enumeration of Drone Statuses
from drone_status import DroneStatus
import position_functions as pf

# Load the DroneController class, which handles interactions with the drone, and the DroneVideoDisplay class, which handles video display
from drone_controller import BasicDroneController

# define the default mapping between joystick buttons and their corresponding actions of autonomus flight
AutonomousFlight 		= 11
StopAutonomousFlight    = 7
EmergencyStop           = 6


ctrl_c = False


command = Twist()

# -linear.x: move backward
# +linear.x: move forward
# -linear.y: move right
# +linear.y: move left
# -linear.z: move down
# +linear.z: move up
# -angular.z: turn right
# +angular.z: turn left


""""This is because pubblishing in topics sometimes fails the first time you pubblish.
In continuos pubblishing systems therw is no big deal but in systems that pubblish only once
it IS very important"""
def publish_once_in_cmd_vel( cmd):

    while not ctrl_c:
        connections = controller.pubCommand.get_num_connections()
        if connections > 0:
            controller.pubCommand.publish(cmd)
            rospy.loginfo("Publish in cmd_vel...")
            break
        else:
           rate.sleep()


# function that stops the drone from any movement
def strop_drone():
    rospy.loginfo("Stopping...")
    command.linear.x = 0.0
    command.angular.z = 0.0
    publish_once_in_cmd_vel(command)
    rospy.loginfo("Command ..." + str(command.linear))

#function that makes the drone turn 90 degrees
def turn_drone():
    rospy.loginfo("Turning...")
    command.linear.x  = 0.0
    command.angular.z = 1.0
    publish_once_in_cmd_vel(command)
    rospy.loginfo("Command ..." + str(command.angular))

# function that makes the drone move forward
def move_forward_drone():
    rospy.loginfo("Moving forward...")
    command.linear.x  = 1.0
    command.angular.z = 0.0
    publish_once_in_cmd_vel(command)
    rospy.loginfo("Command ..." + str(command.linear))

def move_square():
    # this callback is called when the action server is called.
    # this is the function that computes the Fibonacci sequence
    #and returns the sequence to the node that called the action server




    # make the drone takeoff
    i=0
    while not i == 3:
        controller.SendTakeoff()
        rospy.loginfo("Taking off...")
        time.sleep(1)
        i += 1


    # define the seconds to move in each side of the square (which is taken from the goal) and the seconds to turn
    sideSeconds = 2
    turnSeconds = 1.8


    i = 0
    for i in range(0, 4):
        # Logic that makes the robot move forward and turn
        move_forward_drone()
        time.sleep(sideSeconds)
        turn_drone()
        time.sleep(turnSeconds)
        rospy.loginfo("loops " + str(i))

        # the sequence is computed at 1 HZ frequency

    strop_drone()
    i=0

    while not i == 3:
        controller.SendLand()
        rospy.loginfo('Landing')
        time.sleep(1)
        i += 1



# Button 6 is when we start autonomus flight, GOOD LUCK!!!
def ReceiveJoystickMessage(data):
    global pitch

    if data.buttons[AutonomousFlight] == 1:
        rospy.loginfo("STARTING Autonomous Flight, button " + str(AutonomousFlight) + " pressed!")

        move_square()


    elif data.buttons[StopAutonomousFlight] == 1:
        rospy.loginfo("STOPPING Autonomous Flight, button " + str(AutonomousFlight) + " pressed!")
        controller.SendLand()
    elif data.buttons[EmergencyStop] == 1:
        rospy.loginfo("EMERGENCY, STOPPING Autonomous Flight, button " + str(AutonomousFlight) + " pressed!")
        controller.SendEmergency()

# Setup the application
if __name__ == '__main__':
    # Firstly we setup a ros node, so that we can communicate with the other packages
    rospy.init_node('fyp', anonymous=False)


    try:
        # Now we construct our controllers
        controller = BasicDroneController()

        # subscribe to the /joy topic and handle messages of type Joy with the function ReceiveJoystickMessage
        subJoystick = rospy.Subscriber('/joy', Joy, ReceiveJoystickMessage)

        rate = rospy.Rate(10)

        rospy.spin()

    except rospy.ROSInterruptException:
        pass

