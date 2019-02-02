#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseWithCovariance
from beginner_tutorials.cfg import GUIConfig
from dynamic_reconfigure.server import Server
from nav_msgs.msg import Odometry
from lastDroneData import lastDroneDataClass
from lastDroneDataCopy import lastDroneDataClassCopy
from ardrone_autonomy.msg import Navdata
import math





navDataRotZ = 0
navDataRotZ360 = 0
actionCode = 0

#move_msg = Twist()
#move_msg = setUpTwist(0, 0, 0, 0, 0, 0)


targetInMap = Pose()
lastSavedWaypoint = Pose()
estimatedPoseDR = Pose()
externalEstimatedPose = PoseWithCovariance()
lastSavedWayHomePoint = Pose()
targetInDrone = Pose()

latchStartTime = rospy.Duration(5.0)

land_msg = Empty()
takeoff_msg = Empty()
reset_msg = Empty()
messageTwist = Twist()
targetInDrone = Pose()


ctrl_c = False


targetInMap.position.x = 0
targetInMap.position.y = 0
targetInMap.position.z = 0
targetInMap.orientation.x = 0
targetInMap.orientation.y = 0
targetInMap.orientation.z = 0
lastSavedWaypoint.position.x = 0
lastSavedWaypoint.position.y = 0
lastSavedWaypoint.position.z = 0
lastSavedWaypoint.position.x = 0
lastSavedWaypoint.position.y = 0
lastSavedWaypoint.position.z = 0
currentWaypointPtr = -1
currentSavedWaypointPtr = 0
angleAccuracy = 10
waypointAccuracy = 0.95
pointGain = 0.5
angleGain = 0.5
recordFlightPath = False
recordData = False
recordImages = False

firstTimeSamplingData = True
latched = False

samplingFrontCamera = False
poseEstimationMethod = 1
estimatedPoseDR.position.x = 0
estimatedPoseDR.position.y = 0
estimatedPoseDR.position.z = 0
externalEstimatedPose.pose.position.x = 0
externalEstimatedPose.pose.position.y = 0
externalEstimatedPose.pose.position.z = 0
# Safety - Loop Defines
batteryLandThreshold = 5
batteryGoHomeThreshold = 50
wayHomePtr = -1
lastSavedWayHomePoint.position.x = 0
lastSavedWayHomePoint.position.y = 0
lastSavedWayHomePoint.position.z = 0.1
wasGoingBack = False
# Firstly we setup a ros node, so that we can communicate with the other packages
rospy.init_node('beginner_tutorials', anonymous=False)
lastDataSampleTime = rospy.Time()
rate = rospy.Rate(50)
# define the differen publishers and messages that will be used
pub_cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
pub_takeoff = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=1)
pub_land = rospy.Publisher('/ardrone/land', Empty, queue_size=1)
pub_reset = rospy.Publisher("ardrone/reset", Empty, queue_size=1)
lastDroneData = lastDroneDataClass()
currentDroneData = lastDroneDataClass()
lastDroneData.xRot = 0
lastDroneData.yRot = 0
lastDroneData.zRot = 0



def init():
    global messageTwist, lastDroneData

    lastDroneData.timeStamp = rospy.Time()
    currentDroneData.timeStamp = rospy.Time()
    rospy.loginfo("Current dd " + str(currentDroneData.timeStamp))
    rospy.loginfo("last c  dd  " + str(lastDroneData.timeStamp))
    messageTwist = setUpTwist(0, 0, 0, 0, 0, 0)



    Server(GUIConfig, droneGUICallback)
    rospy.Subscriber('/ardrone/navdata', Navdata, navDataCallBack)
    rospy.Subscriber('/ground_truth/state', Odometry, realPoseCallBack)



    run()

