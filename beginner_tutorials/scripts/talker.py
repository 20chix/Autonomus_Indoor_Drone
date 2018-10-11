#!/usr/bin/env python
import rospy
from std_msgs.msg import String

from dynamic_reconfigure.server import Server
from beginner_tutorials.cfg import GUIConfig


toBePrint = ""
counter_1 = 0
counter_2 = 0
counter_3 = 0

dummy_anchor_0 = "0   0   0"
dummy_anchor_1 = "0   30  0"
dummy_anchor_2 = "30  30  0"
dummy_anchor_3 = "30   0  0"
dummy_tag      = " 0   5  3"

cars = {"dwm1001_network_info": 0 }






def talker():
    global counter_1, counter_2, counter_3
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

        pub_Anchor_0.publish(dummy_anchor_0)
        pub_Anchor_1.publish(dummy_anchor_1)
        pub_Anchor_2.publish(dummy_anchor_2)
        pub_Anchor_3.publish(dummy_anchor_3)
        pub_Tag.publish(     dummy_tag)


        rospy.loginfo("sending dummy values: tag = "+ str(dummy_tag))

        dummy_tag = counter_1 + " " + counter_2 + " " + counter_3

        srv.update_configuration(cars)

        counter_1 = counter_1 + 0.01
        counter_2 = counter_2 + 0.001
        counter_3 = counter_3 + 0.00001

        rate.sleep()


def callback(config, level):
    global toBePrint

    toBePrint = config["serial_port"]

    config["dwm1001_network_info"] = str(counter)

    rospy.loginfo("""Reconfigure Request: {dwm1001_network_info}, {open_port},\ 
          {serial_port}, {close_port}""".format(**config))
    return config



if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
