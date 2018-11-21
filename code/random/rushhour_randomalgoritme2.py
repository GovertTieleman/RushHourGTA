import sys
sys.path.insert(0, '../')

# from board import Board
from car import Car
import copy
import random
from classes.board import Board



class RushHour(object):
    """
    Main file for running and solving the game
    """

    def __init__(self, filename):
        """
        Load the board and cars
        """
        # load board
        self.load_game(filename)

        # initialize move_counter
        self.move_counter = 0

    def load_game(self, filename):
        """
        Method for loading the board
        :param filename:
        :return:
        """
        # establish dictionary of coordinates
        coordinates = {}

        # establish dictionary of cars
        self.cars = {}

        # establish move_history list and loop prevention dict
        self.move_history = []

        # open file
        with open(filename, "r") as f:
            # read lines and coordinates, starting with x and y at 1
            lines = f.readlines()
            size = len(lines[0])
            x = 1
            y = 1
            # iterate over characters, creating the board and cars
            for line in lines:
                for char in line.strip():
                    coordinates[x, y] = char
                    if char.isalpha():
                        if char in self.cars:
                            self.cars[char].x.append(x)
                            self.cars[char].y.append(y)
                        else:
                            self.cars[char] = Car(char, x, y, '')
                    x += 1
                x = 1
                y += 1

        # set car orientation
        for car in self.cars:
            if self.cars[car].x[0] - self.cars[car].x[1] == 0:
                self.cars[car].orientation = 'VERTICAL'
            else:
                self.cars[car].orientation = 'HORIZONTAL'

        # create board class
        self.board = Board(size, coordinates)

        # create archive
        self.archive = [copy.copy(self.board.board_string())]

        # create list of allowed moves
        self.allowed_moves = []

        self.recursion_count = 0

        # create car configurations
        self.car_configurations = {self.board: self.cars}


    def find_moves(self, board, cars):
        # initialize list of possible moves
        self.movest_list = []

        # iterate over all car objects
        for car_id in cars:
            # check if car is horizontal
            if cars[car_id].orientation == 'HORIZONTAL':
                # get leftmost and rightmost x of car
                x_left = cars[car_id].x[0]
                x_right = cars[car_id].x[len(cars[car_id].x) - 1]

                # get y of car
                y_car = cars[car_id].y[0]

                # set counter i to 1
                i = 1

                # iterate over fields on the left side of car
                while x_left - i > 0:
                    if board.coordinates[(x_left - i), y_car] != '-':
                        # break if no empty space
                        break
                    else:
                        # append move to movest_list
                        self.movest_list.append(f"{car_id} {-i}")
                        i += 1

                # reset counter
                i = 1

                # iterate over fields on the right side of car
                while x_right + i < board.size:
                    if board.coordinates[(x_right + i), y_car] != '-':
                        # break if no empty space
                        break
                    else:
                        # append move to movest_list
                        self.movest_list.append(f"{car_id} {i}")
                        i += 1

            # check if car is vertical
            if cars[car_id].orientation == 'VERTICAL':
                # get leftmost and rightmost x of car
                y_top = cars[car_id].y[0]
                y_bottom = cars[car_id].y[len(cars[car_id].y) - 1]

                # get y of car
                x_car = cars[car_id].x[0]

                # set counter i to 1
                i = 1

                # iterate over fields on the left side of car
                while y_top - i > 0:
                    if board.coordinates[x_car, (y_top - i)] != '-':
                        # break if no empty space
                        break
                    else:
                        # append move to movest_list
                        self.movest_list.append(f"{car_id} {-i}")
                        i += 1

                # reset counter
                i = 1

                # iterate over fields on the right side of car
                while y_bottom + i < board.size:
                    if board.coordinates[x_car, (y_bottom + i)] != '-':
                        # break if no empty space
                        i = 1
                        break
                    else:
                        # append move to movest_list
                        self.movest_list.append(f"{car_id} {i}")
                        i += 1

        print(f"Possible moves: {self.movest_list}")

        return self.movest_list

    def move_car(self, command):
        """
        Execute a valid move command.
        """
        # split command for use
        command = command.split(' ')

        # get car
        car = self.cars[command[0]]

        # get direction and distance
        move = command[1]
        if move[0] == '-':
            direction = -1
            distance = int(move[1:])
        else:
            direction = 1
            distance = int(move)

        # move car
        if car.orientation == 'HORIZONTAL':
            # replace the whole car on the board by empty squares and move car object
            for i in range(len(car.x)):
                self.board.coordinates[car.x[i], car.y[i]] = '-'
                car.x[i] += distance * direction
            # place the car in its new position on the board
            for x in car.x:
                self.board.coordinates[x, car.y[0]] = car.id
            # return true if move successful
            return True
        elif car.orientation == 'VERTICAL':
            # replace the whole car on the board by empty squares and move car object
            for i in range(len(car.y)):
                self.board.coordinates[car.x[i], car.y[i]] = '-'
                car.y[i] += distance * direction
            # place the car in its new position on the board
            for y in car.y:
                self.board.coordinates[car.x[0], y] = car.id
            # return true if move successful
            return True

    def won(self):
        # get distance to exit for red car
        distance = (self.board.size - self.cars["X"].x[1]) - 1

        # if red car can reach exit, game is won
        if self.cars["X"].move_valid(distance, 1, self.board):
            print(f"Congratulations, you won!\n"
                  f"move history: {self.move_history}")
            return True
        else:
            return False

    def revert_move(self, command):
        """
    Revert a move command.
    """
        # split command for use
        command = command.split(' ')

        # get car
        car = self.cars[command[0]]

        # get direction and distance
        move = command[1]
        if move[0] == '-':
            direction = 1
            distance = int(move[1:])
        else:
            direction = -1
            distance = int(move)

        # move up or down its axis
        if car.move_valid(distance, direction, self.board):
            if car.orientation == 'HORIZONTAL':
                # replace the whole car on the board by empty squares and move car object
                for i in range(len(car.x)):
                    self.board.coordinates[car.x[i], car.y[i]] = '-'
                    car.x[i] += distance * direction
                # place the car in its new position
                for x in car.x:
                    self.board.coordinates[x, car.y[0]] = car.id
                # return true if move successful
                return True
            elif car.orientation == 'VERTICAL':
                # replace the whole car on the board by empty squares and move car object
                for i in range(len(car.y)):
                    self.board.coordinates[car.x[i], car.y[i]] = '-'
                    car.y[i] += distance * direction
                # place the car in its new position
                for y in car.y:
                    self.board.coordinates[car.x[0], y] = car.id
                # return true if move successful ..
                return True
        else:
            # return false if move unsuccessful
            print(f"Move {command} is invalid!\n")
            return False





    def solve(self, rushhour):
        self.random_solve(rushhour, self.archive, self.recursion_count)

    def random_solve(self, rushhour, archive, recursion_count):

        print(f"Number of moves: {recursion_count}\n")

        print(f"Current board: \n{rushhour.board}\n")

        if recursion_count == 500:
            print("More than 500 moves!")
            return False
        else:
            # get list of possible moves
            move_list = rushhour.find_moves(rushhour.board, rushhour.cars)

            # create board for every possible move (in string form)
            for move in move_list:

                # make move
                rushhour.move_car(move)

                # delete already encountered boards
                for board in archive:
                    if board != rushhour.board.board_string():
                        self.allowed_moves.append(move)
                        # break

                # revert move
                rushhour.revert_move(move)

            # if there are no more possible moves to make
            if not self.allowed_moves:
                print("No solution!")
                return False

            # pick random move from move_list
            random_move = random.choice(self.allowed_moves)
            print("random move: "+ random_move)

            rushhour.move_car(random_move)
            self.move_history.append(random_move)

            # check if game is won
            if rushhour.won():
                # Stop, return solution!
                print(f"Game is won! (in {recursion_count} moves)")
                return True

            # makes copies of board and cars
            # current_board = copy.deepcopy(rushhour.board)
            # current_cars = copy.deepcopy(rushhour.car_configurations[rushhour.board])

            # save current board to archive
            archive.append(copy.copy(rushhour.board.board_string()))

        # keep track of number of moves
        recursion_count += 1

        # recursively call this function again
        rushhour.random_solve(rushhour, archive, recursion_count)


    def __str__(self):
        return f"{self.board.coordinates}"


if __name__ == "__main__":
    rushhour = RushHour("../../data/Game1.txt")
    rushhour.solve(rushhour)

