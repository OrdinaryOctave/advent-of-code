import datetime
import requests
import sys

cookie_file = "sessionCookie.txt"
useragent = "https://github.com/OrdinaryOctave/advent-of-code by ordinaryoctave@proton.me"
now = datetime.datetime.now()

loadDay = now.day
loadYear = now.year
setDay, setYear = False, False

if len(sys.argv) > 1:
    loadDay = int(sys.argv[1])
    setDay = True
if len(sys.argv) > 2:
    loadYear = int(sys.argv[2])
    setYear = True

if not setDay and now.hour<5:
    loadDay -= 1
    print("Not 5am yet, loading previous day's challenge")

if loadDay>25 or (loadYear == now.year and (now.month<12 or loadDay > now.day)):
    print(f"Specified day ({loadYear} day {loadDay}) not valid, exiting")
    exit()

inputFilePath = f"{loadYear}/inputs/day{loadDay}"
solutionFilePath = f"{loadYear}/solutions/day{loadDay}.py"

try:
    with open(inputFilePath, "x") as f:
        with open(cookie_file) as g:
            session_cookie = g.read()
        print(f"Making request for {loadYear} day {loadDay} input:")
        r = requests.get(f"https://adventofcode.com/{loadYear}/day/{loadDay}/input", cookies={"session": session_cookie}, headers={"User-Agent": useragent})
        print(f"Saving input to file ({inputFilePath}):")
        f.write(r.text.rstrip())
except:
    print(f"Input file already exists for {loadYear} day {loadDay}, skipping input load")

now = datetime.datetime.now()
templateSolution = f"""# input loaded at {now.time().strftime('%H:%M:%S')}

with open('{inputFilePath}') as f:
    inputData = f.read()

"""

try:
    with open(solutionFilePath, "x") as f:
        print(f"Creating template solution ({solutionFilePath}):")
        f.write(templateSolution)
except:
    print(f"Solution file already exists for {loadYear} day {loadDay}, skipping solution file create")

print(f"Loading complete\nStarting today's challenge at {now.time().strftime('%H:%M:%S')}\nGood luck!")
