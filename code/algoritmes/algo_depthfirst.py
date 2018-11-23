# Algoritme1
import sys
sys.path.insert(0, '../')
sys.setrecursionlimit(10001)

from classes.rush_hour_depth_first import RushHour

class Algorithm(object):
    """
    Main file for running and solving the game
    """

    def __init__(self, game):
        self.game = game
        self.archive = []
        self.winning_moves_list = []
        self.end_board = ""

    def revert(self, move):
        if "-" in move:
            reverse_move = move.replace("-", "")
            return reverse_move
        else:
            reverse_move = move.replace(" ", " -")
            return reverse_move

    # recursive function:
    def find_solution(self, move_count, last_move):

        # Check and update archive
        current_map = self.game.board.board_string()
        self.archive.append(current_map)

        # Update position
        move_list = self.game.find_moves()
        print(f"\n{current_map}:\nmove count:{move_count}\n")
        # if move_count > 0:
        #     # print(f"last move:{last_move}")
        #     reverse_move = self.revert(last_move)
        #     # print(f"reverse move:{reverse_move}")
        #     move_list.remove(reverse_move)
        # move_list.reverse()

        # Check limit
        move_count += 1
        if move_count == 5000:
            return False

        # Iterate over moves
        for move in move_list:
            self.game.move_car(move)
            new_map = self.game.board.board_string()
            if self.game.won():
                print(f"moves: {move_count}")
                self.end_board = self.game.board
                self.winning_moves_list.append(move)
                return True
            elif new_map in self.archive:
                self.game.revert_move(move)
            elif self.find_solution(move_count, move):
                self.winning_moves_list.append(move)
                return True
            else:
                self.game.revert_move(move)
        return False

if __name__ == "__main__":

    # Initialize Algorithm
    game = RushHour("../../data/Game2.txt")
    solution = Algorithm(game)
    count = 0
    move = ""
    print(solution.game.board)
    solution.find_solution(count, move)

    # Result
    solution.winning_moves_list.reverse()
    print(f"Winning moves: {solution.winning_moves_list}")
    if solution.end_board:
        print(f"Final board:\n{solution.end_board}")
    print(f"Archive size: {len(solution.archive)}")