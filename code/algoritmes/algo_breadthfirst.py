def solve(board, cars, moves):
    while not won():
        explore_layer(board, cars, moves)

def explore_layer(layer_boards, layer_cars, layer_moves):
    for board in layer_boards:
        for move in layer_moves[board]:
            move_car()


def next_layer():

