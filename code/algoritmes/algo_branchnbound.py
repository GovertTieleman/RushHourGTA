# Branch n Bound
import sys
from classes.board import Board
sys.path.insert(0, '../')

class BnB(object):
    """
    Branch n Bound class for running and solving the game
    """

    def __init__(self, filename):

        # Load board
        self.board = Board.load_game(self, filename)

        # Attributes
        self.archive = {}
        self.upper_bound = 100

    def solve(self):
        print("\nRunning Branch 'n Bound...\n")
        self.find_solution(0)
        print(f"Algorithm finished. \nArchive size: {len(self.archive)}")

    # Recursive function:
    def find_solution(self, move_count):

        # Update archive
        board = self.board
        current_board = board.board_string()
        self.archive[current_board] = move_count

        # Optional view of progress
        # print(f"{current_board}:\nmove count:{move_count}\narchive size:{len(self.archive)}\n")

        # Check bound
        move_count += 1
        if move_count == self.upper_bound:
            return 1

        # Iterate over valid moves
        move_list = board.find_moves()
        for move in move_list:
            board.move_car(move)

            # Check archive for map and length of route
            new_board = board.board_string()
            if new_board not in self.archive or self.archive[new_board] > move_count:

                # Check win condition
                if board.won():
                    print(f"Solution length: {move_count}\n")
                    self.upper_bound = move_count

                # Make next move
                else:
                    self.find_solution(move_count)

            # Revert move
            board.revert_move(move)
        return 0