import re
import math

def solvesteper(start):
    current = start
    count = 0
    while not current.endswith('Z'):
        direction = left_right[count % len(left_right)]
        current = myDict[current][0 if direction == 'L' else 1]
        count += 1
    return count



tmp = open("data.txt", "r").read().split('\n\n')
left_right = list(tmp[0])
navigation = tmp[1].split('\n')
start = []
left = []
right = []
for element in navigation:
    for idx, elem in enumerate(re.split('= |, ', element)):
        match idx:
            case 0:
                start.append(elem.strip(" |)|("))
            case 1:
                left.append(elem.strip(" |)|("))
            case 2:
                right.append(elem.strip(" |)|("))

values = zip(left, right)
myDict = {k: v for (k, v) in zip(start, values)}
total = 1
for x in start:
    if x.endswith('A'):  # type: ignore
        total = math.lcm(total, solvesteper(x))
print(total)
