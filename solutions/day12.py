#input loaded and ready to go at 05:00:03

def getAllowedMoves(pos, terrain):
    allowedMoves = []
    height = terrain[pos[0]][pos[1]]
    if pos[0] != 0:
        if terrain[pos[0]-1][pos[1]]<=height+1:
            allowedMoves.append([pos[0]-1, pos[1]])
    if pos[1] != 0:
        if terrain[pos[0]][pos[1]-1]<=height+1:
            allowedMoves.append([pos[0], pos[1]-1])
    if pos[0] != len(terrain)-1:
        if terrain[pos[0]+1][pos[1]]<=height+1:
            allowedMoves.append([pos[0]+1, pos[1]])
    if pos[1] != len(terrain[0])-1:
        if terrain[pos[0]][pos[1]+1]<=height+1:
            allowedMoves.append([pos[0], pos[1]+1])
    return allowedMoves

def getMoveCount(startPos, goal, terrain, maxSteps):
    visited = [startPos]
    toVisit = [startPos]
    moveCount = 0
    while True:
        moveCount+=1
        if moveCount >= maxSteps and maxSteps != -1:
            return -1
        toVisitTemp = []
        for position in toVisit:
            moves = getAllowedMoves(position, terrain)
            for move in moves:
                if move == goal:
                    return moveCount
                if move not in visited:
                    visited.append(move)
                    toVisitTemp.append(move)
        toVisit = toVisitTemp
                

with open('inputs/day12') as f:
    input = f.read().rstrip()

lines = input.split('\n')

terrain=[]
startPos=[0, 0]
alternativeStarts = []
goal=[0, 0]
for i in range(len(lines)):
    line = []
    for j in range(len(lines[i])):
        if lines[i][j] == 'S':
            line.append(0)
            startPos = [i, j]
            alternativeStarts.append([i, j])
        elif lines[i][j] == 'E':
            line.append(25)
            goal = [i, j]
        elif lines[i][j] == 'a':
            line.append(0)
            alternativeStarts.append([i, j])
        else:
            line.append(ord(lines[i][j])-ord('a'))
    terrain.append(line)

print(getMoveCount(startPos, goal, terrain, -1))
minSteps = -1
for start in alternativeStarts:
    steps = getMoveCount(start, goal, terrain, minSteps)
    if steps != -1:
        minSteps = steps
print(minSteps)