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
        board = self.load_game(filename)

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

        # create printable board
        for car in self.cars:
            if self.cars[car].x[0] - self.cars[car].x[1] == 0:
                self.cars[car].orientation = 'VERTICAL'
            else:
                self.cars[car].orientation = 'HORIZONTAL'
        for car in self.cars:
            print(self.cars[car].x)
            print(self.cars[car].y)
            print(self.cars[car].orientation)


        # create board class
        self.board = Board(size, coordinates)

        # return board
        return self.board

    def move_car(self, car_id, distance, direction):
        """move car to a valid position"""

        car = self.cars[car_id]

        # direction = +1 of -1
        if car.move_valid(distance, direction):
            if car.orientation == 'HORIZONTAL':
                for i in range(len(car.x)):
                    self.board.coordinates[car.x[i], car.y[i]] = '-'
                    car.x[i] += distance * direction
                for x in car.x:
                    self.board.coordinates[x, car.y[0]] = car_id
            elif car.orientation == 'VERTICAL':
                for i in range(len(car.y)):
                    self.board.coordinates[car.x[i], car.y[i]] = '-'
                    car.y[i] += distance * direction
                for y in car.y:
                    self.board.coordinates[car.x[0], y] = car_id


    def __str__(self):
        return f"{self.board.coordinates}"


if __name__ == "__main__":
    rushhour = RushHour("../../data/Game1.txt")
    print(rushhour.board)
    rushhour.move_car('A', 1, 1)
    print(f"\n{rushhour.board}")
    rushhour.move_car('B', 3, -1)
    print(f"\n{rushhour.board}")

