# input loaded at 11:43:31

def checkReflection(index, field):
    left = field[:index]
    right = field[index:]
    left = left [::-1]
    maxLen = min(len(left), len(right))
    if left[:maxLen] == right[:maxLen]:
        return True
    return False

def findReflectionPoint(pattern, invalidPoint = 0):
    rows = pattern.split("\n")
    columns = [[] for col in rows[0]]
    for row in rows:
        for i, char in enumerate(row):
            columns[i].append(char)
    for i in range(1, len(rows)):
        if 100*i == invalidPoint: continue
        if checkReflection(i, rows):
            return 100*i
    for i in range(1, len(columns)):
        if i == invalidPoint: continue
        if checkReflection(i, columns):
            return i
    return 0

with open('2023/inputs/day13') as f:
    inputData = f.read()

patterns = inputData.split("\n\n")
reflectionPoints = []

for pattern in patterns:
    reflectionPoints.append(findReflectionPoint(pattern))
    
print(sum(reflectionPoints))
newReflectionPoints = []

for p, pattern in enumerate(patterns):
    for x, char in enumerate(pattern):
        if char not in [".", '#']:
            continue
        char = '#' if char == '.' else '.'
        testPattern = f"{pattern[:x]}{char}{pattern[x+1:]}"
        result = findReflectionPoint(testPattern, reflectionPoints[p])
        if result != 0:
            newReflectionPoints.append(result)
            break

print(sum(newReflectionPoints))