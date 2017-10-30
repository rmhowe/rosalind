import sys

def get_dominant_probability(k, m, n):
    total_organisms = k + m + n
    
    dominant_dominant = k / total_organisms * (k - 1) / (total_organisms - 1)
    hetero_hetero = m / total_organisms * (m - 1) / (total_organisms - 1) * 0.75
    recessive_recessive = 0
    dominant_hetero = k / total_organisms * m / (total_organisms - 1) * 2
    dominant_recessive = k / total_organisms * n / (total_organisms - 1) * 2
    hetero_recessive = m / total_organisms * n / (total_organisms - 1)
    
    return dominant_dominant + hetero_hetero + recessive_recessive + dominant_hetero + dominant_recessive + hetero_recessive

def main():
    if len(sys.argv) > 3:
        k = int(sys.argv[1])
        m = int(sys.argv[2])
        n = int(sys.argv[3])
        print(get_dominant_probability(k, m, n))
    else:
        print('Please provide 3 arguments')

if __name__ == '__main__':
    main()
