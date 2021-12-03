from Settlements import Settlements

class Region:

    def __init__(self, regionName):
        self.regionName = regionName
        self.settlements = []
        self.regionSize = 10
        self.activeSettlements = 0
        self.regionCulture = ''


    def canAddSettlement(self):
        if len(self.getSettlements()) < self.regionSize:
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
    def getLowestPopulatedSettlement(self, world):


        settlementsPopulationList = []
        tempMinPopVal = 10000
        tempIndexPopVal = 0
        index = 0
        for settlement in self.settlements:
            settlementsPopulationList.append(settlement.getResidents())
            if len(settlement.getResidents()) < tempMinPopVal:
                tempMinPopVal = len(settlement.getResidents())
                tempIndexPopVal = index
            index += 1
        return self.settlements[tempIndexPopVal]
