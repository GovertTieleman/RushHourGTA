import cProfile

import sys
sys.path.insert(0, '../')

from algoritmes.algo_branchnbound import BnB
from algoritmes.algo_breadthfirst import BF
from algoritmes.algo_depthfirst import DF
from algoritmes.algo_random import R
from algoritmes.algo_smartrandom import SR

class Run_algorithm(object):

    # welcome user
    print(f"\nWelcome to GTA RushHour!\n"
          "Please insert the level you would like to solve.\n")

    level_input = input("Level: ").split(' ')

    while int(level_input[0]) < 1 or int(level_input[0]) > 7:
        print(f"\nRush Hour levels range from level 1 to level 7.")
        level_input = input("Please try again: ").split(' ')

    else:
        filename = "../../data/Game" + str(level_input[0]) + ".txt"

        print(f"\nYou have chosen level {level_input[0]}.\n\n"
              f"Now please insert the algorithm you would like to use to solve this level.\n"
              "You can choose between 'branch n bound', 'breadth first', 'depth first', 'random' and 'smart random'.\n")

        algorithm = input("algorithm: ")

        if algorithm == "branch n bound":
            rushhour = BnB(filename)
            count = 0
            rushhour.solve()

        elif algorithm == "breadth first":
            rushhour = BF(filename)
            rushhour.solve()

        elif algorithm == "depth first":
            rushhour = DF(filename)
            count = 0
            rushhour.find_solution(count)

        elif algorithm == "random":
            rushhour = R(filename)
            rushhour.solve()

        elif algorithm == "smart random":
            game = SR(filename)
            game.solve(game, game.no_solution, game.upper_bound, game.best_game, filename)



