maxCalories = 0
Calories2 = 0
Calories3 = 0
tempCalories = 0

with open("2022/inputs/day1") as f:
    nextLine = f.readline()
    while (nextLine != ""):
        if (nextLine == "\n"):
            if (tempCalories > maxCalories):
                Calories3 = Calories2
                Calories2 = maxCalories
                maxCalories = tempCalories
            elif (tempCalories > Calories2):
                Calories3 = Calories2
                Calories2 = tempCalories
            elif (tempCalories > Calories3):
                Calories3 = tempCalories
            tempCalories = 0
        else:
            thisCalories = int(nextLine)
            tempCalories = tempCalories + thisCalories
        nextLine = f.readline();

print(maxCalories+Calories2+Calories3)