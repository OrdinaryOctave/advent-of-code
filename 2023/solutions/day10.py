# input loaded at 08:18:50

with open('2023/inputs/day10') as f:
    inputData = f.read()

pipeGrid = inputData.split("\n")

for x, row in enumerate(pipeGrid):
    if 'S' in row:
        startLocation = (x, row.find('S'))
        break
loopElements = {startLocation: 'S'}

x, y = startLocation
if pipeGrid[x][y+1] in ['-', 'J', '7']:
    checkLocation = (x, y+1)
elif pipeGrid[x][y-1] in ['-', 'L', 'F']:
    checkLocation = (x, y-1)
elif pipeGrid[x+1][y] in ['|', 'L', 'J']:
    checkLocation = (x+1, y)
else:
    checkLocation = (x-1, y)

prevLocation = startLocation
while checkLocation != startLocation:
    x, y = checkLocation
    loopElements[checkLocation] = pipeGrid[x][y]
    pipeSegment = pipeGrid[x][y]
    match pipeSegment:
        case '|':
            checkLocation = (x-1, y) if (x-1, y) != prevLocation else (x+1, y)
        case '-':
            checkLocation = (x, y-1) if (x, y-1) != prevLocation else (x, y+1)    
        case 'L':
            checkLocation = (x-1, y) if (x-1, y) != prevLocation else (x, y+1)
        case 'J':
            checkLocation = (x-1, y) if (x-1, y) != prevLocation else (x, y-1)
        case '7':
            checkLocation = (x+1, y) if (x+1, y) != prevLocation else (x, y-1)
        case 'F':
            checkLocation = (x+1, y) if (x+1, y) != prevLocation else (x, y+1)
    prevLocation = (x, y)

print(len(loopElements)//2)

blownUpGrid = [['' for j in range ((len(pipeGrid[0]) + 2) * 3)] for i in range((len(pipeGrid) + 2) * 3)]

for x, y in loopElements:
    shape = loopElements[(x, y)]
    x = (x+1)*3 
    y = (y+1)*3
    match shape:
        case '|':
            blownUpGrid[x][y+1] = 'P'
            blownUpGrid[x+1][y+1] = 'P'
            blownUpGrid[x+2][y+1] = 'P'
        case '-':
            blownUpGrid[x+1][y] = 'P'
            blownUpGrid[x+1][y+1] = 'P'
            blownUpGrid[x+1][y+2] = 'P'
        case 'L':
            blownUpGrid[x][y+1] = 'P'
            blownUpGrid[x+1][y+1] = 'P'
            blownUpGrid[x+1][y+2] = 'P'
        case 'J':
            blownUpGrid[x][y+1] = 'P'
            blownUpGrid[x+1][y+1] = 'P'
            blownUpGrid[x+1][y] = 'P'
        case '7':
            blownUpGrid[x+1][y] = 'P'
            blownUpGrid[x+1][y+1] = 'P'
            blownUpGrid[x+2][y+1] = 'P'
        case 'F':
            blownUpGrid[x+1][y+1] = 'P'
            blownUpGrid[x+1][y+2] = 'P'
            blownUpGrid[x+2][y+1] = 'P'
        case 'S':
            for i in range(3):
                for j in range(3):
                    blownUpGrid[x+i][y+j] = 'P'

toVisit = [(0, 0)]
maxX = len(blownUpGrid) - 1
maxY = len(blownUpGrid[0]) - 1
while toVisit:
    x, y = toVisit.pop()
    blownUpGrid[x][y] = 'O'
    if x != 0 and blownUpGrid[x-1][y] == '' and (x-1, y) not in toVisit:
        toVisit.append((x-1, y))
    if y != 0 and blownUpGrid[x][y-1] == '' and (x, y-1) not in toVisit:
        toVisit.append((x, y-1))
    if x != maxX and blownUpGrid[x+1][y] == '' and (x+1, y) not in toVisit:
        toVisit.append((x+1, y))
    if y+1 != maxX and blownUpGrid[x][y+1] == '' and (x, y+1) not in toVisit:
        toVisit.append((x, y+1))

outsideLocations = {}

for x, row in enumerate(blownUpGrid):
    for y, char in enumerate(row):
        if char != '':
            outsideLocations[((x-3)//3, (y-3)//3)] = True

insideLocationCount = 0
for x in range(len(pipeGrid)):
    for y in range(len(pipeGrid[0])):
        if (x, y) not in outsideLocations:
            insideLocationCount += 1

print(insideLocationCount)