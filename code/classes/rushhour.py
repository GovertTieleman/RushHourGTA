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

        # print(self.cars[0].location)

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

        board_printable = ''
        for line in lines:
            board_printable += "  ".join(line)

        # create board class
        self.board = Board(size, coordinates, board_printable)

        # return board
        return self.board

    def __str__(self):
        return f"{self.board.printable}\n{self.board.coordinates}"


if __name__ == "__main__":
    rushhour = RushHour("../../data/Game1.txt")
    print(rushhour)