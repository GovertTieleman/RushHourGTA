# Algoritme1
from rushhour import RushHour


# recursive function:
def find_solution(rushhour, boards, winning_move_list, move_count):
    if rushhour.board in boards:
        return False
    else:
        boards.append(rushhour.board)

    move_list = rushhour.find_moves()
    move_count += 1

    for move in move_list:
        winning_move_list += move
        car = move[0]
        if move[1] == "-":
            direction = -1
        else:
            direction = 1
        distance = move[2]
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
    game = RushHour("../../data/Game1.txt")
    archive = []
    list_moves = []
    count = 0

    find_solution(game, archive, list_moves, count)

    print(f"Winning moves: {list_moves}")