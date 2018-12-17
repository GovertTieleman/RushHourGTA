# Breadth First
import sys
import copy
from classes.board import Board

sys.path.insert(0, '../')


class BF(object):
    """
    Breadth First class for running and solving the game
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

            # stop at max depth
            if depth >= max_depth:
                print(f"max_depth exceeded\n")
                break

            # if visited, skip, otherwise add to archive
            if board.board_string() in visited:
                continue
            else:
                visited.add(board.board_string())

            # break if won
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
