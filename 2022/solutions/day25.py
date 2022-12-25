# input loaded and ready to go at 18:01:19
def SnafuToInt(snafu: str):
    snafuDict = {
        '=': -2,
        '-': -1,
        '0': 0,
        '1': 1,
        '2': 2
    }
    
    integer = 0
    snafu = snafu[::-1]
    for i in range(len(snafu)):
        if i == 0:
            integer += snafuDict[snafu[i]]
        else:
            integer += snafuDict[snafu[i]] * pow(5,i)
    return integer

def intToSnafu(integer: int):
    snafu = []
    while integer != 0:
        snafu.append(integer % 5)
        integer = integer // 5
    
    for i in range(len(snafu)):
        if snafu[i] > 2:
            if snafu[i] == 3:
                snafu[i] = '='
            elif snafu[i] == 4:
                snafu[i] = '-'
            else:
                snafu[i] = str(snafu[i] - 5)
            
            if i+1 != len(snafu):
                snafu[i+1] += 1
            else:
                snafu.append('1')
        else:
            snafu[i] = str(snafu[i])
    
    return ''.join(snafu[::-1])
                

with open('2022/inputs/day25') as f:
    input = f.read()

balloons = input.split('\n')

print(intToSnafu(sum(map(SnafuToInt, balloons))))

