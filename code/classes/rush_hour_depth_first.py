import sys
sys.path.insert(0, '../')

from classes.board import Board
from classes.car import Car

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

        # gridlocks
        self.gridlocks = self.gridlock(0, X, 'HORIZONTAL', X, 1)
        self.gridlock_size = len(self.gridlocks)

    def load_game(self, filename):
        """
    Method for loading the board
    :param filename:
    :return:
    """
        # establish dictionary of coordinates
        coordinates = {}
        self.cars = {}

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

    def find_moves(self):
        # initialize list of possible moves
        self.moveslist = []

        # iterate over all car objects
        for car_id in self.cars:
            # check if car is horizontal
            if self.cars[car_id].orientation == 'HORIZONTAL':
                # get leftmost and rightmost x of car
                x_left = self.cars[car_id].x[0]
                x_right = self.cars[car_id].x[len(self.cars[car_id].x) - 1]

                # get y of car
                y_car = self.cars[car_id].y[0]

                # set counter i to 1
                i = 1

                # iterate over fields on the left side of car
                if x_left - i > 0 and self.board.coordinates[(x_left - i), y_car] == '-':
                        self.moveslist.append(f"{car_id} {-i}")

                # iterate over fields on the right side of car
                if x_right + i < self.board.size and self.board.coordinates[(x_right + i), y_car] == '-':
                        self.moveslist.append(f"{car_id} {i}")

            # check if car is vertical
            if self.cars[car_id].orientation == 'VERTICAL':
                # get leftmost and rightmost x of car
                y_top = self.cars[car_id].y[0]
                y_bottom = self.cars[car_id].y[len(self.cars[car_id].y) - 1]

                # get y of car
                x_car = self.cars[car_id].x[0]

                # set counter i to 1
                i = 1

                # iterate over fields on the left side of car
                if y_top - i > 0 and self.board.coordinates[x_car, (y_top - i)] == '-':
                        self.moveslist.append(f"{car_id} {-i}")

                # iterate over fields on the right side of car
                if y_bottom + i < self.board.size and self.board.coordinates[x_car, (y_bottom + i)] == '-':
                        self.moveslist.append(f"{car_id} {i}")

        return self.moveslist

    def move_car(self, command):
        """
    Execute a valid move command.
    """
        # split command for use
        command = command.split(' ')

        # get car
        car = self.cars[command[0].upper()]

        # get direction and distance
        move = command[1]
        if move[0] == '-':
            direction = -1
            distance = int(move[1:])
        else:
            direction = 1
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
            print(f"Invalid move, {command}\n")
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
            print(f"Invalid move\n")
            return False

    def gridlock(self, count, coordinate, direction):

        penalty = 2

        if direction == 'UP':
            target_coordinate = self.board.coordinates(coordinate[0], coordinate[1] - 1)
        elif direction == 'DOWN':
            target_coordinate = self.board.coordinates(coordinate[0], coordinate[1] + 1)
        elif direction == 'LEFT':
            target_coordinate = self.board.coordinates(coordinate[0] - 1, coordinate[1])
        elif direction == 'RIGHT':
            target_coordinate = self.board.coordinates(coordinate[0] + 1, coordinate[1])

        if target_coordinate == '-':
            return 0
        elif target_coordinate.isalpha():
            count += 1
            return self.gridlock(count, target_coordinate, direction)
        else:
            return count + penalty


    def won(self):
        distance = (self.board.size - self.cars["X"].x[1]) - 1
        if self.cars["X"].move_valid(distance, 1, self.board):
            return True
        else:
            return False

    def play(self):
        # Welcome player into game
        print(f"This is GTA RushHour.\n"
              "Input the car you want to move, followed by the direction and amount of steps.\n"
              "The game is won once you reach the exit!\n")

        # Show the player the board
        print(f"{self.board}\n")

        # Prompt the user for commands until they've won the game.
        while not self.won():
            # find moves
            self.find_moves()

            # get user input
            command = input("move: ")
            car = command[0].upper()

            # exit game if quit command
            if car == "QUIT":
                exit(0)
            # if car doesn't exist, continue
            elif car not in self.cars:
                print("Car not in game, try again")
                continue

            # check if car, direction and distance all exist
            if not car:
                print("Invalid command, try again")
                continue

            # move
            if self.move_car(command):
                # increment move counter
                self.move_counter += 1

                # print new board state
                print(f"{self.board}\nMoves: {self.move_counter}\n")

    def __str__(self):
        return f"{self.board.coordinates}"


if __name__ == "__main__":
    rushhour = RushHour("../../data/BugMap.txt")
    rushhour.play()