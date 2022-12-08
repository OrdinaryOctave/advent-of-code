def avg(array):
    if len(array) == 0:
        return 0
    sum=0
    for num in array:
        sum += num
    average = sum/len(array)
    return average

depthFile = open("Day1/input.txt","r")

#todo: make the variables have sensible names
depthArray1=[]
depthArray2=[]
depthArray3=[]
depthArray4=[]
#there's three comparisons made before the arrays are filled so this is a workaround that works i guess?
depthIncreases=-3

for line in depthFile:
    currentDepth = int(line)

    #there's definitely a better way to do this but this code works i guess?
    depthArray4 = depthArray3
    depthArray3 = depthArray2
    depthArray3.append(currentDepth)
    depthArray2 = depthArray1
    depthArray2.append(currentDepth)
    depthArray1 = [currentDepth]

    if avg(depthArray4) < avg(depthArray3):
        depthIncreases += 1
        #print (depthIncreases)
        #print (depthArray4)
        #print (depthArray3)

print (depthIncreases)