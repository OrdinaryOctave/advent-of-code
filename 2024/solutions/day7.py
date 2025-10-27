# input loaded at 16:55:38

def processCalc(ops, values, debug = False):
    ops = list(ops)
    values = list(values)
    num = values.pop(0)
    for op in ops:
        if op == '+':
            num += values.pop(0)
        elif op == "*":
            num *= values.pop(0)
        else:
            num = int(f"{num}{values.pop(0)}")
    return num


def checkPossibleP1(values, target):
    operatorQueue = [""]
    for i in range(len(values)-1):
        newQueue = []
        for seq in operatorQueue:
            newQueue.append(seq+"+")
            newQueue.append(seq+"*")
        operatorQueue = newQueue
    
    for seq in operatorQueue:
        if processCalc(seq, values) == target:
            return True
    return False

def checkPossibleP2(values, target):
    operatorQueue = [""]
    for i in range(len(values)-1):
        newQueue = []
        for seq in operatorQueue:
            newQueue.append(seq+"+")
            newQueue.append(seq+"*")
            newQueue.append(seq+"|")
        operatorQueue = newQueue
    
    for seq in operatorQueue:
        if processCalc(seq, values) == target:
            return True
    return False


with open('2024/inputs/day7') as f:
    inputData = f.read()

equations = inputData.splitlines()
calibrationResult = 0
calibration2Result = 0
for equation in equations:
    result, values = equation.split(": ")
    result = int(result)
    values = [int(val) for val in values.split(" ")]
    if checkPossibleP1(values, result):
        calibrationResult += result
    elif checkPossibleP2(values, result):
        calibration2Result += result

print(calibrationResult)
print(calibration2Result + calibrationResult)

