# input loaded and ready to go at 12:51:04

def findFace(pos):
    x, y = pos
    if y // 50 == 0:
        return x // 50
    elif y // 50 == 1:
        return 3
    elif y // 50 == 2 and x // 50 == 1:
        return 4
    elif y // 50 == 2 and x // 50 == 0:
        return 5
    else:
        return 6

def getWrappedPosAndDirection(pos, direction):
    face = findFace(pos)
    if face ==  1:
        if direction == 2:
            direction = 0
            pos = (0, 149 - pos[1])
        elif direction == 3:
            direction = 0
            pos = (0, pos[0] + 100)
    elif face == 2:
        if direction == 0:
            direction = 2
            pos = (99, 149 - pos[1])
        elif direction == 1:
            direction = 2
            pos = (99, pos[0] - 50)
        elif direction == 3:
            pos = (pos[0] - 100, 199)
    elif face == 3:
        if direction == 0:
            direction = 3
            pos = (pos[1] + 50, 49)
        elif direction == 2:
            direction = 1
            pos = (pos[1] - 50, 100)
    elif face == 4:
        if direction == 0:
            direction = 2
            pos = (149, 149 - pos[1])
        elif direction == 1:
            direction = 2
            pos = (49, pos[0] + 100)
    elif face == 5:
        if direction == 2:
            direction = 0
            pos = (50, 149 - pos[1])
        elif direction == 3:
            direction = 0
            pos = (50, pos[0] + 50)
    else:
        if direction == 0:
            direction = 3
            pos = (pos[1] - 100, 149)
        elif direction == 1:
            pos = (pos[0] + 100, 0)
        elif direction == 2:
            direction = 1
            pos = (pos[1] - 100, 0)
    return(pos, direction)
            

with open('2022/inputs/day22') as f:
    input = f.read().split('\n\n') 

grid = {}
startPos = (-1, -1)
gridInput = input[0].split('\n')
for y in range(len(gridInput)):
    for x in range(len(gridInput[y])):
        char = gridInput[y][x]
        if char == '.' or char == '#':
            grid[(x, y)] = char
        if startPos == (-1, -1) and char == '.':
            startPos = (x, y)

steps = []
stepsInput = input[1]
while stepsInput != "":
    for i in range(len(stepsInput)):
        if stepsInput[i] == 'R' or stepsInput[i] == 'L':
            steps.append(stepsInput[:i])
            steps.append(stepsInput[i])
            stepsInput = stepsInput[i+1:]
            break
        if i == len(stepsInput) - 1:
            steps.append(stepsInput)
            stepsInput = ""

moves = {
    0: (1, 0),
    1: (0, 1),
    2: (-1, 0),
    3: (0, -1),
}

pos = startPos
direction = 0
for step in steps:
    if step == 'R':
        direction = (direction + 1) % 4
    elif step == 'L':
        direction = (direction - 1) % 4
    else:
        for _ in range(int(step)):
            if (pos[0] + moves[direction][0], pos[1] + moves[direction][1]) in grid:
                if grid[(pos[0] + moves[direction][0], pos[1] + moves[direction][1])] == ".":
                    pos = (pos[0] + moves[direction][0], pos[1] + moves[direction][1])
                else:
                    break
            else:
                if direction == 0:
                    newPos = (min([tile[0] for tile in grid if tile[1] == pos[1]]), pos[1])
                elif direction == 1:
                    newPos = (pos[0], min([tile[1] for tile in grid if tile[0] == pos[0]]))
                elif direction == 2:
                    newPos = (max([tile[0] for tile in grid if tile[1] == pos[1]]), pos[1])
                elif direction == 3:
                    newPos = (pos[0], max([tile[1] for tile in grid if tile[0] == pos[0]]))

                if grid[newPos] == ".":
                    pos = newPos
                else:
                    break

print(1000*(pos[1]+1) + 4 * (pos[0]+1) + direction)

pos = startPos
direction = 0
for step in steps:
    if step == 'R':
        direction = (direction + 1) % 4
        step = step.replace("R", "")
    elif step == 'L':
        direction = (direction - 1) % 4
        step = step.replace("L", "")
    else:
        for _ in range(int(step)):
            if (pos[0] + moves[direction][0], pos[1] + moves[direction][1]) in grid:
                if grid[(pos[0] + moves[direction][0], pos[1] + moves[direction][1])] == ".":
                    pos = (pos[0] + moves[direction][0], pos[1] + moves[direction][1])
                else:
                    break
            else:
                newPos, newDirection = getWrappedPosAndDirection(pos, direction)
                if grid[newPos] == ".":
                    direction = newDirection
                    pos = newPos
                else:
                    break

print(1000*(pos[1]+1) + 4 * (pos[0]+1) + direction)
