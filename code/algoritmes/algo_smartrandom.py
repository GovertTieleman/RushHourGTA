# Smart Random
import sys
import copy
import random
import cProfile
from classes.board import Board
from classes.car import Car

sys.path.insert(0, '../')
sys.setrecursionlimit(25000)


class SR(object):
    """
    Main file for running and solving the game
    """

    def __init__(self, filename):
        """
        Load the board and cars
        """

        # Load board
        self.board = Board.load_game(self, filename)

        # Create archive
        self.archive = [copy.copy(self.board.board_string())]

        # Number of times no solution has been found
        self.no_solution = 0

        # Attributes
        self.allowed_moves = []
        self.winning_moves = []
        self.preferred_moves = []

        # Variable for upper bound
        self.upper_bound = 500
        self.best_game = []
        self.move_history = []


    def solve(self, game, no_solution, upper_bound, best_game, filename):
        print(f"\nBest game so far is: {best_game}!\n")

        print(f"\nNumber of tries: {no_solution}\n")

        # if it hasnt found a (better) solution 10 times in a row
        if no_solution == 100:
            if not best_game:
                print(f"\nNo solution has been found!\n")
                return []
            else:
                print(f"\nOptimal solution found is {best_game} in {len(best_game)} moves!\n")
                return best_game


        game = SR(filename)

        self.board = game.board

        self.archive = [copy.copy(self.board.board_string())]
        self.allowed_moves = []
        self.winning_moves = []
        self.preferred_moves = []
        self.move_history = []

        print("\nCalling random_solve\n")
        last_game = self.random_solve(game, self.archive, upper_bound, no_solution)
        if not last_game:
            self.no_solution += 1
            print("Calling solve\n")
            return self.solve(game, self.no_solution, self.upper_bound, best_game, filename)
        # if it has found a solution
        else:
            self.no_solution += 1
            self.upper_bound = len(last_game)
            best_game = last_game
            return self.solve(game, self.no_solution, self.upper_bound, best_game, filename)

    def random_solve(self, game, archive, upper_bound, no_solution):

        print(f"Board: \n\n{game.board}\n\n")
        print(f"Upper bound is {upper_bound}.")
        print(f"Number of moves already made: {len(self.move_history)}.")
        print(f"Total number of tries: {no_solution}.\n")


        if len(self.move_history) == upper_bound:
            print(f"More than {len(self.move_history)} moves!")
            return []
        else:
            # get list of possible moves
            move_list = self.board.find_moves()

            # create board for every possible move
            for move in move_list:
                # make move
                self.board.move_car(move)
                # if board is not in archive yet
                if self.board.board_string() not in archive:
                    self.allowed_moves.append(move)
                # revert move
                self.board.revert_move(move)

            # if there are no more possible moves to make
            if not self.allowed_moves:
                print("No more moves to make!\nReverting move and trying different move...\n")
                # add board to archive
                archive.append(copy.copy(self.board.board_string()))
                # revert last move made
                if not self.move_history:
                    print("\nNo solution found!\n")
                    return []
                else:
                    self.board.revert_move(self.move_history[-1])
                    # delete last move from move history
                    del self.move_history[-1]
                    # recursively call function again
                    print(f"\nNumber of allowed moves:{len(self.allowed_moves)}\n")
                    return self.random_solve(game, archive, upper_bound, no_solution)
                    # return False

            # check which allowed moves are winning moves and add these to winning_moves
            for move in self.allowed_moves:
                self.board.move_car(move)
                if self.board.won():
                    self.winning_moves.append(move)
                self.board.revert_move(move)

            if not self.winning_moves:
                # filter out preferred moves
                for move in self.allowed_moves:
                    if self.board.more_winnable(self.board, move):
                        self.preferred_moves.append(move)

                if not self.preferred_moves:
                    # choose random move
                    random_move = random.choice(self.allowed_moves)
                    self.board.move_car(random_move)
                    self.move_history.append(random_move)
                else:
                    # choose preferred move
                    random_preferred_move = random.choice(self.preferred_moves)
                    self.board.move_car(random_preferred_move)
                    self.move_history.append(random_preferred_move)
            else:
                # choose winning move
                winning_move = random.choice(self.winning_moves)
                self.board.move_car(winning_move)
                self.move_history.append(winning_move)

            # check if game is won
            if self.board.won() is True:
                return self.move_history

            # save current board to archive
            archive.append(copy.copy(self.board.board_string()))

        # empty lists of allowed moves and winning moves and preferred moves
        del self.allowed_moves[:]
        del self.winning_moves[:]
        del self.preferred_moves[:]

        # recursively call this function again
        return self.random_solve(game, archive, upper_bound, no_solution)

    def __str__(self):
        return f"{self.board.coordinates}"
