import numpy as np

crabsFile = open("2021/inputs/day7","r")
crabStrings = crabsFile.readline().split(",")
crabs = []
for crab in crabStrings:
    crabs.append(int(crab))


#minFuelSpent = 0
#for crab in crabs:
#    distanceMoved = abs(crab-avgPos)
#    for i in range(distanceMoved):
#        minFuelSpent += 1

minFuelSpent = 9999999999999999999999999999999999
for i in range(min(crabs), max(crabs)):
    attemptDistanceMoved = 0
    for crab in crabs:
        crabDistanceMoved = abs(crab-i)
        attemptDistanceMoved += (crabDistanceMoved * (crabDistanceMoved+1)) // 2
    minFuelSpent = min(minFuelSpent, attemptDistanceMoved)

print(minFuelSpent)