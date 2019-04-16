#!/usr/bin/env python

from aid_systemDefinitions       import SYS_DEFS
__author__     = SYS_DEFS.AUTHOR
__version__    = SYS_DEFS.VERSION
__maintainer__ = SYS_DEFS.MAINTAINER
__email__      = SYS_DEFS.EMAIL
__status__     = SYS_DEFS.STATUS


import rospy
import xml.etree.ElementTree    as ElementTree

from localizer_dwm1001.msg       import Anchor
from localizer_dwm1001.msg       import Tag
from std_srvs.srv                import Trigger, TriggerRequest
from localizer_dwm1001.srv       import Anchor_0
from localizer_dwm1001.srv       import Anchor_1
from localizer_dwm1001.srv       import Anchor_2
from localizer_dwm1001.srv       import Anchor_3

import math
import os



from gazebo_msgs.srv import (
    SpawnModel,
    DeleteModel,
)
from geometry_msgs.msg import (
    PoseWithCovariance,
    Pose,
    Twist,
    Point,
    Quaternion,
)


numberAnchor = 0



counterForSDFModelToLoadSameSDFmultipleTimes = 0
dir_of_this_script = os.path.dirname(os.path.realpath(__file__))
gazebo_model_dir = os.path.join(dir_of_this_script, '', 'model')


class LoadDwm1001InGazebo(object):
    waypointsCoordinatesArrayFromDwm1001 = []
    anchorInMap = Pose()

    def loadGazeboModels(self, model_name, model_pose, model_type="sdf",
                         model_reference_frame="base_link"):

        global  counterForSDFModelToLoadSameSDFmultipleTimes

        model_path = gazebo_model_dir

        # Go though every sdf file in the path
        if model_type == "sdf":
            with open(os.path.join(model_path, model_name) + ".sdf", "r") as _file:
                _xml = _file.read().replace('\n', '')


                # Check if gazebo is running, if not skip the loading waypoints part
                try:
                    rospy.wait_for_service('/gazebo/spawn_sdf_model', 1)

                except (rospy.ServiceException, rospy.ROSException) as e:
                    rospy.loginfo("Service call failed:" + str(e) + ", skipping loading waitpoints")
                    return 1

            # Load waypoints into Gazebo using box sdf, this model will be used multiple times since we will have multiple waypoints
            try:
                spawn_sdf = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
                resp_sdf = spawn_sdf(model_name + str(counterForSDFModelToLoadSameSDFmultipleTimes), _xml, "/", model_pose, model_reference_frame)
                rospy.loginfo("Loaded waypoint(s)(%s) succesfully.", model_name+ str(counterForSDFModelToLoadSameSDFmultipleTimes))
                counterForSDFModelToLoadSameSDFmultipleTimes += 1
                rospy.loginfo("Added in gazebo X: " + str(model_pose.position.x) +
                              " Y: " + str(model_pose.position.y) +
                              " Z: " + str(model_pose.position.z))

            except rospy.ServiceException as e:
                rospy.loginfo("Spawn service service call failed: {0}".format(e))
                return False
            return True

        else:
            rospy.logerr("format is not match")

    def populateWaypointsInGazebo(self, x, y, z):

        model_pose = Pose()
        model_pose.position.x = x
        model_pose.position.y = y
        model_pose.position.z = z

        rospy.loginfo("model X: " + str(model_pose.position.x) +
                      " Y: " + str(model_pose.position.y) +
                      " Z: " + str(model_pose.position.z))

        self.loadGazeboModels(model_name ="box",
                              model_pose = model_pose,
                              model_type = "sdf",
                              model_reference_frame = "base_link")



    def anchorsReached(self, waypointCounterDidReached):
        """Check for existence of waypoint and return true if there is one

        :argument
        waypointCounterDidReached -- requested waypoint

        :return
        True -- True only if there is a coordinate in the xml file

        """

        # Loop trough the array of tuple and get only the requested waypoint
        for i in range(len(self.waypointsCoordinatesArrayFromDwm1001)):

            if waypointCounterDidReached == i:
                self.anchorInMap.position.x = self.waypointsCoordinatesArrayFromDwm1001[i][0]
                self.anchorInMap.position.y = self.waypointsCoordinatesArrayFromDwm1001[i][1]
                self.anchorInMap.position.z = self.waypointsCoordinatesArrayFromDwm1001[i][2] +1
                return True



    def getAnchorCoordinates(self):

        return self.anchorInMap

    def execute(self):


        # Wait for the service
        rospy.wait_for_service('/Anchor_0')
        # Create the connection to the service. Remeber it's a Trigger service
        anchor_0_service = rospy.ServiceProxy('/Anchor_0', Anchor_0)
        self.populateWaypointsInGazebo( float(anchor_0_service().x), float(anchor_0_service().y), float(anchor_0_service().z))
        tupleCoordinatesFromXML = (float(anchor_0_service().x), float(anchor_0_service().y), float(anchor_0_service().z))
        self.waypointsCoordinatesArrayFromDwm1001.append(tupleCoordinatesFromXML)

        # Wait for the service
        rospy.wait_for_service('/Anchor_1')
        # Create the connection to the service. Remeber it's a Trigger service
        anchor_1_service = rospy.ServiceProxy('/Anchor_1', Anchor_1)
        self.populateWaypointsInGazebo( anchor_1_service().x, anchor_1_service().y, anchor_1_service().z)
        tupleCoordinatesFromXML = (float(anchor_1_service().x), float(anchor_1_service().y), float(anchor_1_service().z))
        self.waypointsCoordinatesArrayFromDwm1001.append(tupleCoordinatesFromXML)

        # Wait for the service
        rospy.wait_for_service('/Anchor_2')
        # Create the connection to the service. Remeber it's a Trigger service
        anchor_2_service = rospy.ServiceProxy('/Anchor_2', Anchor_2)
        self.populateWaypointsInGazebo( float(anchor_2_service().x), float(anchor_2_service().y), float(anchor_2_service().z))
        tupleCoordinatesFromXML = (float(anchor_2_service().x), float(anchor_2_service().y), float(anchor_2_service().z))
        self.waypointsCoordinatesArrayFromDwm1001.append(tupleCoordinatesFromXML)

        # Wait for the service
        rospy.wait_for_service('/Anchor_3')
        # Create the connection to the service. Remeber it's a Trigger service
        anchor_3_service = rospy.ServiceProxy('/Anchor_3', Anchor_3)
        self.populateWaypointsInGazebo( float(anchor_3_service().x), float(anchor_3_service().y), float(anchor_3_service().z))
        tupleCoordinatesFromXML = (float(anchor_3_service().x), float(anchor_3_service().y), float(anchor_3_service().z))
        self.waypointsCoordinatesArrayFromDwm1001.append(tupleCoordinatesFromXML)



    def addWaypointsFromXMLToGazebo(self, x, y, z):
        rospy.loginfo("Adding into gazebo")
        self.populateWaypointsInGazebo(float(x), float(y), float(z))


