import datetime
from time import sleep
import requests

cookie_file = "sessionCookie.txt"
useragent_file = "useragent.txt"
now = datetime.datetime.now()
loadDay = now.day

if (now.hour==4 and now.minute>55):
    awakeTime = datetime.datetime.combine(datetime.date.today(), datetime.time(hour = 5, second=5))
    sleepTime = (awakeTime-now).total_seconds()
    print(f"not yet 5am, sleeping for {sleepTime} seconds until 5am")
    sleep(sleepTime)
elif (now.hour<5):
    loadDay -= 1
    print("Not 4:55am yet, loading previous day's challenge")

inputFilePath = f"inputs/day{loadDay}"
solutionFilePath = f"solutions/day{loadDay}.py"

try:
    with open(inputFilePath, "x") as f:
        with open(cookie_file) as g:
            session_cookie = g.read()
        with open(useragent_file) as g:
            useragent = g.read()
        print("Making request for input:")
        r = requests.get(f"https://adventofcode.com/{now.year}/day/{loadDay}/input", cookies={"session": session_cookie}, headers={"User-Agent": useragent})
        print("Saving input to file:")
        f.write(r.text)
except:
    print("Input file already exists for today, skipping input load")

now = datetime.datetime.now()
templateSolution = f"""#input loaded and ready to go at {now.time().strftime('%H:%M:%S')}

with open('inputs/day{loadDay}') as f:
    input = f.read()

"""

try:
    with open(solutionFilePath, "x") as f:
        print("Creating template solution:")
        f.write(templateSolution)
except:
    print("Solution file already exists for today, skipping solution file create")

print(f"Loading complete\nStarting today's challenge at {now.time().strftime('%H:%M:%S')}\nGood luck!")
