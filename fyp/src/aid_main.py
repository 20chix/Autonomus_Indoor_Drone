#!/usr/bin/env python

from aid_systemDefinitions       import SYS_DEFS

__author__     = SYS_DEFS.AUTHOR
__version__    = SYS_DEFS.VERSION
__maintainer__ = SYS_DEFS.MAINTAINER
__email__      = SYS_DEFS.EMAIL
__status__     = SYS_DEFS.STATUS

import rospy
import time
from std_msgs.msg                import Empty
from fyp.cfg                     import droneGUIConfig
from dynamic_reconfigure.server  import Server
from nav_msgs.msg                import Odometry
from aid_lastDroneData           import lastDroneDataClass
#from ardrone_autonomy.msg        import Navdata
from aid_loadWaypointsInGazebo   import LoadWaypointsInGazebo
from aid_loadDwm1001InGazebo     import LoadDwm1001InGazebo
from aid_waypoints               import DroneWaypoint
from sensor_msgs.msg             import Joy
from localizer_dwm1001.msg       import Anchor
from localizer_dwm1001.msg       import Tag
from std_srvs.srv                import Trigger, TriggerRequest
from localizer_dwm1001.srv       import Anchor_0
from gazebo_msgs.srv             import DeleteModel # For deleting models from the environment
import mavros_msgs
from geometry_msgs.msg import PoseStamped, TwistStamped


import mavros_msgs
from mavros_msgs import srv
from mavros_msgs.msg import State

import math
from geometry_msgs.msg import (
    PoseWithCovariance,
    Pose,
    Twist,
    TwistStamped
)

navDataRotZ    = 0
navDataRotZ360 = 0
actionState     = 0

latchStartTime        = rospy.Duration(5.0)
externalEstimatedPose = PoseWithCovariance()
lastSavedWayHomePoint = Pose()
targetInDrone         = Pose()
land_msg              = Empty()
takeoff_msg           = Empty()
reset_msg             = Empty()
messageTwist          = Twist()
messageTwistStamped   = TwistStamped()
targetInDrone         = Pose()
targetInMap           = Pose()
lastSavedWaypoint     = Pose()
realPose              = PoseWithCovariance()
droneWaypointsFromXML = DroneWaypoint()
latched               = False


targetInMap.position.x                     = 0
targetInMap.position.y                     = 0
targetInMap.position.z                     = 0
targetInMap.orientation.x                  = 0
targetInMap.orientation.y                  = 0
targetInMap.orientation.z                  = 0
lastSavedWaypoint.position.x               = 0
lastSavedWaypoint.position.y               = 0
lastSavedWaypoint.position.z               = 0
currentWaypointCounterForFlightPath        = 0
currentWaypointCounterForFlightPathDWM1001 = 0
currentSavedWaypointPtr                    = 0
poseEstimationMethod                       = 1
externalEstimatedPose.pose.position.x      = 0
externalEstimatedPose.pose.position.y      = 0
externalEstimatedPose.pose.position.z      = 0
lastDroneData                              = lastDroneDataClass()
currentDroneData                           = lastDroneDataClass()
lastDroneData.xRot                         = 0
lastDroneData.yRot                         = 0
lastDroneData.zRot                         = 0
lastSavedWayHomePoint.position.x           = 0
lastSavedWayHomePoint.position.y           = 0
lastSavedWayHomePoint.position.z           = 0.1
gazeboDwm1001                              = LoadDwm1001InGazebo()
# Setup a node 
rospy.init_node('fyp', anonymous=False)
lastDataSampleTime                         = rospy.Time()
rate                                       = rospy.Rate(10)
# Define publishers and messages that will be used
pub_cmd_vel                                = rospy.Publisher('/cmd_vel'             , Twist, queue_size=1)
pub_takeoff                                = rospy.Publisher('/ardrone/takeoff'     , Empty, queue_size=1)
pub_land                                   = rospy.Publisher('/ardrone/land'        , Empty, queue_size=1)
pub_reset                                  = rospy.Publisher("ardrone/reset"        , Empty, queue_size=1)


pub_cmd_velocity                      = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel',TwistStamped, queue_size = 10)




