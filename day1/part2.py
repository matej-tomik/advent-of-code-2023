with open('input.txt', 'r') as f:
    numbers = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    lines = list(map(str.rstrip, f.readlines()))
    num_of_line = 0
    counter = 0
    for line in lines:
        counter += 1
        for character in line:
            if character.isdigit():
                first = {character: line.index(character)}
                break
        for number in numbers:
            if line.find(number) != -1:
                first.update({number: line.index(number)})

        for character in line[::-1]:
            if character.isdigit():
                last = {character: line[::-1].index(character)}
                break
        for number in numbers:
            if line.find(number) != -1:
                last.update({number: line[::-1].index(number[::-1])})


        tmp = min(first, key=first.get)
        if tmp in numbers:
            left_number = numbers.index(tmp) + 1
        else:
            left_number = tmp
        tmp = min(last, key=last.get)
        if tmp in numbers:
            right_number = numbers.index(tmp) + 1
        else:
            right_number = tmp

        print(str(left_number) + str(right_number))
        num_of_line += int(str(left_number) + str(right_number))
        first.clear()
        last.clear()
    print(num_of_line)
    print(counter)


