# input loaded at 11:22:53

with open('2023/inputs/day16') as f:
    inputData = f.read()
    
objects = {}
for y, line in enumerate(inputData.split("\n")):
    for x, char in enumerate(line):
        if char != '.':
            objects[(x, y)] = char
maxX = len(inputData.split("\n")[0])
maxY = len(inputData.split("\n"))

# energizedTiles = {}
# beams = [(0, 0, 'R')]
# existingBeams = {}
def findEnergizedTiles(startLocation):
    beams = [startLocation]
    existingBeams = {}
    energizedTiles = {}
    while beams:
        x, y, direction = beams.pop()
        while 0 <= x < maxX and 0 <= y < maxY:
            if (x, y, direction) in existingBeams:
                break
            existingBeams[(x, y, direction)] = True
            energizedTiles[(x, y)] = True
            if (x, y) in objects:
                match objects[(x, y)]:
                    case '-':
                        if direction in ['U', 'D']:
                            beams.append((x, y, 'L'))
                            direction = 'R'
                    case '|':
                        if direction in ['L', 'R']:
                            beams.append((x, y, 'U'))
                            direction = 'D'
                    case '\\':
                        if direction == 'L':
                            direction = 'U'
                        elif direction == 'U':
                            direction = 'L'
                        elif direction == 'R':
                            direction = 'D'
                        else:
                            direction = 'R'
                    case '/':
                        if direction == 'L':
                            direction = 'D'
                        elif direction == 'D':
                            direction = 'L'
                        elif direction == 'R':
                            direction = 'U'
                        else:
                            direction = 'R'
            match direction:
                case 'R':
                    x += 1
                case 'L' :
                    x -= 1
                case 'U':
                    y -= 1
                case 'D':
                    y += 1

    return(len(energizedTiles))

print(findEnergizedTiles((0, 0, 'R')))

possibleStarts = []
for i in range(maxX):
    possibleStarts.append((i, 0, 'D'))
    possibleStarts.append((i, maxY-1, 'U'))
for i in range(maxY):
    possibleStarts.append((0, i, 'R'))
    possibleStarts.append((maxX-1, i, 'L'))

maxEnergizedTiles = 0
for start in possibleStarts:
    maxEnergizedTiles = max(maxEnergizedTiles, findEnergizedTiles(start))

print(maxEnergizedTiles)