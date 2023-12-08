# input loaded at 05:00:08

def getHandType(hand):
    uniqueCardValues = set(hand)
    numCardValues = len(uniqueCardValues)
    if 1 in uniqueCardValues:
        numCardValues -= 1
        uniqueCardValues.discard(1)
    
    if numCardValues == 5:
        return 0
    if numCardValues == 4:
        return 1
    if numCardValues == 3:
        for value in uniqueCardValues:
            if hand.count(value) == 3-hand.count(1):
                return 3
        return 2
    if numCardValues == 2:
        for value in uniqueCardValues:
            if hand.count(value) == 4-hand.count(1):
                return 5
        return 4
    return 6

# Return True if hand1 stronger
def compareHands(hand1Entry, hand2Entry):
    hand1 = hand1Entry[0]
    hand2 = hand2Entry[0]
    hand1Type = getHandType(hand1)
    hand2Type = getHandType(hand2)
    
    if hand1Type > hand2Type:
        return True
    if hand2Type > hand1Type:
        return False
    
    for i in range(len(hand1)):
        if hand1[i] > hand2[i]:
            return True
        if hand2[i] > hand1[i]:
            return False
    return False

with open('2023/inputs/day7') as f:
    inputData = f.read()
    
cardValueHex = {'T': 'A', 'J': 'B', 'Q': 'C', 'K': 'D', 'A': 'E'}
handStrings = [hand.split() for hand in inputData.split("\n")]

for part in range(2):
    hands = [([int(cardValueHex.get(card, card), 16) for card in hand], int(bid)) for (hand, bid) in handStrings]
    sortedHands = []
    for i, handEntry in enumerate(hands):
        j = 0
        while j < i and compareHands(handEntry, sortedHands[j]):
            j += 1
        sortedHands.insert(j, handEntry)
                
    winnings = 0

    for i, (hand, bid) in enumerate(sortedHands):
        winnings += (i+1) * bid

    print(winnings)
    cardValueHex['J'] = '1'