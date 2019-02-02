#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import math


from dynamic_reconfigure.server import Server
from beginner_tutorials.cfg import GUIConfig


toBePrint = ""
counter_x = 0
counter_y = 0
counter_z = 0

angle = 0

dummy_anchor_0 = "0   0   0"
dummy_anchor_1 = "0   30  0"
dummy_anchor_2 = "30  30  0"
dummy_anchor_3 = "30   0  0"
dummy_tag      = " 0   0  3"

cars = {"dwm1001_network_info": 0 }






def talker():
    global counter_x, counter_y, counter_z, dummy_tag, angle
    global cars
    
    # initialize node
    rospy.init_node('DWM1001_API', anonymous=False)

    # initialize our topics
    pub_Network  = rospy.Publisher('DWM1001_Network',          String, queue_size=10)
    pub_Anchor_0 = rospy.Publisher('DWM1001_Network_Anchor_0', String, queue_size=10)
    pub_Anchor_1 = rospy.Publisher('DWM1001_Network_Anchor_1', String, queue_size=10)
    pub_Anchor_2 = rospy.Publisher('DWM1001_Network_Anchor_2', String, queue_size=10)
    pub_Anchor_3 = rospy.Publisher('DWM1001_Network_Anchor_3', String, queue_size=10)
    pub_Tag      = rospy.Publisher('DWM1001_Network_Tag',      String, queue_size=10)


    srv = Server(GUIConfig, callback)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():

        coordinates_tag = dummy_tag.split()
        coordinates_anchor_0 = dummy_anchor_0.split()

        inc_x = int(float(coordinates_tag[0]) -  float(coordinates_anchor_0[0]))
        inc_y = int(float(coordinates_tag[1]) -  float(coordinates_anchor_0[1]))

        angle_to_goal = math.atan2(inc_y, inc_x)


        #radius = 15
        #theta = math.radians(angle)
        #counter_y = radius * math.cos(theta) + 0
        #counter_x = radius * math.sin(theta) + 0


        #angle = angle + 1

       # if angle > 360:
        #    angle = 0


        dummy_tag = str(counter_x) + " " + str(counter_y) + " " + str(counter_z)
        rospy.loginfo("sending dummy values: tag = "+ str(dummy_tag))

        pub_Anchor_0.publish(dummy_anchor_0)
        pub_Anchor_1.publish(dummy_anchor_1)
        pub_Anchor_2.publish(dummy_anchor_2)
        pub_Anchor_3.publish(dummy_anchor_3)
        pub_Tag.publish(     dummy_tag)


        srv.update_configuration(cars)




        #if counter_y > 26:
        #    counter_x = counter_x + 0.3

        #if counter_y > 30:
        #    counter_y = 30
        
        #if counter_x > 26:
        #    counter_y = counter_y - 0.3

        #if counter_y < 26:
        #    counter_y = counter_y + 0.3
            #hi


        counter_y = counter_y + 0.01
        #counter_2 = counter_2 + 0.001
        #counter_3 = counter_3 + 0.00001

        rate.sleep()


def callback(config, level):
    global toBePrint

    toBePrint = config["serial_port"]

    config["dwm1001_network_info"] = str(counter_x)

    rospy.loginfo("""Reconfigure Request: {dwm1001_network_info}, {open_port},\ 
          {serial_port}, {close_port}""".format(**config))
    return config



if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
