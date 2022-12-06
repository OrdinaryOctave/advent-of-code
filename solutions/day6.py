#input loaded and ready to go at 14:05:53


with open('inputs/day6') as f:
    
    buffer = []
    readIndex = 0
    for i in range (14):
        buffer.append(f.read(1))
        readIndex += 1
    while (len(set(buffer))!=14):
        buffer.pop(0)
        buffer.append(f.read(1))
        readIndex += 1

print(readIndex)

