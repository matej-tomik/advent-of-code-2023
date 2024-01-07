def find_digit(ln: str, directio: int, numbers, my_dist):
    if numbers:
        for character in ln[::directio]:
            if character.isdigit():
                my_dist.update({character: ln[::directio].index(character)})
        for num in number:
            if ln.find(num) != -1:
                my_dist.update({num: ln[::directio].index(num[::directio])})


def get_num(my_dist):
    tmp = min(my_dist, key=my_dist.get)
    if tmp in number:
        return number.index(tmp) + 1
    else:
        return tmp


number = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
with open('input.txt', 'r') as f:
    lines = list(map(str.rstrip, f.readlines()))
    total = 0
    for line in lines:
        first: dict = {}
        last: dict = {}
        find_digit(line, 1, True, first)
        find_digit(line, 1, False, first)
        find_digit(line, -1, True, last)
        find_digit(line, -1, False, last)
        total += int(str(get_num(first)) + str(get_num(last)))
    print(total)
