# input loaded at 17:57:29
from math import gcd

with open('2024/inputs/day8') as f:
    inputData = f.read()
lines = inputData.splitlines()
MAX_X = len(lines)-1
MAX_Y = len(lines[0])-1

antennae = {}
for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if char != '.':
            antennae.setdefault(char, []).append((x, y))

antinodes = set()
for group in antennae.values():
    for antenna in group:
        x, y = antenna
        for neighbour in group:
            if neighbour == antenna:
                continue
            x2, y2 = neighbour
            dx = x2-x
            dy = y2-y
            antinode = (x-dx, y-dy)
            if (antinode[0] >= 0 and antinode[0] <= MAX_X and
                antinode[1] >= 0 and antinode[1] <= MAX_Y):
                antinodes.add(antinode)

print(len(antinodes))

antinodes = set()
for group in antennae.values():
    for i in range(len(group)):
        antenna = group.pop(0)
        for neighbour in group:
            x, y = antenna
            x2, y2 = neighbour
            dx = x2-x
            dy = y2-y
            divisor = gcd(dx, dy)
            dx = dx // divisor
            dy = dy // divisor
            while (x >= 0 and x <= MAX_X and
                   y >= 0 and y <= MAX_Y):
                antinodes.add((x, y))
                x += dx
                y += dy
            x, y = antenna
            while (x >= 0 and x <= MAX_X and
                   y >= 0 and y <= MAX_Y):
                antinodes.add((x, y))
                x -= dx
                y -= dy

print(len(antinodes))