def init():
    """Initialise ROS time,
    drone linear and angular velocity
    and subscribe to /ardrone/navdata and /ground_truth/state


    """
    global messageTwist, lastDroneData

    #Initialise last and current drone data to ros time
    lastDroneData.timeStamp = rospy.Time()
    currentDroneData.timeStamp = rospy.Time()

    #Initialise message twist to 0
    messageTwist = setUpTwist(0, 0, 0, 0, 0, 0)

    #Initialise Dynamic configuration
    Server(droneGUIConfig, droneGUICallback)

    #Subscribe to these topics
    #rospy.Subscriber('/ardrone/navdata', Navdata, navDataCallBack)
    rospy.Subscriber('/ground_truth/state', Odometry, realPoseCallBack)
    rospy.Subscriber("joy", Joy, JoystickCallBack)

    run()


def deleteModelFromGazebo( modelName ):
    """
    Remove the model with 'modelName' from the Gazebo scene
    :param modelName:
    """
    del_model_prox = rospy.ServiceProxy('gazebo/delete_model', DeleteModel) # model spawner
    del_model_prox(modelName)


def deleteAllWaypointsFromGazebo():
    """
    Remove all models with 'box' + number from the Gazebo scene
    """
    temp_model_name = "box"
    i = 0
    while i < 50:
        deleteModelFromGazebo(temp_model_name + str(i))
        i = i + 1
    rospy.loginfo("Model used as waypoints delete it")


