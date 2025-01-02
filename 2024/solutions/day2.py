# input loaded at 00:34:12

with open('2024/inputs/day2') as f:
    inputData = f.read()

reports = [[int(value) for value in report.split(" ")] for report in inputData.splitlines()]
safeCount = 0

for report in reports:
    increasing = True if report[1] > report[0] else False
    fail = False
    for i in range(1, len(report)):
        currVal = report[i]
        prevVal = report[i-1]
        if increasing and (currVal > prevVal + 3 or currVal < prevVal + 1):
            fail = True
            break
        if not increasing and (currVal < prevVal - 3 or currVal > prevVal - 1):
            fail = True
            break
    if not fail:
        safeCount += 1

print(safeCount)