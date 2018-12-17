# Random
import cProfile
import sys
import random
import copy
import cProfile
from classes.board import Board
from classes.car import Car

sys.path.insert(0, '../')


RECURSION_LIMIT = 10000


class R(object):
    """
    Main file for running and solving the game
    """

    def __init__(self, filename):
        """
        Load the board and cars
        """
        # save filename and load board
        self.filename = filename
        self.board = Board.load_game(self, filename)

        # initialize move_counter
        self.move_counter = 0

        # track recursion depth
        self.recursion_depth = 0
        self.recursion_limit = RECURSION_LIMIT
        self.best_solution = []
        self.best_number_of_moves = 10000

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
            self.board = Board.load_game(self, self.filename)

        print(f"The best solution was: {self.best_solution}\n"
              f"Number of moves: {len(self.best_solution)}")


if __name__ == "__main__":
    rushhour = R("../../data/Game7.txt")
    cProfile.run('rushhour.solve()')


