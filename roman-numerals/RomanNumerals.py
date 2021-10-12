import re
import ipdb


class RomanNumerals:

    def __init__(self):
        self.roman_decode = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        self.arabic_decode = {v:k for k, v in self.roman_decode.items()}
        self.subtract_handler = self.subtraction_regexes()

    
    def subtraction_regexes(self):
        '''Compiles regex patterns to look for that represent valid subtraction
        expressions in the roman numeral systems. Returns a dict that keys each
        pattern to its compiled regular expression
        '''
        valid_subtracts = ["IV","IX","XL","XC","CD","CM"]
        subtract_handler = {}
        for char_pair in valid_subtracts:
            subtract_handler[char_pair] = re.compile(char_pair)
        return subtract_handler
    

    def roman_subtract(self, char_pair):
        larger = char_pair[1]
        smaller = char_pair[0]
        return self.roman_decode[larger] - self.roman_decode[smaller]

    def to_roman(val):
        return ''

    def from_roman(self, roman_num):
        total = 0
        for pair in self.subtract_handler.keys():
            rgx = self.subtract_handler[pair]
            roman_num, n_matches = re.subn(rgx,"",roman_num)
            total += self.roman_subtract(pair) * n_matches
        for char in roman_num:
            total += self.roman_decode[char]
        return total





if __name__ == "__main__":

    foo = RomanNumerals()
    TESTS = ["CMX", "XXI", "MMVII", "DCLXVI", "MCMLXXXIX"]
    VALUES = [910, 21, 2007, 666, 1989]
    for i, case in enumerate(TESTS):
        print(f"Test {i+1}")
        val = foo.from_roman(case)
        if val == VALUES[i]:
            print("test passed! :D")
        else:
            print(f"Expected {VALUES[i]} from {case}, but got {val}...")