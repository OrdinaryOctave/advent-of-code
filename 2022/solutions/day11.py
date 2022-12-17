#input loaded and ready to go at 15:50:30

class Monkey:
    def __init__(self, items, op, testOperand, ifTrue, ifFalse):
        self.items = items
        self.op = op
        self.testOperand = testOperand
        self.ifTrue = ifTrue
        self.ifFalse = ifFalse
        self.itemCounter = 0
    
    def processItems(self, worryDivider):
        for item in self.items:
            self.itemCounter += 1
            item = (eval(self.op)%lcm) // worryDivider
            if item%self.testOperand == 0:
                monkeys[self.ifTrue].addItem(item)
            else:
                monkeys[self.ifFalse].addItem(item)
        self.items = []
    
    def addItem(self, item):
        self.items.append(item)
        
def getMonkeyBusiness(monkeys):
    maxMonkey = 0
    secondMonkey = 0

    for monkey in monkeys:
        if monkey.itemCounter>maxMonkey:
            secondMonkey = maxMonkey
            maxMonkey = monkey.itemCounter
        else:
            secondMonkey = max(monkey.itemCounter, secondMonkey)
    
    return maxMonkey*secondMonkey

def importMonkeys(monkeyString):
    monkeys = []
    monkeyInputs = monkeyString.split("\n\n")
    for monkey in monkeyInputs:
        monkeyLines = monkey.split('\n')
        items = monkeyLines[1].replace("  Starting items: ", "").split(", ")
        items = [int(item) for item in items]
        op = monkeyLines[2].replace("  Operation: new = ", "")
        op = op.replace("old", "item")
        testOperand = int(monkeyLines[3].replace("  Test: divisible by ", ""))
        ifTrue = int(monkeyLines[4].replace("    If true: throw to monkey ", ""))
        ifFalse = int(monkeyLines[5].replace("    If false: throw to monkey ", ""))
        
        monkeys.append(Monkey(items, op, testOperand, ifTrue, ifFalse))
    return monkeys
    
with open('inputs/day11') as f:
    input = f.read().rstrip()

monkeys = importMonkeys(input)
lcm = 1
for monkey in monkeys:
    lcm = lcm * monkey.testOperand

for i in range(20):
    for monkey in monkeys:
        monkey.processItems(3)
print(getMonkeyBusiness(monkeys))

monkeys = importMonkeys(input)

for i in range(10000):
    for monkey in monkeys:
        monkey.processItems(1)
print(getMonkeyBusiness(monkeys))
