import re
f = open("data.txt", "r")
tmp = re.sub('[a-zA-Z]|-', '', f.read())
tmp = tmp[2:].split(':')
seeds = sorted(list(map(int, tmp[0][:len(tmp[0])-3].split(' '))))
seed_to_soil = sorted([list(map(int, x)) for x in [x.split(' ') for x in tmp[1][1:len(tmp[1])-3].split('\n')]])
soil_to_fertilizer = sorted([list(map(int, x)) for x in [x.split(' ') for x in tmp[2][1:len(tmp[2])-3].split('\n')]])
fertilizer_to_water = sorted([list(map(int, x)) for x in [x.split(' ') for x in tmp[3][1:len(tmp[3])-3].split('\n')]])
water_to_light = sorted([list(map(int, x)) for x in [x.split(' ') for x in tmp[4][1:len(tmp[4])-3].split('\n')]])
light_to_temperature = sorted([list(map(int, x)) for x in [x.split(' ') for x in tmp[5][1:len(tmp[5])-3].split('\n')]])
tem_to_humidity = sorted([list(map(int, x)) for x in [x.split(' ') for x in tmp[6][1:len(tmp[6])-3].split('\n')]])
humidity_to_location = sorted([list(map(int, x)) for x in [x.split(' ') for x in tmp[7][1:len(tmp[7])-3].split('\n')]])