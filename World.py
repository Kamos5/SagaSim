from Enums import LifeStatus, Settlements
from Region import Region
import Parameters

class World:

    initYear = 500
    regions = []
    settlementsInitNumber = 2 # max 20


    def __init__(self, startYear=initYear):

        self.initYear = startYear
        self.year = self.initYear
        self.regions = []

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
            self.regions.append(Region("Region " + str(region)))

    def generateSettlements(self):

        for region in self.regions:
            for i in range(self.settlementsInitNumber):
                newSettlement = region.addSettlement()
                # First settlement is always TOWN
                if i == 0:
                    newSettlement.changeSettlementType(Settlements.TOWN)
                else:
                    newSettlement.changeSettlementType(Settlements.VILLAGE)

    def getRegionFromIndex(self, index):
        return self.regions[index]

    def getRegions(self):
        return self.regions