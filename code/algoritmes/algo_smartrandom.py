import sys
sys.path.insert(0, '../')
sys.setrecursionlimit(10000)

from classes.board import Board
from classes.car import Car
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
        self.board = Board(size, coordinates, [])

        # create archive
        self.archive = [copy.copy(self.board.board_string())]

        # create list of allowed moves
        self.allowed_moves = []

        self.winning_moves = []

        self.preferred_moves = []

        self.no_solution = 0

        self.upper_bound = 5000

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

        # print(f"Possible moves: {self.movest_list}")

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
            # print(f"Congratulations, you won!\n"
            #       f"move history: {self.move_history}")
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

    def cars_blocking(self, board):
        blocking_cars = 0
        for i in range(self.cars["X"].x[1] + 1, board.size):
            if board.coordinates[i, self.cars["X"].y[0]] != "-":
                blocking_cars += 1
        return blocking_cars

    def more_winnable(self, board, move):
        blocking_cars_before = self.cars_blocking(board)
        self.move_car(move)
        blocking_cars_after = self.cars_blocking(self.board)
        self.revert_move(move)
        if blocking_cars_after < blocking_cars_before:
            return True
        else:
            return False

    def solve(self, rushhour, no_solution, upper_bound, best_game):
        print(f"\nBest game so far is: {best_game}!\n")

        # if it hasnt found a (better) solution 10 times in a row
        if no_solution == 100:
            if not best_game:
                print(f"\nNo solution has been found!\n")
                return False
            else:
                print(f"\nOptimal solution found is {best_game} in {len(best_game)} moves!\n")
                return True

        # reset all variables
        rushhour = RushHour("../../data/Game2.txt")
        self.archive = [copy.copy(self.board.board_string())]
        self.allowed_moves = []
        self.winning_moves = []
        self.preferred_moves = []
        self.move_history = []

        print("\nCalling random_solve\n")
        last_game = self.random_solve(rushhour, self.archive, upper_bound)
        if not last_game:
            self.no_solution += 1
            print("Calling solve\n")
            return self.solve(rushhour, self.no_solution, self.upper_bound, best_game)
        # if it has found a solution
        else:
            self.upper_bound = len(last_game)
            best_game = last_game
            return self.solve(rushhour, self.no_solution, self.upper_bound, best_game)

    def random_solve(self, rushhour, archive, upper_bound):

        # print number of moves already made
        print(f"Number of moves already made: {len(self.move_history)}\n")

        print(f"Current board (before making move): \n{rushhour.board}\n")

        print(upper_bound)

        if len(self.move_history) == upper_bound:
            print(f"More than {len(self.move_history)} moves!")
            return []
        else:
            # get list of possible moves
            move_list = rushhour.find_moves(rushhour.board, rushhour.cars)

            # create board for every possible move
            for move in move_list:

                # make move
                rushhour.move_car(move)

                # if board is not in archive yet
                if rushhour.board.board_string() not in archive:
                    self.allowed_moves.append(move)

                # revert move
                rushhour.revert_move(move)

            # if there are no more possible moves to make
            if not self.allowed_moves:
                print("No more moves to make!\nReverting move and trying different move...\n")
                # add board to archive
                archive.append(copy.copy(rushhour.board.board_string()))
                # revert last move made
                if not self.move_history:
                    print("\nNo solution found!\n")
                    return []
                else:
                    rushhour.revert_move(self.move_history[-1])
                    # delete last move from move history
                    del self.move_history[-1]
                    # recursively call function again
                    print(f"\nNumber of allowed moves:{len(self.allowed_moves)}\n")
                    return rushhour.random_solve(rushhour, archive, upper_bound)
                    # return False

            # check which allowed moves are winning moves and add these to winning_moves
            for move in self.allowed_moves:
                rushhour.move_car(move)
                if rushhour.won():
                    self.winning_moves.append(move)
                rushhour.revert_move(move)

            # print(f"\nAllowed moves: {self.allowed_moves}")
            # print(f"\nWinning moves: {self.winning_moves}")

            if not self.winning_moves:
                # filter out preferred moves
                for move in self.allowed_moves:
                    if self.more_winnable(rushhour.board, move):
                        self.preferred_moves.append(move)

                # print(f"\nPreferred moves: {self.preferred_moves}\n")

                # if no preferred moves, choose random allowed move
                if not self.preferred_moves:
                    # print("\nMaking random move...\n")
                    random_move = random.choice(self.allowed_moves)
                    rushhour.move_car(random_move)
                    self.move_history.append(random_move)
                else:
                    # print("\nMaking random preferred move...\n")
                    random_preferred_move = random.choice(self.preferred_moves)
                    rushhour.move_car(random_preferred_move)
                    self.move_history.append(random_preferred_move)




                # print("\nMaking random move...\n")
                # random_move = random.choice(self.allowed_moves)
                # print(f"\nRandom move is: {random_move}\n")
                # rushhour.move_car(random_move)
                # self.move_history.append(random_move)
            else:
                print("\nMaking winning move...\n")
                winning_move = random.choice(self.winning_moves)
                print(f"\nWinning move is: {winning_move}\n")
                rushhour.move_car(winning_move)
                self.move_history.append(winning_move)


            # # pick random move from move_list
            # random_move = random.choice(self.allowed_moves)
            #
            # # print("Random move to make is: "+ random_move)
            #
            # # make move and save move to move_history list
            # rushhour.move_car(random_move)
            # self.move_history.append(random_move)

            # check if game is won
            if rushhour.won() is True:
                # Stop, return solution!
                print(f"Game is won! (in {len(self.move_history)} moves)\n"
                      f"move history: {self.move_history}")
                return self.move_history

            # save current board to archive
            archive.append(copy.copy(rushhour.board.board_string()))

        # empty lists of allowed moves and winning moves and preferred moves
        del self.allowed_moves[:]
        del self.winning_moves[:]
        del self.preferred_moves[:]


        # recursively call this function again
        return rushhour.random_solve(rushhour, archive, upper_bound)


    def __str__(self):
        return f"{self.board.coordinates}"


if __name__ == "__main__":
    rushhour = RushHour("../../data/Game2.txt")
    no_solution = 0
    upper_bound = 5000
    best_game = []

    rushhour.solve(rushhour, no_solution, upper_bound, best_game)

