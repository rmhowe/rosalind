import sys
from read_file import read_file

def get_base_counts(sequence):
    base_counts = {}
    for base in sequence:
        base_counts[base] = base_counts.get(base, 0) + 1
            
    return base_counts
    
def main():
    print(read_file(get_base_counts))

if __name__ == '__main__':
    main()