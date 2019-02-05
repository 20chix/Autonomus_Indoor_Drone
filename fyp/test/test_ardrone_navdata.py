#!/usr/bin/env python

## Integration test for peer_subscribe_notify
from time import sleep
import unittest
import rospy
import rostest
from ardrone_autonomy.msg import Navdata


class NavdataTestCase(unittest.TestCase):

    navdata_ok = False

    def callback(self, data):
        self.navdata_ok = True
        pass

    def test_if_ardrone_pubblished(self):
        rospy.init_node('test_ardrone_navdata')
        rospy.Subscriber("/ardrone/navdata", Navdata, self.callback)

        counter = 0


        while not rospy.is_shutdown() and counter < 1 and (not self.navdata_ok):
            sleep(1)
            counter += 1

        self.assertTrue(not self.navdata_ok)

if __name__ == '__main__':
    rostest.rosrun('fyp', 'test_ardrone_navdata', NavdataTestCase)