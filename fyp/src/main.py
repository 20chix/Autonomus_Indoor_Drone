#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def astarCallback(data):
    rospy.loginfo("Astar directions: " +str(data.data))

def talker():
    global counter
    global cars




    rospy.init_node('fyp', anonymous=False)
    # initialize our topics
    pub_RouteN = rospy.Publisher('route_number', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz



    while not rospy.is_shutdown():
        pub_RouteN.publish("2")
        rospy.loginfo("Route 2")
        rate.sleep()

rospy.Subscriber('shortest_path', String, astarCallback)



if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
