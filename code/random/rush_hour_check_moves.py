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
        # show board
        print(f"{self.board}\n")

        moves_list = ['A -2', 'X -1', 'B -2', 'X 1', 'C -1', 'B 1', 'B -1', 'D -1', 'X -2', 'X 2', 'F -2', 'X -2',
                      'X 3', 'E -1', 'H 2', 'J -1', 'X -2', 'L -1', 'J -1', 'K -1', 'K -1', 'X -1', 'F 1', 'X 1',
                      'K 2', 'G 1', 'I -2', 'B 1', 'L -2', 'A 1', 'I 1', 'J 1', 'I 1', 'G -1', 'J -1',
                      'K -3', 'J 2', 'A -1', 'A 1', 'H -2', 'E 3', 'F 3']

        # solve game
        for move in moves_list:
            self.board.move_car(move)
            print(f"{self.board}\n")



if __name__ == "__main__":
    rushhour = RushHour("../../data/Game2.txt")
    rushhour.solve()


