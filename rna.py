import sys
from read_file import read_file

def get_mRNA(dna_sequence):
    return dna_sequence.replace('T', 'U')
    
def main():
    print(read_file(get_mRNA))

if __name__ == '__main__':
    main()