file = open ("Day9/input.txt","r")
heightMapStrings = file.readlines()

heightMap=[]
for line in heightMapStrings:
    lineArray=[]
    for i in range(len(line)):
        try:
            lineArray.append(int(line[i]))
        except:
            pass
    heightMap.append(lineArray)
    print(len(lineArray))

totalRisk = 0
for i in range(len(heightMap)):
    for j in range(len(heightMap[i])):
        lowPoint = True
        if j>0:
            if heightMap[i][j]>=heightMap[i][j-1]:
                lowPoint = False
        if j+1<len(heightMap):
            if heightMap[i][j]>=heightMap[i][j+1]:
                lowPoint = False
        if i+1<len(heightMap[i]):
            if heightMap[i][j]>=heightMap[i+1][j]:
                lowPoint = False
        if i>0:
            if heightMap[i][j]>=heightMap[i-1][j]:
                lowPoint = False
        if lowPoint:
            totalRisk += heightMap[i][j]+1
print (totalRisk)