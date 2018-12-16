from classes.car import Car

class Board(object):
    """
    Representation of the board in Rush Hour.
    """

    def __init__(self, size, coordinates, move_sequence):
        """
        Define grid and create a list for cars.
        """
        # board attributes
        self.size = size
        self.coordinates = coordinates

        # cars
        self.cars = {}

        # sequence and number of moves
        self.move_sequence = move_sequence

    def load_game(self, filename):
        """
        Method for loading the board
        :param filename:
        :return:
        """
        # establish dictionary of coordinates
        coordinates = {}

        # establish dictionary of cars
        cars = {}

        # open file
        with open(filename, "r") as f:
            # read lines and coordinates, starting with x and y at 1
            lines = f.readlines()
            size = len(lines[0].strip())
            x = 1
            y = 1
            # iterate over characters, creating the board and cars
            for line in lines:
                for char in line.strip():
                    coordinates[x, y] = char
                    if char.isalpha():
                        if char in cars:
                            cars[char].x.append(x)
                            cars[char].y.append(y)
                        else:
                            cars[char] = Car(char, x, y, '')
                    x += 1
                x = 1
                y += 1

        # set car orientation
        for car in cars:
            if cars[car].x[0] - cars[car].x[1] == 0:
                cars[car].orientation = 'VERTICAL'
            else:
                cars[car].orientation = 'HORIZONTAL'

        # create board class
        board = Board(size, coordinates, [])

        # add cars to board
        for car in cars:
            board.add_car(cars[car])

        # return board
        return board


    def add_car(self, car):
        """
        Add car objects to board instance.
        """
        self.cars[car.id] = car

    def find_moves(self):
        """
        Find all possible moves on board instance.
        """
        # initialize list of possible moves
        moves_list = []

        # iterate over all car objects
        for car in self.cars:
            # check if car is horizontal
            if self.cars[car].orientation == 'HORIZONTAL':
                # get leftmost and rightmost x of car
                x_left = self.cars[car].x[0]
                x_right = self.cars[car].x[len(self.cars[car].x) - 1]

                # get y of car
                y_car = self.cars[car].y[0]

                # set counter i to 1
                i = 1

                # iterate over fields on the left side of car
                while x_left - i > 0:
                    if self.coordinates[(x_left - i), y_car] != '-':
                        # break if no empty space
                        i = 1
                        break
                    else:
                        # append move to moves_list
                        moves_list.append(f"{car} {-i}")
                        i += 1

                # reset counter
                i = 1

                # iterate over fields on the right side of car
                while x_right + i <= self.size:
                    if self.coordinates[(x_right + i), y_car] != '-':
                        # break if no empty space
                        i = 1
                        break
                    else:
                        # append move to moves_list
                        moves_list.append(f"{car} {i}")
                        i += 1

            # check if car is vertical
            if self.cars[car].orientation == 'VERTICAL':
                # get topmost and bottommost y of car
                y_top = self.cars[car].y[0]
                y_bottom = self.cars[car].y[len(self.cars[car].y) - 1]

                # get y of car
                x_car = self.cars[car].x[0]

                # set counter i to 1
                i = 1

                # iterate over fields at the top of car
                while y_top - i > 0:
                    if self.coordinates[x_car, (y_top - i)] != '-':
                        # break if no empty space
                        i = 1
                        break
                    else:
                        # append move to moves_list
                        moves_list.append(f"{car} {-i}")
                        i += 1

                # reset counter
                i = 1

                # iterate over fields at the bottom of car
                while y_bottom + i <= self.size:
                    if self.coordinates[x_car, (y_bottom + i)] != '-':
                        # break if no empty space
                        i = 1
                        break
                    else:
                        # append move to moves_list
                        moves_list.append(f"{car} {i}")
                        i += 1

        return moves_list

    def more_winnable(self, board, command):
        blocking_cars_before = board.cars_blocking(board)
        board.move_car(command)
        blocking_cars_after = board.cars_blocking(board)
        board.revert_move(command)
        if blocking_cars_after < blocking_cars_before:
            return True
        else:
            return False

    def move_car(self, command):
        """
        Execute a move command.
        """
        # append command to move sequence of board
        self.move_sequence.append(command)

        # split command for use
        command = command.split(' ')

        # get car
        car = self.cars[command[0]]

        # get direction and distance
        move = command[1]
        if move[0] == '-':
            direction = -1
            distance = int(move[1:])
        else:
            direction = 1
            distance = int(move)

        # move car
        if car.orientation == 'HORIZONTAL':
            # replace the whole car on the board by empty squares and move car object
            for i in range(len(car.x)):
                self.coordinates[car.x[i], car.y[i]] = '-'
                car.x[i] += distance * direction

            # place the car in its new position on the board
            for x in car.x:
                self.coordinates[x, car.y[0]] = car.id

            # return true if move successful
            return True
        elif car.orientation == 'VERTICAL':
            # replace the whole car on the board by empty squares and move car object
            for i in range(len(car.y)):
                self.coordinates[car.x[i], car.y[i]] = '-'
                car.y[i] += distance * direction

            # place the car in its new position on the board
            for y in car.y:
                self.coordinates[car.x[0], y] = car.id

            # return true if move successful
            return True

    def revert_move(self, command):
        """
        Revert a move command.
        """
        # remove last command from move_sequence
        del self.move_sequence[-1]

        # split command for use
        command = command.split(' ')

        # get car
        car = self.cars[command[0]]

        # get direction and distance
        move = command[1]
        if move[0] == '-':
            direction = 1
            distance = int(move[1:])
        else:
            direction = -1
            distance = int(move)

        # move car
        if car.orientation == 'HORIZONTAL':
            # replace the whole car on the board by empty squares and move car object
            for i in range(len(car.x)):
                self.coordinates[car.x[i], car.y[i]] = '-'
                car.x[i] += distance * direction

            # place the car in its new position on the board
            for x in car.x:
                self.coordinates[x, car.y[0]] = car.id

            # return true if move successful
            return True
        elif car.orientation == 'VERTICAL':
            # replace the whole car on the board by empty squares and move car object
            for i in range(len(car.y)):
                self.coordinates[car.x[i], car.y[i]] = '-'
                car.y[i] += distance * direction

            # place the car in its new position on the board
            for y in car.y:
                self.coordinates[car.x[0], y] = car.id

            # return true if move successful
            return True

    def cars_blocking(self, board):
        blocking_cars = 0
        for i in range(board.cars["X"].x[1] + 1, board.size):
            if board.coordinates[i, board.cars["X"].y[0]] != "-":
                blocking_cars += 1
        return blocking_cars

    def won(self):
        """
        Check if the game can be won in 1 move
        """
        # get red car
        red_car = self.cars['X']

        # get (rightmost)x and y for red_car
        x_red = red_car.x[1]
        y_red = red_car.y[0]

        # get distance to exit
        distance_to_exit = self.size - x_red

        # check if free path to exit exists
        for i in range(distance_to_exit):
            if self.coordinates[(x_red + i + 1), y_red] != '-':
                # return false if no path to exit
                return False

        # return True if path exists
        print(f"Game solved in {len(self.move_sequence)} moves.\nThe final board: \n{self} "
              f"The winning move sequence was: \n{self.move_sequence}")
        return True

    def board_string(self):
        # create list of coordinates
        coordinates_list = []
        for coordinate in self.coordinates:
            coordinates_list.append(self.coordinates[coordinate])

        # initiate output
        output = ''

        # make counter
        x = 0

        # iterate over coordinates
        for i in range(len(coordinates_list)):
            # check for exit
            if coordinates_list[i] == '#':
                output += "".join(coordinates_list[i])
                continue

            # add newline and reset counter
            if x == self.size:
                output += '\n'
                x = 0

            # add output
            output += "".join(coordinates_list[i])

            # increment counter
            x += 1

        return output

    def __str__(self):
        # create list of coordinates
        coordinates_list = []
        for coordinate in self.coordinates:
            coordinates_list.append(self.coordinates[coordinate])

        # initiate output
        output = ''

        # make counter
        x = 0

        # iterate over coordinates
        for i in range(len(coordinates_list)):
            # check for exit
            if coordinates_list[i] == '#':
                output += "".join(coordinates_list[i])
                continue

            # add newline and reset counter
            if x == self.size:
                output += '\n'
                x = 0

            # add output
            output += "".join(coordinates_list[i])

            # increment counter
            x += 1

        return output
