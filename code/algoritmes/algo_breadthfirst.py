# Breadth First
import cProfile
import sys
import copy
import cProfile
from classes.board import Board
from classes.car import Car

sys.path.insert(0, '../')


class BF(object):
    """
    Main file for running and solving the game
    """

    def __init__(self, filename):
        """
        Load the board and cars
        """
        # load board
        self.board = Board.load_game(self, filename)

        # initialize move_counter
        self.move_counter = 0

    def solve(self):
        # keep list of visited boards
        visited = set()

        # set max_depth
        max_depth = 100

        # create queue of boards and append the starting board
        queue = list()
        queue.append(self.board)

        # iterate over boards in queue
        while len(queue) != 0:
            # get current board
            board = queue.pop(0)

            # get depth
            depth = len(board.move_sequence)

            # show user which board is being considered
            print(f"currently working on this board: \n{board}\n"
                  f"depth: {depth}\n"
                  f"size of queue: {len(queue)}\n"
                  f"size of archive: {len(visited)}\n")

            if depth >= max_depth:
                print(f"max_depth exceeded\n")
                break

            if board.board_string() in visited:
                print(f"board visited\n")
                continue
            else:
                visited.add(board.board_string())

            if board.won():
                break
            else:
                # get moves for board
                moves_list = board.find_moves()

                # iterate over moves in list
                for move in moves_list:
                    # execute move
                    board.move_car(move)

                    # extend queue
                    queue.append(copy.deepcopy(board))

                    # revert move
                    board.revert_move(move)


if __name__ == "__main__":
    rushhour = BF("../../data/Game3.txt")
    cProfile.run('rushhour.solve()')


