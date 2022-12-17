intitialFile = open("2021/inputs/day6","r")
fishStrings = intitialFile.readline()
fishStrings = fishStrings.split(",")

fishList = []
for fish in fishStrings:
    fishList.append(int(fish))

for i in range(80):
    print(i)
    for j in range(len(fishList)):
        if fishList[j] == 0:
            fishList[j] = 6
            fishList.append(8)
        else:
            fishList[j] -= 1
print(len(fishList))