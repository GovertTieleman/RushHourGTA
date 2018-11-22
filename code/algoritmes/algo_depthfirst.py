# Algoritme1
import sys
sys.path.insert(0, '../')

from classes.rush_hour_depth_first import RushHour

class Algorithm(object):
    """
    Main file for running and solving the game
    """

    def __init__(self, game):
        self.game = game
        self.archive = []
        self.winning_moves_list = []
        self.end_board = []

    # recursive function:
    def find_solution(self, move_count):

        # Check and update archive
        current_map = self.game.board.board_string()
        self.archive.append(current_map)

        # Initialize move list
        move_list = self.game.find_moves()
        # move_list.reverse()

        # Check limit
        move_count += 1
        if move_count == 995:
            return False

        # Iterate over moves
        for move in move_list:
            self.game.move_car(move)
            new_map = self.game.board.board_string()
            if self.game.won():
                print(f"moves: {move_count}")
                self.end_board.append(self.game.board)
                self.winning_moves_list.append(move)
                return True
            elif new_map in self.archive:
                self.game.revert_move(move)
            elif self.find_solution(move_count):
                self.winning_moves_list.append(move)
                return True
            else:
                self.game.revert_move(move)
        return False

if __name__ == "__main__":
    game = RushHour("../../data/Game6.txt")
    solution = Algorithm(game)
    count = 1
    print(solution.game.board)
    solution.find_solution(count)
    solution.winning_moves_list.reverse()
    print(f"Winning moves: {solution.winning_moves_list}")
    if solution.end_board:
        print(f"Final board:\n{solution.end_board[0]}")
    print(f"Archive size: {len(solution.archive)}")