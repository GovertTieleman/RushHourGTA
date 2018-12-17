# Depth First
import sys
from classes.board import Board
sys.path.insert(0, '../')
sys.setrecursionlimit(5000)

class DF(object):
    """
    Main class for running and solving the game
    """

    def __init__(self, filename):
        # self.game = game

        # load board
        self.board = Board.load_game(self, filename)
        self.archive = {}

    # Recursive function:
    def find_solution(self, move_count):

        # Check and update archive
        board = self.board
        current_board = board.board_string()
        self.archive[current_board] = move_count

        # Update moves and count
        move_list = board.find_moves()

        # Optional view of progress
        # print(f"{current_board}:\nmove count:{move_count}\narchive size:{len(self.archive)}\n")

        # Check limit
        move_count += 1
        if move_count == 5000:
            return 1

        # Iterate over valid moves
        for move in move_list:
            board.move_car(move)

            # Check archive for map and length of route
            new_board = board.board_string()
            if new_board not in self.archive or self.archive[new_board] > move_count:

                # Check win condition
                if board.won():
                    print(f"Solution length: {move_count}")

                # Make next move
                else:
                    self.find_solution(move_count)

            # Revert move
            board.revert_move(move)
        return 0