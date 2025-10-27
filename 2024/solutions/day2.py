# input loaded at 00:34:12

def checkSafe(report):
    increasing = True if report[1] > report[0] else False
    for i in range(1, len(report)):
        currVal = report[i]
        prevVal = report[i-1]
        if (increasing and (currVal > prevVal + 3 or currVal < prevVal + 1)
            or not increasing and (currVal < prevVal - 3 or currVal > prevVal - 1)):
            return False
    return True

def checkOneSafe(reports):
    for rep in reports:
        if checkSafe(rep):
            return True
    return False

with open('2024/inputs/day2') as f:
    inputData = f.read()

reports = [[int(value) for value in report.split(" ")] for report in inputData.splitlines()]
safeCount = [checkSafe(rep) for rep in reports].count(True)

print(safeCount)

repSets = [[list(rep) for i in range(len(rep)+1)] for rep in reports]
for repSet in repSets:
    for i in range(len(repSet)-1):
        repSet[i].pop(i)
newSafeCount = [checkOneSafe(repSet) for repSet in repSets].count(True)    

print(newSafeCount)