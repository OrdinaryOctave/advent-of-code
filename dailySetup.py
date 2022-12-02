import datetime
import requests

cookie_file = "sessionCookie.txt"
useragent_file = "useragent.txt"

now = datetime.datetime.now()

with open(cookie_file) as f:
    session_cookie = f.read()

with open(useragent_file) as f:
    useragent = f.read()

if (now.hour<5):
    now = now - datetime.timedelta(days = 1)
    print("Not 5am yet, loading previous day's challenge")

inputFilePath = f"inputs/day{now.day}"

try:
    with open(inputFilePath, "x") as f:
        print("Making request for input:")
        r = requests.get(f"https://adventofcode.com/{now.year}/day/{now.day}/input", cookies={"session": session_cookie}, headers={"User-Agent": useragent})
        print("Saving input to file:")
        f.write(r.text)
except:
    print("Input file already exists for today, skipping input load")

solutionFilePath = f"solutions/day{now.day}.py"

boilerplateSolution = f"""with open('inputs/day{now.day}') as f:
    input = f.read()

"""

try:
    with open(solutionFilePath, "x") as f:
        print("Creating boilerplate solution:")
        f.write(boilerplateSolution)
except:
    print("Solution file already exists for today, skipping solution file create")

now = datetime.datetime.now()
print(f"Loading complete\nStarting today's challenge at {now.time().strftime('%H:%M:%S')}\nGood luck!")

