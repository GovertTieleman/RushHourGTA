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

    def board_string(self):
        # create list of coordinates
        coordinateslist = []
        for coordinate in self.coordinates:
            coordinateslist.append(self.coordinates[coordinate])

        # initiate output
        output = ''
        x = 1

        for i in range(len(coordinateslist)):
            if i == (len(coordinateslist) - 1):
                output += "  ".join(coordinateslist[i])
                break

            if coordinateslist[i - 1] == '#':
                output += '\n'

            output += "  ".join(coordinateslist[i])
            x += 1
            if x == self.size:
                if coordinateslist[i + 1] == '#':
                    x = 0
                    continue
                else:
                    output += '\n'
                    x = 1
        return output
