import re

f = open("data.txt", "r")
balls = {
    'red': 12,
    'green': 13,
    'blue': 14
}
total_count = 0
for line in f:
    line_list = re.split('; |, |: ', line.rstrip('\n '))
    count = 0
    for ball in line_list[1:]:
        value, key = ball.split(' ')
        if int(balls[key] < int(value)):
            break
        count += 1
    if count == (len(line_list) - 1):
        number = re.sub('\\D', '', str(line_list[0]))
        total_count += int(number)
print(total_count)
