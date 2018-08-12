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




    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    srv = Server(GUIConfig, callback)
    rate = rospy.Rate(10) # 10hz
    counter = 0

    while not rospy.is_shutdown():


        cars.update({"dwm1001_network_info" : str(counter)})


        rospy.loginfo(toBePrint)


        srv.update_configuration(cars)

        counter = counter + 1
        pub.publish(str(toBePrint))
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
