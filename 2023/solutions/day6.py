# input loaded at 05:00:26

with open('2023/inputs/day6') as f:
    inputData = f.read()

inputData = inputData.split("\n")

timeSplit = inputData[0].split()[1:]
distanceSplit = inputData[1].split()[1:]
raceRecords = []

for i in range(len(timeSplit)):
    raceRecords.append((int(timeSplit[i]), int(distanceSplit[i])))

part1 = 1
for time, distance in raceRecords:
    margin = 0
    validRange = False
    for heldTime in range(time):
        testDistance = heldTime*(time-heldTime)
        if testDistance > distance:
            margin += 1
            validRange = True
        elif validRange:
            break
    
    part1 *= margin

print(part1)

trueTime = int(''.join(timeSplit))
trueDistance = int(''.join(distanceSplit))

margin = 0
validRange = False
for heldTime in range(trueTime):
    testDistance = heldTime*(trueTime-heldTime)
    if testDistance > trueDistance:
        margin += 1
        validRange = True
    elif validRange:
        break
    
print(margin)