def run():
    """
    Based on the received command, land,takeoff, go to a waypoint, pivot and go to waypoint or go to origin

    """
    global currentDroneData , actionState, targetInMap, latchStartTime, latched, wayHomePtr, pub_cmd_velocity, pub_takeoff, pub_land, pub_reset
    latchTime = rospy.Duration(5.0)

    rospy.loginfo("Waiting for a command")

    # Loop until ros is shutdown
    while not rospy.is_shutdown():

        # # Keep publish waypoints to ros
        # publishWaypoints()
        # # Keep publish ardrone position to ros
        # publishArdronePos()

        # Reset the latch  time
        # if actionState == SYS_DEFS.RESET_LATCH_TIME_ACTION_STATE:
        #     latched = False

        # Take off
        if actionState == SYS_DEFS.TAKE_OFF_ACTION_STATE:
            # Set GUIDED Mode 
            setGuidedMode('GUIDED')
            rate.sleep()
            # Arm drone
            setArm()
            rate.sleep()
            # Takeoff
            setTakeoffMode(2)
            #Reset action state 
            actionState = 0
        # Land
        elif actionState == SYS_DEFS.LAND_ACTION_STATE:
            setLandMode()

        # Reset
        # elif actionState == SYS_DEFS.RESET_DRONE_ACTION_STATE:
        #     rospy.loginfo("Resetting")
        #     # Publish reset message
        #     pub_reset.publish(reset_msg)
        #     # Set action state to 0
        #     actionState = 0

        # Go to the waypoint without looking
        # elif actionState == SYS_DEFS.GO_TO_WAYPOINT_WITHOUT_LOOKING_ACTION_STATE:
        #     # Convert drone coordinates into drone frames
        #     returnTargetInDrone(targetInMap)
        #     # Keep going if the waypoint is not reached
        #     if not wayPointReached(SYS_DEFS.WAYPOINT_ACCURACY):
        #         xAct = (targetInDrone.position.x * SYS_DEFS.POINT_GAIN)
        #         yAct = (targetInDrone.position.y * SYS_DEFS.POINT_GAIN)
        #         zAct = (targetInDrone.position.z * SYS_DEFS.POINT_GAIN)

        #         rospy.loginfo("Real Pose X: " + str(realPose.pose.position.x) +
        #                       " Y: " + str(realPose.pose.position.y) +
        #                       " Z: " + str(realPose.pose.position.z))
        #         rospy.loginfo("Acceleration X: " + str(xAct) +
        #                       " Y: " + str(yAct) +
        #                       " Z: " + str(zAct))
        #         rospy.loginfo("Current DD X: " + str(currentDroneData.x) +
        #                       " Y: " + str(currentDroneData.y) +
        #                       " Z: " + str(currentDroneData.z))
        #         rospy.loginfo("Target DD X: " + str(targetInDrone.position.x) +
        #                       " Y: " + str(targetInDrone.position.y) +
        #                       " Z: " + str(targetInDrone.position.z))
        #         command(xAct, yAct, zAct, 0, 0, 0)
        #     else:
        #         rospy.loginfo("Waypoint Reached ")
        #         command(0, 0, 0, 0, 0, 0)
        #         actionState = 0


        # Look at the waypoint
        # elif actionState == SYS_DEFS.LOOK_AT_WAYPOINT_ACTION_STATE:
        #     rospy.loginfo("Looking at the waypoint")
        #     # Convert drone coordinates into drone frames
        #     returnTargetInDrone(targetInMap)
        #     # Adjust z rotation
        #     zRotAct = targetInDrone.orientation.z * SYS_DEFS.POINT_GAIN
        #     command(0, 0, 0, 0, 0, zRotAct)

        # Look and Go to the waypoint
        # elif actionState == SYS_DEFS.LOOK_AND_GO_TO_WAYPOINT_ACTION_STATE:
        #     # Convert drone coordinates into drone frames
        #     returnTargetInDrone(targetInMap)
        #     # Keep going if the waypoint is not reached
        #     if not wayPointReached(SYS_DEFS.WAYPOINT_ACCURACY):
        #         # Check if the drone is facing the waypoint, fix orientation if not
        #         if wayPointFaced(SYS_DEFS.ANGLE_ACCURACY):
        #             # Adjust accelleration with angle gain and point gain
        #             zRotAct = (targetInDrone.orientation.z  * SYS_DEFS.ANGLE_GAIN)
        #             xAct    = (targetInDrone.position.x     * SYS_DEFS.POINT_GAIN)
        #             yAct    = (targetInDrone.position.y     * SYS_DEFS.POINT_GAIN)
        #             zAct    = (targetInDrone.position.z     * SYS_DEFS.POINT_GAIN)
        #             rospy.loginfo("Real Pose X: " + str(realPose.pose.position.x) +
        #                           " Y: " + str(realPose.pose.position.y) +
        #                           " Z: " + str(realPose.pose.position.z))
        #             rospy.loginfo("Acceleration X: " + str(xAct) +
        #                           " Y: " + str(yAct) +
        #                           " Z: " + str(zAct))
        #             rospy.loginfo("Current DD X: " + str(currentDroneData.x) +
        #                           " Y: " + str(currentDroneData.y) +
        #                           " Z: " + str(currentDroneData.z))
        #             rospy.loginfo("Target DD X: " + str(targetInDrone.position.x) +
        #                           " Y: " + str(targetInDrone.position.y) +
        #                           " Z: " + str(targetInDrone.position.z))
        #             command(xAct, yAct, zAct, 0, 0, zRotAct)

        #         else:
        #             # Fix orientation if the drone is not facing the waypoint
        #             rospy.loginfo("Fixing orientation")
        #             zRotAct = targetInDrone.orientation.z * SYS_DEFS.ANGLE_GAIN
        #             command(0, 0, 0, 0, 0, zRotAct)
        #     else:
        #         # Waypoint is reached
        #         rospy.loginfo("Waypoint reached ")
        #         # Now hover
        #         command(0, 0, 0, 0, 0, 0)
        #         # Reset to state 0
        #         actionState = 0

        # Follow Flightpath
        # elif actionState == SYS_DEFS.FOLLOW_FLIGHT_PATH_WAYPOINTS_ACTION_STATE:
        #     # Get the global counter
        #     global currentWaypointCounterForFlightPath
        #     # Get a coordinate from the xml file and assign it to targetInMap
        #     targetInMap = droneWaypointsFromXML.getWaypointsCoordinates()
        #     # Check if the anchor is reached
        #     if droneWaypointsFromXML.extractCoordinatesFromXML(currentWaypointCounterForFlightPath):
        #         # Convert drone coordinates into drone frames
        #         returnTargetInDrone(targetInMap)
        #         # Keep going if the waypoint is not reached
        #         if not wayPointReached(SYS_DEFS.WAYPOINT_ACCURACY):
        #             # Check if the drone is facing the waypoint, fix orientation if not
        #             if wayPointFaced(SYS_DEFS.ANGLE_ACCURACY):
        #                 # Adjust accelleration with angle gain and point gain
        #                 zRotAct = (targetInDrone.orientation.z  * SYS_DEFS.ANGLE_GAIN)
        #                 xAct    = (targetInDrone.position.x     * SYS_DEFS.POINT_GAIN)
        #                 yAct    = (targetInDrone.position.y     * SYS_DEFS.POINT_GAIN)
        #                 zAct    = (targetInDrone.position.z     * SYS_DEFS.POINT_GAIN)
        #                 command(xAct, yAct, zAct, 0, 0, zRotAct)

        #             else:
        #                 # Fix orientation if the drone is not facing the waypoint
        #                 rospy.loginfo("Fixing orientation")
        #                 zRotAct = targetInDrone.orientation.z * SYS_DEFS.ANGLE_GAIN
        #                 command(0, 0, 0, 0, 0, zRotAct)
        #         else:
        #             # Waypoint is reached, move to the next one
        #             rospy.loginfo("Target DD X: " + str(targetInMap.position.x) +
        #                           " Y: " + str(targetInMap.position.y) +
        #                           " Z: " + str(targetInMap.position.z))#
        #             # Increase counter, so we can move to the next waypoint
        #             currentWaypointCounterForFlightPath +=  1
        #             rospy.loginfo("Waypoint Reached " + str(currentWaypointCounterForFlightPath))

        #     else:
        #         # There are no more waypoints to go through
        #         rospy.loginfo("XML waypoints finished")
        #         # Reset counter to 0
        #         currentWaypointCounterForFlightPath = 0
        #         # Now hover so user can see that there are no more anchors
        #         command(0, 0, 0, 0, 0, 0)
        #         # Reset to actionState 0
        #         actionState = 0


        # Follow Flightpath for DWM1001
        # elif actionState == SYS_DEFS.FOLLOW_FLIGHT_PATH_DWM1001_ACTION_STATE:
        #     # Get the global counter
        #     global currentWaypointCounterForFlightPathDWM1001
        #     # Get a coordinate from anchors and assign it to targetInMap
        #     targetInMap = gazeboDwm1001.getAnchorCoordinates()
        #     # Check if the anchor is reached
        #     if gazeboDwm1001.anchorsReached(currentWaypointCounterForFlightPathDWM1001):
        #         # Convert drone coordinates into drone frames
        #         returnTargetInDrone(targetInMap)
        #         # Keep going if the waypoint is not reached
        #         if not wayPointReached(SYS_DEFS.WAYPOINT_ACCURACY):
        #             # Check if the drone is facing the waypoint, fix orientation if not
        #             if wayPointFaced(SYS_DEFS.ANGLE_ACCURACY):
        #                 # Adjust accelleration with angle gain and point gain
        #                 zRotAct = (targetInDrone.orientation.z  * SYS_DEFS.ANGLE_GAIN)
        #                 xAct    = (targetInDrone.position.x     * SYS_DEFS.POINT_GAIN)
        #                 yAct    = (targetInDrone.position.y     * SYS_DEFS.POINT_GAIN)
        #                 zAct    = (targetInDrone.position.z     * SYS_DEFS.POINT_GAIN)
        #                 command(xAct, yAct, zAct, 0, 0, zRotAct)

        #             else:
        #                 # Fix orientation if the drone is not facing the waypoint
        #                 rospy.loginfo("Fixing orientation")
        #                 zRotAct = targetInDrone.orientation.z * SYS_DEFS.ANGLE_GAIN
        #                 command(0, 0, 0, 0, 0, zRotAct)
        #         else:
        #             # Anchor is reached, move to the second one
        #             rospy.loginfo("Target DD X: " + str(targetInMap.position.x) +
        #                           " Y: " + str(targetInMap.position.y) +
        #                           " Z: " + str(targetInMap.position.z))
        #             # Increase counter, so we can move to the next anchor
        #             currentWaypointCounterForFlightPathDWM1001 +=  1
        #             rospy.loginfo("Anchor Reached " + str(currentWaypointCounterForFlightPathDWM1001))

        #     else:
        #         # There are no more anchors to go through
        #         rospy.loginfo("Anchors finished")
        #         # Reset counter to 0
        #         currentWaypointCounterForFlightPathDWM1001 = 0
        #         # Now hover so user can see that there are no more anchors
        #         command(0, 0, 0, 0, 0, 0)
        #         # Reset to actionState 0
        #         actionState = 0

        # Publish message twist produced by action state
        #pub_cmd_velocity.publish(messageTwistStamped)
        rate.sleep()

