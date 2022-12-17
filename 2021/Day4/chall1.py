def checkSolvedCard(cardMarks):
    for i in range(5):
        if cardMarks[i][0] & cardMarks[i][1] & cardMarks[i][2] & cardMarks[i][3] & cardMarks [i][4]:
            return True
        if cardMarks[0][i] & cardMarks[1][i] & cardMarks [2][i] & cardMarks [3][i] & cardMarks [4][i]:
            return True
    #if cardMarks [0][0] & cardMarks [1][1] & cardMarks [2][2] & cardMarks [3][3] & cardMarks [4][4]:
    #    return True
    #if cardMarks [4][0] & cardMarks [3][1] & cardMarks [2][2] & cardMarks [1][3] & cardMarks [0][4]:
    #    return True
    return False

def findFirstCard(orderCalled, bingoCards):
    bingoCardMarks = []
    for i in range(len(bingoCards)):
        tempCardMark = []
        for j in range(5):
            tempCardMarkLine = []
            for k in range (5):
                tempCardMarkLine.append(False)
            tempCardMark.append(tempCardMarkLine)
        bingoCardMarks.append(tempCardMark)
    
    for bingoBall in orderCalled:
        for i in range (len(bingoCards)):
            for j in range(5):
                for k in range(5):
                    if bingoCards[i][j][k] == bingoBall:
                        bingoCardMarks[i][j][k] = True
            if checkSolvedCard(bingoCardMarks[i]):
                return bingoCards[i], bingoBall

file = open("2021/inputs/day4", "r")

orderCalled = file.readline()
orderCalled = orderCalled.split(",")

bingoCards = []

while file.readline()=="\n":
    tempCard = []
    for i in range(5):
        nextLine = file.readline()
        nextLine = nextLine.split()
        nextLine[4] = nextLine[4].strip()
        tempCard.append(nextLine)
    bingoCards.append(tempCard)

firstCardData = findFirstCard(orderCalled, bingoCards)
firstCard = firstCardData[0]
finalNumber = firstCardData[1]

sumOfCard = 0
for i in range(5):
    for j in range(5):
        sumOfCard += int(firstCard[i][j])

print(sumOfCard*int(finalNumber))