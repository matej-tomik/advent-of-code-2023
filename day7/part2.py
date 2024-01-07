from typing import List


def count_char(input_string) -> str:
    unique_chars = set(input_string)
    max_occurrences = 0
    no_J = 0
    for char in unique_chars:
        if char == 'J':
            no_J = input_string.count(char)
        if max_occurrences < input_string.count(char):
            max_occurrences = input_string.count(char)

    if no_J != 0:
        if max_occurrences != no_J:
            if len(unique_chars) <= 4:
                max_occurrences += 1 + no_J
            else:
                max_occurrences += no_J
            if len(unique_chars) <= 3:
                max_occurrences += 1
        else:
            unique_chars.remove('J')
            max_occurrences = 0
            for char in unique_chars:
                if max_occurrences < input_string.count(char):
                    max_occurrences = input_string.count(char)
            match no_J + max_occurrences:
                case 5:
                    max_occurrences = 7
                case 4:
                    max_occurrences = 6
                case 3:
                    max_occurrences = 4
                case 2:
                    max_occurrences = 2
    else:
        if len(unique_chars) <= 3:
            max_occurrences += 1
        if len(unique_chars) <= 2:
            max_occurrences += 1

    return str(max_occurrences)


def custom_sort(string_list: List[List[str]]):
    custom_order = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 0,
                    'Q': 12, 'K': 13, 'A': 14}

    def custom_key(char: str) -> int:
        return int(custom_order.get(char))

    return sorted(string_list, key=lambda s: [custom_key(char) for char in s[0]])


f = open("data.txt", "r")
tmp = f.read()
cards = [x for x in [x.split(' ') for x in tmp.split('\n')]]
for x in range(len(cards)):
    cards[x][0] = count_char(cards[x][0]) + cards[x][0]
cards = custom_sort(cards)
count = 0

for i in range(len(cards)):
    print(cards[i][0])
    count += int(cards[i][1]) * (i+1)

print(count)
