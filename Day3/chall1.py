report = open("Day3/input.txt","r")
numbers = report.readlines()
frequencyOfOne = [0]*(len(numbers[1])-1)

for number in numbers:
    for i in range(len(number)):
        if number[i] == "1":
            frequencyOfOne[i] += 1

gamma = ""
epsilon = ""
for digit in frequencyOfOne:
    if digit > len(numbers)/2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

gammaValue=int(gamma,2)
epsilonValue = int(epsilon,2)
print(gammaValue*epsilonValue)