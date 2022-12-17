def findMatchingChar (string1: str , string2: str):
    for char in string1:
        if (string2.__contains__(char)):
            return char

def getItemPriority(item: str):
    if (item.isupper()):
        return ord(item) - 38
    else:
        return ord(item) - 96

misplacedItems = []
input = " "
rucksacks = []

with open('2022/inputs/day3') as f:
    while (input != ""):
        input = f.readline().rstrip()
        rucksacks.append(input)
        compartments = []
        compartments.append(input[0 : int((len(input)/2))])
        compartments.append(input[int((len(input)/2)) : len(input)])
        misplacedItems.append(findMatchingChar(compartments[0], compartments[1]))
misplacedItems.pop(-1)
rucksacks.pop(-1)

sumPriority = 0

for item in misplacedItems:
    sumPriority += getItemPriority(item)

print (sumPriority)

badgeItems = []

for i in range(0, len(rucksacks), 3):
    for item in rucksacks[i]:
        if (rucksacks[i+1].__contains__(item) and rucksacks[i+2].__contains__(item)):
            badgeItems.append(item)
            break
          
sumPriority = 0

for item in badgeItems:
    sumPriority += getItemPriority(item)

print (sumPriority)
