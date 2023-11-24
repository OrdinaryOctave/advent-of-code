# Advent of Code

My solutions to previous advent of code events

Python scripts should be run from the root directory, not the folder the given solution is stored in

The `dailySetup.py` script will, by default, try to fetch the input for the current day (will only succeed if advent of code is currently happening)
- To fetch other day's inputs, specify arguments when running the script like this: `python dailySetup.py {day} {year}`
- Note that the script was written in GMT and only works with GMT timezone, line 7 should be changed to fix this for other timezones
- The script also requires another file in the root directory titled `sessionCookie.txt` which contains your AoC session cookie, to fetch your input
- Note that it requires the folders `<year>/<inputs>` and `<year>/<solutions>` to be present before running