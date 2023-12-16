# input loaded at 12:24:59

def spinCycle(platform):
    for y, row in enumerate(platform):
        for x, char in enumerate(row):
            if char == 'O':
                for i in range(y, 0, -1):
                    if platform[i-1][x] == '.':
                        platform[i-1][x] = 'O'
                        platform[i][x] = '.'
                        continue
                    break
    for y, row in enumerate(platform):
        for x, char in enumerate(row):
            if char == 'O':
                for i in range(x, 0, -1):
                    if platform[y][i-1] == '.':
                        platform[y][i-1] = 'O'
                        platform[y][i] = '.'
                        continue
                    break
    for y in range(len(platform)-1, -1, -1):
        for x, char in enumerate(platform[y]):
            if char == 'O':
                for i in range(y, len(platform)-1):
                    if platform[i+1][x] == '.':
                        platform[i+1][x] = 'O'
                        platform[i][x] = '.'
                        continue
                    break
    for y, row in enumerate(platform):
        for x in range(len(row)-1, -1, -1):
            if row[x] == 'O':
                for i in range(x, len(row)-1):
                    if platform[y][i+1] == '.':
                        platform[y][i+1] = 'O'
                        platform[y][i] = '.'
                        continue
                    break
    return platform


with open('2023/inputs/day14.example') as f:
    inputData = f.read()

platform = [list(s) for s in inputData.split("\n")]

for y, row in enumerate(platform):
    for x, char in enumerate(row):
        if char == 'O':
            for i in range(y, 0, -1):
                if platform[i-1][x] == '.':
                    platform[i-1][x] = 'O'
                    platform[i][x] = '.'
                    continue
                break

maxY = len(platform)
totalLoad = 0
for y, row in enumerate(platform):
    totalLoad += row.count('O') * (maxY-y)

print(totalLoad)

platform = [list(s) for s in inputData.split("\n")]
prevStates = {}

for i in range(1000000000):
    if str(platform) not in prevStates:
        prevStates[str(platform)] = i
        platform = spinCycle(platform)
        continue
    
    cycleLen = i - prevStates[str(platform)]
    remainingSteps = (1000000000 - i) % cycleLen
    for j in range(remainingSteps):
        platform = spinCycle(platform)
    break
    
    

totalLoad = 0
for y, row in enumerate(platform):
    totalLoad += row.count('O') * (maxY-y)
print(totalLoad)