def setUpTwist( xLinear, yLinear, zLinear, xAngular, yAngular, zAngular):
    """
    Set up and return a message Twist.

    :param xLinear:  Linear velocity x axis (default 0.0)
    :param yLinear:  Linear velocity y axis (default 0.0)
    :param zLinear:  Linear velocity z axis (default 0.0)
    :param xAngular: Angular velocity x axis (default 0.0)
    :param yAngular: Angular velocity y axis (default 0.0)
    :param zAngular: Angular velocity z axis (default 0.0)

    :returns: none

    """

    global messageTwistStamped

    messageTwistStamped.twist.linear.x = xLinear
    messageTwistStamped.twist.linear.y = yLinear
    messageTwistStamped.twist.linear.z = zLinear
    messageTwistStamped.twist.angular.x = xAngular
    messageTwistStamped.twist.angular.y = yAngular
    messageTwistStamped.twist.angular.z = zAngular
    return messageTwistStamped

def command( xLinear, yLinear, zLinear, xAngular, yAngular, zAngular):
    """Form and assign message Twist.

    :argument
    xLinear -- Linear velocity x axis (default 0.0)
    yLinear -- Linear velocity y axis (default 0.0)
    zLinear -- Linear velocity z axis (default 0.0)
    xAngular -- Angular velocity x axis (default 0.0)
    yAngular -- Angular velocity y axis (default 0.0)
    zAngular -- Angular velocity z axis (default 0.0)

    """
    global messageTwistStamped
    messageTwistStamped = setUpTwist(xLinear, yLinear, zLinear, xAngular, yAngular, zAngular)

