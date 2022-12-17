#input loaded and ready to go at 16:36:45

def getScannedLocationsInRow(row):
    scannedLocations = []
    for object in objects:
        sensor = object[0]
        beacon = object[1]
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        
        if row in range(sensor[1]-distance, sensor[1]+distance+1):
            sensorWidth = distance-abs(row-sensor[1])
            scannedLocations.append([sensor[0] - sensorWidth, sensor[0] + sensorWidth])
    
    scannedLocations.sort()
    startPos = scannedLocations[0][0]
    endPos = scannedLocations[0][1]
    combinedScannedLocations = []
    
    for i in range(1, len(scannedLocations)):
        if endPos < scannedLocations[i][0]:
            combinedScannedLocations.append((startPos, endPos))
            startPos = scannedLocations[i][0]
        endPos = max(scannedLocations[i][1], endPos)
    combinedScannedLocations.append((startPos, endPos))
    return combinedScannedLocations

# This won't work if the missing beacon is at x coordinate 0 or 4000000
def findMissingBeacon():
    for row in range(4000001):
        scanRow = getScannedLocationsInRow(row)
        if len(scanRow) > 1:
            for i in range(len(scanRow)-1):
                if scanRow[i][1] < 4000000:
                    return (scanRow[i][1]+1, row)

with open('inputs/day15') as f:
    input = f.read().rstrip()

lines = input.split("\n")
objects = [[[int(coord.split('=')[1]) for coord in obj.split(',')] for obj in line.split(':')] for line in lines]

part1Row = getScannedLocationsInRow(2000000)
beacons = []
for object in objects:
    if object[1] not in beacons:
        beacons.append(object[1])

numberOfFreeTiles = 0
beaconsInPart1Row = 0
for beacon in beacons:
    if beacon[1] == 2000000:
        beaconsInPart1Row += 1

for scannedSection in part1Row:
    numberOfFreeTiles += scannedSection[1]-scannedSection[0]+1

numberOfFreeTiles -= beaconsInPart1Row
print(numberOfFreeTiles)

missingBeacon = findMissingBeacon()
print((missingBeacon[0]*4000000)+ missingBeacon[1])