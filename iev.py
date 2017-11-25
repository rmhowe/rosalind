import sys
from read_file import read_file

def get_num_expected_dominant(number_of_couples):
    dom_dom, dom_het, dom_rec, het_het, het_rec, rec_rec = map(int, number_of_couples.strip().split(' '))

    e_dom_dom = dom_dom * 1 * 2
    e_dom_het = dom_het * 1 * 2
    e_dom_rec = dom_rec * 1 * 2
    e_het_het = het_het * 0.75 * 2
    e_het_rec = het_rec * 0.5 * 2
    e_rec_rec = 0

    return e_dom_dom + e_dom_het + e_dom_rec + e_het_het + e_het_rec + e_rec_rec

def main():
    num_expected_dominant = read_file(get_num_expected_dominant)
    print(num_expected_dominant)

if __name__ == '__main__':
    main()
