from Enums import LifeStatus, Settlements
from Region import Region
import RegionNameGenerator as RNG
import Parameters

class World:

    initYear = Parameters.startingYear
    regions = []
    settlementsInitNumber = Parameters.startingSettlementsPerRegion


    def __init__(self, startYear=initYear):

        self.initYear = startYear
        self.year = self.initYear
        self.regions = []
        self.gameSpeed = 50
        self.families = []
        self.people = []

    def getPeople(self):
        return self.people

    def setPeople(self, people):
        self.people = people

    def addPerson(self, person):
        self.people.append(person)

    def removePeople(self, person):
        self.people.remove(person)

    def getFamilies(self):
        return self.families

    def setFamilies(self, families):
        self.families = families

    def addFamily(self, newFamily):
        self.families.append(newFamily)

    def removeFamily(self, family):
        self.families.remove(family)

    def getGameSpeed(self):
        return self.gameSpeed

    def setGameSpeed(self, newSpeed):
        self.gameSpeed = newSpeed

    def getYear(self):
        return self.year

    def increaseYear(self):
        self.year += 1

    def getCiTySize(self):
        return Parameters.baseCitySize

    def getVillageSize(self):
        return Parameters.baseVillageSize

    def generateRegions(self, regionsNumber = 5):

        for region in range(regionsNumber):
            self.regions.append(Region(RNG.randomEnglishRegionName()))

    def generateSettlements(self):

        for region in self.regions:
            for i in range(self.settlementsInitNumber):
                newSettlement = region.addSettlement(self)
                # First settlement is always TOWN
                if i == 0:
                    newSettlement.changeSettlementType(Settlements.TOWN)
                else:
                    newSettlement.changeSettlementType(Settlements.VILLAGE)

    def getRegionFromIndex(self, index):
        return self.regions[index]

    def getRegions(self):
        return self.regions