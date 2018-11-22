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
