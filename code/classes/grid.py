class Grid(object):
    """
    Representation of the grid in Rush Hour.
    """

    def __init__(self, height, width):
        """
        Define grid and create a list for cars
        """
        self.height = height
        self.width = width
        self.coordinates = self.getCoordinates(height, width)
        self.cars = []
        
    def self.getCoordinates(height, width):
        coordinates = []
        for x in width:
            for y in height:
                coordinates.append(Coordinate(x,y))
        return coordinates

class Coordinate(object:
    """
    Coordinates for the grid
    """
                 
    def __init__(self, x, y):
        self.coordinate = (x,y)
        self.occupiedBy = "" #auto naam of index?
    
    # Zo'n soort functie kan handig zijn
    def self.makeSpace()
        car = self.occupiedBy
        car.move()
