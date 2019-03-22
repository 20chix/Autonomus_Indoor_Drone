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
from ardrone_autonomy.msg        import Navdata
import xml.etree.ElementTree     as ElementTree
from aid_loadWaypointsInGazebo   import LoadWaypointsInGazebo
from sensor_msgs.msg             import Joy
from aid_waypoints               import DroneWaypoint
import math
from geometry_msgs.msg import (
    PoseWithCovariance,
    Pose,
    Twist,
)

navDataRotZ = 0
navDataRotZ360 = 0
actionCode = 0

latchStartTime        = rospy.Duration(5.0)
externalEstimatedPose = PoseWithCovariance()
lastSavedWayHomePoint = Pose()
targetInDrone         = Pose()
land_msg              = Empty()
takeoff_msg           = Empty()
reset_msg             = Empty()
messageTwist          = Twist()
targetInDrone         = Pose()
targetInMap           = Pose()
lastSavedWaypoint     = Pose()
estimatedPoseDR       = Pose()
realPose              = PoseWithCovariance()
droneWaypointsFromXML = DroneWaypoint()



recordFlightPath      = False
recordData            = False
recordImages          = False
firstTimeSamplingData = True
latched               = False
samplingFrontCamera   = False
wasGoingBack          = False


targetInMap.position.x = 0
targetInMap.position.y = 0
targetInMap.position.z = 0
targetInMap.orientation.x = 0
targetInMap.orientation.y = 0
targetInMap.orientation.z = 0

lastSavedWaypoint.position.x = 0
lastSavedWaypoint.position.y = 0
lastSavedWaypoint.position.z = 0

currentWaypointCounterForFlightPath = 0
currentSavedWaypointPtr = 0

poseEstimationMethod = 1


estimatedPoseDR.position.x = 0
estimatedPoseDR.position.y = 0
estimatedPoseDR.position.z = 0
externalEstimatedPose.pose.position.x = 0
externalEstimatedPose.pose.position.y = 0
externalEstimatedPose.pose.position.z = 0

#Create two instances of lastDroneDataClass
lastDroneData = lastDroneDataClass()
currentDroneData = lastDroneDataClass()


lastDroneData.xRot = 0
lastDroneData.yRot = 0
lastDroneData.zRot = 0

# Safety - Loop Defines
batteryLandThreshold = 5
batteryGoHomeThreshold = 50


wayHomePtr = -1


lastSavedWayHomePoint.position.x = 0
lastSavedWayHomePoint.position.y = 0
lastSavedWayHomePoint.position.z = 0.1

# Setup a node 
rospy.init_node('fyp', anonymous=False)
lastDataSampleTime = rospy.Time()
rate = rospy.Rate(50)

# Define publishers and messages that will be used
pub_cmd_vel  = rospy.Publisher('/cmd_vel'             , Twist, queue_size=1)
pub_takeoff  = rospy.Publisher('/ardrone/takeoff'     , Empty, queue_size=1)
pub_land     = rospy.Publisher('/ardrone/land'        , Empty, queue_size=1)
pub_reset    = rospy.Publisher("ardrone/reset"        , Empty, queue_size=1)




