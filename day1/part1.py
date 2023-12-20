def find_first_last_digit(line: str) -> str:
    for character in line:
        if character.isdigit():
            first = character
            break
    for character in line[::-1]:
        if character.isdigit():
            return first + character


with open('input.txt', 'r') as f:
    lines = list(map(str.rstrip, f.readlines()))
    print(sum([int(find_first_last_digit(line)) for line in lines]))
