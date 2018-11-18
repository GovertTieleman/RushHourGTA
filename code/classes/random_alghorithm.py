#
#   # add current board to archive
#   archive.add(board)
#
# def random_algorithm(archive):
#
#   # if archive is empty, all moves have been tried
#   if not archive:
#     return "NO SOLUTION"
#
#   # get random board from archive (make random move)
#   board = random.choice(archive)
#
#   if game.won():
#     stop, return solution
#
#   # add all possible moves to archive
#   # to keep track of the moves already made
#     randomcount = 0
#   for move in find_moves:
#
#     # create boards for every possible move
#     new_board = board.move_car(move)

      # if new_board in archive:
      # randomcount += 1
#
#     # make sure board isnt being passed twice
#     if new_board not in archive:
#       archive.add(new_board)

#    if randomcount == 0:
#      return "NO SOLUTION"
#
#   # recursively call this function
#   return random_algorithm(archive)