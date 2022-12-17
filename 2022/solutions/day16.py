#input loaded and ready to go at 05:00:52

class Valve:
    def __init__(self, name:str, flowRate: int, connections: list):
        self.name = name
        self.flowRate = flowRate
        self.connections = connections

def findShortestDistance(start: str, target: str):
    distance = 0
    toVisit = valves[start].connections
    visited = [start] + toVisit
    while True:
        distance += 1
        if target in toVisit:
            return distance
        nextStep = []
        for valve in toVisit:
            for connection in valves[valve].connections:
                if connection not in visited:
                    nextStep.append(connection)
                    visited.append(connection)
        toVisit = nextStep
        

def findMaxPressureRelease(startValve: Valve, timeLeft = 30, pressureReleased = 0, openValves = []):
    maxPressureRelease = pressureReleased
    for valve in valvesWithFlow:
        if valve not in openValves:
            distance = distances[(startValve.name, valve.name)]
            timeAtValve = (timeLeft - distance) - 1
            if timeAtValve > 0:
                valvePressureReleased = pressureReleased + (timeAtValve * valve.flowRate)
                valvePressureReleased = findMaxPressureRelease(valve, timeAtValve, valvePressureReleased, openValves + [valve])
                maxPressureRelease = max(maxPressureRelease, valvePressureReleased)
    return(maxPressureRelease)

def twoAgentMaxPressureRelease(agent1Valve: Valve, agent2Valve: Valve, agent1Downtime = 0, agent2Downtime = 0,
                                timeLeft = 26, pressureReleased = 0, openValves = []):
    timePass = min(agent1Downtime, agent2Downtime)
    timeLeft -= timePass
    agent1Downtime -= timePass
    agent2Downtime -= timePass
    maxPressureRelease = pressureReleased
    
    if len(openValves) == 2:
        global part2Progress
        part2Progress += 1
        print(f"progress: {part2Progress}/{len(valvesWithFlow)*(len(valvesWithFlow)-1)}")
    
    if agent1Downtime == 0:
        for valve in valvesWithFlow:
            if valve not in openValves:
                downtime = distances[(agent1Valve.name, valve.name)] + 1
                timeAtValve = (timeLeft - downtime)
                if timeAtValve > 0:
                    valvePressureReleased = pressureReleased + (timeAtValve * valve.flowRate)
                    valvePressureReleased = twoAgentMaxPressureRelease(valve, agent2Valve, downtime, agent2Downtime,
                                                                       timeLeft, valvePressureReleased, openValves + [valve])
                    maxPressureRelease = max(maxPressureRelease, valvePressureReleased)
    elif agent2Downtime == 0:
        for valve in valvesWithFlow:
            if valve not in openValves:
                downtime = distances[(agent2Valve.name, valve.name)] + 1
                timeAtValve = (timeLeft - downtime)
                if timeAtValve > 0:
                    valvePressureReleased = pressureReleased + (timeAtValve * valve.flowRate)
                    valvePressureReleased = twoAgentMaxPressureRelease(agent1Valve, valve, agent1Downtime, downtime,
                                                                       timeLeft, valvePressureReleased, openValves + [valve])
                    maxPressureRelease = max(maxPressureRelease, valvePressureReleased)
    return maxPressureRelease
    
with open('2022/inputs/day16') as f:
    input = f.read()

lines = input.split('\n')
valves = {}
valvesWithFlow = []

for line in lines:
    firstSplit = line.split(' has flow rate=')
    name = firstSplit[0].replace('Valve ', '')
    secondSplit = firstSplit[1].split(';')
    flowRate = int(secondSplit[0])
    secondSplit[1] = secondSplit[1].replace(' tunnels lead to valves ', '')
    secondSplit[1] = secondSplit[1].replace(' tunnel leads to valve ', '')
    connections = secondSplit[1].split(', ')
    newValve = Valve(name, flowRate, connections)
    valves[name] = newValve
    if flowRate > 0:
        valvesWithFlow.append(newValve)

distances = {}
for valve in valves:
    for flowValve in valvesWithFlow:
        if valve != flowValve.name:
            distances[(valve, flowValve.name)] = findShortestDistance(valve, flowValve.name)

print("Solution takes a while today, progress indicator printed to console")

part1 = findMaxPressureRelease(valves['AA'])
part2Progress = 0
part2 = twoAgentMaxPressureRelease(valves['AA'], valves['AA'])

print(part1)
print(part2)