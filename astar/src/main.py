#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import math
import time
import random
import astar as ASTAR
from visualization_msgs.msg import *
from geometry_msgs.msg import Point

#Initialize node
rospy.init_node('astar', anonymous=False)
# declare publisher
pubblishRoute = rospy.Publisher('shortest_path', String, queue_size=10)
# Initialize rate to 10hz
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

# TODO replace these coordinate with coordinates from dwm1001
anchor0Coordinates_x = 0
anchor0Coordinates_y = 0
anchor0Coordinates_z = 0

anchor1Coordinates_x = 0
anchor1Coordinates_y = 0
anchor1Coordinates_z = 0

anchor2Coordinates_x = 0
anchor2Coordinates_y = 0
anchor2Coordinates_z = 0

anchor3Coordinates_x = 0
anchor3Coordinates_y = 0
anchor3Coordinates_z = 0

tagCoordinates_x = 0
tagCoordinates_y = 0
tagCoordinates_z = 0


# horizontal size of the map
mapSizeN = 200
# vertical size of the map
mapSizeM = 200
# declare empty array
the_map = []
row = [0] * mapSizeN
# create empty map
for i in range(mapSizeM):
    the_map.append(list(row))



pub_line_min_dist = rospy.Publisher('~astar_line_min_dist', Marker, queue_size=1)

# Draw a line
def DrawALine(tagx, tagy, tagz, goalx, goaly, goalz):
    marker = Marker()
    marker.header.frame_id = "map"
    marker.type = marker.LINE_STRIP
    marker.action = marker.ADD

    # marker scale
    marker.scale.x = 0.05
    marker.scale.y = 0.05
    marker.scale.z = 0.05

    # marker color
    marker.color.a = 1.0
    marker.color.r = 1.0
    marker.color.g = 1.0
    marker.color.b = 0.0

    # marker orientaiton
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0

    # marker line points
    marker.points = []


    # first point
    first_line_point = Point()
    first_line_point.x = tagx
    first_line_point.y = tagy
    first_line_point.z = tagz
    marker.points.append(first_line_point)
    # second point
    second_line_point = Point()
    second_line_point.x = goalx
    second_line_point.y = goaly
    second_line_point.z = goalz
    marker.points.append(second_line_point)


    # Publish the Marker
    pub_line_min_dist.publish(marker)

    rospy.loginfo('Drawing line')



#TODO get coordinates from topic
def DWM1001_Network_Anchor_0callback(data):
    global anchor0Coordinates_x,anchor0Coordinates_y, anchor0Coordinates_z

    coordinates = data.data.split()
    anchor0Coordinates_x = int(float(coordinates[0]))
    anchor0Coordinates_y = int(float(coordinates[1]))
    anchor0Coordinates_z = int(float(coordinates[2]))

#TODO get coordinates from topic
def DWM1001_Network_Anchor_1callback(data):
    global anchor1Coordinates_x,anchor1Coordinates_y, anchor1Coordinates_z

    coordinates = data.data.split()
    anchor1Coordinates_x = int(float(coordinates[0]))
    anchor1Coordinates_y = int(float(coordinates[1]))
    anchor1Coordinates_z = int(float(coordinates[2]))


#TODO get coordinates from topic
def DWM1001_Network_Anchor_2callback(data):
    global anchor2Coordinates_x,anchor2Coordinates_y, anchor2Coordinates_z

    coordinates = data.data.split()
    anchor2Coordinates_x = int(float(coordinates[0]))
    anchor2Coordinates_y = int(float(coordinates[1]))
    anchor2Coordinates_z = int(float(coordinates[2]))

#TODO get coordinates from topic
def DWM1001_Network_Anchor_3callback(data):
    global anchor3Coordinates_x,anchor3Coordinates_y, anchor3Coordinates_z

    coordinates = data.data.split()
    anchor3Coordinates_x = int(float(coordinates[0]))
    anchor3Coordinates_y = int(float(coordinates[1]))
    anchor3Coordinates_z = int(float(coordinates[2]))


#TODO get coordinates from topic
def DWM1001_Network_Tagcallback(data):
    global tagCoordinates_x, tagCoordinates_y, tagCoordinates_z

    coordinates = data.data.split()
    tagCoordinates_x = int(float(coordinates[0]))
    tagCoordinates_y = int(float(coordinates[1]))
    tagCoordinates_z = int(float(coordinates[2]))


def RouteNcallback(data):
    global routeNumber
    global pubblishRoute

    rate.sleep()

    # Check if FYP needs route 0, meaning the drone have to go to anchor 1
    if(data.data == "0"):
        # Calculate shortest path
        route = ASTAR.pathFind(the_map,
                               mapSizeN,
                               mapSizeM,
                               possibleDirections,
                               dx,
                               dy,
                               tagCoordinates_x,
                               tagCoordinates_y,
                               anchor0Coordinates_x,
                               anchor0Coordinates_y)
        # Draw line on Rviz
        DrawALine(tagCoordinates_x, 
                    tagCoordinates_y, 
                    tagCoordinates_z, 
                    anchor0Coordinates_x, 
                    anchor0Coordinates_y, 
                    anchor0Coordinates_z)
        # Log route
        rospy.loginfo('Route Number: 0, directions: ' + str(route))
        # Pubblish route
        pubblishRoute.publish(route)
    elif (data.data == "1"):
        # Calculate shortest path
        route = ASTAR.pathFind(the_map,
                               mapSizeN,
                               mapSizeM,
                               possibleDirections,
                               dx,
                               dy,
                               tagCoordinates_x,
                               tagCoordinates_y,
                               anchor1Coordinates_x,
                               anchor1Coordinates_y)
        # Draw line on Rviz
        DrawALine(tagCoordinates_x, 
                  tagCoordinates_y, 
                  tagCoordinates_z, 
                  anchor1Coordinates_x, 
                  anchor1Coordinates_y, 
                  anchor1Coordinates_z)
        # Log route
        rospy.loginfo('Route Number: 1, directions: ' + str(route))
        # Pubblish route
        pubblishRoute.publish(route)
    elif(data.data == "3"):
        # Calculate shortest path
        route = ASTAR.pathFind(the_map,
                               mapSizeN,
                               mapSizeM,
                               possibleDirections,
                               dx,
                               dy,
                               tagCoordinates_x,
                               tagCoordinates_y,
                               anchor3Coordinates_x,
                               anchor3Coordinates_y)
        # Draw line on Rviz
        DrawALine(tagCoordinates_x, 
                  tagCoordinates_y, 
                  tagCoordinates_z, 
                  anchor3Coordinates_x, 
                  anchor3Coordinates_y, 
                  anchor3Coordinates_z)
        # Log route
        rospy.loginfo('Route Number: 3, directions: ' + str(route))
        # Pubblish route
        pubblishRoute.publish(route)

    else:
        rospy.loginfo('No route pubblished: ')







#TODO dummy data from dummy package, DELETE this after or switch with real deal
rospy.Subscriber('DWM1001_Network_Anchor_0', String, DWM1001_Network_Anchor_0callback)
rospy.Subscriber('DWM1001_Network_Anchor_1', String, DWM1001_Network_Anchor_1callback)
rospy.Subscriber('DWM1001_Network_Anchor_2', String, DWM1001_Network_Anchor_2callback)
rospy.Subscriber('DWM1001_Network_Anchor_3', String, DWM1001_Network_Anchor_3callback)
rospy.Subscriber('DWM1001_Network_Tag',      String, DWM1001_Network_Tagcallback)
rospy.Subscriber('route_number',      String, RouteNcallback)
rospy.loginfo('Waiting for route')
rospy.spin()




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



