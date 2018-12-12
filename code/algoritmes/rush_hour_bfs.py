import cProfile
import sys
sys.path.insert(0, '../')

from classes.board import Board
from classes.car import Car
import copy
import cProfile


class RushHour(object):
    """
    Main file for running and solving the game
    """

    def __init__(self, filename):
        """
        Load the board and cars
        """
        # load board
        self.board = self.load_game(filename)

        # initialize move_counter
        self.move_counter = 0

    def load_game(self, filename):
        """
        Method for loading the board
        :param filename:
        :return:
        """
        # establish dictionary of coordinates and cars
        coordinates = {}
        cars = {}

        # open file
        with open(filename, "r") as f:
            # read lines and coordinates, starting with x and y at 1
            lines = f.readlines()
            size = len(lines[0].strip())
            x = 1
            y = 1
            # iterate over characters, creating the board and cars
            for line in lines:
                for char in line.strip():
                    coordinates[x, y] = char
                    if char.isalpha():
                        if char in cars:
                            cars[char].x.append(x)
                            cars[char].y.append(y)
                        else:
                            cars[char] = Car(char, x, y, '')
                    x += 1
                x = 1
                y += 1

        # set car orientation
        for car in cars:
            if cars[car].x[0] - cars[car].x[1] == 0:
                cars[car].orientation = 'VERTICAL'
            else:
                cars[car].orientation = 'HORIZONTAL'

        # create starting instance of board
        board = Board(size, coordinates, [])

        # add cars to board
        for car in cars:
            board.add_car(cars[car])

        # return board
        return board

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
    rushhour = RushHour("../../data/Game3.txt")
    cProfile.run('rushhour.solve()')


