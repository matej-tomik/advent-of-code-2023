def make_sequence(sequence):
    new_sequence = []
    for x in range(len(sequence)-1):
        new_sequence.append(sequence[x+1] - sequence[x])
    return new_sequence

def make_sequence_of_sequence(sequence):
    list_of_sequences = [sequence]
    while True:
        if len(set(sequence)) == 1:
            sequence = make_sequence(sequence)
            list_of_sequences.append(sequence)
            break
        sequence = make_sequence(sequence)
        list_of_sequences.append(sequence)
    return list_of_sequences

def next_no_sequence(list_of_sequences):
    total = 0
    for sequences in list_of_sequences[:len(list_of_sequences)-1]:
        total += sequences[len(sequences)-1]
    return total

lines = [list(map(int, x)) for x in [x.split(' ') for x in open("data.txt", "r").read().split('\n')]]
final_num = 0
for line in lines:
    final_num += next_no_sequence(make_sequence_of_sequence(line))
print(final_num)
