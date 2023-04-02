import Utils


class Province:

    def __init__(self, worldMap):

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
        self.worldMap = worldMap

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setRandomColor(self):

        r = Utils.randomRange(100, 200)
        g = Utils.randomRange(100, 200)
        b = Utils.randomRange(100, 200)
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

        minX = self.worldMap.x0
        maxX = self.worldMap.getWidth()
        minY = self.worldMap.y0
        maxY = self.worldMap.getHeight()

        for cordX, cordY in self.getCords():

            right = (cordX + 1, cordY)
            left = (cordX - 1, cordY)
            up = (cordX, cordY - 1)
            down = (cordX, cordY + 1)

            if (right in self.getCords() or cordX == maxX-1) and (left in self.getCords() or cordX == minX) and (up in self.getCords() or cordY == minY) and (down in self.getCords() or cordY == maxY - 1):
                self.addInnerCords((cordX, cordY))

    def checkIfIsland(self):

        isIsland = True
        for neighbour in self.getNeighbours():
            if not neighbour.getType() == 'SEA':
                isIsland = False

        self.isIsland = isIsland
