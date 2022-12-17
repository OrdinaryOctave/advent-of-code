intitialFile = open("2021/inputs/day6","r")
fishStrings = intitialFile.readline()
fishStrings = fishStrings.split(",")

fishList = []
for fish in fishStrings:
    fishList.append(int(fish))
    
fishDays = [0]*9
for fish in fishList:
    fishDays[fish] += 1

for i in range(256):
    newFishCount = fishDays[0]
    for i in range(8):
        fishDays[i] = fishDays[i+1]
    fishDays[8] = newFishCount
    fishDays[6] += newFishCount
        

#for i in range(256):
#    for j in range(len(fishList)):
#        if fishList[j] == 0:
#            fishList[j] = 6
#            fishList.append(8)
#        else:
#            fishList[j] -= 1
totalOfFish = 0
for fish in fishDays:
    totalOfFish += fish
print(totalOfFish)