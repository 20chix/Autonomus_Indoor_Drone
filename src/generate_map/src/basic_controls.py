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


server = None
menu_handler = MenuHandler()
br = None
counter = 0


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
    print feedback.marker_name + " is now at " + str(p.x) + ", " + str(p.y) + ", " + str(p.z)


# Marker for tag
def makeBoxControlTag(msg):
    control =  InteractiveMarkerControl()
    control.always_visible = True
    control.markers.append( makeWhiteSphereTag(msg) )
    msg.controls.append( control )
    return control

# Marker for anchor
def makeBoxControlAnchor(msg):
    control =  InteractiveMarkerControl()
    control.always_visible = True
    control.markers.append( makeGreyCubeAnchor(msg) )
    msg.controls.append( control )
    return control

# Marker for tag
def makeWhiteSphereTag( msg ):
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
    int_marker.header.frame_id = "map"
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
def makeGreyCubeAnchor( msg ):
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






def Anchor0callback(data):

    global server
    global anchor0x
    global anchor0y
    global anchor0z

    coordinates = data.data.split()


    # Get the coordinates of the Tag in this format 0 0 0, then split this string using .split() function
    try:
        # Get coordinates
        anchor0x = float(coordinates[0])
        anchor0y = float(coordinates[1])
        anchor0z = float(coordinates[2])
        # Create a new marker with passed coordinates
        position = Point(anchor0x, anchor0y, anchor0z)
        # Add description to the marker
        makeAnchorMarker(position, "Anchor 0")
        # TODO remove this after, Debugging purpose
        rospy.loginfo("Anchor0 x: " + str(anchor0x) + " y: " + str(anchor0y) + " z: " + str(anchor0z))

    except IndexError:
        rospy.loginfo("Index error")
    except ValueError:
       rospy.loginfo("Value error")



def Anchor1callback(data):
    global server
    global anchor1x
    global anchor1y
    global anchor1z


    coordinates = data.data.split()


    # Get the coordinates of the Tag in this format 0 0 0, then split this string using .split() function
    try:
        # Get coordinates
        anchor1x = float(coordinates[0])
        anchor1y = float(coordinates[1])
        anchor1z = float(coordinates[2])
        # Create a new marker with passed coordinates
        position = Point(anchor1x, anchor1y, anchor1z)
        # Add description to the marker
        makeAnchorMarker(position, "Anchor 1")

        # TODO remove this after, Debugging purpose
        rospy.loginfo("Anchor1 x: " + str(anchor1x) + " y: " + str(anchor1y) + " z: " + str(anchor1z))

    except IndexError:
        rospy.loginfo("Index error")
    except ValueError:
       rospy.loginfo("Value error")



def Anchor2callback(data):

    global server
    global anchor2x
    global anchor2y
    global anchor2z

    coordinates = data.data.split()


    # Get the coordinates of the Tag in this format 0 0 0, then split this string using .split() function
    try:
        # Get coordinates
        anchor2x = float(coordinates[0])
        anchor2y = float(coordinates[1])
        anchor2z = float(coordinates[2])
        # Create a new marker with passed coordinates
        position = Point(anchor2x, anchor2y, anchor2z)
        # Add description to the marker
        makeAnchorMarker(position, "Anchor 2")
        # TODO remove this after, Debugging purpose
        rospy.loginfo("Anchor2 x: " + str(anchor2x) + " y: " + str(anchor2y) + " z: " + str(anchor2z))

    except IndexError:
        rospy.loginfo("Index error")
    except ValueError:
       rospy.loginfo("Value error")

def Anchor3callback(data):
    global server
    global anchor3x
    global anchor3y
    global anchor3z

    coordinates = data.data.split()


    # Get the coordinates of the Tag in this format 0 0 0, then split this string using .split() function
    try:
        # Get coordinates
        anchor3x = float(coordinates[0])
        anchor3y = float(coordinates[1])
        anchor3z = float(coordinates[2])
        # Create a new marker with passed coordinates
        position = Point(anchor3x, anchor3y, anchor3z)
        # Add description to the marker
        makeAnchorMarker(position, "Anchor 3")
        # TODO remove this after, Debugging purpose
        rospy.loginfo("Anchor3 x: " + str(anchor3x) + " y: " + str(anchor3y) + " z: " + str(anchor3z))

    except IndexError:
        rospy.loginfo("Index error")
    except ValueError:
       rospy.loginfo("Value error")

def tagCallback(data):
    global tagx
    global tagy
    global tagz
    global server

    coordinates = data.data.split()

    # Get the coordinates of the Tag in this format 0 0 0, then split this string using .split() function
    try:
        # Get coordinates
        tagx = float(coordinates[0])
        tagy = float(coordinates[1])
        tagz = float(coordinates[2])
        # Create a new marker with passed coordinates
        position = Point(tagx, tagy, tagz)
        # Add description to the marker
        makeTagMarker(position, "Tag")
        # Publish marker
        server.applyChanges()
        # TODO remove this after, Debugging purpose
        rospy.loginfo("Tag x: " + str(tagx) + " y: " + str(tagy) + " z: " + str(tagy))

    except IndexError:
        rospy.loginfo("Index error")
    except ValueError:
       rospy.loginfo("Value error")






if __name__=="__main__":
    #server.applyChanges()


    rospy.Subscriber("DWM1001_Network_Anchor_0", String, Anchor0callback)
    rospy.Subscriber("DWM1001_Network_Anchor_1", String, Anchor1callback)
    rospy.Subscriber("DWM1001_Network_Anchor_2", String, Anchor2callback)
    rospy.Subscriber("DWM1001_Network_Anchor_3", String, Anchor3callback)
    rospy.Subscriber("DWM1001_Network_Tag", String, tagCallback)




    # 'commit' changes and send to all clients
   # server.applyChanges()







rospy.spin()
 