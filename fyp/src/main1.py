

import rospy
import time
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
# Load the DroneController class, which handles interactions with the drone, and the DroneVideoDisplay class, which handles video display
from drone_controller import BasicDroneController


class MoveSquareClass(object):
    def __init__(self):

        self.ctrl_c = False
        self.rate = rospy.Rate(10)

    """"This is because pubblishing in topics sometimes fails the first time you pubblish.
    In continuos pubblishing systems therw is no big deal but in systems that pubblish only once
    it IS very important"""
    def publish_once_in_cmd_vel(self, cmd):

        while not self.ctrl_c:
            connections = self.publish_once_in_cmd_vel.get_num_connections()
            if connections > 0:
                self._pub_cmd_vel.pubblish(cmd)
                rospy.loginfo("Publish in cmd_vel...")
                break
            else:
                self.rate.sleep()


    # function that stops the drone from any movement
    def strop_drone(self):
        rospy.loginfo("Stopping...")
        self._move_msg.linear.x = 0.0
        self._move_msg.angular.z = 0.0
        self.publish_once_in_cmd_vel(self._move_msg)

    #function that makes the drone turn 90 degrees
    def turn_drone(self):
        rospy.loginfo("Turning...")
        self._move_msg.linear.x  = 0.0
        self._move_msg.angular.z = 1.0
        self.publish_once_in_cmd_vel(self._move_msg)

    # function that makes the drone move forward
    def move_forward_drone(self):
        rospy.loginfo("Moving forward...")
        self._move_msg.linear.x  = 1.0
        self._move_msg.angular.z = 0.0
        self.publish_once_in_cmd_vel(self._move_msg)

    def move_square(self):
        # this callback is called when the action server is called.
        # this is the function that computes the Fibonacci sequence
        #and returns the sequence to the node that called the action server

        # helper variable
        r = rospy.Rate(1)

        # define the differen publishers and messages that will be used
        self._pub_cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self._move_msg = Twist()
        self._pub_takeoff = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=1)
        self._takeoff_msg = Empty()
        self._pub_land = rospy.Publisher('/ardrone/land', Empty, queue_size=1)
        self._land_msg = Empty()


        # make the drone takeoff
        i=0
        while not i == 3:
            self._pub_takeoff.publish(self._takeoff_msg)
            rospy.loginfo("Taking off...")
            time.sleep(1)
            i += 1


        # define the seconds to move in each side of the square (which is taken from the goal) and the seconds to turn
        sideSeconds = 2
        turnSeconds = 1.8


        i = 0
        for i in range(0, 4):
            # Logic that makes the robot move forward and turn
            self.move_forward_drone()
            time.sleep(sideSeconds)
            self.turn_drone()
            time.sleep(turnSeconds)

            # the sequence is computed at 1 HZ frequency

        self.strop_drone()
        i=0

        while not i == 3:
            self._pub_land.publish(self._land_msg)
            rospy.loginfo('Landing')
            time.sleep(1)
            i += 1



if __name__ == '__main__':
    # Firstly we setup a ros node, so that we can communicate with the other packages
    rospy.init_node('fyp', anonymous=False)
    # Now we construct our controllers
    controller = BasicDroneController()


    move_square1 = MoveSquareClass()
    try:
        move_square1.move_square()
    except rospy.ROSInterruptException:
        pass









