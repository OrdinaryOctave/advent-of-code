import datetime
import requests

cookie_file = "sessionCookie.txt"

now = datetime.datetime.now()

with open(cookie_file) as f:
    session_cookie = f.read();

r = requests.get(f"https://adventofcode.com/{now.year}/day/{now.day}/input", cookies={"session": session_cookie})

inputFilePath = f"inputs/day{now.day}"

with open(inputFilePath, "w") as f:
    f.write(r.text)

solutionFilePath = f"solutions/day{now.day}.py"

boilerplateSolution = f"""with open('inputs/day{now.day}') as f:
    input = f.read()

"""

try:
    with open(solutionFilePath, "x") as f:
        f.write(boilerplateSolution)
except:
    print("Solution file already exists for today")

print(f"Starting today's challenge at {now.time().strftime('%H:%M:%S')}, good luck!")

