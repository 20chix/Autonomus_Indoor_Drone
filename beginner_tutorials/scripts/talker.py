#!/usr/bin/env python




import rospy
from std_msgs.msg import String

from dynamic_reconfigure.server import Server
from beginner_tutorials.cfg import GUIConfig


toBePrint = ""
def talker():





    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    srv = Server(GUIConfig, callback)
    rate = rospy.Rate(10) # 10hz


    while not rospy.is_shutdown():

        rospy.loginfo(toBePrint)
        pub.publish(toBePrint)
        rate.sleep()


def callback(config, level):
    global toBePrint

    toBePrint = config["str_param"]

    rospy.loginfo("""Reconfigure Request: {int_param}, {double_param},\ 
          {str_param}, {bool_param}, {size}""".format(**config))
    return config

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
