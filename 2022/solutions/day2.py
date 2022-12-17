myScore = 0


with open('inputs/day2') as f:
    input = f.readline()
    while (input != ""):
        if (input.__contains__('X')):
            if (input.__contains__('A')):
                myScore+=3
            elif (input.__contains__('B')):
                myScore+=1
            else:
                myScore+=2
        elif (input.__contains__('Y')):
            myScore+=3
            if (input.__contains__('A')):
                myScore+=1
            elif (input.__contains__('B')):
                myScore+=2
            else:
                myScore+=3
        elif (input.__contains__('Z')):
            myScore+=6
            if (input.__contains__('A')):
                myScore+=2
            elif (input.__contains__('B')):
                myScore+=3
            else:
                myScore+=1
        input=f.readline()
        

print(myScore)