def realPoseCallBack(realPoseData):
    """Get real position from /ground_truth/state topic

    :argument
    realPoseData -- Pose data from topic

    """
    global realPose

    realPose = realPoseData.pose


def returnTargetInDrone(target):
    """Convert the coordinates of the target in the drone frame

    :argument target: Pose data from target in the Map

    """

    global currentDroneData

    # The rotation angle, anti-clockwise in radians. degree * Math.PI / 180 for clockwise
    zRot = -(navDataRotZ360 * math.pi / 180)

    # Target XYZ to the Map frame
    xt = target.position.x
    yt = target.position.y
    zt = target.position.z
    xd = currentDroneData.x
    yd = currentDroneData.y
    zd = currentDroneData.z

    # Translation of  position
    # Rotation of a point of the plane around the origin (angle in radians)
    # Same as vec2 (  +cos(a), -sin(a)  +sin(a), +cos(a) )
    targetInDrone.position.x = (math.cos(zRot)) * (xt - xd) - (math.sin(zRot)) * (yt - yd)
    targetInDrone.position.y = (math.sin(zRot)) * (xt - xd) + (math.cos(zRot)) * (yt - yd)
    targetInDrone.position.z = zt - zd
    targetInDrone.orientation.x = 0
    targetInDrone.orientation.y = 0

    # Angle from the Drone X - axis(Roll axis) to the point vector in the drone frame
    if targetInDrone.position.x is not 0:

        # atan2(y,x) is defined as the angle in the Euclidean plane, given 
        # in radians, between the positive x-axis and the ray to the point (x,y) != (0,0).
        # atan2(y,x) returns a single value theta such that -pi < theta =< pi and, for some r > 0,
        targetInDrone.orientation.z = math.atan2(targetInDrone.position.y, targetInDrone.position.x)

    # Precaution not to devide by  zero
    else:
        if targetInDrone.position.y > 0:
            targetInDrone.orientation.z = math.pi / 2

        elif targetInDrone.position.y < 0:
            targetInDrone.orientation.z = -(math.pi) / 2


