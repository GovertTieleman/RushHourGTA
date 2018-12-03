from board import Board
from car import Car
import copy
import random


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
        # show starting board
        print(f"{self.board}\n")

        # create queue of boards
        boards = [copy.deepcopy(self.board)]

        # create exists boolean to check if board in queue
        exists = False

        # initiate moves_tried
        moves_tried = 0

        # iterate over boards in queue
        for board in boards:
            # get depth
            depth = len(board.move_sequence)

            # show user which board is being considered
            print(f"currently working on this board: \n{board}\n"
                  f"depth: {depth}\n"
                  f"size of queue: {len(boards)}\n"
                  f"moves tried: {moves_tried}")

            # make copy of current board
            current_board = copy.deepcopy(board)

            # get moves for board
            moves_list = current_board.find_moves()

            # iterate over moves in list
            for move in moves_list:
                # increment moves_tried
                moves_tried += 1

                # execute move
                board.move_car(move)

                # check for win
                if board.won():
                    return 0

                # check if new board
                new_candidate = board.board_string
                for existing in boards:
                    # prune queue
                    if len(existing.move_sequence) < depth:
                        boards.remove(existing)

                    # if new board already exists in list
                    if new_candidate == existing.board_string:
                        # set exists to True and break off search
                        exists = True
                        break

                    # set exists to false if not found
                    exists = False

                # if new board, add to queue
                if not exists:
                    boards.append(copy.deepcopy(board))

                # reset board
                board = copy.deepcopy(current_board)


if __name__ == "__main__":
    rushhour = RushHour("../../data/TestGameSimple1.txt")
    rushhour.solve()


