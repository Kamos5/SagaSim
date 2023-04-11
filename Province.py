import Enums
import Parameters
import Utils
from Settlements import Settlements
from WorldMapObjClass import WorldMapObjClass


class Province:

    def __init__(self, worldMap):

        self.settlements = []
        self.provinceSize = Parameters.provinceSizeMax
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
        self.cordsUsed = set()

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

    def getCordsUsed(self):
        return self.cordsUsed

    def setCordsUsed(self, cords):
        self.cordsUsed = cords

    def addCordsUsed(self, newCords):
        self.cordsUsed.add(newCords)

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

    def getSettlementFromIndex(self, index):
        return self.settlements[index]

    def getSettlements(self):
        return self.settlements

    def addSettlement(self, world):
        newSettlement = Settlements(self.getRegion().getRegionNumber(), world.getYear())
        newSettlement.setRegion(self.getRegion())
        newSettlement.setProvince(self)
        notClear = True
        secVar = 0
        settlementCord = (0, 0, 0)
        while notClear:
            settlementCord = Utils.randomFromCollection(list(newSettlement.getProvince().getInnerCords()))
            if settlementCord not in newSettlement.getProvince().getCordsUsed():
                notClear = False
            secVar += 1
            if secVar > 100:
                return None
        newSettlement.getProvince().addCordsUsed(settlementCord)
        newSettlement.getProvince().addCordsUsed((settlementCord[0] - 1, settlementCord[1], settlementCord[2]))
        newSettlement.getProvince().addCordsUsed((settlementCord[0] + 1, settlementCord[1], settlementCord[2]))
        newSettlement.getProvince().addCordsUsed((settlementCord[0], settlementCord[1] - 1, settlementCord[2]))
        newSettlement.getProvince().addCordsUsed((settlementCord[0], settlementCord[1] + 1, settlementCord[2]))
        newSettlement.setProvinceCords(settlementCord)
        worldMapObjClass = WorldMapObjClass(colors=(newSettlement.getRegion().getRegionColor(), newSettlement.getProvince().getColor()), cords=(settlementCord[0], settlementCord[1]), objectVar=newSettlement, isInner=False)
        world.getWorldMap().addField(worldMapObjClass, weight=2)

        self.settlements.append(newSettlement)
        newSettlement.maxPopulation = Parameters.baseVillageSize
        # newSettlement.setProvision(Utils.randomFromCollection(self.getTowns()))

        return newSettlement

    def canAddSettlement(self):
        if len(self.getSettlements()) < self.provinceSize:
            return True
        else:
            return False

    def addInitSettlement(self, world, region):
        newSettlement = Settlements(region.getRegionNumber(), world.getYear())
        self.settlements.append(newSettlement)
        newSettlement.maxPopulation = Parameters.baseVillageSize

        return newSettlement

    def getTowns(self):

        townList = []
        for settlement in self.getSettlements():
            if settlement.getSettlementType() == Enums.Settlements.TOWN:
                townList.append(settlement)

        return townList

    def getVillages(self):

        villageList = []
        for settlement in self.getSettlements():
            if settlement.getSettlementType() == Enums.Settlements.VILLAGE:
                villageList.append(settlement)

        return villageList

    def getVillagesExProvisionToThisTown(self, town):

        villageList = []
        for settlement in self.getSettlements():
            if settlement.getSettlementType() == Enums.Settlements.VILLAGE and settlement.getProvision() is not town:
                villageList.append(settlement)

        return villageList

    def getLowestPopulatedSettlement(self):

        tempMinPopVal = 1000000
        lowestPopSettlement = None
        index = 0
        for settlement in self.getSettlements():
            if len(settlement.getResidents()) < tempMinPopVal:
                tempMinPopVal = len(settlement.getResidents())
                lowestPopSettlement = settlement
            index += 1
        return lowestPopSettlement


    def getActiveSettlements(self):
        return self.activeSettlements
    def increaseActiveSettlements(self):
        self.activeSettlements += 1
    def decreaseActiveSettlements(self):
        self.activeSettlements -= 1
    def setActiveSettlements(self, newActiveSettlements):
        self.activeSettlements = newActiveSettlements