# input loaded at 00:37:32


def checkXmasDirection(grid, index, direction, word="MAS"):
    if word == "":
        return True
    x, y = index
    dx, dy = direction
    x += dx
    y += dy
    if x < 0 or y < 0 or x > MAX_X or y > MAX_Y or grid[x][y] != word[0]:
        return False
    return checkXmasDirection(grid, (x, y), (dx, dy), word[1:])
    

def checkXmas(grid, index):
    validCount = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if checkXmasDirection(grid, index, (dx, dy)):
                validCount += 1
    return validCount

def checkX_Mas(grid, index):
    x, y = index
    if x < 1 or y < 1 or x > MAX_X-1 or y > MAX_Y-1:
        return False
    cornerPairs = ((grid[x+1][y+1], grid[x-1][y-1]), (grid[x+1][y-1], grid[x-1][y+1]))
    for pair in cornerPairs:
        if not(pair[0] == 'M' and pair[1] == 'S' or pair[0] == 'S' and pair[1] == 'M'):
            return False
    return True

with open('2024/inputs/day4') as f:
    inputData = f.read()
grid = [list(row) for row in inputData.splitlines()]

MAX_X = len(grid)-1
MAX_Y = len(grid[0])-1

totalXmas = 0
totalX_Mas = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] == 'X':
            totalXmas += checkXmas(grid, (x, y))
        elif grid[x][y] == 'A' and checkX_Mas(grid, (x, y)):
            totalX_Mas += 1
print(totalXmas)
print(totalX_Mas)