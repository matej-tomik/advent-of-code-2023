import re

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

current = 'AAA'
count = 0

while current != 'ZZZ':
    direction = left_right[count % len(left_right)]
    current = myDict[current][0 if direction == 'L' else 1]
    count += 1
print(count)
