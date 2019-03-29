#!/usr/bin/env python
from aid_systemDefinitions       import SYS_DEFS


__author__     = SYS_DEFS.AUTHOR
__version__    = SYS_DEFS.VERSION
__maintainer__ = SYS_DEFS.MAINTAINER
__email__      = SYS_DEFS.EMAIL
__status__     = SYS_DEFS.STATUS

import rospy
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



    def extractCoordinatesFromXML(self, waypointCounterDidReached):
        """Check for existence of waypoint and return true if there is one

        :argument
        waypointCounterDidReached -- requested waypoint

        :return
        True -- True only if there is a coordinate in the xml file

        """

        self.waypointsCoordinatesArrayFromXML = self.getWaypontsCoordinatesInArray()

        # Loop trough the array of tuple and get only the requested waypoint
        for i in range(len(self.waypointsCoordinatesArrayFromXML)):

            if waypointCounterDidReached == i:
                self.waypointInMap.position.x = self.waypointsCoordinatesArrayFromXML[i][0]
                self.waypointInMap.position.y = self.waypointsCoordinatesArrayFromXML[i][1]
                self.waypointInMap.position.z = self.waypointsCoordinatesArrayFromXML[i][2]

                return True



    def getWaypointsCoordinates(self):

        return self.waypointInMap


    def getWaypontsCoordinatesInArray(self):
        """Get all the waypoints(coordinates) from xml file and put them into
        an array of tuple

        :argument

        :return


        """

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