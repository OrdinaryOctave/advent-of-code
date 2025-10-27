# input loaded at 17:55:07
import re
# wow... day 3 and I already broke my no imports challenge... I did not want the pain of doing this without regex

with open('2024/inputs/day3') as f:
    inputData = f.read()

p  = re.compile(r"mul\((\d{,3}),(\d{,3})\)")
pairs = [(int(pair[0]), int(pair[1])) for pair in re.findall(p, inputData)]

print(sum(map(lambda nums: nums[0] * nums[1], pairs)))

count = 0
parts = inputData.split("do()")
for part in parts:
    cut = re.search(r"don't\(\)", part)
    if cut is not None:
        part = part[:cut.start()]
    pairs = [(int(pair[0]), int(pair[1])) for pair in re.findall(p, part)]
    count += sum(map(lambda nums: nums[0] * nums[1], pairs))

print(count)