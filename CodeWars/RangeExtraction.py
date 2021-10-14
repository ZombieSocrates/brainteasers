'''
https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
'''

def solution(args):
    ranges = []
    curr_range = []
    for i , v in enumerate(args):
        curr_range.append(v)
        try:
            next_val = args[i + 1]
        except IndexError as e:
            next_val = 0.5
        if next_val - v != 1:
            ranges.append(curr_range)
            curr_range = []
    return ",".join(ranges_to_strings(x) for x in ranges)


def ranges_to_strings(sublist):
    if len(sublist) == 1:
        return f"{sublist[0]}"
    elif len(sublist) == 2:
        return ",".join([str(v) for v in sublist])
    else:
        return f"{sublist[0]}-{sublist[-1]}"
         















if __name__ == "__main__":

    foo = [-3,-2,-1,2,10,15,16,18,19,20]
    bar = [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]
    print(solution(foo))

    print(solution(bar))


