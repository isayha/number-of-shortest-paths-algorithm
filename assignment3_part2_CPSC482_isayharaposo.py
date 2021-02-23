# Assignment 3
# Part 2 (Python Source Code)
# CPSC 482
# Isayha Raposo
# Student Number: 230133508

import sys
from files import *

# Handles data retrieval (see files.py)
data = getData(sys.argv)

# Processes the first line of data (Obtains the specified source and destination nodes):
dataLine = data.readline().strip('\n')
try:
    sourceNode, destinationNode = (int(node) for node in dataLine.split(", "))
except:
    handleDataIssue(True, "Line 1 of data file incorrectly formatted.")

# Processes the remaining lines of data (Obtains the specified adjacency matrix and condenses it to improve performance):
adjacencyMatrix = []
nodeCount = 0

dataLine = data.readline().strip('\n')
while not (dataLine == ""):
    nodeCount += 1
    try:
        adjacencyMatrix.append([node for node, isAdjacent in enumerate(dataLine.split(" ")) if int(isAdjacent) == 1])
    except:
        handleDataIssue(True, ("Line " + nodeCount + 1 + " of data file incorrectly formatted."))
    dataLine = data.readline().strip('\n')

# Algorithm:
# This algorithm is a modified breadth-first search (BFS) algorithm that allows for/keeps track of the number of
# repeated visits to the destination node where said visits originate from distinct paths and said distinct paths
# are all of the same (shortest possible) length
lengthOfShortestPath = None
numberOfShortestPaths = 0

# Handles edge case in which the source node is the same as the destination node
if sourceNode == destinationNode:
    lengthOfShortestPath = 0
    numberOfShortestPaths = 1

visited = [False] * nodeCount # Used to keep track of which nodes have already been visited
visited[sourceNode] =  True # Mark the source node as visited

queue = [[sourceNode, 0]] # [node, pathLength]
while queue:
    node = queue[0][0]
    pathLength = queue[0][1]

    # Prevents consideration of paths longer than the length of the shortest path
    # (We don't consider child nodes if the length of the path that led to the current (parent) node is equal to or
    # exceeds the length of the shortest path, as doing so would be redundant)
    if lengthOfShortestPath is not None:
        if pathLength == lengthOfShortestPath:
            break

    # Adds child nodes of the current (parent) node to the queue, where said child nodes have not already been visited
    # (To prevent redundancies). The one exception being if a given child node is the destination node; 
    # in such a case, the number of shortest paths is incremented, and no further action is taken.
    for nextNode in adjacencyMatrix[node]:
        if nextNode == destinationNode:
            lengthOfShortestPath = pathLength + 1 # As per Breadth-First Search
            numberOfShortestPaths += 1
        elif visited[nextNode] is False:
            visited[nextNode] = True
            queue.append([nextNode, pathLength + 1])

    queue.pop(0)

# Prints results
print("Length of shortest path between node " + str(sourceNode) + " and node " + str(destinationNode) + ": " + str(lengthOfShortestPath))
print("Number of shortest paths between node " + str(sourceNode) + " and node " + str(destinationNode) + ": " + str(numberOfShortestPaths))
        
    