# input loaded at 11:51:15

def getHashValue(string, currentValue = 0):
    if string == "":
        return currentValue
    currentValue += ord(string[0])
    currentValue = (currentValue * 17) % 256
    return(getHashValue(string[1:], currentValue))

with open('2023/inputs/day15') as f:
    inputData = f.read()

seq = inputData.split(',')
resultSum = 0
for string in seq:
    resultSum += getHashValue(string)
print(resultSum)

boxes = {}
for string in seq:
    if string[-2] == '=':
        label = string[:-2]
        operation = '='
        focalLen = int(string[-1])
    else:
        label = string[:-1]
        operation = '-'
    box = getHashValue(label)
    lenses = boxes.get(box, [])
    lensAdded = False
    for i, lens in enumerate(lenses):
        if lens[0] == label:
            lensAdded = True
            if operation == '=':
                lenses[i][1] = focalLen
            else:
                del lenses[i]
            break
    if not lensAdded and operation == '=':
        lenses.append([label, focalLen])
    boxes[box] = lenses

totalFocusingPower = 0
for box in boxes:
    for i, (label, focalLen) in enumerate(boxes[box]):
        totalFocusingPower += ((box+1) * (i+1) * focalLen)
print(totalFocusingPower) 