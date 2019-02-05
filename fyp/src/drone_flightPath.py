#!/usr/bin/env python
import rospy
from xml.dom.minidom import parse
from geometry_msgs.msg          import Pose
from time import sleep
import xml.etree.ElementTree as ET

targetCoordinates = Pose()
waypointsCoordinatesArray = []



# parse an xml file by name
mydoc = parse('waypoints.xml')

tree = ET.parse('waypoints.xml')
root = tree.getroot()

# find the first 'item' object
for elem in root:
    print(elem.find('waypoint').get('number'))

# find all "item" objects and print their "name" attribute
for elem in root:
    for subelem in elem.findall('waypoint'):

        # if we don't need to know the name of the attribute(s), get the dict
        print(subelem.attrib)

        # if we know the name of the attribute, access it directly
        print(subelem.get('name'))