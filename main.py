import cProfile

import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from run_algorithm import Run_algorithm

def main():
    Run_algorithm()

if __name__ == "__main__":
    main()