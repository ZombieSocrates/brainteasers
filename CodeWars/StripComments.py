import re

'''
https://www.codewars.com/kata/51c8e37cee245da6b40000bd/
'''

def solution(string, markers):
    for m in markers:
        rgx = fr".?\{m}[^\n]*"
        string = re.subn(rgx, "", string)[0]
    return string.rstrip(" ")




if __name__ == "__main__":
    
    print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
    print(solution("a #b\nc\nd $e f g", ["#", "$"]))
    print(solution("#", ["#"]))