from Enums import LifeStatus,Settlements
from Region import Region

class World:

    initYear = 500
    regions = []
    settlementsInitNumber = 4 # max 20

    def __init__(self, startYear=initYear):
        self.initYear = startYear
        self.year = self.initYear
        self.regions = []

    def getYear(self):
        return self.year

    def increaseYear(self):
        self.year += 1

    def getAllAliveMembersNames(self, family, people):

        aliveMembersNames = []
        for person in people:
            if person in family.getAliveAllMembersUUIDs() and person.lifeStatus == LifeStatus.ALIVE:
                aliveMembersNames.append(person.firstName)
        return aliveMembersNames

    def generateRegions(self, regionsNumber = 5):

        for region in range(regionsNumber):
            self.regions.append(Region("Region " + str(region)))

    def generateSettlements(self):

        for region in self.regions:
            for i in range(self.settlementsInitNumber):
                region.addSettlement()
                # First settlement is always TOWN
                if i == 0:
                    region.settlements[0].changeSettlementType(Settlements.TOWN)


    def getRegionFromIndex(self, index):
        return self.regions[index]

    def getRegions(self):
        return self.regions