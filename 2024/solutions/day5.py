# input loaded at 11:34:25

def checkValidUpdate(rules, update):
    for i, page in enumerate(update):
        for prevPage in update[:i]:
            if prevPage in rules.get(page, []):
                return False
    return True

def fixUpdate(rules, update):
    for i in reversed(range(len(update))):
        for j in range(i+1):
            for prevPage in update[:j]:
                if prevPage in rules.get(update[j], []):
                    tmp = update[j]
                    update[j] = update[j-1]
                    update[j-1] = tmp
                    break   

with open('2024/inputs/day5') as f:
    inputData = f.read()

rules, updates = inputData.split("\n\n")
rules = [[int(page) for page in rule.split("|")] for rule in rules.splitlines()]
updates = [[int(page) for page in update.split(",")] for update in updates.splitlines()]

mustFollow = {}
prerequesites = {}
for rule in rules:
    mustFollow[rule[0]] = mustFollow.get(rule[0], []) + [rule[1]]
    prerequesites[rule[1]] = prerequesites.get(rule[1], []) + [rule[0]]

middleSum = 0
middleSumFixed = 0
incorrectUpdates = []
for update in updates:
    if checkValidUpdate(mustFollow, update):
        middleSum += update[len(update)//2]
    else:
        fixUpdate(mustFollow, update)
        middleSumFixed += update[len(update)//2]

print(middleSum)
print(middleSumFixed)
