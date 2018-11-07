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

        # if self.x[0] - self.x[1] == 0:
        #     self.orientation = VERTICAL
