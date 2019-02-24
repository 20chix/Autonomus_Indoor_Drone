#!/usr/bin/env python

"""
Copyright (c) 2011, Willow Garage, Inc.
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the Willow Garage, Inc. nor the names of its
      contributors may be used to endorse or promote products derived from
      this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

import rospy
import copy

from interactive_markers.interactive_marker_server import *
from interactive_markers.menu_handler import *
from visualization_msgs.msg import *
from geometry_msgs.msg import Point
from tf.broadcaster import TransformBroadcaster
from std_msgs.msg import String
from aid_waypoints               import DroneWaypoint

from geometry_msgs.msg import (
    PoseWithCovariance,
    Pose,
    Twist,
)


droneWaypointsFromXML = DroneWaypoint()
server = None
menu_handler = MenuHandler()
br = None
counterForSDFModelToLoadSameSDFmultipleTimes = 0

tagx = 0
tagy = 0
tagz = 0

anchor0x = 0
anchor0y = 0
anchor0z = 0

anchor1x = 0
anchor1y = 0
anchor1z = 0

anchor2x = 0
anchor2y = 0
anchor2z = 0

anchor3x = 0
anchor3y = 0
anchor3z = 0

rospy.init_node("generate_map")
server = InteractiveMarkerServer("DWM1001_Anchors_And_Tag_Server")

pub_line_min_dist = rospy.Publisher('~line_min_dist', Marker, queue_size=1)


def processFeedback(feedback):
    p = feedback.pose.position
    print
    feedback.marker_name + " is now at " + str(p.x) + ", " + str(p.y) + ", " + str(p.z)


# Marker for tag
def makeBoxControlTag(msg):
    control = InteractiveMarkerControl()
    control.always_visible = True
    control.markers.append(makeWhiteSphereTag(msg))
    msg.controls.append(control)
    return control


# Marker for anchor
def makeBoxControlAnchor(msg):
    control = InteractiveMarkerControl()
    control.always_visible = True
    control.markers.append(makeGreyCubeAnchor(msg))
    msg.controls.append(control)
    return control


# Marker for tag
def makeWhiteSphereTag(msg):
    marker = Marker()

    marker.type = Marker.SPHERE
    marker.scale.x = msg.scale * 0.45
    marker.scale.y = msg.scale * 0.45
    marker.scale.z = msg.scale * 0.45
    marker.color.r = 1
    marker.color.g = 1
    marker.color.b = 1
    marker.color.a = 1.0
    return marker


def makeTagMarker(position, name):
    int_marker = InteractiveMarker()
    int_marker.header.frame_id = "base_link"
    int_marker.pose.position = position
    int_marker.scale = 1

    int_marker.name = name
    int_marker.description = name

    makeBoxControlTag(int_marker)

    control = InteractiveMarkerControl()
    control.orientation.w = 1
    control.orientation.x = 0
    control.orientation.y = 1
    control.orientation.z = 0
    control.interaction_mode = InteractiveMarkerControl.MOVE_ROTATE
    int_marker.controls.append(copy.deepcopy(control))
    control.interaction_mode = InteractiveMarkerControl.MOVE_AXIS
    int_marker.controls.append(control)

    server.insert(int_marker, processFeedback)


# Marker for tag
def makeGreyCubeAnchor(msg):
    marker = Marker()

    marker.type = Marker.CUBE
    marker.scale.x = msg.scale * 0.45
    marker.scale.y = msg.scale * 0.45
    marker.scale.z = msg.scale * 0.45
    marker.color.r = 0.5
    marker.color.g = 0.5
    marker.color.b = 0.5
    marker.color.a = 1.0
    return marker


def makeAnchorMarker(position, name):
    int_marker = InteractiveMarker()
    int_marker.header.frame_id = "map"
    int_marker.pose.position = position
    int_marker.scale = 1
    int_marker.description = name
    int_marker.name = name

    makeBoxControlAnchor(int_marker)

    control = InteractiveMarkerControl()
    control.orientation.w = 1
    control.orientation.x = 0
    control.orientation.y = 1
    control.orientation.z = 0
    control.interaction_mode = InteractiveMarkerControl.MOVE_ROTATE
    int_marker.controls.append(copy.deepcopy(control))
    control.interaction_mode = InteractiveMarkerControl.MOVE_AXIS
    int_marker.controls.append(control)

    server.insert(int_marker, processFeedback)


def waypoint1Callback(data):
    global server

    # Get the coordinates of the Tag in this format 0 0 0, then split this string using .split() function
    try:

        # Add description to the marker
        makeTagMarker(data.position, "Waypoint1")
        # Publish marker
        server.applyChanges()
        # TODO remove this after, Debugging purpose
        rospy.loginfo("Waypoint x: " + str(data.position.x) + " y: " + str(data.position.y) + " z: " + str(data.position.z))

    except IndexError:
        rospy.loginfo("Index error")
    except ValueError:
        rospy.loginfo("Value error")


if __name__ == "__main__":
    # server.applyChanges()


    counter = 0


    rospy.Subscriber("/aid/waypoint/1", Pose, waypoint1Callback)
    #ospy.Subscriber("/aid/waypoint/1", Pose, waypoint2Callback)
    #rospy.Subscriber("/aid/waypoint/1", Pose, waypoint3Callback)
    #rospy.Subscriber("/aid/waypoint/1", Pose, waypoint4Callback)
    #rospy.Subscriber("/aid/waypoint/1", Pose, waypoint5Callback)


    # 'commit' changes and send to all clients
# server.applyChanges()


rospy.spin()
