#!/usr/bin/env python

import rospy
import copy
from interactive_markers.interactive_marker_server  import InteractiveMarkerServer
from interactive_markers.menu_handler               import *
from visualization_msgs.msg                         import (InteractiveMarkerControl, Marker, InteractiveMarker )
from geometry_msgs.msg                              import Point
from localizer_dwm1001.msg                          import Anchor
from localizer_dwm1001.msg                          import Tag


server       = None
rospy.init_node("display_map")
server = InteractiveMarkerServer("DWM1001_Anchors_And_Tag_Server")


class DisplayInRviz:


    def processFeedback(self, feedback):
        """
        Process feedback of markers

        :param: feedback of markers

        :returns: none

        """
        p = feedback.pose.position
        rospy.loginfo(feedback.marker_name + " is pluginsnow at " + str(p.x) + ", " + str(p.y) + ", " + str(p.z))


    def makeBoxControlTag(self,msg):
        """
        Create a box controll for tag

        :param: msg from marker

        :returns: control

        """

        control =  InteractiveMarkerControl()
        control.always_visible = True
        control.markers.append( self.makeWhiteSphereTag(msg) )
        msg.controls.append( control )
        return control

    def makeBoxControlAnchor(self, msg):
        """
        Create a box control for anchor

        :param: msg from marker

        :returns: control

        """
        control =  InteractiveMarkerControl()
        control.always_visible = True
        control.markers.append( self.makeGreyCubeAnchor(msg) )
        msg.controls.append( control )
        return control

    def makeWhiteSphereTag(self, msg ):
        """
        Create a white sphere for tag

        :param: msg from marker

        :returns: marker

        """

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


    def makeGreyCubeAnchor(self, msg):
        """
        Create a grey cube for anchor

        :param: msg from marker

        :returns: marker

        """

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



    def makeTagMarker(self, position, name):
        """
        Make coordinates and control for tag

        :param: position of tag
        :param: name for tag

        :returns:

        """

        int_marker = InteractiveMarker()
        int_marker.header.frame_id = "map"
        int_marker.pose.position = position
        int_marker.scale = 1

        int_marker.name = name
        int_marker.description = name

        self.makeBoxControlTag(int_marker)

        control = InteractiveMarkerControl()
        control.orientation.w = 1
        control.orientation.x = 0
        control.orientation.y = 1
        control.orientation.z = 0
        control.interaction_mode = InteractiveMarkerControl.MOVE_ROTATE
        int_marker.controls.append(copy.deepcopy(control))
        control.interaction_mode = InteractiveMarkerControl.MOVE_AXIS
        int_marker.controls.append(control)

        server.insert(int_marker, self.processFeedback)



    def makeAnchorMarker(self, position, name):
        """
        Make coordinates and control for anchor

        :param: position of anchor
        :param: name for anchor

        :returns:

        """

        int_marker = InteractiveMarker()
        int_marker.header.frame_id = "map"
        int_marker.pose.position = position
        int_marker.scale = 1
        int_marker.description = name
        int_marker.name = name

        self.makeBoxControlAnchor(int_marker)

        control = InteractiveMarkerControl()
        control.orientation.w = 1
        control.orientation.x = 0
        control.orientation.y = 1
        control.orientation.z = 0
        control.interaction_mode = InteractiveMarkerControl.MOVE_ROTATE
        int_marker.controls.append(copy.deepcopy(control))
        control.interaction_mode = InteractiveMarkerControl.MOVE_AXIS
        int_marker.controls.append(control)

        server.insert(int_marker, self.processFeedback)



    def Anchor0callback(self,data):
        """
        Callback from topic /dwm1001/anchor0

        :param: data of anchor 0

        :returns:

        """
        global server

        # Get the coordinates of the Tag in this format 0 0 0, then split this string using .split() function
        try:
            # Create a new marker with passed coordinates
            position = Point(data.x, data.y, data.z)
            # Add description to the marker
            self.makeAnchorMarker(position, "Anchor 0")
            # TODO remove this after, Debugging purpose
            rospy.loginfo("Anchor0 x: " + str(data.x) + " y: " + str(data.y) + " z: " + str(data.z))
        except ValueError:
           rospy.loginfo("Value error")



    def Anchor1callback(self,data):
        """
        Callback from topic /dwm1001/anchor1

        :param: data of anchor 1

        :returns:

        """

        global server

        # Get the coordinates of the Tag in this format 0 0 0, then split this string using .split() function
        try:
            # Create a new marker with passed coordinates
            position = Point(data.x, data.y, data.z)
            # Add description to the marker
            self.makeAnchorMarker(position, "Anchor 1")

            # TODO remove this after, Debugging purpose
            rospy.loginfo("Anchor1 x: "+ str(data.x) + " y: " + str(data.y) + " z: " + str(data.z))

        except ValueError:
           rospy.loginfo("Value error")



    def Anchor2callback(self,data):
        """
        Callback from topic /dwm1001/anchor2

        :param: data of anchor 2

        :returns:

        """

        global server

        # Get the coordinates of the Tag in this format 0 0 0, then split this string using .split() function
        try:
            # Create a new marker with passed coordinates
            position = Point(data.x, data.y, data.z)
            # Add description to the marker
            self.makeAnchorMarker(position, "Anchor 2")
            # TODO remove this after, Debugging purpose
            rospy.loginfo("Anchor2 x: " + str(data.x) + " y: " + str(data.y) + " z: " + str(data.z))

        except ValueError:
           rospy.loginfo("Value error")

    def Anchor3callback(self,data):
        """
        Callback from topic /dwm1001/anchor3

        :param: data of anchor 3

        :returns:

        """

        global server

        # Get the coordinates of the Tag in this format 0 0 0, then split this string using .split() function
        try:
            # Create a new marker with passed coordinates
            position = Point(data.x, data.y, data.z)
            # Add description to the marker
            self.makeAnchorMarker(position, "Anchor 3")
            # TODO remove this after, Debugging purpose
            rospy.loginfo("Anchor3 x: " + str(data.x) + " y: " + str(data.y) + " z: " + str(data.z))

        except ValueError:
           rospy.loginfo("Value error")

    def TagCallback(self,data):
        """
        Callback from topic /dwm1001/tag

        :param: data of tag

        :returns:

        """
        global server

        # Get the coordinates of the Tag in this format 0 0 0, then split this string using .split() function
        try:
            # Create a new marker with passed coordinates
            position = Point(data.x, data.y, data.z)
            # Add description to the marker
            self.makeTagMarker(position, "Tag")
            # Publish marker
            server.applyChanges()

            # TODO remove this after, Debugging purpose
            rospy.loginfo("Tag x: " + str(data.x) + " y: " + str(data.y) + " z: " + str(data.z))

        except ValueError:
           rospy.loginfo("Value error")



    def start(self):
        rospy.Subscriber("/dwm1001/anchor0", Anchor, self.Anchor0callback)
        rospy.Subscriber("/dwm1001/anchor1", Anchor, self.Anchor1callback)
        rospy.Subscriber("/dwm1001/anchor2", Anchor, self.Anchor2callback)
        rospy.Subscriber("/dwm1001/anchor3", Anchor, self.Anchor3callback)
        rospy.Subscriber("/dwm1001/tag"    , Tag   , self.TagCallback)
        rospy.spin()



def main():
    displayInRviz = DisplayInRviz()
    displayInRviz.start()

if __name__=="__main__":
    main()

