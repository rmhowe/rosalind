import sys

def read_file(fn):
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        print('Please provide a file name')
        sys.exit(0)

    with open(file_name, 'r') as input_file:
        contents = input_file.read()
        return fn(contents)