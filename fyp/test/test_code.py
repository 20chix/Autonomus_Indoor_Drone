#!/usr/bin/env python

import unittest
import rostest


class MyTestCase(unittest.TestCase):

    def test_whatever(self):
        pass



if __name__ == "__main__":
    rostest.rosrun('fyp', 'test_code', MyTestCase)



