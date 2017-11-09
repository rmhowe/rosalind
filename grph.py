from parse_fasta import parse_fasta

def get_overlap_graph(sequences, k):
    overlaps = []

    for label_a, sequence_a in sequences.items():
        for label_b, sequence_b in sequences.items():
            if label_a != label_b and sequence_a[-k:] == sequence_b[:k]:
                overlaps.append([label_a, label_b])

    return overlaps

def main():
    with open('grph.txt', 'r') as input_file:
        sequences = parse_fasta(input_file)
        overlap_graph = get_overlap_graph(sequences, k=3)
        for overlap in overlap_graph:
            print(' '.join(overlap))

if __name__ == '__main__':
    main()
