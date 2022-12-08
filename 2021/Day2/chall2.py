instructionsFile = open("Day2/input.txt","r")
instructions = instructionsFile.readlines()

hPos = 0
depth = 0
aim = 0
for instruction in instructions:
    splitInstruction = instruction.split()
    if splitInstruction[0] == "forward":
        hPos += int(splitInstruction[1])
        depth += aim*int(splitInstruction[1])
    elif splitInstruction[0] == "down":
        aim += int(splitInstruction[1])
    elif splitInstruction[0] == "up":
        aim -= int(splitInstruction[1])

print (hPos)
print (depth)
print (hPos*depth)