import re
import copy

def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * int(x)
    return result


f = open("data.txt", "r")
balls = {
    'red': 0,
    'green': 0,
    'blue': 0
}
total_count = 0
for line in f:
    line_list = re.split('; |, |: ', line.rstrip('\n '))
    max_no_balls = copy.deepcopy(balls)
    for ball in line_list[1:]:
        value, key = ball.split(' ')
        if int(max_no_balls[key]) < int(value):
            max_no_balls[key] = value
    total_count += multiplyList(max_no_balls.values())
print(total_count)
