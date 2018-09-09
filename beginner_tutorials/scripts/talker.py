#!/usr/bin/env python
import rospy
from std_msgs.msg import String

from dynamic_reconfigure.server import Server
from beginner_tutorials.cfg import GUIConfig


toBePrint = ""
counter = 0
cars = {"dwm1001_network_info": 0}






def talker():
    global counter
    global cars




    rospy.init_node('DWM1001_API', anonymous=False)


    # initialize our topics
    pub_Network  = rospy.Publisher('DWM1001_Network',          String, queue_size=10)
    pub_Anchor_0 = rospy.Publisher('DWM1001_Network_Anchor_0', String, queue_size=10)
    pub_Anchor_1 = rospy.Publisher('DWM1001_Network_Anchor_1', String, queue_size=10)
    pub_Anchor_2 = rospy.Publisher('DWM1001_Network_Anchor_2', String, queue_size=10)
    pub_Tag      = rospy.Publisher('DWM1001_Network_Tag',      String, queue_size=10)


    srv = Server(GUIConfig, callback)
    rate = rospy.Rate(10) # 10hz
    counter = 0

    while not rospy.is_shutdown():


        #cars.update({"dwm1001_network_info" : str(counter)})

        pub_Anchor_0.publish("0  0  0")
        pub_Anchor_1.publish("1  1  1")
        pub_Anchor_2.publish("2  2  2")
        pub_Tag.publish("5  5  5")


        rospy.loginfo("0  0  0")


        srv.update_configuration(cars)

        counter = counter + 1
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
