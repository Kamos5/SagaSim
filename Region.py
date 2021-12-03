from Settlements import Settlements
from RegionFeatures import Features
import Parameters
import Utils
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
        additionalFeatureThreshold = 10
        self.settlements.append(Settlements(self.regionName))
        newSettlement = self.settlements[len(self.getSettlements())-1]
        newSettlement.maxPopulation = Parameters.baseVillageSize
        randomNumberFeatures = Utils.randomRange(1, 100)
        newSettlement.addFeature([Utils.randomFromEnumCollection(Features)])
        while randomNumberFeatures > 90:
            randomNumberFeatures = Utils.randomRange(1, 100)
            newSettlement.addFeature([Utils.randomFromEnumCollection(Features)])
        newSettlement.recalculatePopWithFeatures()
        return newSettlement

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
