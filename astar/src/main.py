#__author__ = 'Hadi Elmekawi'
import math
import time
import random
import astar as ASTAR




possibleDirections = 8 # number of possible directions to move on the map

if possibleDirections == 4:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
elif possibleDirections == 8:
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

mapSizeN = 40 # horizontal size of the map
mapSizeM = 40 # vertical size of the map
the_map = []
row = [0] * mapSizeN
for i in range(mapSizeM): # create empty map
    the_map.append(list(row))

# TODO, add obstacles if you need to fillout the map with a '0' pattern, meaning obstcles
for x in range(mapSizeN / 8, mapSizeN * 7 / 8):
    the_map[mapSizeM / 2][x] = 1
for y in range(mapSizeM/8, mapSizeM * 7 / 8):
    the_map[y][mapSizeN / 2] = 1

# TODO delete this once you finish debugging randomly select start and finish locations from a list
startFinishList = []
startFinishList.append((0, 0, mapSizeN - 1, mapSizeM - 1))
startFinishList.append((0, mapSizeM - 1, mapSizeN - 1, 0))
startFinishList.append((mapSizeN / 2 - 1, mapSizeM / 2 - 1, mapSizeN / 2 + 1, mapSizeM / 2 + 1))
startFinishList.append((mapSizeN / 2 - 1, mapSizeM / 2 + 1, mapSizeN / 2 + 1, mapSizeM / 2 - 1))
startFinishList.append((mapSizeN / 2 - 1, 0, mapSizeN / 2 + 1, mapSizeM - 1))
startFinishList.append((mapSizeN / 2 + 1, mapSizeM - 1, mapSizeN / 2 - 1, 0))
startFinishList.append((0, mapSizeM / 2 - 1, mapSizeN - 1, mapSizeM / 2 + 1))
startFinishList.append((mapSizeN - 1, mapSizeM / 2 + 1, 0, mapSizeM / 2 - 1))
(xStart, yStart, xFinish, yFinish) = random.choice(startFinishList)


# Coordinates start and finish point
#xStart = 0
#yStart = 0
#xFinish = 39
#yFinish = 0

print 'Map size (X,Y): ', mapSizeN, mapSizeM
print 'Start: ', xStart, yStart
print 'Finish: ', xFinish, yFinish
t = time.time()
route = ASTAR.pathFind(the_map, mapSizeN, mapSizeM, possibleDirections, dx, dy, xStart, yStart, xFinish, yFinish)


print 'Time to generate the route (seconds): ', time.time() - t
print 'Route:'
print route

# mark the route on the map
if len(route) > 0:
    x = xStart
    y = yStart
    the_map[y][x] = 2
    for i in range(len(route)):
        j = int(route[i])
        x += dx[j]
        y += dy[j]
        the_map[y][x] = 3
    the_map[y][x] = 4

# display the map with the route added
print 'Map:'
for y in range(mapSizeM):
    for x in range(mapSizeN):
        xy = the_map[y][x]
        if xy == 0:
            print '.', # space
        elif xy == 1:
            print 'O', # obstacle
        elif xy == 2:
            print 'S', # start
        elif xy == 3:
            print 'R', # route
        elif xy == 4:
            print 'F', # finish
    print

raw_input('Press Enter...')