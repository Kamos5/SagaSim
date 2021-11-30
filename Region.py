from Settlements import Settlements

class Region:

    def __init__(self, regionName):
        self.regionName = regionName
        self.settlements = []
        self.regionSize = 20
        self.activeSettlements = 0
        self.regionCulture = ''


    def addSettlement(self):
        if self.canAddSettlement():
            self.settlements.append(Settlements(self.regionName))
        else:
            return False

    def getSettlementFromIndex(self, index):
        return self.settlements[index]

    def getSettlements(self):
        return self.settlements

    def getActiveSettlements(self):
        return self.activeSettlements
    def increaseActiveSettlements(self):
        self.activeSettlements += 1
    def decreaseActiveSettlements(self):
        self.activeSettlements -= 1
    def setActiveSettlements(self, newActiveSettlements):
        self.activeSettlements = newActiveSettlements

    def canAddSettlement(self):
        return len(self.settlements) < self.regionSize

