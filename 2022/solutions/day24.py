# input loaded and ready to go at 11:11:21

def moveBlizzards(blizzards):
    newBlizzards = []
    for blizzard in blizzards:
        newX = blizzard[0][0]
        newY = blizzard[0][1]
        direction = blizzard[1]
        if direction == '^':
            newY -= 1
            if newY == 0:
                newY = MAX_Y
        elif direction == 'v':
            newY += 1
            if newY == MAX_Y + 1:
                newY = 1
        elif direction == '>':
            newX += 1
            if newX == MAX_X + 1:
                newX = 1
        elif direction == '<':
            newX -= 1
            if newX == 0:
                newX = MAX_X
        newBlizzards.append(((newX, newY), direction))
    return newBlizzards

def getMoveDirections(pos):
    moveList = [pos]
    if pos[1] == 0:
        moveList.append((pos[0], pos[1]+1))
        return moveList
    if pos[1] == MAX_Y + 1:
        moveList.append((pos[0], pos[1]-1))
        return moveList
    if pos[0] > 1:
        moveList.append((pos[0]-1, pos[1]))
    if pos[1] > 1:
        moveList.append((pos[0], pos[1]-1))
    if pos[0] < MAX_X:
        moveList.append((pos[0]+1, pos[1]))
    if pos[1] < MAX_Y:
        moveList.append((pos[0], pos[1]+1))
    if pos == (1, 1):
        moveList.append((pos[0], pos[1]-1))
    if pos == (MAX_X, MAX_Y):
        moveList.append((pos[0], pos[1]+1))
    return moveList
    
def getStepsToGoal(startPos, goalPos, blizzards):
    toVisit = {}
    toVisit[startPos] = True
    timeTaken = 0
    while True:
        timeTaken += 1
        nextStepVisit = {}
        blizzards = moveBlizzards(blizzards)
        blizzardLocs = {}
        for blizzard in blizzards:
            blizzardLocs[blizzard[0]] = True
        for pos in toVisit:
            for move in getMoveDirections(pos):
                if move == goalPos:
                    return (timeTaken, blizzards)
                if move not in blizzardLocs:
                    nextStepVisit[move] = True
        toVisit = nextStepVisit

with open('2022/inputs/day24') as f:
    input = f.read().split('\n')

blizzards = []

MAX_Y = len(input) - 2
MAX_X = len(input[0]) - 2

for y in range(len(input)):
    for x in range(len(input[y])):
        if input[y][x] != '#' and input[y][x] != '.':
            blizzards.append(((x, y), input[y][x]))
        elif y == 0 and input [y][x] == '.':
            startPos = (x, y)
        elif y == MAX_Y + 1 and input[y][x] == '.':
            goal = (x, y)

result = getStepsToGoal(startPos, goal, blizzards)
steps = result[0]
blizzards = result[1]
print(steps)

result = getStepsToGoal(goal, startPos, blizzards)
steps += result[0]
blizzards = result[1]
result = getStepsToGoal(startPos, goal, blizzards)
steps += result[0]
print(steps)