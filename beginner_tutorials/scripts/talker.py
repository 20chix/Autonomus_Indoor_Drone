#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from beginner_tutorials.msg import Anchor
from beginner_tutorials.msg import Tag

def talker():
    pub = rospy.Publisher('/chatter', String, queue_size=10)
    pub_anchor0 = rospy.Publisher('/dwm1001/anchor0', Anchor, queue_size=10)
    pub_anchor1 = rospy.Publisher('/dwm1001/anchor1', Anchor, queue_size=10)
    pub_anchor2 = rospy.Publisher('/dwm1001/anchor2', Anchor, queue_size=10)
    pub_anchor3 = rospy.Publisher('/dwm1001/anchor3', Anchor, queue_size=10)
    pub_tag = rospy.Publisher('/dwm1001/tag', Tag, queue_size=10)

    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    # construct the object for the tag
    tag = Tag(float(5),
              float(5),
              float(2))

    anchor0 = Anchor(str("ID"),
                     float(5.9),
                     float(5.4),
                     float(2.2),
                     float(2.50),)

    anchor1 = Anchor(str("ID2"),
                     float(1.9),
                     float(1.4),
                     float(2.2),
                     float(1.50),)

    anchor2 = Anchor(str("ID3"),
                     float(1.9),
                     float(1.4),
                     float(2.2),
                     float(1.50),)

    anchor3 = Anchor(str("ID4"),
                     float(1.9),
                     float(1.4),
                     float(2.2),
                     float(1.50),)


    while not rospy.is_shutdown():
        pub_tag.publish(tag)
        pub_anchor0.publish(anchor0)
        pub_anchor1.publish(anchor1)
        pub_anchor2.publish(anchor2)
        pub_anchor3.publish(anchor3)

        anchor0.x = anchor0.x + 1.0
        anchor0.y = anchor0.y + 1.0
        anchor0.z = anchor0.z + 1.0

        anchor1.x = anchor1.x + 1.0
        anchor1.y = anchor1.y + 1.0
        anchor1.z = anchor1.z + 1.0

        anchor2.x = anchor2.x + 1.0
        anchor2.y = anchor2.y + 1.0
        anchor2.z = anchor2.z + 1.0

        anchor3.x = anchor3.x + 1.0
        anchor3.y = anchor3.y + 1.0
        anchor3.z = anchor3.z + 1.0


        tag.x = tag.x + 1.0
        tag.y = tag.y + 1.0
        tag.z = tag.z + 1.0

        hello_str = "Hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
