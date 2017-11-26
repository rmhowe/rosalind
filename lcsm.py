from parse_fasta import parse_fasta

def get_common_substrings(sequenceA, sequenceB):
    common_substrings = set()
    sequenceA_substrings = set()
    sequence_length = len(sequenceA)
    for i in range(sequence_length):
        for j in range(i, sequence_length):
            sequenceA_substrings.add(sequenceA[i:j+1])

    for substring in sequenceA_substrings:
        if sequenceB.find(substring) != -1:
            common_substrings.add(substring)

    return list(common_substrings)

def get_longest_common_substring(sequences, common_substrings):
    common_substrings.sort(key=len, reverse=True)
    for substring in common_substrings:
        common = True
        for sequence in sequences.values():
            if sequence.find(substring) == -1:
                common = False
                break
        if common:
            return substring

    return ''


def main():
    with open('lcsm.txt', 'r') as input_file:
        sequences = parse_fasta(input_file)
        sequence_keys = list(sequences.keys())
        if len(sequence_keys) == 0:
            print('Please provide some sequences in FASTA format')
        elif len(sequence_keys) == 1:
            print(sequences[sequence_keys[0]])
        else:
            sequenceA = sequences[sequence_keys[0]]
            sequenceB = sequences[sequence_keys[1]]
            common_substrings = get_common_substrings(sequenceA, sequenceB)
            longest_common_substring = get_longest_common_substring(sequences, common_substrings)
            print(longest_common_substring)

if __name__ == '__main__':
    main()
