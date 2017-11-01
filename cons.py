from parse_fasta import parse_fasta

def get_profile_matrix(sequences):
    for i in range(1, len(sequences)):
        if len(sequences[i-1]) != len(sequences[i]):
            raise ValueError('Sequences must all be of the same length')

    matrix = {
        'A': [0] * len(sequences[0]),
        'C': [0] * len(sequences[0]),
        'G': [0] * len(sequences[0]),
        'T': [0] * len(sequences[0])
    }
    for sequence in sequences:
        for i, base in enumerate(sequence):
            matrix[base][i] += 1

    return matrix

def get_consensus_sequence(profile_matrix):
    sequence = ''
    for i in range(0, len(profile_matrix['A'])):
        max_occurences = 0
        consensus_base = ''
        for base, occurences in profile_matrix.items():
            if occurences[i] > max_occurences:
                max_occurences = occurences[i]
                consensus_base = base
        sequence += consensus_base

    return sequence

def main():
    with open('cons.txt', 'r') as input_file:
        sequences = parse_fasta(input_file)
        profile_matrix = get_profile_matrix(list(sequences.values()))
        consensus_sequence = get_consensus_sequence(profile_matrix)

        print(consensus_sequence)
        for base, occurences in profile_matrix.items():
            formatted_occurences = ' '.join(map(str, occurences))
            print('%s: %s' % (base, formatted_occurences))

if __name__ == '__main__':
    main()
