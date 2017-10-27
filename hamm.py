def get_hamming_distance(sequence_a, sequence_b):
    if len(sequence_a) != len(sequence_b):
        raise ValueError('Sequences must be of equal length')
    
    hamming_distance = 0
    for index, base in enumerate(sequence_a):
        if base != sequence_b[index]:
            hamming_distance += 1
        
    return hamming_distance

def main():
    with open('hamm.txt', 'r') as input_file:
        sequence_a = input_file.readline().strip()
        sequence_b = input_file.readline().strip()
        print(get_hamming_distance(sequence_a, sequence_b))

if __name__ == '__main__':
    main()
