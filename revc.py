import sys
from read_file import read_file

def get_reverse_complement(dna_sequence):
    mapping = str.maketrans('ATCG', 'TAGC')
    return dna_sequence.translate(mapping)[::-1]
    
def main():
    print(read_file(get_reverse_complement))

if __name__ == '__main__':
    main()