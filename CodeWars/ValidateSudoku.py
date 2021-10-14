import math

'''
https://www.codewars.com/kata/540afbe2dc9f615d5e000425
'''



class Sudoku(object):

    def __init__(self, data):
        self.data = data
        self.dimension = len(data)
        self.group_target = set([v for v in range(1, self.dimension + 1)])


    def is_valid(self):
        if not self.validate_dimension():
            return False
        if not self.validate_rows():
            return False
        if not self.validate_columns():
            return False
        if not self.validate_squares():
            return False
        return True


    def validate_dimension(self):
        '''Dimension must be N > 0, and sqrt(N) must be an integer'''
        sqrt_is_int = math.sqrt(self.dimension).is_integer()
        nonzero_dim = self.dimension > 0
        return sqrt_is_int & nonzero_dim


    def validate_rows(self):
        '''Each row needs to be of length N and can only contain the 
        integers 1 through N.
        
        FUN FACT: Using isinstance(x, int) will return true if x is 
        boolean :/
        '''
        for row in self.data:
            if len(row) != self.dimension:
                return False
            row_set = set([x for x in row if type(x) == int])
            row_overlap = self.group_target.intersection(row_set)
            if len(row_overlap) != self.dimension :
                return False
        return True

    
    def validate_columns(self):
        '''Each column needs to contain the integers 1 through N. Note we
        already checked appropriate data type and appropriate dimension in
        the validate_rows function.'''
        for c in range(self.dimension):
            col_set = set([row[c] for row in self.data])
            col_overlap = self.group_target.intersection(col_set)
            if len(col_overlap) != self.dimension:
                return False
        return True


    def validate_squares(self):
        '''Every sqrt(N) by sqrt(N) square has to contain the integers 
        1 through N.'''
        for square in self.get_little_squares():
            sq_set = set(square)
            sq_overlap = self.group_target.intersection(sq_set)
            if len(sq_overlap) != self.dimension:
                return False
        return True


    def get_little_squares(self):
        little_squares = []
        square_dim = int(math.sqrt(self.dimension))
        curr_square = []
        for n in range(square_dim):
            base_col = square_dim * n 
            for r in range(self.dimension):
                curr_square.extend(self.data[r][base_col:base_col + square_dim])
                if len(curr_square) == self.dimension:
                    little_squares.append(curr_square)
                    curr_square = []
        return little_squares











        






if __name__ == "__main__":

    # Valid Sudoku
    goodSudoku1 = Sudoku([
        [7,8,4, 1,5,9, 3,2,6],
        [5,3,9, 6,7,2, 8,4,1],
        [6,1,2, 4,3,8, 7,5,9],

        [9,2,8, 7,1,5, 4,6,3],
        [3,5,7, 8,4,6, 1,9,2],
        [4,6,1, 9,2,3, 5,8,7],
      
        [8,7,6, 3,9,4, 2,1,5],
        [2,4,3, 5,6,1, 9,7,8],
        [1,9,5, 2,8,7, 6,3,4]
    ])

    goodSudoku2 = Sudoku([
        [1,4, 2,3],
        [3,2, 4,1],

        [4,1, 3,2],
        [2,3, 1,4]
    ])

    # Invalid Sudoku
    badSudoku1 = Sudoku([
        [0,2,3, 4,5,6, 7,8,9],
        [1,2,3, 4,5,6, 7,8,9],
        [1,2,3, 4,5,6, 7,8,9],
      
        [1,2,3, 4,5,6, 7,8,9],
        [1,2,3, 4,5,6, 7,8,9],
        [1,2,3, 4,5,6, 7,8,9],
      
        [1,2,3, 4,5,6, 7,8,9],
        [1,2,3, 4,5,6, 7,8,9],
        [1,2,3, 4,5,6, 7,8,9]
    ])

    badSudoku2 = Sudoku([
        [1,2,3,4,5],
        [1,2,3,4],
        [1,2,3,4],  
        [1]
    ])

    print(goodSudoku1.is_valid())
    print(goodSudoku2.is_valid())
    
    print(badSudoku1.is_valid())
    print(badSudoku2.is_valid())



