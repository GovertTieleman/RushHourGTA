class Car(object):
    """
    Representation of a car in Rush Hour
    """

    def __init__(self, id, x, y, orientation):
        """
        Initialize an Item
        give it a name, description and an initial room id
        """
        self.id = id
        self.x = [x]
        self.y = [y]
        self.orientation = orientation

    def move_valid(self, distance, direction, board):
        if self.orientation == 'HORIZONTAL':
            for i in range(len(self.x)):
                if (self.x[i] + distance * direction) < 1 or (self.x[i] + distance * direction) > 6:
                    return False
                if board.coordinates[(self.x[i] + distance * direction), self.y[i]] != '-' \
                        and board.coordinates[(self.x[i] + distance * direction), self.y[i]] != self.id:
                    return False
            return True
        elif self.orientation == 'VERTICAL':
            for i in range(len(self.y)):
                if (self.y[i] + distance * direction) < 1 or (self.y[i] + distance * direction) > 6:
                    return False
                if board.coordinates[self.x[i], (self.y[i] + distance * direction)] != '-' \
                        and board.coordinates[self.x[i], (self.y[i] + distance * direction)] != self.id:
                    return False
            return True

