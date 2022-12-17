#input loaded and ready to go at 05:00:03

def pairOrder(left, right):
    left = list(left)
    right = list(right)
    
    for i in range(min(len(left), len(right))):
        if type(left[i]) != type(right[i]):
            if type(left[i]) == int:
                left[i] = [left[i]]
            else:
                right[i] = [right[i]]

        if left[i] != right[i]:
            if type(left[i]) == int:
                return left[i] - right[i]
            listCompare = pairOrder(left[i], right[i])
            if listCompare != 0:
                return listCompare
            
    return len(left) - len(right)

def checkPairOrder(left, right):
    return pairOrder(left, right) < 0

        
with open('inputs/day13') as f:
    input = f.read().rstrip()
inputPairs = list(map(lambda x: x.split("\n"), input.split("\n\n")))
pairs = []
for pair in inputPairs:
    pairs.append(tuple(map(lambda x: eval(x), pair)))

sum = 0
for i in range(len(pairs)):
    if checkPairOrder(pairs[i][0], pairs[i][1]):
        sum += i+1
print(sum)

packets = [[[2]], [[6]]]
for pair in pairs:
    packets.append(pair[0])
    packets.append(pair[1])

sorted = False
while not sorted:
    sorted = True
    for i in range(len(packets)-1):
        if not checkPairOrder(packets[i], packets[i+1]):
            packets[i], packets[i+1] = packets[i+1], packets[i]
            sorted = False
            
print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))