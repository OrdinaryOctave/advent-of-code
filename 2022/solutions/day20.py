# input loaded and ready to go at 07:08:55

def decrypt(numList, iterations):
    for _ in range(iterations):
        for i in range(len(numList)):
            for j in range(len(numList)):
                if numList[j][1] == i:
                    listElem = numList.pop(j)
                    newIndex = (j + listElem[0]) % len(numList)
                    numList.insert(newIndex, listElem)
                    break
        # print([x[0] for x in numList])
    
    targetIndex = None
    for i in range(len(numList)):
        if numList[i][0] == 0:
            targetIndex = i
            break
    sumCoord = 0
    for i in range(3):
        targetIndex = (targetIndex + 1000) % len(numList)
        sumCoord += numList[targetIndex][0]
    return sumCoord

    
with open('2022/inputs/day20') as f:
    input = f.read()
numbers = input.split('\n')

numList = []
for i in range(len(numbers)):
    numList.append((int(numbers[i]), i))
    
print(decrypt(numList.copy(), 1))
secondNumList = [(x[0]*811589153, x[1]) for x in numList]
print(decrypt(secondNumList.copy(), 10))