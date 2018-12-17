# Algoritme1
import sys
import cProfile
sys.path.insert(0, '../')
sys.setrecursionlimit(5000)

# from classes.rush_hour_depth_first import RushHour
from classes.board import Board
from classes.car import Car

class DF(object):
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
        board = self.board
        current_board = board.board_string()
        self.archive[current_board] = move_count

        # Update moves and count
        move_list = board.find_moves()
        print(f"\nmove list: {move_list}\n")

        print(f"{current_board}:\nmove count:{move_count}\narchive size:{len(self.archive)}\n")

        # Check limit
        move_count += 1
        if move_count == 5000:
            return False

        # Iterate over valid moves
        for move in move_list:
            board.move_car(move)
            new_board = board.board_string()

            # Check win condition
            if board.won():
                print(f"Algorithm succeeded, solution found with length: {move_count + 1}")
                self.end_board = board
                self.winning_moves_list.append(move)
                return True

            # Check archive for map and length of route
            if new_board in self.archive and self.archive[new_board] <= move_count:
                board.revert_move(move)

            # Make next move
            elif self.find_solution(move_count):
                self.winning_moves_list.append(move)
                return True

            # Else reverse move
            else:
                board.revert_move(move)
        return False


if __name__ == "__main__":


    #
    rush_hour = DF("../../data/Game3.txt")
    count = 0
    cProfile.run('rush_hour.find_solution(count)')


    #

    # Initialize Algorithm
    # game = RushHour("../../data/Game2.txt")
    # solution = Algorithm(game)
    # count = 0
    # print(solution.game.board)
    # solution.find_solution(count)

    # # Result
    # if solution.end_board:
    #     solution.winning_moves_list.reverse()
    #     print("Solution:", ", ".join(solution.winning_moves_list), f"\nFinal board:\n{solution.end_board}")
    # else:
    #     print("No solution found")
    # print(f"Archive size: {len(solution.archive)}\n")