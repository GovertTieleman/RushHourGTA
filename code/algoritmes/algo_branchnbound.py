import cProfile
import sys
sys.path.insert(0, '../')

# from classes.rush_hour_depth_first import RushHour
from classes.board import Board
from classes.car import Car

UPPER_BOUND = 20


class BnB(object):
    """
    Main class for running and solving the game
    """

    def __init__(self, filename):
        # self.game = game

        # load board
        self.board = Board.load_game(self, filename)

        self.archive = {}
        self.winning_moves_list = []
        self.end_board = ""

    # Recursive function:
    def find_solution(self, move_count):

        # Check and update archive
        current_board = self.board.board_string()
        self.archive[current_board] = move_count

        # Update moves and count
        move_list = self.board.find_moves()
        print(f"{current_board}:\nmove count:{move_count}\narchive size:{len(self.archive)}\n")

        # Check limit
        move_count += 1
        if move_count == UPPER_BOUND + 1:
            return False

        # Iterate over valid moves
        for move in move_list:
            self.board.move_car(move)
            new_board = self.board.board_string()

            # Check archive for map and length of route
            if new_board in self.archive and self.archive[new_board] <= move_count:
                self.board.revert_move(move)

            # Check win condition
            elif self.board.won():
                print(f"Algorithm succeeded, solution found with length: {move_count}")
                self.end_board = self.board
                self.winning_moves_list.append(move)
                return True

            # Make next move
            elif self.find_solution(move_count):
                self.winning_moves_list.append(move)
                return True

            # Else reverse move
            else:
                self.board.revert_move(move)
        return False

if __name__ == "__main__":

    rushhour = BnB("../../data/Game3.txt")
    count = 0
    cProfile.run('rushhour.find_solution(count)')

    # Initialize Algorithm
    # game = RushHour("../../data/Game2.txt")
    # solution = Algorithm(game)
    # count = 0
    # print(solution.game.board)
    # cProfile.run('solution.find_solution(count)')

    # Result
    if rushhour.end_board:
        rushhour.winning_moves_list.reverse()
        print("Solution:", ", ".join(rushhour.winning_moves_list), ", X -> #" f"\nFinal board:\n{rushhour.end_board}")
    else:
        print("No solution found")
    print(f"Archive size: {len(rushhour.archive)}\n")