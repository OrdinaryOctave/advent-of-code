#input loaded and ready to go at 05:08:14
# This code feels like it's wrong but it got me the right answer so it's staying
# I have no clue if this works with other inputs but it feels like it only works
# because of some weird quirk of my input

with open('2022/inputs/day17') as f:
    input = f.read()

wind = [*input]

shapes = [((2,0), (3,0), (4,0), (5,0)),
          ((3,0), (2,1), (3,1), (4,1), (3,2)),
          ((2,0), (3,0), (4,0), (4,1), (4,2)),
          ((2,0), (2,1), (2,2), (2,3)),
          ((2,0), (3,0), (2,1), (3,1))]

occupied = {}
maxHeight = 0
minHeight = 1
shapeCount = len(shapes)
windCount = len(wind)
nextShape = 0
nextWind = 0
cycleFound = False
iteration = 0
previousStates = []

while not cycleFound:
    iteration += 1
    rock = shapes[nextShape]
    nextShape = (nextShape + 1) % shapeCount
    rock = [(p[0], p[1]+maxHeight+4) for p in rock]
    
    moving = True
    while moving:
        direction = wind[nextWind]
        nextWind = (nextWind + 1) % windCount
        if direction == ">":
            xModifier = 1
        else:
            xModifier = -1
        
        newPos = [(p[0]+xModifier, p[1]) for p in rock]
        for point in newPos:
            if point[0] < 0 or point[0] > 6:
                newPos = rock
                break
            if point[1] in occupied and occupied[point[1]][point[0]]:
                newPos = rock
                break
        rock = newPos
        
        newPos = [(p[0], p[1]-1) for p in rock]
        for point in newPos:
            if point[1] < 1:
                newPos = rock
                moving = False
                break
            if point[1] in occupied and occupied[point[1]][point[0]]:
                newPos = rock
                moving = False
                break
        rock = newPos
    for point in rock:
        if maxHeight < point[1]:
            maxHeight = point[1]
            occupied[point[1]] = [False] * 7
        occupied[point[1]][point[0]] = True
    
    newMinHeight = minHeight
    for row in occupied:
        if occupied[row] == [True] * 7:
            newMinHeight = max(row, newMinHeight)
    
    if newMinHeight > minHeight:
        while newMinHeight > minHeight:
            del occupied[minHeight]
            minHeight += 1
        
        archiveDict = {}
        for i in range(len(occupied)):
            archiveDict[i+1] = occupied[i+minHeight]
        thisState = ((archiveDict, nextWind, nextShape), maxHeight, iteration)
        for state in previousStates:
            if state[0] == thisState[0]:
                cycleFound = True
        previousStates.append(thisState)
            
lastState = previousStates[-1]

for i in range(len(previousStates)):
    if previousStates[i][0] == lastState[0]:
        cycleStart = previousStates[i]
        break

cycleLength = lastState[2]-cycleStart[2]
cycleHeight = lastState[1]-cycleStart[1]

maxHeight = 0
minHeight = 1
occupied = {}

for i in range((1000000000000-cycleStart[2])%cycleLength):
    rock = shapes[nextShape]
    nextShape = (nextShape + 1) % shapeCount
    rock = [(p[0], p[1]+maxHeight+4) for p in rock]
    
    moving = True
    while moving:
        direction = wind[nextWind]
        nextWind = (nextWind + 1) % windCount
        if direction == ">":
            xModifier = 1
        else:
            xModifier = -1
        
        newPos = [(p[0]+xModifier, p[1]) for p in rock]
        for point in newPos:
            if point[0] < 0 or point[0] > 6:
                newPos = rock
                break
            if point[1] in occupied and occupied[point[1]][point[0]]:
                newPos = rock
                break
        rock = newPos
        
        newPos = [(p[0], p[1]-1) for p in rock]
        for point in newPos:
            if point[1] < 1:
                newPos = rock
                moving = False
                break
            if point[1] in occupied and occupied[point[1]][point[0]]:
                newPos = rock
                moving = False
                break
        rock = newPos
    for point in rock:
        if maxHeight < point[1]:
            maxHeight = point[1]
            occupied[point[1]] = [False] * 7
        occupied[point[1]][point[0]] = True
    
    newMinHeight = minHeight
    for row in occupied:
        if occupied[row] == [True] * 7:
            newMinHeight = max(row, newMinHeight)
    
    while newMinHeight > minHeight:
        del occupied[minHeight]
        minHeight += 1
    

print(maxHeight+cycleStart[1]+(cycleHeight*((1000000000000-cycleStart[2])//cycleLength)))
