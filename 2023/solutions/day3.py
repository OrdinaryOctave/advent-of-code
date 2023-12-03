# input loaded at 05:00:03

def checkPartNumber(y, minX, maxX):
    partNum = int(schematic[y][minX:maxX+1])
    validPart = False
    if minX == 0:
        minX += 1
    if maxX == len(schematic[0])-1:
        maxX -=1
    coords = [(x,y) for x in range(minX-1, maxX+2)]
    if y != 0:
        coords += [(x,y-1) for x in range(minX-1, maxX+2)]
    if y != len(schematic)-1:
        coords += [(x,y+1) for x in range(minX-1, maxX+2)]
        
    for x, z in coords:
        char = schematic[z][x]
        if not char.isdigit() and char != '.':
            validPart = True
            if char == '*':              
                if (x,z) in gears:
                    gears[(x,z)].append(partNum)
                else:
                    gears[(x,z)] = [partNum]
                
    return validPart

with open('2023/inputs/day3') as f:
    input = f.read()

schematic = [line for line in input.split('\n')]
parts = []
gears = {}

for i, row in enumerate(schematic):
    minJ = -1
    for j, char in enumerate(row):
        if char.isdigit():
            maxJ = j
            if minJ == -1:
                minJ = j
            continue
        if minJ == -1:
            continue
        if checkPartNumber(i, minJ, maxJ):
            parts.append(int(row[minJ:j]))
        minJ = -1
    if minJ != -1 and checkPartNumber(i, minJ, len(row)-1):
        parts.append(int(row[minJ:len(row)]))
            
print(sum(parts))

gearRatioSum = 0
for gear in gears.values():
    if len(gear) == 2:
        gearRatioSum += gear[0] * gear[1]
        
print(gearRatioSum)