file = open("2021/inputs/day8","r")
values = file.readlines()
outputs = []
for value in values:
    outputs.append((value.split("|")[1]).split())

outputValues = []
for output in outputs:
    valueString = ""
    for digit in output:
        if len(digit) == 2:
            valueString += "1"
        elif len(digit) == 3:
            valueString += "7"
        elif len(digit) == 4:
            valueString += "4"
        elif len(digit) == 7:
            valueString += "8"
        elif len(digit) == 6:
            if 'f' not in digit:
                valueString += "0"
            elif 'a' not in digit:
                valueString += "6"
            else:
                valueString += "9"
        elif len(digit) == 5:
            if 'a' not in digit:
                valueString += "5"
            elif 'b' not in digit:
                valueString += "2"
            else:
                valueString += "3"
    outputValues.append(int(valueString))

total = 0
for value in outputValues:
    total += value
print(total)