def init():
    """Initialise ROS time,
    drone linear and angular velocity
    and subscribe to /ardrone/navdata and /ground_truth/state

    :argument

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
    rospy.Subscriber('/ardrone/navdata', Navdata, navDataCallBack)
    rospy.Subscriber('/ground_truth/state', Odometry, realPoseCallBack)
    rospy.Subscriber("joy", Joy, JoystickCallBack)

    gazeboWaypoints = LoadWaypointsInGazebo()
    gazeboWaypoints.addWaypointsFromXMLToGazebo()




    run()

def run():
    """Based on the received command, land,takeoff, go to a waypoint, pivot and go to waypoint or go to origin 

    :argument

    """
    global currentDroneData , actionCode, targetInMap, latchStartTime, latched, wayHomePtr, pub_cmd_vel, pub_takeoff, pub_land, pub_reset
    latchTime = rospy.Duration(5.0)
    rospy.loginfo("Waiting for a command")


    while not rospy.is_shutdown():

        publishWaypoints()
        publishArdronePos()

        # Reset the latch  time
        if actionCode == 0:
            latched = False

        # Take off
        elif actionCode == 1:
            if (not latched):
                latchStartTime = rospy.get_rostime()
                latched = True

            if rospy.get_rostime() < latchStartTime + latchTime:
                pub_takeoff.publish(takeoff_msg)
                rospy.loginfo("Taking off")
            else:
                command(0, 0, 0, 0, 0, 0)
                actionCode = 0
        # Land
        elif actionCode == 2:
            if currentDroneData.z <=  0.5:

                if (not latched):
                    latchStartTime = rospy.get_rostime()
                    latched = True

                if (rospy.get_rostime() < latchStartTime + latchTime):
                    pub_land.publish(land_msg)
                    rospy.loginfo("Landing...")
                else:
                    actionCode = 0

            else:
                command(0, 0, -1, 0, 0, 0)
                actionCode = 2

        # Reset
        elif actionCode == 3:
            rospy.loginfo("inside state 3...")
            pub_reset.publish(reset_msg)
            actionCode = 0

        # Go to Waypoint
        elif actionCode == 4:
            returnTargetInDrone(targetInMap)
            if not wayPointReached(SYS_DEFS.WAYPOINT_ACCURACY):

                gain = 0.3
                xAct = (targetInDrone.position.x * gain)
                yAct = (targetInDrone.position.y * gain)
                zAct = (targetInDrone.position.z * gain)

                rospy.loginfo("Real Pose X: " + str(realPose.pose.position.x) +
                              " Y: " + str(realPose.pose.position.y) +
                              " Z: " + str(realPose.pose.position.z))
                rospy.loginfo("Acceleration X: " + str(xAct) +
                              " Y: " + str(yAct) +
                              " Z: " + str(zAct))

                rospy.loginfo("Current DD X: " + str(currentDroneData.x) +
                              " Y: " + str(currentDroneData.y) +
                              " Z: " + str(currentDroneData.z))

                rospy.loginfo("Target DD X: " + str(targetInDrone.position.x) +
                              " Y: " + str(targetInDrone.position.y) +
                              " Z: " + str(targetInDrone.position.z))

                command(xAct, yAct, zAct, 0, 0, 0)
            else:
                rospy.loginfo("Waypoint Reached ")
                command(0, 0, 0, 0, 0, 0)
                actionCode = 0


                #hello


        # Look at waypoint
        elif actionCode == 5:
            rospy.loginfo("inside state 5...")
            returnTargetInDrone(targetInMap)
            gain = 0.5  # Proportional goal
            zRotAct = targetInDrone.orientation.z * gain
            command(0, 0, 0, 0, 0, zRotAct)

        # Get Waypoint
        elif actionCode == 6:
            rospy.loginfo("inside state 6...")
            returnTargetInDrone(targetInMap)
            rospy.loginfo("" + str(targetInMap))

        # Look and Go to waypoint
        elif actionCode == 7:
            returnTargetInDrone(targetInMap)
            if not wayPointReached(SYS_DEFS.WAYPOINT_ACCURACY):
                if (wayPointFaced(SYS_DEFS.ANGLE_ACCURACY)):
                    zRotAct = (targetInDrone.orientation.z * SYS_DEFS.ANGLE_GAIN)
                    xAct = (targetInDrone.position.x * SYS_DEFS.POINT_GAIN)
                    yAct = (targetInDrone.position.y * SYS_DEFS.POINT_GAIN)
                    zAct = (targetInDrone.position.z * SYS_DEFS.POINT_GAIN)
                    rospy.loginfo("Real Pose X: " + str(realPose.pose.position.x) +
                                  " Y: " + str(realPose.pose.position.y) +
                                  " Z: " + str(realPose.pose.position.z))
                    rospy.loginfo("Acceleration X: " + str(xAct) +
                                  " Y: " + str(yAct) +
                                  " Z: " + str(zAct))

                    rospy.loginfo("Current DD X: " + str(currentDroneData.x) +
                                  " Y: " + str(currentDroneData.y) +
                                  " Z: " + str(currentDroneData.z))

                    rospy.loginfo("Target DD X: " + str(targetInDrone.position.x) +
                                  " Y: " + str(targetInDrone.position.y) +
                                  " Z: " + str(targetInDrone.position.z))

                    command(xAct, yAct, zAct, 0, 0, zRotAct)
                else:
                    rospy.loginfo("fixing orientation")
                    zRotAct = targetInDrone.orientation.z *  SYS_DEFS.ANGLE_GAIN
                    command(0, 0, 0, 0, 0, zRotAct)
            else:
                rospy.loginfo("Waypoint Reached ")
                command(0, 0, 0, 0, 0, 0)
                actionCode = 0

        # Follow Flightpath
        elif actionCode == 8:

            global currentWaypointCounterForFlightPath
            targetInMap = droneWaypointsFromXML.getWaypointsCoordinates()
            if droneWaypointsFromXML.extractCoordinatesFromXML(currentWaypointCounterForFlightPath):
                returnTargetInDrone(targetInMap)
                if not wayPointReached(SYS_DEFS.WAYPOINT_ACCURACY):
                    if wayPointFaced(SYS_DEFS.ANGLE_ACCURACY):
                        zRotAct = (targetInDrone.orientation.z  * SYS_DEFS.ANGLE_GAIN)
                        xAct    = (targetInDrone.position.x     * SYS_DEFS.POINT_GAIN)
                        yAct    = (targetInDrone.position.y     * SYS_DEFS.POINT_GAIN)
                        zAct    = (targetInDrone.position.z     * SYS_DEFS.POINT_GAIN)
                        command(xAct, yAct, zAct, 0, 0, zRotAct)

                    else:
                        rospy.loginfo("fixing orientation")
                        zRotAct = targetInDrone.orientation.z * SYS_DEFS.ANGLE_GAIN
                        command(0, 0, 0, 0, 0, zRotAct)
                else:
                    rospy.loginfo("Target DD X: " + str(targetInMap.position.x) +
                                  " Y: " + str(targetInMap.position.y) +
                                  " Z: " + str(targetInMap.position.z))
                    currentWaypointCounterForFlightPath +=  1
                    rospy.loginfo("Waypoint Reached " + str(currentWaypointCounterForFlightPath))

            else:
                rospy.loginfo("XML waypoints finished")
                currentWaypointCounterForFlightPath = 0
                command(0, 0, 0, 0, 0, 0)
                actionCode = 0






        # Go Home
        elif actionCode == 9:
            returnTargetInDrone(targetInMap)
            if not wayPointReached(SYS_DEFS.WAYPOINT_ACCURACY):
                if wayPointReached(SYS_DEFS.ANGLE_ACCURACY):
                    zRotAct = targetInDrone.orientation.z * SYS_DEFS.ANGLE_GAIN
                    xAct = (targetInDrone.position.x * SYS_DEFS.POINT_GAIN)
                    yAct = (targetInDrone.position.y * SYS_DEFS.POINT_GAIN)
                    zAct = (targetInDrone.position.z * SYS_DEFS.POINT_GAIN)
                    command(xAct, yAct, zAct, 0, 0, zRotAct)
                else:
                    zRotAct = targetInDrone.orientation.z * SYS_DEFS.ANGLE_GAIN
                    command(0, 0, 0, 0, 0, zRotAct)
            # Waypoint reached
            else:
                if (wayHomePtr - 1 >= 0):
                    rospy.loginfo("Waypoint" + str(currentWaypointCounterForFlightPath) +
                                  " Reached : X " + str(realPose.pose.position.x) +
                                  " Y: " + str(realPose.pose.position.y) +
                                  " X: " + str(realPose.pose.position.z))


                    wayHomePtr -= 1
                    command(0, 0, 0, 0, 0, 0)

                else:
                    rospy.loginfo("Home sweet home")
                    actionCode = 2  # Land
                    command(0, 0, 0, 0, 0, 0)

            rospy.spin()

        pub_cmd_vel.publish(messageTwist)
        rate.sleep()

def setUpTwist( xLinear, yLinear, zLinear, xAngular, yAngular, zAngular):
    """Set up and return a message Twist.

    :argument
    xLinear -- Linear velocity x axis (default 0.0)
    yLinear -- Linear velocity y axis (default 0.0)
    zLinear -- Linear velocity z axis (default 0.0)
    xAngular -- Angular velocity x axis (default 0.0)
    yAngular -- Angular velocity y axis (default 0.0)
    zAngular -- Angular velocity z axis (default 0.0)

    """

    global messageTwist

    messageTwist.linear.x = xLinear
    messageTwist.linear.y = yLinear
    messageTwist.linear.z = zLinear
    messageTwist.angular.x = xAngular
    messageTwist.angular.y = yAngular
    messageTwist.angular.z = zAngular
    return messageTwist

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
    global messageTwist
    messageTwist = setUpTwist(xLinear, yLinear, zLinear, xAngular, yAngular, zAngular)

def realPoseCallBack(realPoseData):
    """Get real position from /ground_truth/state topic

    :argument
    realPoseData -- Pose data from topic

    """
    global realPose

    realPose = realPoseData.pose


def returnTargetInDrone(target):
    """Convert the coordinates of the target in the drone frame

    :argument
    target -- Pose data from target in the Map

    """

    global currentDroneData

    zRot = -(navDataRotZ360 * math.pi / 180)

    # Target XYZ to the Map frame
    xt = target.position.x
    yt = target.position.y
    zt = target.position.z
    xd = currentDroneData.x
    yd = currentDroneData.y
    zd = currentDroneData.z

    # Translation of  position
    targetInDrone.position.x = (math.cos(zRot)) * (xt - xd) - (math.sin(zRot)) * (yt - yd)
    targetInDrone.position.y = (math.sin(zRot)) * (xt - xd) + (math.cos(zRot)) * (yt - yd)
    targetInDrone.position.z = zt - zd
    targetInDrone.orientation.x = 0
    targetInDrone.orientation.y = 0

    # Angle from the Drone X - axis(Roll axis) to the point vector in the drone frame
    if targetInDrone.position.x is not 0:

        # atan2() returns a value in all 4 quadrants given the x, y vectors
        targetInDrone.orientation.z = math.atan2(targetInDrone.position.y, targetInDrone.position.x)

    # Precaution not to devide by  zero
    else:
        if targetInDrone.position.y > 0:
            targetInDrone.orientation.z = math.pi / 2

        elif targetInDrone.position.y < 0:
            targetInDrone.orientation.z = -(math.pi) / 2


def navDataCallBack(nav_msg):
    """Read navdata from the arDrone

    :argument
    nav_msg -- NavData data from target in the Map

    """
    
    global firstTimeSamplingData, navDataRotZ360, droneState, battery, navDataRotZ, lastDroneData, realPose

    currentDroneData.timeStamp = nav_msg.header.stamp

    droneState = nav_msg.state
    battery = nav_msg.batteryPercent
    navDataRotZ = nav_msg.rotZ

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

    if not firstTimeSamplingData:

        differenceTIme = (currentDroneData.timeStamp - lastDroneData.timeStamp).to_sec()
        differenceTIme = differenceTIme + 0.02

        currentDroneData.xRotVel = (currentDroneData.xRot - lastDroneData.xRot)/differenceTIme  # Degrees / Sec
        currentDroneData.yRotVel = (currentDroneData.yRot - lastDroneData.yRot)/differenceTIme  # Degrees / sec
        currentDroneData.zRotVel = (currentDroneData.zRot - lastDroneData.zRot)/differenceTIme  # Degrees / sec

        if poseEstimationMethod == 1:
            currentDroneData.x = realPose.pose.position.x  # meters[m]
            currentDroneData.y = realPose.pose.position.y  # meters[m]
            currentDroneData.z = realPose.pose.position.z  # meters[m]

        elif poseEstimationMethod == 2:
            currentDroneData.x = externalEstimatedPose.pose.position.x  # meters[m]
            currentDroneData.y = externalEstimatedPose.pose.position.y  # meters[m]
            currentDroneData.z = externalEstimatedPose.pose.position.z  # meters[m]

    firstTimeSamplingData = False
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
    """Determine if the waypoint  is faced 

    :arguments
    tolerance -- tolerance of the waypoint faced
    
    """
    if ((abs(targetInDrone.orientation.z)) < tolerance):
        return True
    return False


# Decide on what safety action to follow
def decideSafetyAction():
    global actionCode, wasGoingBack, battery, testBatteryBellowLand, testBatteryBellowGoHome, testNoWifi, noWifi
    # Emergency Land
    if (battery <= batteryLandThreshold | testBatteryBellowLand):
        actionCode = 2
    else:
        if (battery <= batteryGoHomeThreshold | testBatteryBellowGoHome):
            wasGoingBack = True
        elif (noWifi | testNoWifi):
            wasGoingBack = True
        else:
            if wasGoingBack:
                wasGoingBack = False
                actionCode = 0
                command(0, 0, 0, 0, 0, 0)

            if ((abs(currentDroneData.x - lastSavedWayHomePoint.position.x) >= 0.5) |
                    (abs(currentDroneData.x - lastSavedWayHomePoint.position.y) >= 0.5) |
                    (abs(currentDroneData.x - lastSavedWayHomePoint.position.z) >= 0.5)):

                if wayHomePtr >= 0:
                    lastSavedWayHomePoint.position.x = currentDroneData.x
                    lastSavedWayHomePoint.position.y = currentDroneData.y
                    lastSavedWayHomePoint.position.z = currentDroneData.z
                else:
                    lastSavedWayHomePoint.position.x = 0
                    lastSavedWayHomePoint.position.y = 0
                    lastSavedWayHomePoint.position.z = 0.2




def publishArdronePos():

    global realPose

    dronePos = realPose.pose  # meters[m]
    pub_ardrone_get_pose = rospy.Publisher('/aid/ardrone/get_pos/', Pose, queue_size=1)
    pub_ardrone_get_pose.publish(dronePos)


def publishWaypoints():


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

    global actionCode

    rospy.loginfo(data.axes[SYS_DEFS.AXIS_YAW])

    if data.buttons[SYS_DEFS.BUTTON_EMERGENCY] == 1:
        rospy.loginfo("Emergency Button Pressed: " + str(SYS_DEFS.BUTTON_EMERGENCY))

    elif data.buttons[SYS_DEFS.BUTTON_EMERGENCY_BACKUP] == 1:
        rospy.loginfo("Emergency backup Button Pressed: " + str(SYS_DEFS.BUTTON_EMERGENCY_BACKUP))

    elif data.buttons[SYS_DEFS.BUTTON_LAND] == 1:
        rospy.loginfo("Land Button Pressed: " + str(SYS_DEFS.BUTTON_LAND))
        actionCode = 2

    elif data.buttons[SYS_DEFS.BUTTON_TAKEOFF] == 1:
        rospy.loginfo("Take off Button Pressed: " + str(SYS_DEFS.BUTTON_TAKEOFF))
        actionCode = 1

    elif data.buttons[SYS_DEFS.BUTTON_EMERGENCY] == 1:
        rospy.loginfo("Emergency landing button pressed: " + str(SYS_DEFS.BUTTON_EMERGENCY))
        pub_reset.publish(reset_msg)

    elif data.buttons[SYS_DEFS.BUTTON_EMERGENCY_BACKUP] == 1:
        rospy.loginfo("Emergency landing backup pressed: " + str(SYS_DEFS.BUTTON_EMERGENCY_BACKUP))
        pub_reset.publish(reset_msg)

    elif data.buttons[SYS_DEFS.BUTTON_HOVER] == 1:
        rospy.loginfo("Hover Button Pressed: " + str(SYS_DEFS.BUTTON_HOVER))
        actionCode = 0
        command(0, 0, 0, 0, 0, 0)

    elif data.buttons[SYS_DEFS.BUTTON_FOLLOW_FLIGHT_PATH] == 1:
        rospy.loginfo("Follow flight path pressed: " + str(SYS_DEFS.BUTTON_FOLLOW_FLIGHT_PATH))
        actionCode = 8

    else:
        command(data.axes[SYS_DEFS.AXIS_PITCH] / SYS_DEFS.SCALE_PITCH,
                data.axes[SYS_DEFS.AXIX_ROLL] / SYS_DEFS.SCALE_ROLL,
                data.axes[SYS_DEFS.AXIS_Z] / SYS_DEFS.SCALE_Z ,
                0,
                0 ,
                data.axes[SYS_DEFS.AXIS_YAW] / SYS_DEFS.SCALE_YAW)

        rospy.loginfo("pitch" + str(data.axes[SYS_DEFS.AXIS_PITCH] / SYS_DEFS.SCALE_PITCH) +
                      " roll " + str(data.axes[SYS_DEFS.AXIX_ROLL] / SYS_DEFS.SCALE_ROLL) +
                      " yaw: " + str(data.axes[SYS_DEFS.AXIS_YAW] / SYS_DEFS.SCALE_YAW))


def droneGUICallback( config, level):
    """Dynamic configuration to control waypoints 

    :argument
    config -- data passed from GUI
    
    """

    global actionCode, targetInMap

    if config["land"] == True:
        actionCode = 2
        config["land"] = False
        rospy.loginfo("""Reconfigure Request Action code: {actionCode}""".format(**config))

    elif config["take_off"] == True:
        actionCode = 1
        config["take_off"] = False
        rospy.loginfo("""Reconfigure Request Action code: {actionCode}""".format(**config))

    elif config["forward"] == True:
        config["forward"] = False
        actionCode = 0
        command(1, 0, 0, 0, 0, 0)
        rospy.loginfo("""Reconfigure Request Action code: {actionCode}""".format(**config))

    elif config["backward"] == True:
        config["backward"] = False
        actionCode = 0
        command(-1, 0, 0, 0, 0, 0)
        rospy.loginfo("""Reconfigure Request Action code: {actionCode}""".format(**config))

    elif config["left"] == True:
        config["left"] = False
        actionCode = 0
        command(0, 0.5, 0, 0, 0, 0)
        rospy.loginfo("""Reconfigure Request Action code: {actionCode}""".format(**config))

    elif config["right"] == True:
        config["right"] = False
        actionCode = 0
        command(0, -0.5, 0, 0, 0, 0)
        rospy.loginfo("""Reconfigure Request Action code: {actionCode}""".format(**config))

    elif config["hover"] == True:
        config["hover"] = False
        actionCode = 0
        command(0, 0, 0, 0, 0, 0)
        rospy.loginfo("""Reconfigure Request Action code: {actionCode}""".format(**config))

    elif config["look_at_waypoint"] == True:
        config["look_at_waypoint"] = False
        targetInMap.position.x = config["targetInMapX"]
        targetInMap.position.y = config["targetInMapY"]
        targetInMap.position.z = config["targetInMapZ"]
        actionCode = 5
        rospy.loginfo("""Reconfigure Request Action code: {actionCode}""".format(**config))

    elif config["go_to_waypoint"] == True:
        config["go_to_waypoint"] = False
        targetInMap.position.x = config["targetInMapX"]
        targetInMap.position.y = config["targetInMapY"]
        targetInMap.position.z = config["targetInMapZ"]
        actionCode = 4
        rospy.loginfo("""Reconfigure Request Action code: {actionCode}""".format(**config))

    elif config["look_and_go"] == True:
        config["look_and_go"] = False
        targetInMap.position.x = config["targetInMapX"]
        targetInMap.position.y = config["targetInMapY"]
        targetInMap.position.z = config["targetInMapZ"]
        actionCode = 7
        rospy.loginfo("""Reconfigure Request Action code: {actionCode}""".format(**config))

    elif config["get_waypoint"] == True:
        config["get_waypoint"] = False
        targetInMap.position.x = config["targetInMapX"]
        targetInMap.position.y = config["targetInMapY"]
        targetInMap.position.z = config["targetInMapZ"]
        actionCode = 6
        rospy.loginfo("""Reconfigure Request Action code: {actionCode}""".format(**config))

    elif config["followFlightPath"] == True:
        config["followFlightPath"]= False
        actionCode = 8
        rospy.loginfo("""Reconfigure Request Action code: {actionCode}""".format(**config))

    return config


if __name__ == '__main__':

    try:
        init()
    except rospy.ROSInterruptException:
        pass
