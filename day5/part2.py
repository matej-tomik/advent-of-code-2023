import re

f = open("data.txt", "r")
tmp = re.sub('[a-zA-Z]|-', '', f.read())
tmp = tmp[2:].split(':')
seeds = (list(map(int, tmp[0][:len(tmp[0])-3].split(' '))))
converter = [
    sorted([list(map(int, x)) for x in [x.split(' ') for x in tmp[1][1:len(tmp[1]) - 3].split('\n')]],
           key=lambda x: x[1]),
    sorted([list(map(int, x)) for x in [x.split(' ') for x in tmp[2][1:len(tmp[2]) - 3].split('\n')]],
           key=lambda x: x[1]),
    sorted([list(map(int, x)) for x in [x.split(' ') for x in tmp[3][1:len(tmp[3]) - 3].split('\n')]],
           key=lambda x: x[1]),
    sorted([list(map(int, x)) for x in [x.split(' ') for x in tmp[4][1:len(tmp[4]) - 3].split('\n')]],
           key=lambda x: x[1]),
    sorted([list(map(int, x)) for x in [x.split(' ') for x in tmp[5][1:len(tmp[5]) - 3].split('\n')]],
           key=lambda x: x[1]),
    sorted([list(map(int, x)) for x in [x.split(' ') for x in tmp[6][1:len(tmp[6]) - 3].split('\n')]],
           key=lambda x: x[1]),
    sorted([list(map(int, x)) for x in [x.split(' ') for x in tmp[7][1:len(tmp[7])].split('\n')]],
           key=lambda x: x[1])]
# print(converter)
# print(seeds)
t = []
for i in range(1, len(seeds), 2):
    t.append([seeds[i - 1], seeds[i]])
seeds = t
counter = 0
for iteration in converter:
    for seed in seeds:
        for block in iteration:
            if seed[0] + seed[1] <= block[1]:
                break
            if seed[0] >= (block[1] + block[2]):
                continue
            if seed[0] < block[1]:
                seeds.append([seed[0], block[1] - seed[0]])
                if (block[1] + block[2]) >= (seed[0] + seed[1]):
                    seeds[counter][1] = seed[0] + seed[1] - block[1]
                    seeds[counter][0] = block[0]
                    break
                else:
                    seeds.append([block[1] + block[2], (seed[0] + seed[1]) - (block[1] + block[2])])
                    seeds[counter][1] = block[2]
                    seeds[counter][0] = block[0]
                    break
            if seed[0] > block[1]:
                if (block[1] + block[2]) >= (seed[0] + seed[1]):
                    seeds[counter][0] = seed[0] + block[0] - block[1]
                    break
                else:
                    seeds.append([block[1] + block[2], (seed[0] + seed[1]) - (block[1] + block[2])])
                    seeds[counter][1] = - seed[0] + block[2] + block[1]
                    seeds[counter][0] = seed[0] - block[1] + block[0] - 1
                    break

        counter += 1
    counter = 0
seeds.sort()
print(seeds)
print(seeds[0])

# 50855035 right 75281324??
