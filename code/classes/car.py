class Car(object):
    """
    Representation of a car in Rush Hour
    """

    def __init__(self, id, coordinates, orientation):
        """
        Initialize an Item
        give it a name, description and an initial room id
        """
        self.id = id
        self.orientation = orientation
        self.coordinates = coordinates
