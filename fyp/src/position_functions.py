# Libraries
import roslib;

#roslib.load_manifest('ardrone_interface')
import rospy
#import pygame
import std_srvs.srv
import time
from subprocess import Popen
#from pygame.locals import *
from std_msgs.msg import *
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
import time
from ardrone_autonomy.msg import Navdata  # for receiving navdata feedback
# An enumeration of Drone Statuses
from drone_status import DroneStatus
import pid
from std_msgs.msg import Empty

c_max_critical_time = 3
c_min_critical_time = 0.2


class DroneMaster:
    def __init__(self):

        # ROS Settings
        self.publisher_land = rospy.Publisher('/ardrone/land', Empty)
        self.publisher_takeOff = rospy.Publisher('/ardrone/takeoff', Empty)
        self.publisher_reset = rospy.Publisher('/ardrone/reset',
                                               Empty)  # edited by Ardillo make a reset possible after over-tilt
        self.publisher_parameters = rospy.Publisher('/cmd_vel', Twist)
        # self.subscriber_camera_front  = rospy.Subscriber( '/ardrone/front/image_raw',  Image, self.__callback ) # Front image
        # self.subscriber_camera_bottom = rospy.Subscriber( '/ardrone/bottom/image_raw', Image, self.__callback ) # Bottom image
        # self.subscriber_tracker       = rospy.Subscriber( '/tld_tracked_object', BoundingBox, self.__callback_tracker ) # Tracker

        # Subscribe to the /ardrone/navdata topic, of message type navdata, and call self.ReceiveNavdata when a message is received
        self.subNavdata = rospy.Subscriber('/ardrone/navdata', Navdata, self.ReceiveNavdata)
        self.status = -1
        self.parameters = Twist()
        self.speed = 0.4
        self.airborne = False
        self.max_critical_time = 3  # sec
        self.min_critical_time = 0.2  # sec
        self.vx = self.vy = self.vz = self.ax = self.ay = self.az = 0.0
        self.x = self.y = self.z = self.alfa = self.betta = self.gamma = 0.0
        # gain_p, gain_i, gain_d
        self.linearxpid = pid.Pid2(0.5, 0.0, 0.5)
        self.linearypid = pid.Pid2(0.5, 0.0, 0.5)
        self.last_time = None
        self.dt = 0.0

    def ReceiveNavdata(self, navdata):
        # Although there is a lot of data in this packet, we're only interested in the state at the moment
        self.status = navdata.state
        self.vx = navdata.vx / 1e3
        self.vy = navdata.vy / 1e3
        self.vz = navdata.vz / 1e3
        if self.last_time == None:
            self.last_time = rospy.Time.now()
            self.dt = 0.0
        else:
            now_time = rospy.Time.now()
            self.dt = (now_time - self.last_time).to_sec()
            self.last_time = now_time
        self.x = self.x + self.vx * self.dt
        self.y = self.y + self.vy * self.dt
        self.z = self.z + self.vz * self.dt
        rospy.loginfo(
        'ReceiveNavdata x=' + str(round(self.x, 3)) + '; y=' + str(round(self.y, 3)) + '; z=' + str(round(self.z, 3)))

    def getStatus(self):
        return self.status

    def takeoff(self, distance, a_timeout=0):
        self.publisher_takeOff.publish(Empty())
        self.airborne = True

    def land(self):
        self.publisher_land.publish(Empty())
        self.airborne = False

    def reset(self):
        self.publisher_reset.publish(Empty())
        self.airborne = False

    def goTo(self, x, y, z, dt):
        self.clear()
        while abs(x - self.x) > 0.05 or abs(y - self.y) > 0.05 or abs(z - self.z) > 0.05:
            self.parameters.linear.x = (x - self.x) / 10
            self.parameters.linear.y = (y - self.y) / 10
            self.parameters.linear.z = (z - self.z) / 10
            self.publisher_parameters.publish(self.parameters)
            rospy.loginfo(
            'goTo x=' + str(round(self.x, 3)) + '; y=' + str(round(self.y, 3)) + '; z=' + str(round(self.z, 3)))
            time.sleep(dt)

    def move_right(self, distance, a_timeout=0):
        self.parameters.linear.y = self.linearypid.update(-self.speed, self.vy, 0.0, self.dt)
        self.publisher_parameters.publish(self.parameters)
        time.sleep(a_timeout)

    def move_left(self, distance, a_timeout=0):
        self.parameters.linear.y = self.linearypid.update(self.speed, self.vy, 0.0, self.dt)
        self.publisher_parameters.publish(self.parameters)
        time.sleep(a_timeout)

    def move_forward(self, distance, a_timeout=0):
        self.parameters.linear.x = self.linearxpid.update(self.speed, self.vx, 0.0, self.dt)
        self.publisher_parameters.publish(self.parameters)
        time.sleep(a_timeout)

    def move_backward(self, distance, a_timeout=0):
        self.parameters.linear.x = self.linearxpid.update(-self.speed, self.vx, 0.0, self.dt)
        self.publisher_parameters.publish(self.parameters)
        time.sleep(a_timeout)

    def move_up(self, distance, a_timeout=0):
        self.parameters.linear.z = self.speed
        self.publisher_parameters.publish(self.parameters)
        time.sleep(a_timeout)

    def move_down(self, distance, a_timeout=0):
        self.parameters.linear.z = -self.speed
        self.publisher_parameters.publish(self.parameters)
        time.sleep(a_timeout)

    def yaw_left(self, speed, a_time):
        self.parameters.angular.z = self.speed
        self.publisher_parameters.publish(self.parameters)
        time.sleep(a_time)

    def yaw_right(self, speed, a_time):
        self.parameters.angular.z = -self.speed
        self.publisher_parameters.publish(self.parameters)
        time.sleep(a_time)

    def move_left_right(self, distance, a_timeout=0):
        self.move_left(distance, a_timeout / 3)
        self.move_right(distance, 2 * a_timeout / 3)

    def move_right_left(self, distance, a_timeout=0):
        self.move_right(distance, a_timeout / 3)
        self.move_left(distance, 2 * a_timeout / 3)

    def move_up_down(self, distance, a_timeout=0):
        self.move_up(distance, a_timeout / 3)
        self.move_down(distance, 2 * a_timeout / 3)

    def move_down_up(self, distance, a_timeout=0):
        self.move_down(distance, a_timeout / 3)
        self.move_up(distance, 2 * a_timeout / 3)

    def move_yaw_left_right(self, speed, a_timeout=0):
        self.yaw_left(speed, a_timeout / 3)
        self.yaw_right(speed, 2 * a_timeout / 3)

    def move_yaw_right_left(self, speed, a_timeout=0):
        self.yaw_right(speed, a_timeout / 3)
        self.yaw_left(speed, 2 * a_timeout / 3)

    def stream(self, method_name, par1=1, par2=0.3):
        method = getattr(self, method_name)
        return method(par1, par2)

    def clear(self):
        self.parameters.linear.x = 0
        self.parameters.linear.y = 0
        self.parameters.linear.z = 0
        self.parameters.angular.x = 0
        self.parameters.angular.y = 0
        self.parameters.angular.z = 0
#		self.publisher_parameters.publish( self.parameters )