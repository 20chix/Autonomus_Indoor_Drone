#!/usr/bin/env python

## Integration test for peer_subscribe_notify
from time import sleep
import unittest
import time
import rospy
import rostest
from localizer_dwm1001.msg      import Anchor
from localizer_dwm1001.msg      import Tag


class AnchorTestCase(unittest.TestCase):

    anchorData_ok = False

    def callback(self, data):
        self.anchorData_ok = True
        pass

    def test_if_anchor_0_is_published(self):
        rospy.init_node('test_anchor_1')
        rospy.Subscriber("/dwm1001/anchor1", Anchor, self.callback)
        counter = 0
        while not rospy.is_shutdown() and counter < 10 and (not self.anchorData_ok):
            time.sleep(1)
            counter += 1

        self.assertTrue(self.anchorData_ok)

if __name__ == '__main__':
    rostest.rosrun('localizer_dwm1001', 'test_anchor_1', AnchorTestCase)