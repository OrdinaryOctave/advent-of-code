# input loaded at 05:00:00

with open('2023/inputs/day2') as f:
    input = f.read()

games = input.split('\n')

maxCubes = {
    "red"   : 12,
    "green" : 13,
    "blue"  : 14
}
validGamesSum = 0
totalPower = 0

for i, game in enumerate(games):
    gameFailed = False
    gamePower = 1
    minCubes = {
    "red"   : 0,
    "green" : 0,
    "blue"  : 0
    }
    
    rounds = game.split(": ")[1].split("; ")
    for round in rounds:
        marbles = round.split(", ")
        for marble in marbles:
            count, colour = marble.split(" ")
            if (int(count) > maxCubes[colour]):
                gameFailed = True
            minCubes[colour] = max(minCubes[colour], int(count))
    
    if not gameFailed:
        validGamesSum += i+1
    for value in minCubes.values():
        gamePower *= value
    totalPower += gamePower

print(validGamesSum)
print(totalPower)    