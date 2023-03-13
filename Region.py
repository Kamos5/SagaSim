import Enums
import Utils
from Settlements import Settlements
import Parameters

class Region():

    def __init__(self, regionName):
        self.regionName = regionName
        self.settlements = []
        self.regionSize = Parameters.regionSizeMax
        self.activeSettlements = 0
        self.regionCulture = ''
        self.uiExpand = True
        self.weather = Enums.weatherStatus.NORMAL
        self.daysSinceLastWeatherChange = 0
        self.events = []
        self.weatherHistory = []

    def getUIExpand(self):
        return self.uiExpand

    def setUIExpand(self, newValue):
        self.uiExpand = newValue

    def canAddSettlement(self):
        if len(self.getSettlements()) < self.regionSize:
            return True
        else:
            return False

    def getWeather(self):
        return self.weather

    def setWeather(self, newWeater):
        self.weatherHistory.append(newWeater.value[1])
        self.weather = newWeater

    def getTowns(self):

        townList =[]
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

    def addInitSettlement(self, world):
        newSettlement = Settlements(self.regionName, world.getYear())
        self.settlements.append(newSettlement)
        newSettlement.maxPopulation = Parameters.baseVillageSize

        return newSettlement

    def addSettlement(self, world):
        newSettlement = Settlements(self.regionName, world.getYear())
        self.settlements.append(newSettlement)
        newSettlement.maxPopulation = Parameters.baseVillageSize
        newSettlement.setProvision(Utils.randomFromCollection(self.getTowns()))

        return newSettlement

    def getSettlementFromIndex(self, index):
        return self.settlements[index]

    def getRegionName(self):
        return self.regionName

    def getSettlements(self):
        return self.settlements

    def setDaysSinceWeatherChangeCounter(self, days):
        self.daysSinceLastWeatherChange = days

    def increaseDaysSinceWeatherChangeCounter(self):
        self.daysSinceLastWeatherChange += 1

    def decreaseDaysSinceWeatherChangeCounter(self):

        if self.daysSinceLastWeatherChange > 0:
            self.daysSinceLastWeatherChange -= 1

    def getDaysSinceWeatherChange(self):
        return self.daysSinceLastWeatherChange

    def resetDaysSinceWeatherChange(self):
        self.daysSinceLastWeatherChange = 0

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

    def getWeatherHistory(self):
        return self.weatherHistory

    def getEvent(self):
        return self.events