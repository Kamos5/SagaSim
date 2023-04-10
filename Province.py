import Utils


class Province:

    def __init__(self, worldMap):

        self.name = ''
        self.color = (0, 0, 0)
        self.borderColor = (0, 0, 0)
        self.cords = set()
        self.middleCords = (0, 0)
        self.setRandomColor()
        self.neighbours = set()
        self.provinceType = 'TERRAIN'
        self.region = None
        self.innerCords = set()     #(x,y,cordType (inner 0 /outer 1-8))
        self.outerCords = set()    #0 (inner); 1 (border LEFT); 2 (RIGHT); 3 (UP); 4(DOWN); 5(LEFT+RIGHT) 6(UP+DOWN); 7 (LEFT+UP); 8(RIGHT+UP); 9 (LEFT+DOWN); 10 (RIGHT+DOWN); 11 (LEFT+RIGHT+UP); 12 (LEFT+RIGHT+DOWN); 13 (RIGHT+UP+DOWN); 14 (LEFT+UP+DOWN); 15 (LEFT+RIGHT+UP+DOWN)
        self.isIsland = False
        self.worldMap = worldMap

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setRandomColor(self):

        r = Utils.randomRange(50, 150)
        g = Utils.randomRange(50, 150)
        b = Utils.randomRange(50, 150)
        self.color = (r, g, b)

    def setColor(self, color):
        self.color = color

    def addCords(self, x, y):
        self.cords.add((x, y))

    def getCords(self):
        return self.cords

    def getColor(self):
        return self.color

    def getMiddleCords(self):
        return self.middleCords

    def setMiddleCord(self):
        mean0 = sum(elt[0] for elt in self.getCords()) // len(self.getCords())
        mean1 = sum(elt[1] for elt in self.getCords()) // len(self.getCords())
        self.middleCords = (mean0, mean1)

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

    def addOuterCords(self, cords):
        self.outerCords.add(cords)

    def getOuterCords(self):
        return self.outerCords

    def markInnerCords(self):

        for cordX, cordY in self.getCords():

            right = (cordX + 1, cordY)
            left = (cordX - 1, cordY)
            up = (cordX, cordY - 1)
            down = (cordX, cordY + 1)

            if right in self.getCords() and left in self.getCords() and up in self.getCords() and down in self.getCords():
                self.addInnerCords((cordX, cordY, 0))

            else:
                if right in self.getCords() and left not in self.getCords() and up in self.getCords() and down in self.getCords():
                    self.addOuterCords((cordX, cordY, 8))  # ONLY LEFT BORDER # LEFT   1000 dec 8
                elif right not in self.getCords() and left in self.getCords() and up in self.getCords() and down in self.getCords():
                    self.addOuterCords((cordX, cordY, 4))  # ONLY RIGHT BORDER # RIGHT 0100 dec 4
                elif right in self.getCords() and left in self.getCords() and up not in self.getCords() and down in self.getCords():
                    self.addOuterCords((cordX, cordY, 2))  # ONLY UP BORDER # UP 0010 dec 2
                elif right in self.getCords() and left in self.getCords() and up in self.getCords() and down not in self.getCords():
                    self.addOuterCords((cordX, cordY, 1))  # ONLY DOWN BORDER # DOWN 0001 dec 1
                elif right not in self.getCords() and left not in self.getCords() and up in self.getCords() and down in self.getCords():
                    self.addOuterCords((cordX, cordY, 12))  # ONLY LEFT+RIGHT BORDER  # LEFT+RIGHT 1100 dec 12
                elif right in self.getCords() and left in self.getCords() and up not in self.getCords() and down not in self.getCords():
                    self.addOuterCords((cordX, cordY, 3))  # ONLY UP+DOWN BORDER # UP+DOWN 0011 dec 3
                elif right in self.getCords() and left not in self.getCords() and up not in self.getCords() and down in self.getCords():
                    self.addOuterCords((cordX, cordY, 10))  # ONLY LEFT+UP BORDER # LEFT+UP 1010 dec 10
                elif right not in self.getCords() and left in self.getCords() and up not in self.getCords() and down in self.getCords():
                    self.addOuterCords((cordX, cordY, 6))  # ONLY RIGHT+UP BORDER # RIGHT+UP 0110 dec 6
                elif right in self.getCords() and left not in self.getCords() and up in self.getCords() and down not in self.getCords():
                    self.addOuterCords((cordX, cordY, 9))  # ONLY LEFT+DOWN BORDER # LEFT+DOWN 1001 dec 9
                elif right not in self.getCords() and left in self.getCords() and up in self.getCords() and down not in self.getCords():
                    self.addOuterCords((cordX, cordY, 5))  # ONLY RIGHT+DOWN BORDER # RIGHT+DOWN 0101 dec 5
                elif right not in self.getCords() and left not in self.getCords() and up not in self.getCords() and down in self.getCords():
                    self.addOuterCords((cordX, cordY, 14))  # ONLY LEFT+RIGHT+UP BORDER # LEFT+RIGHT+UP 1110 dec 14
                elif right not in self.getCords() and left not in self.getCords() and up in self.getCords() and down not in self.getCords():
                    self.addOuterCords((cordX, cordY, 13))  # ONLY LEFT+RIGHT+DOWN BORDER # LEFT+RIGHT+DOWN 1101 dec 13
                elif right not in self.getCords() and left in self.getCords() and up not in self.getCords() and down not in self.getCords():
                    self.addOuterCords((cordX, cordY, 7))  # ONLY RIGHT+UP+DOWN BORDER # RIGHT+UP+DOWN 0111 dec 7
                elif right in self.getCords() and left not in self.getCords() and up not in self.getCords() and down not in self.getCords():
                    self.addOuterCords((cordX, cordY, 11))  # ONLY LEFT+UP+DOWN BORDER  # LEFT+UP+DOWN 1011 dec 11
                elif right not in self.getCords() and left not in self.getCords() and up not in self.getCords() and down not in self.getCords():
                    self.addOuterCords((cordX, cordY, 15))  # ONLY LEFT+RIGHT+UP+DOWN BORDER   # RIGHT+LEFT+UP+DOWN 1111 dec 15


    def checkIfIsland(self):

        isIsland = True
        for neighbour in self.getNeighbours():
            if not neighbour.getType() == 'SEA':
                isIsland = False

        self.isIsland = isIsland
