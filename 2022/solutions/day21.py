# input loaded and ready to go at 11:36:37

def getMonkeyValue(monkeys, target):
    targetMonkey = monkeys[target]
    if type(targetMonkey) != tuple:
        return monkeys[target]
    leftValue = str(getMonkeyValue(monkeys, targetMonkey[0]))
    rightValue = str(getMonkeyValue(monkeys, targetMonkey[2]))
    return eval(leftValue + targetMonkey[1] + rightValue)

def getMonkeyEquation(monkeys, target):
    targetMonkey = monkeys[target]
    if type(targetMonkey) != tuple:
        return monkeys[target]
    leftValue = str(getMonkeyEquation(monkeys, targetMonkey[0]))
    rightValue = str(getMonkeyEquation(monkeys, targetMonkey[2]))
    equation = '(' + leftValue + targetMonkey[1] + rightValue + ')'
    if not equation.__contains__('x'):
        return eval(equation)
    return equation

def readMonkeys(input: str):
    monkeys = [x.split(': ') for x in input.split('\n')]
    monkeyDict = {}
    for monkey in monkeys:
        monkeySplit = monkey[1].split(' ')
        if len(monkeySplit) == 1:
            monkeyDict[monkey[0]] = int(monkey[1])
        else:
            monkeyDict[monkey[0]] = tuple(monkeySplit)
    return monkeyDict

with open('2022/inputs/day21') as f:
    input = f.read()
    
monkeys = readMonkeys(input)
print(int(getMonkeyValue(monkeys, 'root')))

monkeys['humn'] = 'x'
leftMonkey = monkeys['root'][0]
rightMonkey = monkeys['root'][2]
monkeys['root'] = (leftMonkey, '=', rightMonkey)

# This is kinda cheating cause right now I just get the equation and then put it in an online solver to get the value
# I'll come back and make it solve the equation properly
print(getMonkeyEquation(monkeys, 'root'))