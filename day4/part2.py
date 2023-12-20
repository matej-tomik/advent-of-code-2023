f = open("data.txt", "r")
f = f.readlines()

count = 0
points = 0
total_points = [1] * len(f)
tmp = []
for line in f:
    count += 1
    for char_w in list(filter(None, line[10:40].split(' '))):
            if char_w in list(filter(None, line[42:len(line)-1].split(' '))):
                if not (points == 0):
                    points += 1
                else:
                    points = 1
    tmp.append(points)
    if count+points > len(total_points):
        points = len(total_points) - count

    while points > 0:
        total_points[count+points-1] += total_points[count-1]
        points -= 1
print(sum(total_points))

