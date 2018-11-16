# Algoritme

from rushhour import RushHour

# recursive function:
def find_solution(rushhour, archive, winning_move_list):
    if rushhour.board in archive:
        return 1
    else:
        archive += rushhour.board

    for move in rushhour.moveslist:
        step = rushhour.play(move)      # play methode moet hiervoor aangepast worden
        if step.won():                  # self.won = False toevoegen aan RushHour class
            winning_move_list += move
            return 0
        else:
            next_step = find_solution()
            if next_step == 0:
                winning_move_list += move
                return 0
            else:
                return 1

# Initialize variables

rushhour = RushHour("../../data/Game1.txt")
archive = []
winning_move_list = []

find_solution(rushhour, archive, winning_move_list)


print(winning_move_list)
print(move_count)



