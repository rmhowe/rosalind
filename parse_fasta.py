def parse_fasta(input_file):
    sequences = {}
    label = ''
    for line in input_file:
        line = line.strip()
        if line[0] is '>':
            label = line[1:]
        else:
            sequences[label] = sequences.get(label, '') + line

    return sequences
