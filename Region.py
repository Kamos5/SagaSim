from Settlements import Settlements
from RegionFeatures import Features
import SettlementFeatures as SF
import Parameters
import Utils

class Region():

    def __init__(self, regionName):
        self.regionName = regionName
        self.settlements = []
        self.regionSize = 8
        self.activeSettlements = 0
        self.regionCulture = ''
        self.uiExpand = True

    def getUIExpand(self):
        return self.uiExpand

    def setUIExpand(self, newValue):
        self.uiExpand = newValue

    def canAddSettlement(self):
        if len(self.getSettlements()) < self.regionSize:
            return True
        else:
            return False

    def addSettlement(self, world):
        newSettlement = Settlements(self.regionName, world.getYear())
        self.settlements.append(newSettlement)
        newSettlement.maxPopulation = Parameters.baseVillageSize

        return newSettlement

    def getSettlementFromIndex(self, index):
        return self.settlements[index]

    def getRegionName(self):
        return self.regionName


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
