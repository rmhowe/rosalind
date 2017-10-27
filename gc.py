def get_gc_contents(input_file):
    sequence_lengths = {}
    gc_counts = {}
    for line in input_file:
        line = line.rstrip()
        if line[0] == '>':
            label = line[1:]
        else:
            sequence_lengths[label] = sequence_lengths.get(label, 0) + len(line)
            gc_counts[label] = gc_counts.get(label, 0) + line.count('G') + line.count('C')
            
    gc_contents = {}
    for label in sequence_lengths:
        gc_contents[label] = gc_counts[label] / sequence_lengths[label] * 100
    
    return gc_contents

def get_highest_from_dict(d):
    highest_value = -1
    for key, value in d.items():
        if value > highest_value:
            highest_value = value
            highest_key = key
            
    return (highest_key, highest_value)
    
def main():
    with open('gc.txt', 'r') as input_file:
        gc_contents = get_gc_contents(input_file)
        label, gc_content = get_highest_from_dict(gc_contents)
        print(label)
        print(gc_content)

if __name__ == '__main__':
    main()