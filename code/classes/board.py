# from car import car


class Board(object):
    """
    Representation of the board in Rush Hour.
    """

    def __init__(self, size, coordinates):
        """
        Define grid and create a list for cars
        """
        self.size = size
        self.coordinates = coordinates

    def __str__(self):
        coords = []
        for point in self.coordinates:
            coords.append(self.coordinates[point])

        output = ''
        x = 1
        for i in range(len(coords)):
            if i == (len(coords) - 1):
                output += "  ".join(coords[i])
                break

            if coords[i - 1] == '#':
                output += '\n'

            output += "  ".join(coords[i])
            x += 1
            if x == self.size:
                if coords[i + 1] == '#':
                    x = 0
                    continue
                else:
                    output += '\n'
                    x = 1
        return output