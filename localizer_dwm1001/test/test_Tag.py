#!/usr/bin/env python

from time import sleep
import unittest
import time
import rospy
from localizer_dwm1001.msg      import Tag
import rosunit

# Structure Message Anchor
# string id
# float64  x
# float64  y
# float64  z
# float64  distanceFromTag

class TagTestCase(unittest.TestCase):

    tagData_ok = False
    tag       = Tag()

    def callback(self, data):
        self.tagData_ok = True
        self.tag       = data

    # Test existance of topic
    def test_if_anchor_3_is_published(self):
        rospy.init_node('test_tag')
        rospy.Subscriber("/dwm1001/tag", Tag, self.callback)
        counter = 1
        # give 5 seconds to check the topic is publishing something
        while not rospy.is_shutdown() and counter < 5 and (not self.tagData_ok):
            time.sleep(1)
            counter += 1
            rospy.loginfo("looping")

        self.assertTrue(self.tagData_ok)


    # Test the x of tag if is a float
    def test_if_tag_x_is_float(self):
        if  isinstance(self.tag.x, float):
            self.assertTrue(True)
        else:
            self.assertTrue(False)


    # Test the y of tag if is a float
    def test_if_tag_y_is_float(self):
        if  isinstance(self.tag.y, float):
            self.assertTrue(True)
        else:
            self.assertTrue(False)


    # Test the z of tag if is a float
    def test_if_tag_z_is_float(self):
        if  isinstance(self.tag.z, float):
            self.assertTrue(True)
        else:
            self.assertTrue(False)



if __name__ == '__main__':
    rosunit.unitrun('localizer_dwm1001', 'test_Tag_3_Publisher', TagTestCase)


