import cProfile
import sys
sys.path.insert(0, '../')

# from classes.rush_hour_depth_first import RushHour
from classes.board import Board
from classes.car import Car

class BnB(object):
    """
    Main class for running and solving the game
    """

    def __init__(self, filename):
        # self.game = game

        # load board
        self.board = Board.load_game(self, filename)
        self.filename = filename

        self.archive = {}
        self.winning_moves_list = []
        self.end_board = ""
        self.upper_bound = 100

    def solve(self):
        while self.find_solution(0):
            self.board = Board.load_game(self, self.filename)
            self.winning_moves_list.clear()
        print(f"Algorithm finished. \narchive: {len(self.archive)}")

    # Recursive function:
    def find_solution(self, move_count):

        # Update archive
        board = self.board
        current_board = board.board_string()
        self.archive[current_board] = move_count

        # Update moves and count
        move_list = board.find_moves()
        #print(f"{current_board}:\nmove count:{move_count}\narchive size:{len(self.archive)}\n")

        # Check bound
        move_count += 1
        if move_count == self.upper_bound:
            return False

        # Iterate over valid moves
        for move in move_list:
            board.move_car(move)

            # Check archive for map and length of route
            new_board = board.board_string()
            if new_board in self.archive and self.archive[new_board] <= move_count > 7:
                board.revert_move(move)

            # Check win condition
            elif board.won():
                print(f"Algorithm succeeded, solution found with length: {move_count}")

                # Update attributes
                self.upper_bound = move_count
                self.archive[current_board] = move_count
                self.end_board = board
                self.winning_moves_list.append(move)
                return True

            # Make next move
            elif self.find_solution(move_count):

                # If solution found, add move to the winning move sequence
                self.winning_moves_list.append(move)
                return True

            # Else reverse move
            else:
                board.revert_move(move)
        return False

if __name__ == "__main__":

    rush_hour = BnB("../../data/Game3.txt")
    count = 0
    cProfile.run('rush_hour.solve()')

    # Result
    if rush_hour.end_board:
        rush_hour.winning_moves_list.reverse()
        print("Solution:", ", ".join(rush_hour.winning_moves_list), ", X -> #" f"\nFinal board:\n{rush_hour.end_board}")
    else:
        print("No solution found")
    print(f"Archive size: {len(rush_hour.archive)}\n")