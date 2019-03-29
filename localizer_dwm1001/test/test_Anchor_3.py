#!/usr/bin/env python

from time import sleep
import unittest
import time
import rospy
from localizer_dwm1001.msg      import Anchor
import rosunit

# Structure Message Anchor
# string id
# float64  x
# float64  y
# float64  z
# float64  distanceFromTag

class Anchor3TestCase(unittest.TestCase):

    anchorData_ok = False
    anchor3       = Anchor()

    def callback(self, data):
        self.anchorData_ok = True
        self.anchor3       = data

    # Test existance of topic
    def test_if_anchor_3_is_published(self):
        rospy.init_node('test_anchor_3')
        rospy.Subscriber("/dwm1001/anchor3", Anchor, self.callback)
        counter = 1
        # give 5 seconds to check the topic is publishing something
        while not rospy.is_shutdown() and counter < 5 and (not self.anchorData_ok):
            time.sleep(1)
            counter += 1
            rospy.loginfo("looping")

        self.assertTrue(self.anchorData_ok)

    # Test the id of Anchor if is a string
    def test_if_anchor_3_id_is_string(self):
        if  isinstance(self.anchor3.id, str):
            self.assertTrue(True)
        else:
            self.assertTrue(False)


    # Test the x of Anchor if is a float
    def test_if_anchor_3_x_is_float(self):
        if  isinstance(self.anchor3.x, float):
            self.assertTrue(True)
        else:
            self.assertTrue(False)


    # Test the y of Anchor if is a float
    def test_if_anchor_3_y_is_float(self):
        if  isinstance(self.anchor3.y, float):
            self.assertTrue(True)
        else:
            self.assertTrue(False)


    # Test the z of Anchor if is a float
    def test_if_anchor_3_z_is_float(self):
        if  isinstance(self.anchor3.z, float):
            self.assertTrue(True)
        else:
            self.assertTrue(False)


    # Test the z of Anchor if is a float
    def test_if_anchor_3_distanceFromTag_is_float(self):
        if isinstance(self.anchor3.distanceFromTag, float):
            self.assertTrue(True)
        else:
            self.assertTrue(False)



if __name__ == '__main__':
    rosunit.unitrun('localizer_dwm1001', 'test_Anchor_3_Publisher', Anchor3TestCase)


