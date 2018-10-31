class Waggie(object):
    """
    Representation of a car in Rush Hour
    """

    def __init__(front_coordinates, back_coordinates):
        self.front = coordinates front (x1, y1)
        self.back = coordinates back (x2, y2)
        self.direction = self.direct(self.front, self.back)
        self.length = self.calculateLength(self.front, self.back, self.direction)
        self.freespace = self.findspace()
        
        self.direct():
            if y1 - y2 == 0:
                return horizontal 
            else: == 0:
                return vertical
        
        self.length():
            if self.direction == horizontal:
                return abs(x1 - x2)
            else:
                return abs(y1 - y2)
        
        self.findspace():
            if self.direction == horizontal:
                look at y1 - 1 and y2 + 1 and beyond, return free coordinates
            else:
                look at x1 - 1 and x2 + 1 and beyond, return free coordinates

        self.move():
            change coordinates to new coordinates
