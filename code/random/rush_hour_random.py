from board import Board
from car import Car
import random
import copy
import cProfile

RECURSION_LIMIT = 100000


class RushHour(object):
    """
    Main file for running and solving the game
    """

    def __init__(self, filename):
        """
        Load the board and cars
        """
        # save filename and load board
        self.filename = filename
        self.board = self.load_game(filename)

        # initialize move_counter
        self.move_counter = 0

        # track recursion depth
        self.recursion_depth = 0
        self.recursion_limit = RECURSION_LIMIT
        self.best_solution = []
        self.best_number_of_moves = 100000

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
        # while recursion limit not exceeded
        while self.recursion_depth < self.recursion_limit:
            # increment recursion depth
            self.recursion_depth += 1
            print(self.recursion_depth)

            # make random moves until game is won
            while not self.board.won():
                # execute moves
                self.board.move_car(random.choice(self.board.find_moves()))

            # check if the found solution is the best so far
            if len(self.board.move_sequence) < self.best_number_of_moves:
                self.best_solution = copy.copy(self.board.move_sequence)
                self.best_number_of_moves = len(self.best_solution)

            # reset board
            self.board = self.load_game(self.filename)

        print(f"The best solution was: {self.best_solution}\n"
              f"Number of moves: {len(self.best_solution)}")


if __name__ == "__main__":
    rushhour = RushHour("../../data/Game7.txt")
    cProfile.run('rushhour.solve()')


