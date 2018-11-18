from board import Board
from car import Car
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
        self.cars = {}

        # establish move_history list and loop prevention dict
        self.archive = [self.board]
        self.loop_prevention = {}


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
        moves_list = []

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
                while x_left - i > 0:
                    if self.board.coordinates[(x_left - i), y_car] != '-':
                        # break if no empty space
                        break
                    else:
                        # append move to moves_list
                        moves_list.append(f"{car_id} {-i}")
                        i += 1

                # reset counter
                i = 1

                # iterate over fields on the right side of car
                while x_right + i < self.board.size:
                    if self.board.coordinates[(x_right + i), y_car] != '-':
                        # break if no empty space
                        break
                    else:
                        # append move to moves_list
                        moves_list.append(f"{car_id} {i}")
                        i += 1

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
                while y_top - i > 0:
                    if self.board.coordinates[x_car, (y_top - i)] != '-':
                        # break if no empty space
                        break
                    else:
                        # append move to moves_list
                        moves_list.append(f"{car_id} {-i}")
                        i += 1

                # reset counter
                i = 1

                # iterate over fields on the right side of car
                while y_bottom + i < self.board.size:
                    if self.board.coordinates[x_car, (y_bottom + i)] != '-':
                        # break if no empty space
                        i = 1
                        break
                    else:
                        # append move to moves_list
                        moves_list.append(f"{car_id} {i}")
                        i += 1

        return moves_list

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

    def random_solve(self, archive, current_board):
        # get list of possible moves
        move_list = rushhour.find_moves()

        # if there are no more possible moves to make
        if not move_list:
            # Stop, no solution!
            return False

        # create board for every possible move (in string form)
        for move in move_list:

            # delete already encountered boards
            if new_board in archive:
                move_list.remove(move)

                # create new board for every move
                new_board = self.board

        # pick random move from move_list
        command = random.choice(move_list)

        # create board after random move
        current_board = rushhour.move_car(command)

        # make move
        rushhour.move_car(command)

        # check if game is won
        if rushhour.won():
            # Stop, return solution!
            return True

        # save current board to archive
        archive.append(current_board)

        # recursively call this function again
        rushhour.random_solve(archive, current_board)



    def __str__(self):
        return f"{self.board.coordinates}"


if __name__ == "__main__":
    rushhour = RushHour("../../data/Game1.txt")
    rushhour.random_solve()

