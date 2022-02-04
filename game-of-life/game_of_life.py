import math
import pdb

from enum import Enum
from pprint import pprint
from typing import List


class CellStates(Enum):
    '''Not certain I see a tremendous amount of bonus value in having this be 
    an Enum instead of a dictionary, but wanted to experiment.
    '''

    DEAD = 0
    ALIVE = 1
    DEAD_TO_ALIVE = 2
    ALIVE_TO_DEAD = 3


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
        self.neighbor_lookup = self.make_neighbor_mapping()


    def is_valid_board(self) -> bool:
        '''TODO: Make sure that:
            - each row in the board only has zeros or ones on it
            - each row has the same number of columns
        '''
        pass


    def is_valid_coordinate(self, row_idx:int, col_idx:int) -> bool:
        if (row_idx < 0) or (col_idx < 0):
            return False
        if (row_idx >= self.n_rows) or (col_idx >= self.n_cols):
            return False
        return True


    def _calculate_neighbors(self, row_idx:int, col_idx:int) -> List[tuple]:
        '''Given an input row and column index, returns a list of tuples with 
        the coordinates of board cells that are neighbors to this input pair.
        '''
        valid_coords = []
        for row_shift in [-1, 0, 1]:
            for col_shift in [-1, 0, 1]:
                if row_shift == 0 and col_shift == 0:
                    continue
                new_row = row_idx + row_shift
                new_col = col_idx + col_shift
                if self.is_valid_coordinate(new_row, new_col):
                    valid_coords.append((new_row, new_col))
        return valid_coords


    def make_neighbor_mapping(self) -> dict:
        '''calculates neighbors for every coordinate on the board and stores 
        them in a dictionary so we don't have to repeatedly do this on the fly.
        '''
        coord_to_neighbors = {}
        for row_idx in range(self.n_rows):
            for col_idx in range(self.n_cols):
                coord_key = (row_idx, col_idx)
                neighbor_vals = self._calculate_neighbors(row_idx, col_idx)
                coord_to_neighbors[coord_key] = neighbor_vals
        return coord_to_neighbors


    def get_neighbors(self, row_idx, col_idx) -> List[tuple]:
        coord_key = (row_idx, col_idx)
        return self.neighbor_lookup[coord_key]



        



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


    for row_idx in range(conway.n_rows):
        for col_idx in range(conway.n_cols):
            neighbors = conway.get_neighbors(row_idx, col_idx)
            print(f"({row_idx}, {col_idx}):{len(neighbors)} neighbors")
            pprint(neighbors)
            print("---------" *5)
















