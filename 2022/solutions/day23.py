# input loaded and ready to go at 09:02:11

def checkAdjacent(elf ,elves):
    if ((elf[0]-1, elf[1]-1) in elves or
        (elf[0]-1, elf[1]) in elves or
        (elf[0]-1, elf[1]+1) in elves or
        (elf[0], elf[1]-1) in elves or
        (elf[0], elf[1]+1) in elves or
        (elf[0]+1, elf[1]-1) in elves or
        (elf[0]+1, elf[1]) in elves or
        (elf[0]+1, elf[1]+1) in elves):
        return True
    return False

def checkValidMove(direction, elves, elf):
    if direction == 'N':
        if ((elf[0], elf[1]-1) in elves or
           (elf[0]-1, elf[1]-1) in elves or
           (elf[0]+1, elf[1]-1) in elves):
            return False
    elif direction == 'S':
        if ((elf[0], elf[1]+1) in elves or
           (elf[0]-1, elf[1]+1) in elves or
           (elf[0]+1, elf[1]+1) in elves):
            return False
    elif direction == 'W':
        if ((elf[0]-1, elf[1]) in elves or
           (elf[0]-1, elf[1]-1) in elves or
           (elf[0]-1, elf[1]+1) in elves):
            return False
    elif direction == 'E':
        if ((elf[0]+1, elf[1]) in elves or
           (elf[0]+1, elf[1]-1) in elves or
           (elf[0]+1, elf[1]+1) in elves):
            return False
    return True

def getMoveLocation(direction, elf):
    if direction == 'N':
        return (elf[0], elf[1]-1)
    elif direction == 'S':
        return (elf[0], elf[1]+1)
    elif direction == 'W':
        return (elf[0]-1 , elf[1])
    return (elf[0]+1 , elf[1])

def doMoveRound(elves, directions):
    allowedMoves = {}
    elfMoves = {}
    newElves = {}
    
    for elf in elves:
        if checkAdjacent(elf, elves):
            for direction in directions:
                if checkValidMove(direction, elves, elf):
                    moveLocation = getMoveLocation(direction, elf)
                    elfMoves[elf] = moveLocation
                    if moveLocation in allowedMoves:
                        allowedMoves[moveLocation] = False
                    else:
                        allowedMoves[moveLocation] = True
                    break
                if direction == directions[3]:
                    newElves[elf] = True
        else:
            newElves[elf] = True
    
    for elf in elfMoves:
        if allowedMoves[elfMoves[elf]]:
            newElves[elfMoves[elf]] = True
        else:
            newElves[elf] = True
    
    if len(newElves) != len(elves):
        print(len(newElves), len(elves))
    return newElves


with open('2022/inputs/day23') as f:
    input = f.read()

elves = {}

lines = input.split('\n')
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == '#':
            elves[(x, y)] = True

trialDirections = ['N', 'S', 'W', 'E']

for i in range(10):
    elves = doMoveRound(elves, trialDirections)
    trialDirections.append(trialDirections.pop(0))

minX, maxX, minY, maxY = 0, 0, 0, 0

for elf in elves:
    minX = min(minX, elf[0])
    maxX = max(maxX, elf[0])
    minY = min(minY, elf[1])
    maxY = max(maxY, elf[1])

emptyGround = (1 + maxX - minX) * (1 + maxY - minY)
emptyGround -= len(elves)
print(emptyGround)

rounds = 10
finished = False
while not finished:
    rounds += 1
    newElves = doMoveRound(elves, trialDirections)
    if newElves != elves:
        elves = newElves
        trialDirections.append(trialDirections.pop(0))
    else:
        finished = True

print(rounds)
