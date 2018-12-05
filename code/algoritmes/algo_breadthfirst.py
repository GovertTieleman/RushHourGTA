import cProfile
import sys
sys.path.insert(0, '../')

from random.rush_hour_bfs.py import RushHour


class Algorithm(object):
    """
    Main class for running and solving the game
    """

    def __init__(self, game):
        self.game = game
        self.archive = {}
        self.winning_moves_list = []
        self.end_board = ""

    # Recursive function:
    def find_solution(self):

        # keep list of visited boards
        visited = set()

        # set max_depth
        max_depth = 100

        # create queue of boards and append the starting board
        queue = list()
        queue.append(self.board)

        # iterate over boards in queue
        while len(queue) != 0:
            # get current board
            board = queue.pop(0)

            # get depth
            depth = len(board.move_sequence)

            # show user which board is being considered
            print(f"currently working on this board: \n{board}\n"
                  f"depth: {depth}\n"
                  f"size of queue: {len(queue)}\n"
                  f"size of archive: {len(visited)}\n")

            if depth >= max_depth:
                print(f"max_depth exceeded\n")
                break

            if board.board_string() in visited:
                print(f"board visited\n")
                continue
            else:
                visited.add(board.board_string())

            if board.won():
                break
            else:
                # get moves for board
                moves_list = board.find_moves()

                # iterate over moves in list
                for move in moves_list:
                    # execute move
                    board.move_car(move)

                    # extend queue
                    queue.append(copy.deepcopy(board))

                    # revert move
                    board.revert_move(move)


if __name__ == "__main__":
    # Initialize Algorithm
    game = RushHour("../../data/Game2.txt")
    solution = Algorithm(game)
    count = 0
    print(solution.game.board)
    cProfile.run(solution.find_solution(count))

    # Result
    if solution.end_board:
        solution.winning_moves_list.reverse()
        print("Solution:", ", ".join(solution.winning_moves_list), ", X -> #" f"\nFinal board:\n{solution.end_board}")
    else:
        print("No solution found")
    print(f"Archive size: {len(solution.archive)}\n")
