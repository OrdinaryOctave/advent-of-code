#input loaded and ready to go at 10:30:59

containedAssignments = 0
overlappingPairs = 0

with open('inputs/day4') as f:
    input=f.readline().rstrip()
    while (input != ""):
        pairs = input.split(",")
        splitPairs = [[int(num) for num in pairs[0].split("-")], [int(num) for num in pairs[1].split("-")]]
        
        
        if ((splitPairs[0][0]<=splitPairs[1][0] and splitPairs[0][1]>=splitPairs[1][1]) or
            (splitPairs[1][0]<=splitPairs[0][0] and splitPairs[1][1]>=splitPairs[0][1])):
            containedAssignments += 1
        
        if ((splitPairs[0][0]<=splitPairs[1][0] and splitPairs[0][1]>=splitPairs[1][0]) or
            (splitPairs[1][0]<=splitPairs[0][0] and splitPairs[1][1]>=splitPairs[0][0])):
            overlappingPairs += 1
        
        input = f.readline().rstrip()

print(containedAssignments)
print(overlappingPairs)