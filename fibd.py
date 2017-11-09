import sys

memo = {}
def get_fibonacci(n, m):
    args = (n, m)
    if args in memo:
        return memo[args]

    if n <= 2:
        result = 1
    elif n <= m:
        result = get_fibonacci(n - 1, m) + get_fibonacci(n - 2, m)
    else:
        result = get_fibonacci(n - 1, m) + get_fibonacci(n - 2, m) - get_fibonacci(n - m - 1, m)

    memo[args] = result
    return result

def main():
    if len(sys.argv) > 2:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        print(get_fibonacci(n, m))
    else:
        print('Please provide 2 arguments')

if __name__ == '__main__':
    main()
