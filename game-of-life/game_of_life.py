import pdb

from collections import Counter, defaultdict
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
        self.generation_index = 0
        self.neighbor_lookup = self._make_neighbor_mapping()
        self.generation_stats = defaultdict(dict)


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


    def _make_neighbor_mapping(self) -> dict:
        '''calculates neighbors for every coordinate on the board and stores 
        them in a dictionary so we don't have to repeatedly do this on the fly.
        '''
        coord_to_neighbors = {}
        for row_idx in range(self.n_rows):
            for col_idx in range(self.n_cols):
                coord_key = (row_idx, col_idx)
                neighbor_coords = self._calculate_neighbors(row_idx, col_idx)
                coord_to_neighbors[coord_key] = neighbor_coords
        return coord_to_neighbors


    def get_neighbors(self, row_idx:int, col_idx:int) -> List[tuple]:
        '''Given an input row and column index, use the lookup attribute 
        we created to quickly fetch its neighbor 
        '''
        coord_key = (row_idx, col_idx)
        return self.neighbor_lookup[coord_key]


    def tally_neighbor_values(self, row_idx:int, col_idx:int) -> dict:
        value_tally = Counter()
        for neighbor_coord in self.get_neighbors(row_idx, col_idx):
            neighbor_row = neighbor_coord[0]
            neighbor_col = neighbor_coord[1]
            neighbor_val = self.board[neighbor_row][neighbor_col]
            value_tally.update([neighbor_val])
        return value_tally


    def is_cell_alive(self, row_idx:int, col_idx:int) -> bool:
        '''Returns a boolean flag indicating if the cell is alive in the
        current cycle. We need to know this to update its value properly.
        '''
        curr_val = self.board[row_idx][col_idx]
        if curr_val == self.game_states.ALIVE.value:
            return True
        if curr_val == self.game_states.ALIVE_TO_DEAD.value:
            return True 
        return False


    def get_new_value(self, is_live_cell:bool, value_tally:dict) -> int:
        '''Applies the conditions of the game as specified in the problem 
        description
        '''
        n_alive = value_tally[self.game_states.ALIVE.value]
        n_alive += value_tally[self.game_states.ALIVE_TO_DEAD.value]
        if is_live_cell: 
            if (n_alive == 2) or (n_alive == 3):
                return self.game_states.ALIVE.value
            return self.game_states.ALIVE_TO_DEAD.value 
        else:
            if n_alive == 3:
                return self.game_states.DEAD_TO_ALIVE.value
            return self.game_states.DEAD.value


    def update_this_cell(self, row_idx: int, col_idx:int, verbose = False) -> None:
        '''Does not return anything; modifies the cell at row_idx, col_idx to
        the state it will be for the next cycle.
        '''
        currently_alive = self.is_cell_alive(row_idx, col_idx)
        neighbor_tally = self.tally_neighbor_values(row_idx, col_idx)
        next_value = self.get_new_value(currently_alive, neighbor_tally)
        if verbose:
            curr_value = self.board[row_idx][col_idx]
            curr_state = self.game_states(curr_value).name
            print(f"This cell is {curr_state}")
            pprint(neighbor_tally)
            print(f"The next state: {self.game_states(next_value).name}")
            print("---------" *5, "\n")
        self.board[row_idx][col_idx] = next_value


    def calculate_cell_updates(self, verbose = False):
        for row_idx in range(self.n_rows):
            for col_idx in range(self.n_cols):
                self.update_this_cell(row_idx, col_idx, verbose = verbose)


    def execute_cell_updates(self, verbose = False) -> None:
        '''After we've marked each cell with an update value, we execute the 
        transitional states of ALIVE_TO_DEAD and DEAD_TO_ALIVE by switching 
        those board values to 0 and 1, respectively.

        As a sort of debug step, we also retain a record of how many state
        transitions there were in this "generation" and store that history at 
        the instance level.
        '''
        transition_counter = Counter()
        for row_idx in range(self.n_rows):
            for col_idx in range(self.n_cols):
                cell_value = self.board[row_idx][col_idx]
                cell_state = self.game_states(cell_value).name
                if cell_state == "ALIVE_TO_DEAD":
                    self.board[row_idx][col_idx] = self.game_states.DEAD.value
                if cell_state == "DEAD_TO_ALIVE":
                    self.board[row_idx][col_idx] = self.game_states.ALIVE.value
                transition_counter.update([cell_state])
        self.generation_stats[self.generation_index] = transition_counter
        if verbose:
            print(f"Effects in generation {self.generation_index + 1}")
            pprint(transition_counter)


    def run_update(self, verbose = False) -> None:
        self.calculate_cell_updates(verbose = verbose)
        self.execute_cell_updates(verbose = verbose)
        self.generation_index += 1


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
    print("-------" * 5, "\n")

    print("Here are the finite states of each cell")
    for state in conway.game_states:
        print(f"\t{state.name}: {state.value}")
    print("--------" * 5, "\n")

    
    pdb.set_trace()
    #conway.run_update(verbose = True)


    '''
    TODO: because we are keeping track of generations, we can stop
    updating the board when we see don't see transitions happening 
    for ... say five iterations.

    Manually inspecting this example board, there stops being progress 
    made after 6 "generations" or so.
    '''
















