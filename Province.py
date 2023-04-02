import Utils


class Province:

    def __init__(self):

        self.name = ''
        self.color = (0, 0, 0)
        self.borderColor = (0, 0, 0)
        self.cords = set()
        self.setRandomColor()
        self.neighbours = set()
        self.provinceType = 'TERRAIN'
        self.region = None
        self.innerCords = set()
        self.isIsland = False

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setRandomColor(self):

        r = Utils.randomRange(50, 220)
        g = Utils.randomRange(50, 220)
        b = Utils.randomRange(50, 220)
        self.color = (r, g, b)

    def setColor(self, color):
        self.color = color

    def addCords(self, x, y):
        self.cords.add((x, y))

    def getCords(self):
        return self.cords

    def getColor(self):
        return self.color

    def addNeighbour(self, newNeighbour):

        self.neighbours.add(newNeighbour)

    def getNeighbours(self):
        return self.neighbours

    def getType(self):
        return self.provinceType

    def setType(self, newType):
        self.provinceType = newType

    def setRegion(self, region):
        self.region = region

    def getRegion(self):
        return self.region

    def addInnerCords(self, cords):
        self.innerCords.add(cords)

    def getInnerCords(self):
        return self.innerCords

    def markInnerCords(self):

        for cordX, cordY in self.getCords():
            if (cordX+1, cordY) in self.getCords() and (cordX-1, cordY) in self.getCords() and (cordX, cordY+1) in self.getCords() and (cordX, cordY-1) in self.getCords():
                self.addInnerCords((cordX, cordY))

    def checkIfIsland(self):

        isIsland = True
        for neighbour in self.getNeighbours():
            if not neighbour.getType() == 'SEA':
                isIsland = False

        self.isIsland = isIsland
