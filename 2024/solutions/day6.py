# input loaded at 16:02:08

def detectLoop(guard, obstacles):
    guardPos, guardDirection = guard
    visited = set()
    while True:
        x, y = guardPos
        dx, dy, nextDirection = DIRECTIONS[guardDirection]
        while (x + dx, y + dy) in obstacles:
            guardDirection = nextDirection
            dx, dy, nextDirection = DIRECTIONS[guardDirection]
        guardPos = (x + dx, y + dy)
        if x == -1 or y == -1 or x == MAX_X or y == MAX_Y:
            return False
        if (x, y, guardDirection) in visited:
            return True
        visited.add((x, y, guardDirection))

with open('2024/inputs/day6') as f:
    inputData = f.read()

lines = inputData.splitlines()
MAX_X = len(lines)
MAX_Y = len(lines[0])
DIRECTIONS = {
    "^": (-1, 0, ">"),
    ">": (0, 1, "v"),
    "v": (1, 0, "<"),
    "<": (0, -1, "^")
}

obstacles = set()
guardPos = None
guardDirection = None

for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if char == '.':
            continue
        elif char == '#':
            obstacles.add((x, y))
        else:
            guardPos = (x, y)
            guardDirection = char

startGuard = (guardPos, guardDirection)
visited = set()

left = False
while not left:
    x, y = guardPos
    dx, dy, nextDirection = DIRECTIONS[guardDirection]
    while (x + dx, y + dy) in obstacles:
        guardDirection = nextDirection
        dx, dy, nextDirection = DIRECTIONS[guardDirection]
    guardPos = (x + dx, y + dy)
    if x == -1 or y == -1 or x == MAX_X or y == MAX_Y:
        left = True
    else:
        visited.add((x, y))

print(len(visited))

obstacleCandidates = visited
obstacleCandidates.remove(startGuard[0])
validCandidateCount = 0

for i, pos in enumerate(obstacleCandidates):
    if i%200 == 0:
        #Progress indicator
        print(i/len(obstacleCandidates))
    if detectLoop(startGuard, obstacles|{pos}):
        validCandidateCount += 1

print(validCandidateCount)