#!/usr/bin/env python
import rospy
from xml.dom.minidom import parse
from geometry_msgs.msg          import Pose
from time import sleep
import xml.etree.ElementTree as ElementTree
from operator import itemgetter
import os

dir_of_this_script = os.path.dirname(os.path.realpath(__file__))
gazebo_model_dir = os.path.join(dir_of_this_script, '', 'waypoints')


# Parse XML
treeFromXML = ElementTree.parse(str(gazebo_model_dir)+'/waypoints.xml')
# Get the root of XML
rootInXML = treeFromXML.getroot()

# Declare an empty Pose object
waypointCoordinatesFromXML = Pose()

# Declare an empty array
waypointsCoordinatesArrayFromXML = []

# Loop trough each child in XML
for coordinateValueInXML in rootInXML.findall('waypoint'):
    x = coordinateValueInXML.get('x')
    y = coordinateValueInXML.get('y')
    z = coordinateValueInXML.get('z')

    # Create a tuple with x y z value from XML
    tupleCoordinatesFromXML = (int(x), int(y), int(z))

    print("Coordinates")
    print("X: " + str(x))
    print("Y: " + str(y))
    print("Z: " + str(z))




    # Append into array
    waypointsCoordinatesArrayFromXML.append(tupleCoordinatesFromXML)

