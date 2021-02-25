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
        handleDataIssue(True, ("Line " + str(nodeCount + 1) + " of data file incorrectly formatted."))
    dataLine = data.readline().strip('\n')

# Algorithm:
# This algorithm is a modified version of Dijkstra's algorithm that keeps track of the number of
# repeated visits to the destination node where said visits originate from distinct paths and said distinct paths
# are all of the same (shortest possible) length
lengthOfShortestPath = None
numberOfShortestPaths = 0

visited = [False] * nodeCount # Used to keep track of which nodes have already been visited

queue = [[sourceNode, 0]] # [node, pathLength, visited]
while queue:
    node = queue[0][0]
    pathLength = queue[0][1]
    visited[node] =  True # Mark the node as visited
    # Prevents consideration of paths longer than the length of the shortest path
    # (We don't consider child nodes if the length of the path that led to the current (parent) node is equal to or
    # exceeds the length of the shortest path, as doing so would be redundant)
    queue.pop(0)
    if lengthOfShortestPath is not None:
        if pathLength > lengthOfShortestPath:
            break
    if node == destinationNode:
        if lengthOfShortestPath is None or pathLength < lengthOfShortestPath:
            lengthOfShortestPath = pathLength
            numberOfShortestPaths = 1
        elif lengthOfShortestPath == pathLength:
            numberOfShortestPaths += 1
    else:
        # Adds child nodes of the current (parent) node to the queue, where said child nodes have not already been visited
        for nextNode in adjacencyMatrix[node]:
            if visited[nextNode] is False:
                queue.append([nextNode, pathLength + 1])

# Prints results
print("Length of shortest path between node " + str(sourceNode) + " and node " + str(destinationNode) + ": " + str(lengthOfShortestPath))
print("Number of shortest paths between node " + str(sourceNode) + " and node " + str(destinationNode) + ": " + str(numberOfShortestPaths))
        
    