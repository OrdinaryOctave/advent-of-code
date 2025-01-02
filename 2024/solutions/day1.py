# input loaded at 00:20:49

with open('2024/inputs/day1') as f:
    inputData = f.read()

list1 = []
list2 = []

for line in inputData.splitlines():
    loc1, loc2 = map(int, line.split("   "))
    list1.append(loc1)
    list2.append(loc2)

list1.sort()
list2.sort()

totalDistance = 0
for loc1, loc2 in zip(list1, list2):
    totalDistance += abs(loc1-loc2)

print(totalDistance)

list2LocationFrequencies = {}
for location in list2:
    list2LocationFrequencies[location] = list2LocationFrequencies.get(location, 0) + 1

similarityScore = 0
for location in list1:
    similarityScore += location * list2LocationFrequencies.get(location, 0)

print(similarityScore)