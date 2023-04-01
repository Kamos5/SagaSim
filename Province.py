import Utils


class Provinve:

    def __init__(self):

        self.name = ''
        self.color = (0, 0, 0)
        self.cords = set()
        self.setRandomColor()

    def setRandomColor(self):

        r = Utils.randomRange(50, 255)
        g = Utils.randomRange(50, 255)
        b = Utils.randomRange(50, 255)
        self.color = (r, g, b)

    def addCords(self, x, y):
        self.cords.add((x, y))

    def getCords(self):
        return self.cords

    def getColor(self):
        return self.color