#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import math
import time
import random
import astar as ASTAR

#Initialize node
rospy.init_node('astar', anonymous=False)
# declare publiusher
pub = rospy.Publisher('shortest_path', String, queue_size=10)
# 10hz
rate = rospy.Rate(10)
# number of possible directions to move on the map
possibleDirections = 8
# only left right north and south
if possibleDirections == 4:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
# allow diagonal
elif possibleDirections == 8:
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

# Coordinates start and finish point
xStart = 0
yStart = 0
xFinish = 39
yFinish = 0

#TODO get coordinates from topic
def DWM1001_Network_Anchor_0callback(data):
    #rospy.loginfo('Anchor 0 data: ' + str(data.data))
    rate.sleep()

#TODO get coordinates from topic
def DWM1001_Network_Anchor_1callback(data):
    #rospy.loginfo('Anchor 1 data: ' + str(data.data))
    rate.sleep()

#TODO get coordinates from topic
def DWM1001_Network_Anchor_2callback(data):
    #rospy.loginfo('Anchor 2 data: ' + str(data.data))
    rate.sleep()

#TODO get coordinates from topic
def DWM1001_Network_Tagcallback(data):
    #rospy.loginfo('Tag data:      ' + str(data.data))
    rate.sleep()


def RouteNcallback(data):
    rospy.loginfo('Route Number: ' + str(data.data))
    rate.sleep()

    if(data.data == "1"):
        rospy.loginfo('Route Number: 1')
    elif (data.data == "2"):
        rospy.loginfo('Route Number: 2')
    elif(data.data == "3"):
        rospy.loginfo('Route Number: 3')
    elif (data.data == "0"):
        rospy.loginfo('Route Number: 0')





#TODO dummy data from dummy package, DELETE this after or switch with real deal
rospy.Subscriber('DWM1001_Network_Anchor_0', String, DWM1001_Network_Anchor_0callback)
rospy.Subscriber('DWM1001_Network_Anchor_1', String, DWM1001_Network_Anchor_1callback)
rospy.Subscriber('DWM1001_Network_Anchor_2', String, DWM1001_Network_Anchor_2callback)
rospy.Subscriber('DWM1001_Network_Tag',      String, DWM1001_Network_Tagcallback)
rospy.Subscriber('Route_N',      String, RouteNcallback)
rospy.spin()

# horizontal size of the map
mapSizeN = 40
# vertical size of the map
mapSizeM = 40
# declare empty array
the_map = []
row = [0] * mapSizeN
# create empty map
for i in range(mapSizeM):
    the_map.append(list(row))

# TODO, add obstacles if you need to fillout the map with a '0' pattern, meaning obstcles
#for x in range(mapSizeN / 8, mapSizeN * 7 / 8):
#    the_map[mapSizeM / 2][x] = 1
#for y in range(mapSizeM/8, mapSizeM * 7 / 8):
#    the_map[y][mapSizeN / 2] = 1

# TODO delete this once you finish debugging randomly select start and finish locations from a list
#startFinishList = []
#startFinishList.append((0, 0, mapSizeN - 1, mapSizeM - 1))
#startFinishList.append((0, mapSizeM - 1, mapSizeN - 1, 0))
#startFinishList.append((mapSizeN / 2 - 1, mapSizeM / 2 - 1, mapSizeN / 2 + 1, mapSizeM / 2 + 1))
#startFinishList.append((mapSizeN / 2 - 1, mapSizeM / 2 + 1, mapSizeN / 2 + 1, mapSizeM / 2 - 1))
#startFinishList.append((mapSizeN / 2 - 1, 0, mapSizeN / 2 + 1, mapSizeM - 1))
#startFinishList.append((mapSizeN / 2 + 1, mapSizeM - 1, mapSizeN / 2 - 1, 0))
#startFinishList.append((0, mapSizeM / 2 - 1, mapSizeN - 1, mapSizeM / 2 + 1))
#startFinishList.append((mapSizeN - 1, mapSizeM / 2 + 1, 0, mapSizeM / 2 - 1))
#(xStart, yStart, xFinish, yFinish) = random.choice(startFinishList)




#TODO DELETE this after debugging
#rospy.loginfo('Map size (X,Y): ' + str(mapSizeN) +' ' + str(mapSizeM))
#rospy.loginfo('Start: ' + str(xStart) +' '+ str(yStart))
#rospy.loginfo('Finish: '+ str(xFinish) + ' ' +str(yFinish))
#rospy.loginfo('Time to generate the route (seconds): '+ str(TIME.time() - TIME))
#TIME = time.time()
#route = ASTAR.pathFind(the_map, mapSizeN, mapSizeM, possibleDirections, dx, dy, xStart, yStart, xFinish, yFinish)

#TODO delete all below after debuggiong
#pub.publish(str(route))
#rospy.loginfo('Route: ' + str(route))




# mark the route on the map
#if len(route) > 0:
#    x = xStart
#    y = yStart
#    the_map[y][x] = 2
#    for i in range(len(route)):
#        j = int(route[i])
#        x += dx[j]
#        y += dy[j]
#        the_map[y][x] = 3
#the_map[y][x] = 4

# display the map with the route added
#rospy.loginfo('Map:')
#for y in range(mapSizeM):
#    for x in range(mapSizeN):
#        xy = the_map[y][x]
#        if xy == 0:
#            print '.', # space
#        elif xy == 1:
#            print 'O', # obstacle
#        elif xy == 2:
#            print 'S', # start
#        elif xy == 3:
#            print 'R', # route
#        elif xy == 4:
#            print 'F', # finish
 #   print

#raw_input('Press Enter...')



