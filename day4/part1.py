f = open("data.txt", "r")
total_points = 0
points = 0

for line in f:
    points = 0
    for char_w in list(filter(None, line[10:40].split(' '))):
            if char_w in list(filter(None, line[42:len(line)-1].split(' '))):
                if not (points == 0):
                    points = points * 2
                else:
                    points = 1
    total_points += points
print(total_points)
