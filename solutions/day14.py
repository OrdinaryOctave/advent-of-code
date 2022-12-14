#input loaded and ready to go at 05:02:28
# This solution is horribly unoptimised but it gets the right answer eventually
# Part 2 took almost 29 mins to solve

def addRock(rock: list, occupied: list):
    if rock[0] not in occupied:
        occupied.append(rock[0])
    for i in range(len(rock)-1):
        if rock[i+1] not in occupied:
            occupied.append(rock[i+1])
        xDiff = rock[i][0] - rock[i+1][0]
        yDiff = rock[i][1] - rock[i+1][1]
        if abs(xDiff) > 1:
            if xDiff < 0:
                startingPoint = rock[i]
            else:
                startingPoint = rock[i+1]
            for i in range(1, abs(xDiff)):
                point = (startingPoint[0]+i, startingPoint[1])
                if point not in occupied:
                    occupied.append(point)
        if abs(yDiff) > 1:
            if yDiff < 0:
                startingPoint = rock[i]
            else:
                startingPoint = rock[i+1]
            for i in range(1, abs(yDiff)):
                point = (startingPoint[0], startingPoint[1]+i)
                if point not in occupied:
                    occupied.append(point)

def addSand(lowestRock: int, occupied: list):
    sandPos = (500, 0)
    while sandPos[1] < lowestRock:
        if (sandPos[0], sandPos[1]+1) not in occupied:
            sandPos = (sandPos[0], sandPos[1]+1)
        elif (sandPos[0]-1, sandPos[1]+1) not in occupied:
            sandPos = (sandPos[0]-1, sandPos[1]+1)
        elif (sandPos[0]+1, sandPos[1]+1) not in occupied:
            sandPos = (sandPos[0]+1, sandPos[1]+1)
        else:
            occupied.append(sandPos)
            return True
    return False

def addSandPartTwo(floor: int,occupied: list):
    sandPos = (500, 0)
    sandCount = 0
    while True:
        if (sandPos[1] == floor - 1):
            occupied.append(sandPos)
            sandCount += 1
            sandPos = (500, 0)
            
        elif (sandPos[0], sandPos[1]+1) not in occupied:
            sandPos = (sandPos[0], sandPos[1]+1)
        elif (sandPos[0]-1, sandPos[1]+1) not in occupied:
            sandPos = (sandPos[0]-1, sandPos[1]+1)
        elif (sandPos[0]+1, sandPos[1]+1) not in occupied:
            sandPos = (sandPos[0]+1, sandPos[1]+1)
        else:
            occupied.append(sandPos)
            sandCount += 1
            if sandPos == (500, 0):
                return sandCount
            sandPos = (500, 0)
            

with open('inputs/day14') as f:
    input = f.read().rstrip()

rocks = list(map(lambda x: list(map(lambda y: tuple(map(lambda z: int(z), y.split(','))), x.split(' -> '))),input.splitlines()))

occupied = []
for rock in rocks:
    addRock(rock, occupied)

maxY = 0
for point in occupied:
    maxY = max(point[1], maxY)

sandCount = 0
while addSand(maxY, occupied):
    sandCount += 1
    
print(sandCount)

floorLevel = maxY + 2
print(addSandPartTwo(floorLevel, occupied)+sandCount)