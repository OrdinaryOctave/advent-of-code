import numpy as np

crabsFile = open("2021/inputs/day7","r")
crabStrings = crabsFile.readline().split(",")
crabs = []
for crab in crabStrings:
    crabs.append(int(crab))

avgPos = int(np.median(crabs))

fuelSpent = 0
for crab in crabs:
    fuelSpent += abs(avgPos-crab)
print(fuelSpent)