def navDataCallBack(nav_msg):
    """Read navdata from the arDrone

    :argument nav_msg: NavData data from drone in the gazebo

    """
    
    global navDataRotZ360, droneState, navDataRotZ, lastDroneData, realPose

    #  Get the time stamp of drone
    currentDroneData.timeStamp = nav_msg.header.stamp

    droneState = nav_msg.state
    # For future reference get the battery level of the drone
    battery = nav_msg.batteryPercent
    navDataRotZ = nav_msg.rotZ

    # Check if Z rotation is below 0, if it is add 360 degrees to it
    if nav_msg.rotZ < 0:
        navDataRotZ360 = nav_msg.rotZ + 360
    else:
        navDataRotZ360 = nav_msg.rotZ

    # Linear Velocities
    # 1 km/s is 1000 metres per second which is 1000 [m / sec]
    currentDroneData.xVel = nav_msg.vx /SYS_DEFS.LINEAR_VELOCITY_KPS
    currentDroneData.yVel = nav_msg.vy /SYS_DEFS.LINEAR_VELOCITY_KPS
    currentDroneData.zVel = nav_msg.vz /SYS_DEFS.LINEAR_VELOCITY_KPS

    # Linear Accelerations
    # The metre per second squared is the unit of acceleration in the International System of Units (SI)
    # https://en.wikipedia.org/wiki/Metre_per_second_squared [m / s ^ 2]
    # 1 g0 	980.665 	32.1740 	9.80665 	1
    currentDroneData.xAcc = nav_msg.ax * SYS_DEFS.LINEAR_ACCELLERATION_M_PER_SEC
    currentDroneData.yAcc = nav_msg.ay * SYS_DEFS.LINEAR_ACCELLERATION_M_PER_SEC
    currentDroneData.zAcc = nav_msg.az * SYS_DEFS.LINEAR_ACCELLERATION_M_PER_SEC

    # Angular Rotations in Degrees
    currentDroneData.xRot = nav_msg.rotX
    currentDroneData.yRot = nav_msg.rotY
    currentDroneData.zRot = nav_msg.rotZ

    differenceTIme = (currentDroneData.timeStamp - lastDroneData.timeStamp).to_sec()
    # Add 0.02 incase the time is the same
    differenceTIme = differenceTIme + 0.02

    currentDroneData.xRotVel = (currentDroneData.xRot - lastDroneData.xRot)/differenceTIme  # Degrees / Sec
    currentDroneData.yRotVel = (currentDroneData.yRot - lastDroneData.yRot)/differenceTIme  # Degrees / sec
    currentDroneData.zRotVel = (currentDroneData.zRot - lastDroneData.zRot)/differenceTIme  # Degrees / sec

    if poseEstimationMethod == 1:
        currentDroneData.x = realPose.pose.position.x  # meters[m]
        currentDroneData.y = realPose.pose.position.y  # meters[m]
        currentDroneData.z = realPose.pose.position.z  # meters[m]

    # Assign the currentDroneData to lastDroneData
    lastDroneData = currentDroneData



def wayPointReached(tolerance):
    """Determine if the waypoint is reached with a tolerance level

    Keyword arguments:
    
    """
    global currentDroneData
    if abs(targetInDrone.position.x) < tolerance :
        if abs(targetInDrone.position.y) < tolerance :
            if abs(targetInDrone.position.z) < tolerance:
                return True
    return False


def wayPointFaced(tolerance):
    """Determine if the waypoint  is faced with absolute value and tolerance

    :arguments
    tolerance -- tolerance of the waypoint faced
    
    """
    if ((abs(targetInDrone.orientation.z)) < tolerance):
        return True
    return False


def publishArdronePos():
    """Publish ARDrone position
    
    """
    global realPose

    dronePos = realPose.pose  # meters[m]
    pub_ardrone_get_pose = rospy.Publisher('/aid/ardrone/get_pos/', Pose, queue_size=1)
    pub_ardrone_get_pose.publish(dronePos)


def publishWaypoints():
    """Publish waypoints from xml file 

    """

    waypointPoseFromXML = Pose()
    counter = 0
    for waypoint in droneWaypointsFromXML.getWaypontsCoordinatesInArray():
        counter = counter + 1
        waypointPoseFromXML.position.x = waypoint[0]
        waypointPoseFromXML.position.y = waypoint[1]
        waypointPoseFromXML.position.z = waypoint[2]
        rate.sleep()
        #rospy.loginfo("publioshing waypoint " + str(waypointPoseFromXML))
        pub_waypoint = rospy.Publisher('/aid/waypoint/'+ str(counter), Pose, queue_size=1)
        pub_waypoint.publish(waypointPoseFromXML)

