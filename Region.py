from Settlements import Settlements

class Region:

    def __init__(self, regionName):
        self.regionName = regionName
        self.settlements = []
        self.regionSize = 20
        self.activeSettlements = 0
        self.regionCulture = ''


    def canAddSettlement(self):
        if self.canAddSettlement():
            return True
        else:
            return False

    def addSettlement(self):
        self.settlements.append(Settlements(self.regionName))

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

    def getLowestPopulatedSettlement(self):

        settlementsPopulationList = []
        tempMinPopVal = 10000
        tempIndexPopVal = 0
        index = 0
        for settlement in self.settlements:
            settlementsPopulationList.append(settlement.getResidents())
            if len(settlement.getResidents()) < tempMinPopVal:
                tempIndexPopVal = index
            index += 1
        return self.settlements[tempIndexPopVal]
