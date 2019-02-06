#!/usr/bin/env python
import rospy
from xml.dom.minidom import parse
from geometry_msgs.msg          import Pose
from time import sleep
import xml.etree.ElementTree as ElementTree
from operator import itemgetter








def extractCoordinatesFromXML(waypointCounterReached):
    """Get all the coordinate from XML file
        and assign it into an array of tuples

    :argument
    waypointCounterReached -- requested waypoint

    :return
    waypointCoordinatesFromXML -- Pose format

    """
    # Parse XML
    treeFromXML = ElementTree.parse('waypoints.xml')
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

        # Append into array
        waypointsCoordinatesArrayFromXML.append(tupleCoordinatesFromXML)

    # Loop trough the array of tuple and get only the requested waypoint
    for i in range(len(waypointsCoordinatesArrayFromXML)):

        if waypointCounterReached == i:
            waypointCoordinatesFromXML.position.x = waypointsCoordinatesArrayFromXML[i][0]
            waypointCoordinatesFromXML.position.y = waypointsCoordinatesArrayFromXML[i][1]
            waypointCoordinatesFromXML.position.z = waypointsCoordinatesArrayFromXML[i][2]
            return waypointCoordinatesFromXML


if __name__ == '__main__':


    try:

        # move_square.actionCode = 2

        waypointCounterToRead = 1

        if extractCoordinatesFromXML(waypointCounterToRead) == None:
            print("Waypoints finished..")
        else:
            print("Requested coordinates")
            print("X: " + str(extractCoordinatesFromXML(waypointCounterToRead).position.x))
            print("Y: " + str(extractCoordinatesFromXML(waypointCounterToRead).position.y))
            print("Z: " + str(extractCoordinatesFromXML(waypointCounterToRead).position.z))
        # time.sleep(3)
        # move_square.actionCode = 2

    except rospy.ROSInterruptException:
        pass
