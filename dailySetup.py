import datetime
import requests

cookie_file = "sessionCookie.txt"
useragent_file = "useragent.txt"
now = datetime.datetime.now()

# Edit these before running to load previous days/years
loadDay = now.day
loadYear = now.year

if now.hour<5 and loadDay == now.day:
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
        with open(useragent_file) as g:
            useragent = g.read()
        print(f"Making request for {loadYear} day {loadDay} input:")
        r = requests.get(f"https://adventofcode.com/{loadYear}/day/{loadDay}/input", cookies={"session": session_cookie}, headers={"User-Agent": useragent})
        print(f"Saving input to file ({inputFilePath}):")
        f.write(r.text.rstrip())
except:
    print(f"Input file already exists for {loadYear} day {loadDay}, skipping input load")

now = datetime.datetime.now()
templateSolution = f"""# input loaded and ready to go at {now.time().strftime('%H:%M:%S')}

with open('{inputFilePath}') as f:
    input = f.read()

"""

try:
    with open(solutionFilePath, "x") as f:
        print(f"Creating template solution ({solutionFilePath}):")
        f.write(templateSolution)
except:
    print(f"Solution file already exists for {loadYear} day {loadDay}, skipping solution file create")

print(f"Loading complete\nStarting today's challenge at {now.time().strftime('%H:%M:%S')}\nGood luck!")
