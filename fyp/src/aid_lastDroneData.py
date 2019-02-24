#!/usr/bin/env python
import rospy



class lastDroneDataClass:


    # timestamp from ROS time
    timeStamp = rospy.Time()

    # ACtual Drone Position
    x = 0
    y = 0
    z = 0


    #Measured  Drone Velocities
    xVel = 0
    yVel = 0
    zVel = 0


    #Measured Drone Accelerations
    xAcc = 0
    yAcc = 0
    zAcc = 0


    #Measured Drone Orientation
    xRot = 0
    yRot = 0
    zRot = 0


    #Measured Drone Angular  Velocities
    xRotVel = 0
    yRotVel = 0
    zRotVel = 0
