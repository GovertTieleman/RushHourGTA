from board import Board
from car import Car


class RushHour():
    """
    Main file for running and solving the game
    """

    def __init__(self, filename):
        """
        Load the board and cars
        """
        # load board
        self.load_game(filename)

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


        # print(self.cars[0].location)

        # create printable board

        # set car orientation

        for car in self.cars:
            if self.cars[car].x[0] - self.cars[car].x[1] == 0:
                self.cars[car].orientation = 'VERTICAL'
            else:
                self.cars[car].orientation = 'HORIZONTAL'

        # create board class
        self.board = Board(size, coordinates)

        # return board
        return self.board

    def move_car(self, car_id, distance, direction):
        """
        Execute a valid move command.
        """
        # get car
        car = self.cars[car_id]

        # move up or down its axis
        if car.move_valid(distance, direction, self.board):
            if car.orientation == 'HORIZONTAL':
                # replace the whole car on the board by empty squares and move car object
                for i in range(len(car.x)):
                    self.board.coordinates[car.x[i], car.y[i]] = '-'
                    car.x[i] += distance * direction
                # place the car in its new position
                for x in car.x:
                    self.board.coordinates[x, car.y[0]] = car_id
                # return true if move successful
                return True
            elif car.orientation == 'VERTICAL':
                # replace the whole car on the board by empty squares and move car object
                for i in range(len(car.y)):
                    self.board.coordinates[car.x[i], car.y[i]] = '-'
                    car.y[i] += distance * direction
                # place the car in its new position
                for y in car.y:
                    self.board.coordinates[car.x[0], y] = car_id
                # return true if move successful
                return True
        else:
            # return false if move unsuccessful
            print(f"Invalid move\n")
            return False

    def won(self):
        distance = self.board.size - self.cars["X"].x[1]
        if self.cars["X"].move_valid(distance, 1, self.board):
            print("Congratulations, you won!")
            exit(0)
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

            # get user input
            command = input("move: ").split(' ')
            car = command[0].upper()

            # exit game if quit command
            if car == "QUIT":
                exit(0)
            # if car doesn't exist, continue
            elif car not in self.cars:
                print("Car not in game, try again")
                continue

            # get direction and distance
            move = command[1]
            if move[0] == '-':
                direction = -1
                distance = move[1:]
            else:
                direction = 1
                distance = move

            # check if car, direction and distance all exist
            if not car or not direction or not distance:
                print("Invalid command, try again")
                continue

            # move
            if self.move_car(car, int(direction), int(distance)):
                # print new board state
                print(f"{self.board}\n")

    def __str__(self):
        return f"{self.board.coordinates}"


if __name__ == "__main__":
    rushhour = RushHour("../../data/Game1.txt")
    rushhour.play()

