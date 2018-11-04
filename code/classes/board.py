# from car import car

class Board(object):
    """
    Representation of the board in Rush Hour.
    """

    def __init__(self, size, coordinates, printable):
        """
        Define grid and create a list for cars
        """
        self.size = size
        self.coordinates = coordinates
        self.printable = printable
        self.cars = []

# class Coordinate(object:
#     """
#     Coordinates for the grid
#     """
#
#     def __init__(self, x, y):
#         self.coordinate = (x,y)
#         self.occupiedBy = "" #auto naam of index?
#
#     # Zo'n soort functie kan handig zijn
#     def self.makeSpace()
#         car = self.occupiedBy
#         car.move()
