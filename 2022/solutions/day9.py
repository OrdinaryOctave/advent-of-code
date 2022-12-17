#input loaded and ready to go at 13:56:03

with open('inputs/day9') as f:
    input = f.read()
    
def moveHead(direction, head):
    if direction == 'L':
        head[0] -= 1
    elif direction == 'R':
        head[0] += 1
    elif direction == 'U':
        head[1] += 1
    elif direction == 'D':
        head[1] -= 1

def moveTail(head, tail):
    xDiff = head[0]-tail[0]
    yDiff = head[1]-tail[1]
    if abs(xDiff) < 2 and abs(yDiff) < 2:
        return
    if xDiff < 0:
        tail[0] -= 1
    if xDiff > 0:
        tail[0] += 1
    if yDiff < 0:
        tail[1] -= 1
    if yDiff > 0:
        tail[1] += 1
    

moves=input.split('\n')
moves.pop(-1)
moveSplit = []
for move in moves:
    moveSplit.append(move.split(" "))

knotLocations = [[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0]] 
firstTailLocations = []
lastTailLocations = []

for move in moveSplit:
    for repeat in range(int(move[1])):
        moveHead(move[0], knotLocations[0])
        for i in range(9):
            moveTail(knotLocations[i], knotLocations[i+1])
        staticTail = tuple(knotLocations[1])
        if staticTail not in firstTailLocations:
            firstTailLocations.append(staticTail)
        staticTail = tuple(knotLocations[9])
        if staticTail not in lastTailLocations:
            lastTailLocations.append(staticTail)
            
print(len(firstTailLocations))
print(len(lastTailLocations))