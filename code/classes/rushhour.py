from board import board


class RushHour():
    """
    Main file for running and solving the game
    """

    def __init__(self, filename):
        """
        Load the board and cars
        """
        # load board
        board_loaded = self.load_board(filename)

    def load_board(self, filename):
        """
        Method for loading the board
        :param filename:
        :return:
        """
        # open file
        with open(filename, "r") as f:
            # read lines
            lines = f.readlines()
            size = len(lines[0])

    def __str__(self):
        # TODO
        pass


if __name__ == "__main__":
    rushhour = RushHour("data/Game1.txt")
    print(RushHour)
