# Algoritme
from rushhour import RushHour

# recursive function:
def find_solution(rushhour, archive, winning_move_list, move_count):
    if rushhour.board in archive:
        return False
    else:
        archive.append(rushhour.board)

    movelist = rushhour.find_moves()
    move_count += 1

    for move in movelist:
        car = move[0]
        if move[2] == "-":
            direction = -1
        else:
            direction = 1
        distance = move[-1:]
        rushhour.move_car(car, direction, int(distance))
        if rushhour.won():
            winning_move_list += move
            return True
        else:
            if find_solution(rushhour, archive, winning_move_list, move_count):
                winning_move_list += move
                return True
            else:
                return False


# Initialize variables

if __name__ == "__main__":
    rushhour = RushHour("../../data/Game1.txt")
    archive = []
    winning_move_list = []
    move_count = 0

    find_solution(rushhour, archive, winning_move_list, move_count)

    print(f"Winning moves: {winning_move_list}")
