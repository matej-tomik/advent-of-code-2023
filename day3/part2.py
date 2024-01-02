

def gere_ratio(position, line_set):
    tmp = (line_set[0][position - 1:position + 2] + '.' + line_set[1][position - 1] + '.' + line_set[1][position + 1]
           + '.' + line_set[2][position - 1:position + 2])
    first_num_pos = -1
    second_num_pos = -1
    num_count = 0
    pos_count = 0
    was_dot = True
    for char in tmp:
        if char.isnumeric() and was_dot:
            if first_num_pos != -1:
                second_num_pos = pos_count
            if first_num_pos == -1:
                first_num_pos = pos_count
            num_count += 1
            was_dot = False
        elif not char.isnumeric():
            was_dot = True
        pos_count += 1
    if num_count == 2:
        return get_num(first_num_pos, position, line_set)*get_num(second_num_pos, position, line_set)
    else:
        return 0


def get_num(pos, position, line_set):
    line_get_num = ''
    match pos:
        case p if 0 <= p < 3:
            line_get_num = line_set[0]
        case 4:
            line_get_num = line_set[1]
            pos -= 4
        case 6:
            line_get_num = line_set[1]
            pos -= 4
        case p if 8 <= p < 11:
            line_get_num = line_set[2]
            pos -= 8
    num = line_get_num[position - 1 + pos]
    left_was_num = True
    right_was_num = True
    pos_count = 1
    while left_was_num or right_was_num:
        if left_was_num:
            if line[position - 1 + pos - pos_count].isnumeric():
                num = line[position - 1 + pos - pos_count] + num
            else:
                left_was_num = False
        if right_was_num:
            if line[position - 1 + pos + pos_count].isnumeric():
                num += line[position - 1 + pos + pos_count]
            else:
                right_was_num = False
        pos_count += 1
    return int(num)


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
        if character == '*':
            total_count += gere_ratio(position_count, data_set[line_count - 1: line_count + 2])
        position_count += 1
    line_count += 1
    position_count = 0
print(total_count)
