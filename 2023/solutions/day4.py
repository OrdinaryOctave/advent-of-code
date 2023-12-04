# input loaded at 05:47:29

with open('2023/inputs/day4') as f:
    inputData = f.read()

cardsStrings = [line.replace("  ", " 0").split(": ")[1] for line in inputData.split("\n")]
cards = []
points = 0
totalCards = 0

for card in cardsStrings:
    sWin, sNums = card.split(" | ")
    win = [int(num) for num in sWin.split(" ")]
    nums = [int(num) for num in sNums.split(" ")]
    cards.append([1, win, nums])

for index, (count, win, nums) in enumerate(cards):
    totalCards += count
    matchingNums = 0
    for num in nums:
        if num in win:
            matchingNums += 1
            cards[index+matchingNums][0] += count
    if matchingNums > 0:
        points += pow(2, matchingNums-1)
    
print(points)
print(totalCards)
