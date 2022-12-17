#input loaded and ready to go at 13:29:01

with open('2022/inputs/day10') as f:
    input = f.read()

instructions = input.split('\n')

cycleCount = 0
x = 1
strength = 0

for instruction in instructions:
    cycleCount+=1
    if (cycleCount-20)%40 == 0:
        strength += cycleCount*x 
        
    if instruction != "noop":
        operand = int(instruction.split(" ")[1])
        
        cycleCount+=1
        if (cycleCount-20)%40 == 0:
            strength += cycleCount*x
            
        x += operand
        

print(strength)

cycleCount = 0
x = 1
crtOutput = ""

for instruction in instructions:
    if abs(x-(cycleCount%40))<=1:
        crtOutput+='#'
    else:
        crtOutput+=' '
    
    cycleCount+=1
    if cycleCount%40 == 0:
        crtOutput += "\n" 
        
    if instruction != "noop":
        operand = int(instruction.split(" ")[1])
        
        if abs(x-(cycleCount%40))<=1:
            crtOutput+='#'
        else:
            crtOutput+=' '
        cycleCount+=1
        if cycleCount%40 == 0:
            crtOutput += "\n" 
            
        x += operand

print(crtOutput)