def run():
    global currentDroneData , actionCode, latchStartTime, latched, wayHomePtr, pub_cmd_vel, pub_takeoff, pub_land, pub_reset



    rospy.loginfo("inside run...")
    latchTime = rospy.Duration(5.0)


    # Decide Saftey Action if Saftey-Loops are enables
    # if (safeFlight):
    #    decideSafetyAction()

    while not rospy.is_shutdown():

        # Reset the latch  time
        if actionCode == 0:
            latched = False

        # Take off
        elif actionCode == 1:
            rospy.loginfo("inside state 1...")
            if (not latched):
                latchStartTime = rospy.get_rostime()
                latched = True

            if rospy.get_rostime() < latchStartTime + latchTime:
                pub_takeoff.publish(takeoff_msg)
                rospy.loginfo("taking off")
                rospy.loginfo("going to %s %s %s" % (
                    estimatedPoseDR.position.x, estimatedPoseDR.position.y,
                    estimatedPoseDR.position.y))

            else:
                command(0, 0, 0, 0, 0, 0)
                actionCode = 0
        # Land
        elif actionCode == 2:
            rospy.loginfo("inside state 2...")
            if currentDroneData.z <= 0.5:

                if (not latched):
                    latchStartTime = rospy.get_rostime()
                    latched = True

                if (rospy.get_rostime() < latchStartTime + latchTime):
                    pub_land.publish(land_msg)
                    rospy.loginfo("landing")
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
            rospy.loginfo("inside state 4...")
            returnTargetInDrone(targetInMap)
            gain = 0.3
            xAct = (targetInDrone.position.x * gain)
            yAct = (targetInDrone.position.y * gain)
            zAct = (targetInDrone.position.z * gain)
            rospy.loginfo("going to %s %s %s %s %s %s" % (xAct, yAct, zAct, 0, 0, 0))
            command(xAct, yAct, zAct, 0, 0, 0)

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
            if not wayPointReached(waypointAccuracy):
                if (wayPointFaced(angleAccuracy)):
                    zRotAct = (targetInDrone.orientation.z * angleGain)
                    xAct = (targetInDrone.position.x * pointGain)
                    yAct = (targetInDrone.position.y * pointGain)
                    zAct = (targetInDrone.position.z * pointGain)
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
                    zRotAct = targetInDrone.orientation.z *  angleGain
                    command(0, 0, 0, 0, 0, zRotAct)
            else:
                rospy.loginfo("Waypoint Reached ")
                command(0, 0, 0, 0, 0, 0)
                actionCode = 0

        # Follow Flightpath
        elif actionCode == 8:
            rospy.loginfo("inside state 8...")
            returnTargetInDrone(targetInMap)
            if (currentWaypointPtr > -1):
                # If Waypoint reached
                if (not wayPointReached(waypointAccuracy)):
                    # If waypoint faced
                    if (wayPointFaced(angleAccuracy)):
                        zRotAct = targetInDrone.orientation.z * angleGain
                        xAct = (targetInDrone.position.x * pointGain)
                        yAct = (targetInDrone.position.y * pointGain)
                        zAct = (targetInDrone.position.z * pointGain)
                        command(xAct, yAct, zAct, 0, 0, zRotAct)
                    else:
                        zRotAct = targetInDrone.orientation.z * angleGain
                        command(0, 0, 0, 0, 0, zRotAct)
                else:
                    rospy.loginfo("Waypoint" + str(currentWaypointPtr) +
                                  " Reached : X " + str(targetInMap.position.x) +
                                  " Y: " + str(targetInMap.position.y) +
                                  " X: " + str(targetInMap.position.z))
                    command(0, 0, 0, 0, 0, 0)
            else:
                command(0, 0, 0, 0, 0, 0)

        # Go Home
        elif actionCode == 9:

            rospy.loginfo("inside state 9...")
            returnTargetInDrone(targetInMap)
            if (not wayPointReached(waypointAccuracy)):
                if (wayPointReached(angleAccuracy)):
                    zRotAct = targetInDrone.orientation.z * angleGain
                    xAct = (targetInDrone.position.x * pointGain)
                    yAct = (targetInDrone.position.y * pointGain)
                    zAct = (targetInDrone.position.z * pointGain)
                    command(xAct, yAct, zAct, 0, 0, zRotAct)
                else:
                    zRotAct = targetInDrone.orientation.z * angleGain
                    command(0, 0, 0, 0, 0, zRotAct)
            # Waypoint reached
            else:
                if (wayHomePtr - 1 >= 0):
                    rospy.loginfo("Waypoint" + str(currentWaypointPtr) +
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

""""This is because pubblishing in topics sometimes fails the first time you pubblish.
In continuos pubblishing systems therw is no big deal but in systems that pubblish only once
it IS very important"""

def publishOnceInCmdVel(self, cmd):
    while not ctrl_c:
        connections = pub_cmd_vel.get_num_connections()
        if connections > 0:
            pub_cmd_vel.publish(cmd)
            rospy.loginfo("Publish in cmd_vel...")
            break
        else:
            rate.sleep()

def setUpTwist( xLinear, yLinear, zLinear, xAngular, yAngular, zAngular):

    global messageTwist
    messageTwist.linear.x = xLinear
    messageTwist.linear.y = yLinear
    messageTwist.linear.z = zLinear
    messageTwist.angular.x = xAngular
    messageTwist.angular.y = yAngular
    messageTwist.angular.z = zAngular
    return messageTwist

def command( xLinear, yLinear, zLinear, xAngular, yAngular, zAngular):
    global messageTwist
    messageTwist = setUpTwist(xLinear, yLinear, zLinear, xAngular, yAngular, zAngular)

def realPoseCallBack( realPoseData):
    global realPose

    realPose = realPoseData.pose

# Convert the coordinates of the target in the drone frame
def returnTargetInDrone(target):
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
    if (targetInDrone.position.x is not 0):

        # atan2() returns a value in all 4 quadrants given the x, y vectors
        targetInDrone.orientation.z = math.atan2(targetInDrone.position.y, targetInDrone.position.x)

    # Precaution not to devide by  zero
    else:
        if (targetInDrone.position.y > 0):
            targetInDrone.orientation.z = math.pi / 2

        elif (targetInDrone.position.y < 0):
            targetInDrone.orientation.z = -(math.pi) / 2

# NavData readings
def navDataCallBack(nav_msg):
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
    currentDroneData.xVel = nav_msg.vx/1000  # [m / sec]
    currentDroneData.yVel = nav_msg.vy/1000  # [m / sec]
    currentDroneData.zVel = nav_msg.vz/1000  # [m / sec]

    # Linear Accelerations
    currentDroneData.xAcc = nav_msg.ax * 9.81  # [m / s ^ 2]
    currentDroneData.yAcc = nav_msg.ay * 9.81  # [m / s ^ 2]
    currentDroneData.zAcc = nav_msg.az * 9.81  # [m / s ^ 2]

    # Angular Rotations
    currentDroneData.xRot = nav_msg.rotX  # Degrees
    currentDroneData.yRot = nav_msg.rotY  # Degrees
    currentDroneData.zRot = nav_msg.rotZ  # Degrees

    if not firstTimeSamplingData:

        dt = (currentDroneData.timeStamp - lastDroneData.timeStamp).to_sec()
        dt = dt + 0.02

        currentDroneData.xRotVel = (currentDroneData.xRot - lastDroneData.xRot)/dt  # Degrees / Sec
        currentDroneData.yRotVel = (currentDroneData.yRot - lastDroneData.yRot)/dt  # Degrees / sec
        currentDroneData.zRotVel = (currentDroneData.zRot - lastDroneData.zRot)/dt  # Degrees / sec

        if poseEstimationMethod == 1:
            currentDroneData.x = realPose.pose.position.x  # meters[m]
            currentDroneData.y = realPose.pose.position.y  # meters[m]
            currentDroneData.z = realPose.pose.position.z  # meters[m]

        elif poseEstimationMethod == 2:
            currentDroneData.x = externalEstimatedPose.pose.position.x  # meters[m]
            currentDroneData.y = externalEstimatedPose.pose.position.y  # meters[m]
            currentDroneData.z = externalEstimatedPose.pose.position.z  # meters[m]

        elif poseEstimationMethod == 3:
            estimatePoseDeadReckoning()
            currentDroneData.x = estimatedPoseDR.pose.position.x  # meters[m]
            currentDroneData.y = estimatedPoseDR.pose.position.y  # meters[m]
            currentDroneData.z = estimatedPoseDR.pose.position.z  # meters[m]

    # Motor  PWM
    # values(not available in tum_simulator)
    # currentDroneData.motor1 = nav_msg.motor1;
    # currentDroneData.motor2 = nav_msg.motor2;
    # currentDroneData.motor3 = nav_msg.motor3;
    # currentDroneData.motor4 = nav_msg.motor4;

    firstTimeSamplingData = False
    lastDroneData = currentDroneData

# Estimate the Pose internaly using Dead Reckoning
def estimatePoseDeadReckoning():

    zRot = navDataRotZ360 * math.pi / 180
    dt = (currentDroneData.timeStamp - lastDroneData.timeStamp).toSec()
    xd1 = estimatedPoseDR.position.x
    xd2 = currentDroneData.xVel * dt
    yd1 = estimatedPoseDR.position.y
    yd2 = currentDroneData.yVel * dt

    estimatedPoseDR.position.x = xd1 + (math.cos(zRot) * (xd2) - math.sin(zRot) * (yd2))
    estimatedPoseDR.position.y = yd1 + (math.sin(zRot) * (xd2) + math.cos(zRot) * (yd2))
    estimatedPoseDR.position.z = estimatedPoseDR.position.z + currentDroneData.zVel * dt  # m

# Determine if the waypoint has been reached with a tolerance level
def wayPointReached(tolerance):
    global currentDroneData
    if ((abs(targetInDrone.position.x)) < tolerance) :
        if ((abs(targetInDrone.position.y)) < tolerance) :
            if ((abs(targetInDrone.position.z)) < tolerance):
                return True
    return False

# Determine if the waypoint is being faced with a tolerance level
def wayPointFaced(tolerance):
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

# function that stops the drone from any movement
def strop_drone(self):
    rospy.loginfo("Stopping...")
    command(0, 0, 0, 0, 0, 0)
    publishOnceInCmdVel(messageTwist)

# function that makes the drone turn 90 degrees
def turn_drone(self):
    rospy.loginfo("Turning...")
    command(0, 0, 0, 0, 0, 1)
    publishOnceInCmdVel(messageTwist)

# function that makes the drone move forward
def move_forward_drone(self):
    rospy.loginfo("Moving forward...")
    command(1, 0, 0, 0, 0, 0)
    publishOnceInCmdVel(messageTwist)

def move_square(self):

    # make the drone takeoff
    i = 0
    while not i == 3:
        pub_takeoff.publish(takeoff_msg)
        rospy.loginfo("Taking off...")
        time.sleep(1)
        i += 1

    # define the seconds to move in each side of the square (which is taken from the goal) and the seconds to turn
    sideSeconds = 2
    turnSeconds = 1.5

    i = 0
    for i in range(0, 4):
        # Logic that makes the robot move forward and turn
        move_forward_drone()
        time.sleep(sideSeconds)
        turn_drone()
        time.sleep(turnSeconds)
        rospy.loginfo("loops " + str(i))
        # the sequence is computed at 1 HZ frequency

    strop_drone()
    i = 0

    while not i == 3:
        pub_land.publish(land_msg)
        rospy.loginfo('Landing')
        time.sleep(1)
        i += 1

def droneGUICallback( config, level):
    global actionCode, targetInMap
    #actionCode = int(config["actionCode"])

    if config["land"] == True:
        actionCode = 2
        config["land"] = False
    elif config["take_off"] == True:
        actionCode = 1
        config["take_off"] = False
    elif config["forward"] == True:
        config["forward"] = False
        actionCode = 0
        command(1, 0, 0, 0, 0, 0)
    elif config["backward"] == True:
        config["backward"] = False
        actionCode = 0
        command(-1, 0, 0, 0, 0, 0)
    elif config["left"] == True:
        config["left"] = False
        actionCode = 0
        command(0, 0.5, 0, 0, 0, 0)
    elif config["right"] == True:
        config["right"] = False
        actionCode = 0
        command(0, -0.5, 0, 0, 0, 0)
    elif config["hover"] == True:
        config["hover"] = False
        actionCode = 0
        command(0, 0, 0, 0, 0, 0)
    elif config["look_at_waypoint"] == True:
        config["look_at_waypoint"] = False
        targetInMap.position.x = config["targetInMapX"]
        targetInMap.position.y = config["targetInMapY"]
        targetInMap.position.z = config["targetInMapZ"]
        actionCode = 5
    elif config["go_to_waypoint"] == True:
        config["go_to_waypoint"] = False
        targetInMap.position.x = config["targetInMapX"]
        targetInMap.position.y = config["targetInMapY"]
        targetInMap.position.z = config["targetInMapZ"]
        actionCode = 4
    elif config["look_and_go"] == True:
        config["look_and_go"] = False
        targetInMap.position.x = config["targetInMapX"]
        targetInMap.position.y = config["targetInMapY"]
        targetInMap.position.z = config["targetInMapZ"]
        actionCode = 7

    elif config["get_waypoint"] == True:
        config["get_waypoint"] = False
        targetInMap.position.x = config["targetInMapX"]
        targetInMap.position.y = config["targetInMapY"]
        targetInMap.position.z = config["targetInMapZ"]
        actionCode = 6

    rospy.loginfo("""Reconfigure Request: {actionCode}""".format(**config))
    return config


if __name__ == '__main__':


    try:

        # move_square.actionCode = 2
        init()
        # time.sleep(3)
        # move_square.actionCode = 2

    except rospy.ROSInterruptException:
        pass
