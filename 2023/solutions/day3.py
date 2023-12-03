# input loaded at 05:00:03

with open('2023/inputs/day3') as f:
    input = f.read()

schematic = input.split('\n')
rowLength = len(schematic[0])
parts = []

for x, row in enumerate(schematic):
    enumeratedRow = enumerate(row)
    for y, char in enumeratedRow:
        if char.isdigit():
            parts.append([(x,y), 1])
            while next(enumeratedRow, (0, '.'))[1].isdigit():
                parts[-1][1] += 1
            
validParts = []
gears = {}

for (x, y), length in parts:
    partNum = int(schematic[x][y:y+length])
    neighbourCoords = []
    for row in range(max(x-1, 0), min(len(schematic), x+2)):
        neighbourCoords += [(row, col) for col in range(max(y-1, 0), min(y+length+1, rowLength))]
    validPart = False
    for row, col in neighbourCoords:
        char = schematic[row][col]
        if not char.isdigit() and char != '.':
            validPart = True
            if char == '*':
                gears.setdefault((row, col), []).append(partNum)
    if validPart:
        validParts.append(partNum)
    
print(sum(validParts))

gearRatioSum = 0
for gear in gears.values():
    if len(gear) == 2:
        gearRatioSum += gear[0] * gear[1]
        
print(gearRatioSum)
