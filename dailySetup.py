import datetime
import requests

cookie_file = "sessionCookie.txt"

today = datetime.date.today()

with open(cookie_file) as f:
    session_cookie = f.read();

r = requests.get(f"https://adventofcode.com/{today.year}/day/{today.day}/input", cookies={"session": session_cookie})

inputFilePath = "inputs/day"+str(today.day)

with open(inputFilePath, "w") as f:
    f.write(r.text)

solutionFilePath = "solutions/day"+str(today.day)+".py"

boilerplateSolution = """with open('inputs/day"""+str(today.day)+"""') as f:
    input = f.read()

"""
try:
    with open(solutionFilePath, "x") as f:
        f.write(boilerplateSolution)
except:
    print("Solution file already exists for today")