# A* Shortest Path Algorithm
# http://en.wikipedia.org/wiki/A*
#Directions
#           5       6     7
#             ^     ^    ^
#               \   |   /
#                \  |  /
#                 \ | /
#        4 <------- T ------> 0
#                 / | \
#                /  |  \
#               /   |   \
#              >    ^    >
#             3     2    1
#

from heapq import heappush, heappop # for priority queue
import math
import time
import random

class node:
    xPos = 0 # x position
    yPos = 0 # y position
    distance = 0 # total distance already travelled to reach the node
    priority = 0 # priority = distance + remaining distance estimate
    def __init__(self, xPos, yPos, distance, priority):
        self.xPos = xPos
        self.yPos = yPos
        self.distance = distance
        self.priority = priority
    def __lt__(self, other): # comparison method for priority queue
        return self.priority < other.priority
    def updatePriority(self, xDest, yDest):
        self.priority = self.distance + self.estimate(xDest, yDest) * 10 # A*
    # give higher priority to going straight instead of diagonally
    def nextMove(self, dirs, d): # d: direction to move
        if dirs == 8 and d % 2 != 0:
            self.distance += 14
        else:
            self.distance += 10
    # Estimation function for the remaining distance to the goal.
    def estimate(self, xDest, yDest):
        xd = xDest - self.xPos
        yd = yDest - self.yPos
        # Euclidian Distance
        #d = math.sqrt(xd * xd + yd * yd)
        # Manhattan distance
        # d = abs(xd) + abs(yd)
        # Chebyshev distance
        d = max(abs(xd), abs(yd))
        return(d)

# A-star algorithm.
# The path returned will be a string of digits of directions.
def pathFind(the_map, mapSizeN, mapSizeM, dirs, directionX, directionY, xStart, yStart, xFinish, yFinish):
    closed_nodes_map = [] # map of closed (tried-out) nodes
    open_nodes_map = [] # map of open (not-yet-tried) nodes
    dir_map = [] # map of dirs
    row = [0] * mapSizeN
    for i in range(mapSizeM): # create 2d arrays
        closed_nodes_map.append(list(row))
        open_nodes_map.append(list(row))
        dir_map.append(list(row))

    priorityQueue = [[], []] # priority queues of open (not-yet-tried) nodes
    priorityQueueIndex = 0 # priority queue index
    # create the start node and push into list of open nodes
    n0 = node(xStart, yStart, 0, 0)
    n0.updatePriority(xFinish, yFinish)
    heappush(priorityQueue[priorityQueueIndex], n0)
    open_nodes_map[yStart][xStart] = n0.priority # mark it on the open nodes map

    # A* search
    while len(priorityQueue[priorityQueueIndex]) > 0:
        # get the current node w/ the highest priority
        # from the list of open nodes
        n1 = priorityQueue[priorityQueueIndex][0] # top node
        n0 = node(n1.xPos, n1.yPos, n1.distance, n1.priority)
        x = n0.xPos
        y = n0.yPos
        heappop(priorityQueue[priorityQueueIndex]) # remove the node from the open list
        open_nodes_map[y][x] = 0
        closed_nodes_map[y][x] = 1 # mark it on the closed nodes map

        # quit searching when the goal is reached
        # if n0.estimate(xB, yB) == 0:
        if x == xFinish and y == yFinish:
            # generate the path from finish to start
            # by following the dirs
            path = ''
            while not (x == xStart and y == yStart):
                j = dir_map[y][x]
                c = str((j + dirs / 2) % dirs)
                path = c + path
                x += directionX[j]
                y += directionY[j]
            return path



        # generate moves (child nodes) in all possible dirs
        for i in range(dirs):
            xdx = x + directionX[i]
            ydy = y + directionY[i]
            if not (xdx < 0 or xdx > mapSizeN - 1 or ydy < 0 or ydy > mapSizeM - 1
                    or the_map[ydy][xdx] == 1 or closed_nodes_map[ydy][xdx] == 1):
                # generate a child node
                m0 = node(xdx, ydy, n0.distance, n0.priority)
                m0.nextMove(dirs, i)
                m0.updatePriority(xFinish, yFinish)
                # if it is not in the open list then add into that
                if open_nodes_map[ydy][xdx] == 0:
                    open_nodes_map[ydy][xdx] = m0.priority
                    heappush(priorityQueue[priorityQueueIndex], m0)
                    # mark its parent node direction
                    dir_map[ydy][xdx] = (i + dirs / 2) % dirs
                elif open_nodes_map[ydy][xdx] > m0.priority:
                    # update the priority
                    open_nodes_map[ydy][xdx] = m0.priority
                    # update the parent direction
                    dir_map[ydy][xdx] = (i + dirs / 2) % dirs
                    # replace the node
                    # by emptying one priorityQueue to the other one
                    # except the node to be replaced will be ignored
                    # and the new node will be pushed in instead
                    while not (priorityQueue[priorityQueueIndex][0].xPos == xdx and priorityQueue[priorityQueueIndex][0].yPos == ydy):
                        heappush(priorityQueue[1 - priorityQueueIndex], priorityQueue[priorityQueueIndex][0])
                        heappop(priorityQueue[priorityQueueIndex])
                    heappop(priorityQueue[priorityQueueIndex]) # remove the target node
                    # empty the larger size priority queue to the smaller one
                    if len(priorityQueue[priorityQueueIndex]) > len(priorityQueue[1 - priorityQueueIndex]):
                        priorityQueueIndex = 1 - priorityQueueIndex
                    while len(priorityQueue[priorityQueueIndex]) > 0:
                        heappush(priorityQueue[1-priorityQueueIndex], priorityQueue[priorityQueueIndex][0])
                        heappop(priorityQueue[priorityQueueIndex])
                    priorityQueueIndex = 1 - priorityQueueIndex
                    heappush(priorityQueue[priorityQueueIndex], m0) # add the better node instead
    return '' # if no route found