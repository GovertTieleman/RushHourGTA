import cProfile
import time

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

    # prompt user for level
    while True:
        level_input = input("Level: ")
        if level_input == "":
            print("\nïnvalid input")
            continue
        elif not level_input.isdigit():
            print("\nïnvalid input")
            continue
        else:
            level_input = int(level_input)

        if level_input in range(1, 8):
            break
        else:
            print("\ninvalid input")

    # make filename string
    filename = "../../data/Game" + str(level_input) + ".txt"

    print(f"\nYou have chosen level {level_input}.\n"
          f"Now please insert the algorithm you would like to use to solve this level.\n"
          f"You can choose between:\n1. branch n bound\n2. breadth first\n3. depth first\n4. random\n5. smart random\n")

    # prompt user for algorithm
    while True:
        algorithm = input("\ninsert algorithm number: ")
        if algorithm == "":
            print("\nïnvalid input")
            continue
        elif not algorithm.isdigit():
            print("\nïnvalid input")
            continue
        else:
            algorithm = int(algorithm)

        if algorithm in range(1, 6):
            break
        else:
            print("\ninvalid input")

    # run chosen algorithm
    if algorithm == 1:
        rushhour = BnB(filename)
        count = 0
        print("\n\n\nPreparing to run Branch 'n Bound...\n\n\n")
        time.sleep(2)
        cProfile.runctx("rushhour.solve()", globals(), locals())

    elif algorithm == 2:
        rushhour = BF(filename)
        print("\n\n\nPreparing to run Breadth First...\n\n\n")
        time.sleep(2)
        cProfile.runctx("rushhour.solve()", globals(), locals())

    elif algorithm == 3:
        rushhour = DF(filename)
        count = 0
        print("\n\n\nPreparing to run Depth First...\n\n\n")
        time.sleep(2)
        cProfile.runctx("rushhour.find_solution(count)", globals(), locals())

    elif algorithm == 4:
        rushhour = R(filename)
        print("\n\n\nPreparing to run Random...\n\n\n")
        time.sleep(2)
        cProfile.runctx("rushhour.solve()", globals(), locals())

    elif algorithm == 5:
        game = SR(filename)
        print("\n\n\nPreparing to run Random...\n\n\n")
        time.sleep(2)
        cProfile.runctx("game.solve(game, game.no_solution, game.upper_bound, game.best_game, filename)", globals()
                        , locals())



