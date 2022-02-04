import math
import pdb

from enum import Enum
from pprint import pprint
from typing import List


class CellStates(Enum):

    DEAD = 0
    ALIVE = 1
    WILL_DIE = 2
    WILL_LIVE = 3

class GameOfLife(object):
    '''
    Class for solving Conway's Game of life problem. Full description can be 
    found here: https://www.hackerrank.com/challenges/conway

    For the time being, I'm assuming the non-adversarial version of this game
    '''

    game_states = CellStates

    def __init__(self, board: List[list]):
        '''TODO: write docstring
        '''
        self.board = board
        self.n_rows = len(self.board)
        self.n_cols = len(self.board[0]) 
        self.cycles_run = 0


    def is_valid_board(self) -> bool:
        '''TODO: Make sure that:
            - each row in the board only has zeros or ones on it
            - each row has the same number of columns
        '''
        pass


    def is_valid_coordinate(self, row_val:int, col_val:int) -> bool:
        if (row_val < 0) or (col_val) < 0:
            return False
        if (row_val >= self.n_rows) or (col_val >= self.n_cols):
            return False
        return True


if __name__ == "__main__":


    TEST_BOARD = [
        [0, 1, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 1],
        [0, 1, 1, 0, 0, 1]
    ]

    conway = GameOfLife(board = TEST_BOARD)

    print("Here is the board!!!")
    pprint(conway.board)
    print(f"Board dimensions: ({conway.n_rows, conway.n_cols})")
    print("-------" * 5)

    print("Here are the finite states of each cell")
    for state in conway.game_states:
        print(f"\t{state.name}: {state.value}")


    for coord in [(0,0), (5,3), (-1, 4), (8,3)]: 
        row = coord[0]
        col = coord[1]
        is_valid = conway.is_valid_coordinate(row_val = row, col_val = col)
        print(f"Is {coord} valid? {is_valid}")
















