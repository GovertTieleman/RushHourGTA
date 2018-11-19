# Algoritme1
from rushhour_random_algo import RushHour

class Algorithm(object):
    """
    Main file for running and solving the game
    """

    def __init__(self, game):
        self.game = game
        self.archive = []
        self.moves_list = []

    # recursive function:
    def find_solution(self, move_count):

        # Check and update archive
        current_map = self.game.board.board_string()
        if current_map in self.archive:
            return False
        else:
            self.archive.append(current_map)

        # Initialize move list
        move_list = self.game.find_moves()
        move_count += 1

        # Iterate over moves
        for move in move_list:
            self.game.move_car(move)
            if self.game.won():
                self.moves_list += move
                return True
            elif self.find_solution(move_count):
                self.moves_list += move
                return True
        return False

if __name__ == "__main__":
    game = RushHour("../../data/Game1.txt")
    solution = Algorithm(game)
    count = 0
    solution.find_solution(count)
    print(f"Winning moves: {solution.moves_list}")
