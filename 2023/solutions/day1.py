# input loaded at 05:00:02

with open('2023/inputs/day1') as f:
    input = f.read()
input = input.split('\n')

# PART 1
calibrationValues=[]

for line in input:
    firstNum = 0
    lastNum = 0
    for char in line:
        try:
            lastNum = int(char)
            if firstNum == 0:
                firstNum = lastNum
        except:
            continue
    calibrationValues.append(int(f"{firstNum}{lastNum}"))

print(sum(calibrationValues))

#PART 2
calibrationValues = []
wordNumbers = {
    "one"   : 1,
    "two"   : 2,
    "three" : 3,
    "four"  : 4,
    "five"  : 5,
    "six"   : 6,
    "seven" : 7,
    "eight" : 8,
    "nine"  : 9
}

for line in input:
    firstNum = 0
    lastNum = 0
    
    for i, char in enumerate(line):
        foundNum = 0
        try:
            foundNum = int(char)
        except:
            if len(line) - i > 2 and line[i:i+3] in wordNumbers:
                foundNum = wordNumbers[line[i:i+3]]
            elif len(line) - i > 3 and line[i:i+4] in wordNumbers:
                foundNum = wordNumbers[line[i:i+4]]
            elif len(line) - i > 4 and line[i:i+5] in wordNumbers:
                foundNum = wordNumbers[line[i:i+5]]

        if foundNum != 0:                  
            lastNum = foundNum
            if firstNum == 0:
                firstNum = foundNum

    calibrationValues.append(int(f"{firstNum}{lastNum}"))

print(sum(calibrationValues))
