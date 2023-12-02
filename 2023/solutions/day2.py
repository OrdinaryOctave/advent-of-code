# input loaded at 05:00:00

with open('2023/inputs/day2') as f:
    input = f.read()

games = input.split('\n')

# PART 1
maxValues = {
    "r" : 12,
    "g" : 13,
    "b" : 14
}

validGamesSum = 0

for i, game in enumerate(games):
    gameFailed = False
    rounds = game.split(": ")[1].split("; ")
    for round in rounds:
        marbles = round.split(", ")
        for marble in marbles:
            count, colour = marble.split(" ")
            if (int(count) > maxValues[colour[:1]]):
                gameFailed = True
    if not gameFailed:
        validGamesSum += i+1

print(validGamesSum)

#PART 2
totalPower = 0

for game in games:
    gamePower = 1
    minCubes = {
    "r" : 0,
    "g" : 0,
    "b" : 0
    }
    
    rounds = game.split(": ")[1].split("; ")
    for round in rounds:
        marbles = round.split(", ")
        for marble in marbles:
            count, colour = marble.split(" ")
            colour = colour[:1]
            minCubes[colour] = max(minCubes[colour], int(count))
            
    for value in minCubes.values():
        gamePower *= value
    totalPower += gamePower
    
print(totalPower)    
