# input loaded at 06:19:44
from math import lcm

with open('2023/inputs/day8') as f:
    inputData = f.read()

directions, mapString = inputData.split("\n\n")

map = {}
directionsLen = len(directions)

for node in mapString.split("\n"):
    baseNode, connections = node.split(" = (")
    connections = connections.split(", ")
    map[baseNode] = (connections[0], connections[1][:3])

currentNode = 'AAA'
steps = 0
while currentNode != 'ZZZ':
    direction = 0 if directions[steps % directionsLen] == 'L' else 1
    currentNode = map[currentNode][direction]
    steps += 1

print(steps)
currentNodes = [node for node in map if node[2]=='A']
stepsNeeded = []
steps = 0
targetFound = False
while currentNodes:
    direction = 0 if directions[steps % directionsLen] == 'L' else 1
    targetFound = True
    for i, node in enumerate(currentNodes):
        currentNodes[i] = map[node][direction]
    
    steps+=1
    for node in currentNodes:
        if node[2] == 'Z':
            stepsNeeded.append(steps)
            currentNodes.remove(node)

print(lcm(*stepsNeeded))
