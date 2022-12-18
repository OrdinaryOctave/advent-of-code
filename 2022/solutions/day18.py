# input loaded and ready to go at 05:00:09
        
with open('2022/inputs/day18') as f:
    input = f.read()

cubes = [[int(y) for y in x.split(',')] for x in input.split('\n')]
exposedSides = []

for cube in cubes:
    testCube = list(cube)
    for i in range(3):
        testCube[i]-=1
        if testCube not in cubes:
            exposedSides.append(list(testCube))
        testCube[i]+=2
        if testCube not in cubes:
            exposedSides.append(list(testCube))
        testCube[i]-=1
print(len(exposedSides))

maxX = max([cube[0] for cube in cubes])
maxY = max([cube[1] for cube in cubes])
maxZ = max([cube[2] for cube in cubes])
maxCube = [maxX, maxY, maxZ]

outside = []
for y in range(-1, maxY+2):
    for z in range(-1, maxZ+2):
        outside.append([-1, y, z])
        outside.append([maxX+1, y, z])
for x in range(-1, maxX+2):
    for z in range(-1, maxZ+2):
        outside.append([x, -1, z])
        outside.append([x, maxY+1, z])
for x in range(-1, maxX+2):
    for y in range(-1, maxY+2):
        outside.append([x, y, -1])
        outside.append([x, y, maxZ+1])

for tile in outside:
    testTile = list(tile)
    for i in range(3):
        testTile[i]+=1
        if testTile[i] <= maxCube[i] and testTile not in cubes and testTile not in outside:
            outside.append(list(testTile))
        testTile[i]-=2
        if testTile[i] >= 0 and testTile not in cubes and testTile not in outside:
            outside.append(list(testTile))
        testTile[i]+=1
        
externalCount = 0
for side in exposedSides:
    if side in outside:
        externalCount += 1
print(externalCount)