def find_digit(line: str, directio: int) -> str:
    for character in line[::directio]:
        if character.isdigit():
            return character


with open('input.txt', 'r') as f:
    lines = list(map(str.rstrip, f.readlines()))
    print(sum([int(find_digit(line, 1) + find_digit(line, -1)) for line in lines]))
