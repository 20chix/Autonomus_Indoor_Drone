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
    # Declare an empty array
    waypointsCoordinatesArrayFromXML = []




    def extractCoordinatesFromXML(self, waypointCounterReached):
        """Get all the coordinate from XML file
            and assign it into an array of tuples

        :argument
        waypointCounterReached -- requested waypoint

        :return
        waypointCoordinatesFromXML -- Pose format

        """

        dir_of_this_script = os.path.dirname(os.path.realpath(__file__))
        gazebo_model_dir = os.path.join(dir_of_this_script, '', 'waypoints')
        # Parse XML
        treeFromXML = ElementTree.parse(str(gazebo_model_dir) + '/waypoints.xml')

        # Get the root of XML
        rootInXML = treeFromXML.getroot()



        # Loop trough each child in XML
        for coordinateValueInXML in rootInXML.findall('waypoint'):
            x = coordinateValueInXML.get('x')
            y = coordinateValueInXML.get('y')
            z = coordinateValueInXML.get('z')

            # Create a tuple with x y z value from XML
            tupleCoordinatesFromXML = (int(x), int(y), int(z))

            # Append into array
            self.waypointsCoordinatesArrayFromXML.append(tupleCoordinatesFromXML)

        # Loop trough the array of tuple and get only the requested waypoint
        for i in range(len(self.waypointsCoordinatesArrayFromXML)):

            if waypointCounterReached == i:
                self.waypointInMap.position.x = self.waypointsCoordinatesArrayFromXML[i][0]
                self.waypointInMap.position.y = self.waypointsCoordinatesArrayFromXML[i][1]
                self.waypointInMap.position.z = self.waypointsCoordinatesArrayFromXML[i][2]

                return True


    def getWaypointsCoordinates(self):

        return self.waypointInMap


    def getWaypontsCoordinatesInArray(self):

        # Declare an empty array
        dummyWaypointsCoordinatesArrayFromXML = []



        dir_of_this_script = os.path.dirname(os.path.realpath(__file__))
        gazebo_model_dir = os.path.join(dir_of_this_script, '', 'waypoints')
        # Parse XML
        treeFromXML = ElementTree.parse(str(gazebo_model_dir) + '/waypoints.xml')

        # Get the root of XML
        rootInXML = treeFromXML.getroot()



        # Loop trough each child in XML
        for coordinateValueInXML in rootInXML.findall('waypoint'):
            x = coordinateValueInXML.get('x')
            y = coordinateValueInXML.get('y')
            z = coordinateValueInXML.get('z')

            # Create a tuple with x y z value from XML
            tupleCoordinatesFromXML = (int(x), int(y), int(z))

            # Append into array
            dummyWaypointsCoordinatesArrayFromXML.append(tupleCoordinatesFromXML)




        return  dummyWaypointsCoordinatesArrayFromXML