import pdb

from collections import defaultdict
'''
Solution to

https://www.codewars.com/kata/5254ca2719453dcc0b00027d


LOL turns out I already solved this by just cheating and
importing itertools. RIP.
'''

def permutations(input_str):
    tracking_dict = defaultdict(list)
    for i, a in enumerate(input_str):
        tracking_dict[a] = [b for j,b in enumerate(input_str) if j!= i]
    letters_left = len(input_str) - 1
    while letters_left > 0:    
        curr_keys = [k for k in tracking_dict.keys()]
        for k in curr_keys:
            for i,v in enumerate(tracking_dict[k]):
                tracking_dict[k+v] = tracking_dict[k].copy()
                tracking_dict[k+v].remove(v)
            tracking_dict.pop(k)
        letters_left += -1
    return [k for k in tracking_dict.keys()]


if __name__ == "__main__":


    for testcase in ["a", "ab", "aabb", "abcd"]:
        print(f"permutations for {testcase}:")
        print(permutations(testcase))
    