def get_occurence_indices(s, t):
    indices = []
    index = s.find(t)
    while index is not -1:
        indices.append(index + 1)
        index = s.find(t, index + 1)

    return indices

def main():
    with open('subs.txt', 'r') as input_file:
        s = input_file.readline().strip()
        t = input_file.readline().strip()
        print(' '.join(map(str, get_occurence_indices(s, t))))

if __name__ == '__main__':
    main()
