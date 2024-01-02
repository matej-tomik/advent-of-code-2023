import re


f = open("data.txt", "r")
tmp = re.sub('[a-zA-Z]|-', '', f.read())
tmp = tmp[2:].split(':')
seeds = sorted(list(map(int, tmp[0][:len(tmp[0])-3].split(' '))))
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
counter = 0
block_counter = 0
for iteration in converter:
    for seed in seeds:
        for block in iteration[block_counter:]:
            if seed >= block[1]:
                if seed <= (block[1] + block[2]):
                    seeds[counter] = block[0] + seeds[counter] - block[1]
                    break
                else:
                    block_counter += 1
            else:
                break
        counter += 1
    block_counter = 0
    counter = 0
    seeds.sort()
print(seeds[0])
