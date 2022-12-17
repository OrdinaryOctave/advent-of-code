#input loaded and ready to go at 09:24:51

from collections import deque

with open('2022/inputs/day5') as f:
    setupStack = deque()
    line = f.readline().rstrip('\n')
    while (line != ""):
        setupStack.append(line)
        line = f.readline().rstrip('\n')
    
    stacks = []
    for i in range(9):
        stacks.append(deque())
    
    setupStack.pop()
    while setupStack:
        line = setupStack.pop()
        for i in range(9):
            if line[(i*4)+1] != " ":
                stacks[i].append(line[(i*4)+1])
    
    line = f.readline().rstrip("\n")
    while (line != ""):
        instructions = line.split(" ")
        numberToMove = int(instructions[1])
        startingStack = int(instructions[3])-1
        destinationStack = int(instructions[5])-1
        tempStack = deque()
        
        for i in range(numberToMove):
            tempStack.append(stacks[startingStack].pop())
        for i in range(numberToMove):
            stacks[destinationStack].append(tempStack.pop())
            
        line = f.readline().rstrip("\n")
        print(line)
        
topStacks = ""
for i in range(9):
    topStacks = topStacks + stacks[i].pop()

print(topStacks)