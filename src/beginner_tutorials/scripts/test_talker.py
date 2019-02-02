#!/usr/bin/env python

import unittest
import rospy
from std_msgs.msg import String
from time import sleep
import rostest

class TalkerTestCase(unittest.TestCase):

    talker_ok = False

    def callback(self, data):
        self.talker_ok = True


    def test_if_talker_publish(self):

        rospy.init_node('test_talker')
        rospy.Subscriber('/DWM1001_Network_Anchor_0', String, self.callback)


        counter = 0
        while not rospy.is_shutdown() and counter < 5 and (not self.talker_ok):
            sleep(1)
            counter += 1


        self.assertTrue(self.talker_ok)



if __name__ == '__main__':
    rostest.rosrun('beginner_tutorials', 'test_talker', TalkerTestCase)