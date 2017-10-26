import sys

memo = {}
def get_fibonacci(n, k):
    args = (n, k)
    if args in memo:
        return memo[args]

    if n == 1 or n == 2:
        result = 1
    else:
        result = get_fibonacci(n - 1, k) + get_fibonacci(n - 2, k) * k
    
    memo[args] = result
    return result
    
def main():
    if len(sys.argv) > 2:
        n = int(sys.argv[1])
        k = int(sys.argv[2])
        print(get_fibonacci(n, k))
    else:
        print('Please provide 2 arguments')

if __name__ == '__main__':
    main()