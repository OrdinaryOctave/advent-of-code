file = open("Day8/input.txt","r")
values = file.readlines()
outputs = []
for value in values:
    outputs.append((value.split("|")[1]).split())

uniqueDigits = 0
for output in outputs:
    for digit in output:
        if len(digit) == 2:
            uniqueDigits += 1
        elif len(digit) == 3:
            uniqueDigits += 1
        elif len(digit) == 4:
            uniqueDigits += 1
        elif len(digit) == 7:
            uniqueDigits += 1
            
print(uniqueDigits)