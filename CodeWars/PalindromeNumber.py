from collections import Counter
from itertools import combinations
from pprint import pprint



'''

IN PROGRESS SOLUTION TO:

https://www.codewars.com/kata/556f4a5baa4ea7afa1000046


Passes all of the fixed tests...

Seems to be breaking on long lists with very large numbers? Maybe
I am not getting



EXAMPLE FAILING TESTS

Testing for [25564, 14, 83842, 42024], 
Expecting: 8632105012368
3218605068123 should equal 8632105012368


Testing for [652, 2, 88, 35041, 75188, 0, 53028, 7369], 
Expecting: 8744211109011124478
3300658427248560033 should equal 8744211109011124478
'''


def multiply_list(in_list: list):
    '''return the product of all numbers provided in the input_list'''
    prod = 1
    for x in in_list:
        prod *= x
    return prod


def filter_zeros_and_ones(in_list: list):
    '''Including duplicate zeros and ones isn't helpful here. This ensures 
    any input doesn't have dupes of these numbers
    '''
    out_list = []
    for m, n in Counter(in_list).items():
        if m > 1:
            out_list.extend([m] * n)
        elif m == 1:
            out_list.extend([m] * min(2, n))
        else:
            out_list.append(0)
    return out_list


def numeric_palindrome(*args):
    filtered_args = filter_zeros_and_ones(args)
    biggest_pal = 0
    for k in range(2, len(filtered_args) + 1):
        for selections in combinations(filtered_args, k):
            select_product = multiply_list(list(selections))
            dgt_count = Counter([int(b) for b in str(select_product)])
            sorter = lambda x: (x[1], x[0])
            dgt_sort = sorted(dgt_count.items(), key = sorter, reverse = True)
            pal_digits = []
            for digit, count in dgt_sort:
                if count // 2 > 0:
                    n = (count // 2) * 2
                    for d in [digit] * n:
                        pal_digits.insert(int(len(pal_digits) / 2), str(d))
                    dgt_count[digit] -= n
                    if dgt_count[digit] == 0:
                        dgt_count.pop(digit)
            if len(dgt_count) > 0:
                max_key = max([k for k in dgt_count.keys()])
                pal_digits.insert(int(len(pal_digits) / 2), str(max_key))
            pal_str = ''.join(pal_digits).strip('0')
            pal_num = int(pal_str) if pal_str else 0
            biggest_pal = max(pal_num, biggest_pal)
    return biggest_pal
   





if __name__ == "__main__":

    test_cases = [
        ([15,125,8], 8),
        ([57, 62, 23], 82128),
        ([11, 6], 66),
        ([2824, 2399], 7764677)
    ]
    n_passes = 0
    
    for arguments, output in test_cases:
        if numeric_palindrome(*arguments) == output:
            print(f"Test with {arguments} succeeded :D")
            n_passes += 1
        else:
            print(f"BOO....TEST WITH {arguments} FAILED :P ")

    if n_passes == len(test_cases):
        print("All Tests Passed")
    else:
        print(f"{n_passes}/{len(test_cases)} tests passed")
    
