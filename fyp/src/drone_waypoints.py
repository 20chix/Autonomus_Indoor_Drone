#!/usr/bin/env python


__author__     = "Hadi Elmekawi"
__version__    = "1.0"
__maintainer__ = "Hadi Elmekawi"
__email__      = "w1530819@my.westminster.ac.uk"
__status__     = "Development"


import xml.etree.ElementTree     as ElementTree
import os
from geometry_msgs.msg import (
    PoseWithCovariance,
    Pose,
    Twist,
)



class DroneWaypoint(object):

    waypointInMap = Pose()




    def extractCoordinatesFromXML(self, waypointCounterReached):
        """Get all the coordinate from XML file
            and assign it into an array of tuples

        :argument
        waypointCounterReached -- requested waypoint

        :return
        waypointCoordinatesFromXML -- Pose format

        """

        global targetInMap, currentWaypointCounterForFlightPath, actionCode
        dir_of_this_script = os.path.dirname(os.path.realpath(__file__))
        gazebo_model_dir = os.path.join(dir_of_this_script, '', 'waypoints')
        # Parse XML
        treeFromXML = ElementTree.parse(str(gazebo_model_dir) + '/waypoints.xml')

        # Get the root of XML
        rootInXML = treeFromXML.getroot()

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
                self.waypointInMap.position.x = waypointsCoordinatesArrayFromXML[i][0]
                self.waypointInMap.position.y = waypointsCoordinatesArrayFromXML[i][1]
                self.waypointInMap.position.z = waypointsCoordinatesArrayFromXML[i][2]

                return True


    def getWaypointsCoordinates(self):

        return self.waypointInMap