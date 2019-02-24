#!/usr/bin/env python


__author__     = "Hadi Elmekawi"
__version__    = "1.0"
__maintainer__ = "Hadi Elmekawi"
__email__      = "w1530819@my.westminster.ac.uk"
__status__     = "Development"


import rospy
import time
from std_msgs.msg               import Empty
from fyp.cfg                    import droneGUIConfig
from dynamic_reconfigure.server import Server
from nav_msgs.msg               import Odometry
from ardrone_autonomy.msg       import Navdata
import xml.etree.ElementTree    as ElementTree


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


counterForSDFModelToLoadSameSDFmultipleTimes = 0

dir_of_this_script = os.path.dirname(os.path.realpath(__file__))
gazebo_model_dir = os.path.join(dir_of_this_script, '', 'model')


class LoadWaypointsInGazebo(object):

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

            except rospy.ServiceException as e:
                rospy.loginfo("Spawn service service call failed: {0}".format(e))
                return False
            return True

        # Go though every urdf file in the path
        elif model_type == "urdf":
            with open(os.path.join(model_path, model_name) + ".urdf", "r") as _file:
                _xml = _file.read().replace('\n', '')


                # Check if gazebo is running, if not skip the loading waypoints part
                try:
                    rospy.wait_for_service('/gazebo/spawn_sdf_model', 2)

                except (rospy.ServiceException, rospy.ROSException) as e:
                    rospy.loginfo("Service call failed:" + str(e) + ", skipping loading waitpoints")
                    return 1


            # Load waypoints into Gazebo using box urdf, this model will be used multiple times since we will have multiple waypoints
            try:
                spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
                resp_urdf = spawn_urdf(model_name, _xml, "/", model_pose, model_reference_frame)
                rospy.loginfo("loading %s succesfully", model_name)
            except:
                rospy.logerr("Spawn URDF service call failed: {0}")
                return False
            return True
        else:
            rospy.logerr("format is not match")

    def populateWaypointsInGazebo(self, x, y, z):

        model_pose = Pose()
        model_pose.position.x = x
        model_pose.position.y = y
        model_pose.position.z = z

        self.loadGazeboModels(model_name ="box",
                              model_pose = model_pose,
                              model_type = "sdf",
                              model_reference_frame = "base_link")


    def addWaypointsFromXMLToGazebo(self):

        dir_of_this_script = os.path.dirname(os.path.realpath(__file__))

        gazeboModelDir = os.path.join(dir_of_this_script, '', 'waypoints')

        # Parse XML
        treeFromXML = ElementTree.parse(str(gazeboModelDir) + '/waypoints.xml')
        # Get the root of XML
        rootInXML = treeFromXML.getroot()

        # Loop trough each child in XML
        for coordinateValueInXML in rootInXML.findall('waypoint'):
            x = coordinateValueInXML.get('x')
            y = coordinateValueInXML.get('y')
            z = coordinateValueInXML.get('z')
            self.populateWaypointsInGazebo(int(x), int(y), int(z))


