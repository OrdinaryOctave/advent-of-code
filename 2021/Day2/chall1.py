instructionsFile = open("2021/inputs/day2","r")
instructions = instructionsFile.readlines()

hPos = 0
depth = 0
for instruction in instructions:
    splitInstruction = instruction.split()
    if splitInstruction[0] == "forward":
        hPos += int(splitInstruction[1])
    elif splitInstruction[0] == "down":
        depth += int(splitInstruction[1])
    elif splitInstruction[0] == "up":
        depth -= int(splitInstruction[1])

print (hPos)
print (depth)
print (hPos*depth)