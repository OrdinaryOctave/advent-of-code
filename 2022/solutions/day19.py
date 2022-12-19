# input loaded and ready to go at 05:00:23

def getBestGeodes(costs, robots = [1,0,0,0], startResources = [0,0,0,0], timeLeft = 24, previousMax = 0):
    resources = list(startResources)
    for i in range(4):
        resources[i] += robots[i]
    if timeLeft == 1:
        return resources[3]
    timeLeft -= 1
        
    theoreticalMax = resources[3]
    for i in range(timeLeft):
        theoreticalMax += robots[3] + i
    if theoreticalMax < previousMax:
        return previousMax
    
    maxGeodes = getBestGeodes(costs, robots, resources, timeLeft, previousMax)
    for i in range(3, -1, -1):
        doTrial = False
        trialResources = list(resources)
        if i == 3 and costs[3][0] <= startResources[0] and costs[3][1] <= startResources[2]:
            trialResources[0] -= costs[3][0]
            trialResources[2] -= costs[3][1]
            trialRobots = list(robots)
            trialRobots[3] += 1
            trialGeodes = getBestGeodes(costs, trialRobots, trialResources, timeLeft, maxGeodes)
            maxGeodes = max(maxGeodes, trialGeodes)
            break
        elif i == 0 and costs[0] <= startResources[0] and robots[0] < costs[4]:
            trialResources[0] -= costs[0]
            doTrial = True
        elif i == 1 and costs[1] <= startResources[0] and robots[1] < costs[2][1]:
            trialResources[0] -= costs[1]
            doTrial = True
        elif i == 2 and costs[i][0] <= startResources[0] and costs[i][1] <= startResources[1]:
            trialResources[0] -= costs[i][0]
            trialResources[1] -= costs[i][1]
            doTrial = True
        if doTrial:
            trialRobots = list(robots)
            trialRobots[i] += 1
            trialGeodes = getBestGeodes(costs, trialRobots, trialResources, timeLeft, maxGeodes)
            maxGeodes = max(maxGeodes, trialGeodes)
    return maxGeodes


with open('2022/inputs/day19.example') as f:
    input = f.read().split('\n')

costsList = []
for line in input:
    line = line.split(': ')[1]
    robots = line.split('. ')
    ore = robots[0].replace('Each ore robot costs ', '')
    ore = int(ore.replace(' ore', ''))
    clay = robots[1].replace('Each clay robot costs ', '')
    clay = int(clay.replace(' ore', ''))
    obsidian = robots[2].replace('Each obsidian robot costs ', '')
    obsidian = obsidian.split(' ore and ')
    obsidian[1] = obsidian[1].replace(' clay', '')
    obsidian = (int(obsidian[0]), int(obsidian[1]))
    geode = robots[3].replace('Each geode robot costs ', '')
    geode = geode.split(' ore and ')
    geode[1] = geode[1].replace(' obsidian.', '')
    geode = (int(geode[0]), int(geode[1]))
    maxOreCost = max(ore, clay, obsidian[0], geode[0])
    costsList.append((ore, clay, obsidian, geode, maxOreCost))

qualityLevel = 0
for i in range(len(costsList)):
    bestGeodes = getBestGeodes(costsList[i])
    qualityLevel += (i+1) * bestGeodes
    print(f'Calculated blueprint {i+1}/30       Number of geodes opened:{bestGeodes}')
    
print(qualityLevel)