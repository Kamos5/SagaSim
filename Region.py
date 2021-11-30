from Settlements import Settlements

class Region:

    def __init__(self, regionName):
        self.regionName = regionName
        self.settlements = []
        self.regionSize = 1
        self.regionCulture = ''


    def addSettlement(self):
        self.settlements.append(Settlements(self.regionName))

    def getSettlementFromIndex(self, index):
        return self.settlements[index]