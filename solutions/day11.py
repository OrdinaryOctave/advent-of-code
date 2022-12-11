#input loaded and ready to go at 15:50:30
# Hard coding the monkeys because it's easier - this won't work with other inputs
# This code is only part 2 - I just modified part 1 code to produce the resuls

class Monkey:
    def __init__(self, items, op, testOperand, ifTrue, ifFalse):
        self.items = items
        self.op = op
        self.testOperand = testOperand
        self.ifTrue = ifTrue
        self.ifFalse = ifFalse
        self.itemCounter = 0
    
    def processItems(self):
        for item in self.items:
            self.itemCounter += 1
            item = eval(self.op)%lcm
            if item%self.testOperand == 0:
                monkeys[self.ifTrue].addItem(item)
            else:
                monkeys[self.ifFalse].addItem(item)
        self.items = []
    
    def addItem(self, item):
        self.items.append(item)
        

monkeys = [Monkey([71, 56, 50, 73], "item*11", 13, 1, 7)]
monkeys.append(Monkey([70, 89, 82], "item+1", 7, 3, 6))
monkeys.append(Monkey([52, 95], "item*item", 3, 5, 4))
monkeys.append(Monkey([94, 64, 69, 87, 70], "item+2", 19, 2, 6))
monkeys.append(Monkey([98, 72, 98, 53, 97, 51], "item + 6", 5, 0, 5))
monkeys.append(Monkey([79], "item+7", 2, 7, 0))
monkeys.append(Monkey([77, 55, 63, 93, 66, 90, 88, 71], "item*7", 11, 2, 4))
monkeys.append(Monkey([54, 97, 87, 70, 59, 82, 59], "item+8", 17, 1, 3))
lcm = 9699690 # lowest common multiple of all testOperands

for i in range(10000):
    for monkey in monkeys:
        monkey.processItems()
    print(i)

maxMonkey = 0
secondMonkey = 0

for monkey in monkeys:
    if monkey.itemCounter>maxMonkey:
        secondMonkey = maxMonkey
        maxMonkey = monkey.itemCounter
    else:
        secondMonkey = max(monkey.itemCounter, secondMonkey)

print(maxMonkey*secondMonkey)