def JoystickCallBack(data):
    """
    Callback for everytime we use the joystick

    :param data: button values from joystick


    """
    global actionState, gazeboDwm1001

    if data.buttons[SYS_DEFS.BUTTON_LAND] == 1:
        rospy.loginfo("Land Button Pressed: " + str(SYS_DEFS.BUTTON_LAND))
        actionState = 2

    elif data.buttons[SYS_DEFS.BUTTON_TAKEOFF] == 1:
        rospy.loginfo("Take off Button Pressed: " + str(SYS_DEFS.BUTTON_TAKEOFF))
        actionState = 1

    # elif data.buttons[SYS_DEFS.BUTTON_EMERGENCY] == 1:
    #     rospy.loginfo("Loading waypoints from XML file: " + str(SYS_DEFS.BUTTON_EMERGENCY))
    #     # load waypoints from xml
    #     gazeboWaypoints = LoadWaypointsInGazebo()
    #     gazeboWaypoints.addWaypointsFromXMLToGazebo()


    # elif data.buttons[SYS_DEFS.BUTTON_LOAD_DWM1001] == 1:
    #     rospy.loginfo("loading waypoint from dwm1001: " + str(SYS_DEFS.BUTTON_EMERGENCY_BACKUP))
    #     # load dwm1001 anchors
    #     gazeboDwm1001.execute()

    elif data.buttons[SYS_DEFS.BUTTON_HOVER] == 1:
        rospy.loginfo("Hover Button Pressed: " + str(SYS_DEFS.BUTTON_HOVER))
        actionState = 0
        command(0, 0, 0, 0, 0, 0)

    # elif data.buttons[SYS_DEFS.BUTTON_FOLLOW_FLIGHT_PATH_XML] == 1:
    #     rospy.loginfo("Follow flight path pressed: " + str(SYS_DEFS.BUTTON_FOLLOW_FLIGHT_PATH_XML))
    #     actionState = 8

    # elif data.buttons[SYS_DEFS.BUTTON_FOLLOW_FLIGHT_PATH_DWM1001] == 1:
    #     rospy.loginfo("Follow flight path  from dwm1001 pressed: " + str(SYS_DEFS.BUTTON_FOLLOW_FLIGHT_PATH_DWM1001))
    #     actionState = 9

    else:
        # controle axes, pitch, roll and yaw
        command(data.axes[SYS_DEFS.AXIX_ROLL] / SYS_DEFS.SCALE_ROLL,
                data.axes[SYS_DEFS.AXIS_PITCH] / SYS_DEFS.SCALE_PITCH,
                data.axes[SYS_DEFS.AXIS_Z] / SYS_DEFS.SCALE_Z ,
                0,
                0 ,
                data.axes[SYS_DEFS.AXIS_YAW] / SYS_DEFS.SCALE_YAW)

        rospy.loginfo("pitch: " + str(data.axes[SYS_DEFS.AXIS_PITCH] / SYS_DEFS.SCALE_PITCH) +
                      " roll: " + str(data.axes[SYS_DEFS.AXIX_ROLL] / SYS_DEFS.SCALE_ROLL) +
                      " yaw: " + str(data.axes[SYS_DEFS.AXIS_YAW] / SYS_DEFS.SCALE_YAW))


    pub_cmd_velocity.publish(messageTwistStamped)


def droneGUICallback( config, level):
    """Dynamic configuration to control waypoints 

    :argument config: data passed from GUI
    
    """

    global actionState, targetInMap, gazeboDwm1001


    if config["land"] == True:
        actionState = 2
        config["land"] = False
        rospy.loginfo("Reconfigure request to LAND")

    elif config["take_off"] == True:
        actionState = 1
        config["take_off"] = False
        rospy.loginfo("Reconfigure request to TAKEOFF")

    elif config["forward"] == True:
        config["forward"] = False
        actionState = 0
        command(0, -1, 0, 0, 0, 0)
        rospy.loginfo("Reconfigure request to go forward")

    elif config["backward"] == True:
        config["backward"] = False
        actionState = 0
        command(0, 1, 0, 0, 0, 0)
        rospy.loginfo("Reconfigure request to go backward")

    elif config["left"] == True:
        config["left"] = False
        actionState = 0
        command(0.5, 0, 0, 0, 0, 0)
        rospy.loginfo("Reconfigure request to go left")

    elif config["right"] == True:
        config["right"] = False
        actionState = 0
        command(-0.5, 0, 0, 0, 0, 0)
        rospy.loginfo("Reconfigure request to go right")

    elif config["hover"] == True:
        config["hover"] = False
        actionState = 0
        command(0, 0, 0, 0, 0, 0)
        rospy.loginfo("Reconfigure request to hover")

        #TODO add implementation 
    elif config["deleteWaypoints"] == True:
        config["deleteWaypoints"] = False
        deleteAllWaypointsFromGazebo()
        rospy.loginfo("""Reconfigure Request Action code: {deleteWaypoints}""".format(**config))

         #TODO add implementation 
    elif config["look_at_waypoint"] == True:
        config["look_at_waypoint"] = False
        targetInMap.position.x = config["targetInMapX"]
        targetInMap.position.y = config["targetInMapY"]
        targetInMap.position.z = config["targetInMapZ"]
        actionState = 5
        rospy.loginfo("""Reconfigure Request Action code: {look_at_waypoint}""".format(**config))

         #TODO add implementation 
    elif config["go_to_waypoint"] == True:
        config["go_to_waypoint"] = False
        targetInMap.position.x = config["targetInMapX"]
        targetInMap.position.y = config["targetInMapY"]
        targetInMap.position.z = config["targetInMapZ"]
        actionState = 4
        rospy.loginfo("""Reconfigure Request Action code: {go_to_waypoint}""".format(**config))

         #TODO add implementation 
    elif config["look_and_go"] == True:
        config["look_and_go"] = False
        targetInMap.position.x = config["targetInMapX"]
        targetInMap.position.y = config["targetInMapY"]
        targetInMap.position.z = config["targetInMapZ"]
        actionState = 7
        rospy.loginfo("""Reconfigure Request Action code: {look_and_go}""".format(**config))

         #TODO add implementation 
    elif config["load_waypoint_gazebo"] == True:
        config["load_waypoint_gazebo"] = False
        # load waypoints from xml
        gazeboWaypoints = LoadWaypointsInGazebo()
        gazeboWaypoints.addWaypointsFromXMLToGazebo()
        rospy.loginfo("""Reconfigure Request : {load_waypoint_gazebo}""".format(**config))

         #TODO add implementation 
    elif config["load_waypoint_dwm1001"] == True:
        config["load_waypoint_dwm1001"] = False
        # load dwm1001 anchors
        gazeboDwm1001.execute()
        rospy.loginfo("""Reconfigure Request : {load_waypoint_dwm1001}""".format(**config))

         #TODO add implementation 
    elif config["followFlightPathWaypoints"] == True:
        config["followFlightPathWaypoints"]= False
        actionState = 8
        rospy.loginfo("""Reconfigure Request Action code: {followFlightPathWaypoints}""".format(**config))

         #TODO add implementation 
    elif config["followFlightPathDwm1001"] == True:
        config["followFlightPathDwm1001"]= False
        actionState = 9
        rospy.loginfo("""Reconfigure Request Action code: {followFlightPathDwm1001}""".format(**config))

    # Publish command to the topic     
    pub_cmd_velocity.publish(messageTwistStamped)
    return config

