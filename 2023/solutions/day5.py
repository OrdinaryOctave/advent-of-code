# input loaded at 05:00:05

with open('2023/inputs/day5') as f:
    inputData = f.read()

almanac = inputData.split("\n\n")

seeds = [int (x) for x in almanac.pop(0).replace("seeds: ", "").split(" ")]

unprocessedSeedRanges = []
for i in range(len(seeds)):
    if i % 2 == 0:
        unprocessedSeedRanges.append([seeds[i]])
    else:
        unprocessedSeedRanges[i//2].append(seeds[i]+seeds[i-1])

for mapping in almanac:
    newSeeds = seeds.copy()
    for entry in mapping.split("\n")[1:]:
         destination, source, length = [int(x) for x in entry.split(" ")]
         for i, seed in enumerate(seeds):
            if seed >= source and seed < source+length:
                newSeeds[i] = destination+(seed-source)

    seeds = newSeeds

print(min(seeds))


for mapping in almanac:
    newSeedRanges = []
    map = []
    for entry in mapping.split("\n")[1:]:
         destination, source, length = [int(x) for x in entry.split(" ")]
         map.append((source-destination, source, source+length))
    
    while unprocessedSeedRanges:
        seedsChanged = False
        startSeed, endSeed = unprocessedSeedRanges.pop()
        for transformation, sourceStart, sourceEnd in map:
            if startSeed >= sourceStart and endSeed < sourceEnd:
                startSeed -= transformation
                endSeed -= transformation
                newSeedRanges.append([startSeed, endSeed])
                seedsChanged = True
                break
            if startSeed >= sourceStart and startSeed < sourceEnd:
                startSeed -= transformation
                newSeedRanges.append([startSeed, sourceEnd-transformation-1])
                unprocessedSeedRanges.append([sourceEnd, endSeed])
                seedsChanged = True
                break
            if startSeed < sourceStart and endSeed >= sourceStart:
                if endSeed < sourceEnd:
                    unprocessedSeedRanges.append([startSeed, sourceStart-1])
                    newSeedRanges.append([sourceStart-transformation, endSeed-transformation])
                    seedsChanged = True
                    break
                unprocessedSeedRanges.append([startSeed, sourceStart-1])
                unprocessedSeedRanges.append([sourceEnd, endSeed])
                newSeedRanges.append([sourceStart-transformation, sourceEnd-transformation-1])
                seedsChanged = True
                break
        
        if not seedsChanged:
            newSeedRanges.append([startSeed, endSeed])

    unprocessedSeedRanges = newSeedRanges

seedRangeStarts = [x[0] for x in unprocessedSeedRanges]
print(min(seedRangeStarts))