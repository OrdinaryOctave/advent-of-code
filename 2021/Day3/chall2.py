report = open("Day3/input.txt","r")
oxygenRating = report.readlines()
carbonRating = oxygenRating.copy()

for i in range(len(oxygenRating[0])-1):
    toRemove=[]
    frequencyOfOne=[0]*(len(oxygenRating[1])-1)
    leastCommon = ""
    for number in oxygenRating:
        for j in range(len(number)):
            if number[j] == "1":
                frequencyOfOne[j] += 1
    for digit in frequencyOfOne:
        if digit >= ((len(oxygenRating))/2):
            leastCommon += "0"
        else:
            leastCommon += "1"
    for number in oxygenRating:
        if leastCommon[i] == number[i]:
            toRemove.append(number)
    for number in toRemove:
        oxygenRating.remove(number)
    if len(oxygenRating) == 1:
        break

for i in range(len(carbonRating[0])-1):
    toRemove=[]
    frequencyOfOne=[0]*(len(carbonRating[1])-1)
    mostCommon = ""
    for number in carbonRating:
        for j in range(len(number)):
            if number[j] == "1":
                frequencyOfOne[j] += 1
    for digit in frequencyOfOne:
        if digit >= len(carbonRating)/2:
            mostCommon += "1"
        else:
            mostCommon += "0"
    for number in carbonRating:
        if mostCommon[i] == number[i]:
            toRemove.append(number)
    for number in toRemove:
        carbonRating.remove(number)
    if len(carbonRating) == 1:
        break

oxygenRatingValue = int(oxygenRating[0], 2)
carbonRatingValue = int(carbonRating[0], 2)
print(oxygenRatingValue*carbonRatingValue)