#Arm the drone
def setArm():
    rospy.loginfo("Arming drone ")
    rospy.wait_for_service('/mavros/cmd/arming')
    try:
        armService = rospy.ServiceProxy('/mavros/cmd/arming', mavros_msgs.srv.CommandBool)
        armService(True)
    except rospy.ServiceException, e:
        rospy.logerr("Service arm call failed: %s"%e)

# Set mode to passed variable 
def setGuidedMode(droneMode):
    rospy.loginfo("Changing MODE to: "+ str(droneMode))
    rospy.wait_for_service('/mavros/set_mode')
    try:
        flightModeService = rospy.ServiceProxy('/mavros/set_mode', mavros_msgs.srv.SetMode)
        #http://wiki.ros.org/mavros/CustomModes for custom modes
        isModeChanged = flightModeService(custom_mode= droneMode) #return true or false
        if isModeChanged:
            rospy.loginfo("MODE changed to: "+ str(droneMode))
        else:
            rospy.logwarn("MODE changed to: "+ str(droneMode))

    except rospy.ServiceException, e:
        rospy.logerr("service set_mode call failed: %s. GUIDED Mode could not be set. Check that GPS is enabled"%e)

# Takeoff drone
def setTakeoffMode(altitudePassed):
    rospy.loginfo("Taking off.... ")
    rospy.wait_for_service('/mavros/cmd/takeoff')
    try:
        takeoffService = rospy.ServiceProxy('/mavros/cmd/takeoff', mavros_msgs.srv.CommandTOL) 
        takeoffService(altitude = altitudePassed, latitude = 0, longitude = 0, min_pitch = 0, yaw = 0)
    except rospy.ServiceException, e:
        rospy.logerr("Service takeoff call failed: %s"%e)

def setLandMode():
    rospy.loginfo("Landing.... ")
    rospy.wait_for_service('/mavros/cmd/land')
    try:
        landService = rospy.ServiceProxy('/mavros/cmd/land', mavros_msgs.srv.CommandTOL)
        #http://wiki.ros.org/mavros/CustomModes for custom modes
        isLanding = landService(altitude = 0, latitude = 0, longitude = 0, min_pitch = 0, yaw = 0)
    except rospy.ServiceException, e:
        rospy.logerr("service land call failed: %s. The vehicle cannot land "%e)     

if __name__ == '__main__':

    try:
        init()
    except rospy.ROSInterruptException:
        pass
