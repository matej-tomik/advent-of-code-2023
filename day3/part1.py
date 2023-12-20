def is_valid(position, count, line_set):
    if(line_set[0][position - count - 1:position + 1] + line_set[2][position - count - 1:position + 1] +
       line_set[1][position] + line_set[1][position - count - 1]).count('.') < (2 * count + 6):
        return int(line_set[1][position - count:position])
    else:
        return 0

f = open("data.txt", "r")
line = ''
data_set = []
for line in f:
    data_set.extend(['.' + line.rstrip('\n ') + '.'])
data_set.insert(0, ''.rjust(len(line)+1, '.'))
data_set.append(''.rjust(len(line)+1, '.'))

total_count = 0
position_count = 0
line_count = 1
consecutive_num_count = 0
for line in data_set[1:(len(data_set)-1)]:
    for character in line:
        if character.isnumeric():
            consecutive_num_count += 1
        elif consecutive_num_count > 0:
            total_count += is_valid(position_count, consecutive_num_count, data_set[line_count - 1: line_count + 2])
            consecutive_num_count = 0
        position_count += 1
    line_count += 1
    position_count = 0
print(total_count)
