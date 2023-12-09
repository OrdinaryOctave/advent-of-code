# input loaded at 07:46:39
def getNextValues(sequence):
    if set(sequence) == {0}:
        return (0, 0)
    valueDiffs = []
    for i in range(len(sequence)-1):
        valueDiffs.append(sequence[i+1]-sequence[i])
    next, prev = getNextValues(valueDiffs)
    return (sequence[-1]+next, sequence[0]-prev)

with open('2023/inputs/day9') as f:
    inputData = f.read()

sequences = [[int(x) for x in string.split()] for string in inputData.split("\n")]
sumNextValues = 0
sumPrevValues = 0
for history in sequences:
    next, prev = getNextValues(history)
    sumNextValues += next
    sumPrevValues += prev

print(sumNextValues)
print(sumPrevValues)