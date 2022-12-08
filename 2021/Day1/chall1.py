depthFile = open("Day1/input.txt", "r")

depthIncreases = 0
previousDepth = int(depthFile.readline())

for currentDepth in depthFile:
    currentDepth = int(currentDepth)
    if previousDepth < currentDepth:
        depthIncreases += 1
    previousDepth = currentDepth

print (depthIncreases)