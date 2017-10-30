import sys

def get_permutations(values):
    permutations = []
    
    if len(values) == 1:
        return [values]
    for value in values:
        values_subset = list(values)
        values_subset.remove(value)
        for sub_permutations in get_permutations(values_subset):
            permutations.append([value] + sub_permutations)
    
    return permutations

def main():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        values = list(map(str, list(range(1, n + 1))))
        permutations = get_permutations(values)
        print(len(permutations))
        for p in permutations:
            print(' '.join(p))
    else:
        print('Please provide a number <= 7')

if __name__ == '__main__':
    main()
