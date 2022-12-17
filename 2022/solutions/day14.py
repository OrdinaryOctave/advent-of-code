#input loaded and ready to go at 05:02:28

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

# Function unused - keeping for posterity
# Took almost 29 mins to solve part 2 using this function
def addSandPartTwo(floor: int, occupied: list):
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

# new solution to part 2, much more efficient (BFS for all possible sand locations)
def findMaxSandLocations(floor: int, occupied: list):
    visitLocations = [(500, 0)]
    sandCount = 0
    while len(visitLocations) != 0:
        location = visitLocations.pop(0)
        sandCount += 1
        if location[1]+1 != floor:
            moves = [(location[0], location[1]+1), (location[0]-1, location[1]+1), (location[0]+1, location[1]+1)]
            for move in moves:
                if move not in visitLocations and move not in occupied:
                    visitLocations.append(move)
    return sandCount

with open('2022/inputs/day14') as f:
    input = f.read()

rocks = list(map(lambda x: list(map(lambda y: tuple(map(lambda z: int(z), y.split(','))), x.split(' -> '))),input.splitlines()))

occupied = []
for rock in rocks:
    addRock(rock, occupied)

maxY = 0
for point in occupied:
    maxY = max(point[1], maxY)

# new part 2 solution - has to run before part 1 because addSand modifies the occupied list
floorLevel = maxY + 2
maxSandCount = findMaxSandLocations(floorLevel, occupied)

sandCount = 0
while addSand(maxY, occupied):
    sandCount += 1
    
print(sandCount)
print(maxSandCount)

# Original part 2 solution - took almost 29 mins to solve both parts
#print(addSandPartTwo(floorLevel, occupied)+sandCount)