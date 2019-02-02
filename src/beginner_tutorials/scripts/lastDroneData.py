#!/usr/bin/env python
import rospy
class lastDroneDataClass:
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


#
#
#
# class lastDroneData:
#
#     def __init__(self,x, y, z, xVel, yVel, zVel, xAcc, yAcc, zAcc, xRot, yRot, zRot, xRotVel, yRotVel, zRotVel ):
#         # ACtual Drone Position
#         self._x = x
#         self._y = y
#         self._z = z
#
#
#         #Measured  Drone Velocities
#         self._xVel = xVel
#         self._yVel = yVel
#         self._zVel = zVel
#
#
#         #Measured Drone Accelerations
#         self._xAcc = xAcc
#         self._yAcc = yAcc
#         self._zAcc = zAcc
#
#
#         #Measured Drone Orientation
#         self._xRot = xRot
#         self._yRot = yRot
#         self._zRot = zRot
#
#
#         #Measured Drone Angular  Velocities
#         self._xRotVel = xRotVel
#         self._yRotVel = yRotVel
#         self._zRotVel = zRotVel
#
#
#
#
#
#     def getX(self):
#         return self._x
#
#     def getY(self):
#         return self._y
#
#     def getZ(self):
#         return self._y
#
#
#     def setX(self, x):
#         self._x = x
#
#     def setY(self, y):
#         self._y = y
#
#     def setZ(self, z):
#         self._z = z
#
#
#
#
#     def getxVel(self):
#         return self._xVel
#
#     def getyVel(self):
#         return self._yVel
#
#     def getzVel(self):
#         return self._zVel
#
#     def setxVel(self, xVel):
#         self._xVel = xVel
#
#     def setyVel(self, yVel):
#         self._yVel = yVel
#
#     def setzVel(self, zVel):
#         self._zVel = zVel
#
#
#
#     def getxAcc(self):
#         return self._xAcc
#
#     def getyAcc(self):
#         return self._yAcc
#
#     def getzAcc(self):
#         return self._zAcc
#
#     def setxAcc(self, xAcc):
#         self._xAcc = xAcc
#
#     def setyAcc(self, yAcc):
#         self._yAcc = yAcc
#
#     def setzAcc(self, zAcc):
#         self._zAcc = zAcc
#
#
#     def getxRot(self):
#         return self._xRot
#
#     def getyRot(self):
#         return self._yAcc
#
#     def getzRot(self):
#         return self._zRot
#
#     def setxRot(self, xRot):
#         self._xRot = xRot
#
#     def setyRot(self, yRot):
#         self._yRot = yRot
#
#     def setzRot(self, zRot):
#         self._zRot = zRot
#
#
#
#     def getxRotVel(self):
#         return self._xRotVel
#
#     def getyRotVel(self):
#         return self._yRotVel
#
#     def getzRotVel(self):
#         return self._zRotVel
#
#     def setxRotVel(self, xRotVel):
#         self._xRotVel = xRotVel
#
#     def setyRotVel(self, yRotVel):
#         self._yRotVel = yRotVel
#
#     def setzRotVel(self, zRotVel):
#         self._zRotVel = zRotVel
#
#
#
