# input loaded at 08:52:40

with open('2023/inputs/day11') as f:
    inputData = f.read()

galaxyMap = [[char for char in line] for line in inputData.split("\n")]

allX = set()
allY = set()
galaxies = []

for x, row in enumerate(galaxyMap):
    for y, char in enumerate(row):
        if char == '#':
            allX.add(x)
            allY.add(y)
            galaxies.append((x, y))

part1Distance = 0
part2Distance =0
for i, galaxy in enumerate(galaxies):
    x, y = galaxy
    for j in range(i+1, len(galaxies)):
        targetX, targetY = galaxies[j]
        distance = abs(x - targetX) + abs(y - targetY)
        part1Distance += distance
        part2Distance += distance
        for k in range(min(x, targetX), max(x, targetX)):
            if k not in allX:
                part1Distance += 1
                part2Distance += 999999
        for k in range(min(y, targetY), max(y, targetY)):
            if k not in allY:
                part1Distance += 1
                part2Distance += 999999
        

print(part1Distance)
print(part2Distance)