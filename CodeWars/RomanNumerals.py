import re


'''
Solution to the following:

https://www.codewars.com/kata/51b66044bce5799a7f000003
'''

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
        self.replace_handler = self.replacement_regexes()

    
    def subtraction_regexes(self):
        '''Compiles regex patterns to look for that represent valid subtraction
        expressions in the roman numeral systems. Returns a dict that keys each
        pattern to its compiled regular expression.

        We use this in self.from_roman() if we need to translate one of these 
        patterns into a subtraction instead of using self.roman_decode directly
        '''
        valid_subtracts = ["IV","IX","XL","XC","CD","CM"]
        subtract_handler = {}
        for char_pair in valid_subtracts:
            subtract_handler[char_pair] = re.compile(char_pair)
        return subtract_handler
    

    def roman_subtract(self, char_pair):
        '''returns the numerical value associated with one of the valid 
        subtractions determined by the two-character sequences above.'''
        larger = char_pair[1]
        smaller = char_pair[0]
        return self.roman_decode[larger] - self.roman_decode[smaller]


    def from_roman(self, roman_num):
        total = 0
        for pair in self.subtract_handler.keys():
            rgx = self.subtract_handler[pair]
            roman_num, n_matches = re.subn(rgx,"",roman_num)
            total += self.roman_subtract(pair) * n_matches
        for char in roman_num:
            total += self.roman_decode[char]
        return total


    def replacement_regexes(self):
        '''Compiles regex patterns to find four occurences of I, X, or C 
        preceded by a V, L, or D, respectively. 

        This sets us up to do string replacements in self.to_roman() after 
        we have decoded the arabic numeral using modular arithmetic.
        '''
        tetra_letters = [r"V?I{4}",r"L?X{4}", r"D?C{4}"]
        replace_handler = {}
        for pattern in tetra_letters:
            replace_handler[pattern] = re.compile(pattern)
        return replace_handler


    def roman_replace(self, match_str):
        '''Given a matched string with four I's, four X's, or four C's, returns 
        the appropriate replacement as follows:

            IIII -> IV
            VIIII -> IX
            XXXX -> XL
            LXXXX -> XC 
            CCCC -> CD
            DCCCC -> CM
        '''
        four_char = len(match_str) == 4
        if "I" in match_str:
            return "IV" if four_char else "IX"
        elif "X" in match_str:
            return "XL" if four_char else "XC"
        else:
            return "CD" if four_char else "CM"  


    def to_roman(self, val):
        out = ""
        for div in sorted(self.arabic_decode.keys(), reverse = True):
            quotient = val // div
            if quotient > 0:
                out = f"{out}{self.arabic_decode[div] * quotient}"
                val = val % div
        for exp in self.replace_handler.keys():
            match_exp = re.search(self.replace_handler[exp], out)
            if match_exp:
                found_tetra = match_exp.group()
                out = out.replace(found_tetra, self.roman_replace(found_tetra))
        return out





if __name__ == "__main__":

    foo = RomanNumerals()
    ROMAN_NUMS = ["CMX", "XXI", "MMVII", "DCLXVI", "MCMLXXXIX", "M", "MCMXC"]
    ARABIC_NUMS = [910, 21, 2007, 666, 1989, 1000, 1990]
    for i, roman in enumerate(ROMAN_NUMS):
        arabic = ARABIC_NUMS[i]
        print(f"Test {i+1}")
        print("\tRoman to Arabic")
        a_val = foo.from_roman(roman)
        if a_val == arabic:
            print("\t\tR to A test passed! :D")
        else:
            print(f"\t\tExpected {arabic} from {roman}, but got {a_val}...")
        print("\tArabic to Roman")
        r_val = foo.to_roman(arabic)
        if r_val == roman:
            print("\t\tA to R test passed! :D")
        else:
            print(f"\t\tExpected {roman} from {arabic}, but got {r_val}...")