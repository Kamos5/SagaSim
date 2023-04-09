import Enums
import Utils
from Settlements import Settlements
import Parameters
from WorldMapObjClass import WorldMapObjClass


class Region():

    def __init__(self, regionName):
        self.regionNumber = 0
        self.regionName = regionName
        self.settlements = []
        self.regionSize = Parameters.regionSizeMax
        self.activeSettlements = 0
        self.regionCulture = ''
        self.regionColor = (0, 0, 0)
        self.regionStartingCords = (0, 0)
        self.regionTerritories = set()
        self.uiExpand = True
        self.weather = Enums.weatherStatus.NORMAL
        self.daysSinceLastWeatherChange = 0
        self.events = []
        self.weatherHistory = []
        self.currentTemperature = 0
        self.temperatureHistory = []
        self.provinces = []
        self.provincesInnerCords = (0, 0)
        self.outerProvincesBorders = set()

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

    def getRegionNumber(self):
        return self.regionNumber

    def setRegionNumber(self, number):
        self.regionNumber = number

    def setWeather(self, newWeater):
        self.weatherHistory.append(newWeater.value[1])
        self.weather = newWeater

    def setRegionColor(self, color):
        self.regionColor = color

    def getRegionColor(self):
        return self.regionColor

    def setStartingCords(self, cords):
        self.startingCords = cords

    def getStartingCords(self):
        return self.startingCords

    def getRegionTerritories(self):
        return self.regionTerritories

    def addRegionTerritory(self, region):
        if len(region) > 0:
            self.regionTerritories.add(region)

    def removeRegionTerritory(self, removeRegion):
        self.regionTerritories.remove(removeRegion)

    def getTowns(self):

        townList = []
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
        newSettlement = Settlements(self.regionNumber, world.getYear())
        self.settlements.append(newSettlement)
        newSettlement.maxPopulation = Parameters.baseVillageSize

        return newSettlement

    def addSettlement(self, world):
        newSettlement = Settlements(self.regionNumber, world.getYear())
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

    def getCurrentTemperature(self):
        return self.currentTemperature

    def setCurrentTemperature(self, newTemp):
        self.currentTemperature = newTemp
        self.addendTemperatureHistory(newTemp)

    def getTemperatureHistory(self):
        return self.temperatureHistory

    def addendTemperatureHistory(self, temp):
        self.temperatureHistory.append(temp)

    def addProvince(self, province):
        self.provinces.append(province)

    def getProvinces(self):
        return self.provinces

    def removeProvince(self, province):
        self.provinces.remove(province)

    def getCordTypeBit(self, type, bitNumber):

        typeBit = list(format(type, 'b'))
        if len(typeBit) == 1:
            typeBit.insert(0, '0')
        if len(typeBit) == 2:
            typeBit.insert(0, '0')
        if len(typeBit) == 3:
            typeBit.insert(0, '0')
        return typeBit[bitNumber]


    def changeCordTypeBit(self, type, bitNumber):

        typeBit = list(format(type, 'b'))
        if len(typeBit) == 1:
            typeBit.insert(0, '0')
        if len(typeBit) == 2:
            typeBit.insert(0, '0')
        if len(typeBit) == 3:
            typeBit.insert(0, '0')

        if typeBit[bitNumber] == '1':
            typeBit[bitNumber] = '0'

        s = [str(integer) for integer in typeBit]
        a_string = "".join(s)

        res = int(a_string, 2)

        return res

    def mergeTypes(self, typeProvince, typeProvince2, mode=0):
        if mode == 0:
            return typeProvince & typeProvince2
        elif mode == 1:
            return typeProvince | typeProvince2
        elif mode == 2:
            return typeProvince ^ typeProvince2


    def generateRegionalProvincesMap(self, world):

        outerTempProvinceBorders = set()
        outerProvincesBordersDict = {}


        for province in self.getProvinces():

            for outerProvinceCord in province.getOuterCords():
                outerTempProvinceBorders.add((outerProvinceCord, province))
                # worldMapObjClass = WorldMapObjClass(colors=(self.getRegionColor(), province.getColor()), cords=(outerProvinceCord[0], outerProvinceCord[1]), objectVar=province, isInner=False, outerType=outerProvinceCord[2])
                # world.getWorldMap().addField(worldMapObjClass, weight=1)
        # print(len(outerTempProvinceBorders))
        cordsUsed = set()
        for cords, province in outerTempProvinceBorders:
            cordsX, cordsY, cordsT = cords
            for cords2, province2 in outerTempProvinceBorders.difference((cords, province)):
                if cords != cords2 and (cords, cords2) not in cordsUsed:

                    cords2X, cords2Y, cords2T = cords2
                    if cordsX + 1 == cords2X and cordsY == cords2Y and self.getCordTypeBit(cordsT, 1) == self.getCordTypeBit(cords2T, 0) == '1':

                        if (cordsX, cordsY) not in outerProvincesBordersDict:
                            outerProvincesBordersDict[(cordsX, cordsY)] = (self.changeCordTypeBit(cordsT, 1), province, (cordsX, cordsY))
                        else:
                            dictType, dictProvince, dictCords = outerProvincesBordersDict[(cordsX, cordsY)]
                            mergedType = self.mergeTypes(self.changeCordTypeBit(cordsT, 1), dictType)
                            outerProvincesBordersDict.pop((cordsX, cordsY))
                            outerProvincesBordersDict[(cordsX, cordsY)] = (mergedType, dictProvince, (cordsX, cordsY))

                        if (cords2X, cords2Y) not in outerProvincesBordersDict:
                            outerProvincesBordersDict[(cords2X, cords2Y)] = (self.changeCordTypeBit(cords2T, 0), province2, (cords2X, cords2Y))
                        else:
                            dictType, dictProvince, dictCords = outerProvincesBordersDict[(cords2X, cords2Y)]
                            mergedType = self.mergeTypes(self.changeCordTypeBit(cords2T, 0), dictType)
                            outerProvincesBordersDict.pop((cords2X, cords2Y))
                            outerProvincesBordersDict[(cords2X, cords2Y)] = (mergedType, dictProvince, (cords2X, cords2Y))


                    elif cordsX - 1 == cords2X and cordsY == cords2Y and self.getCordTypeBit(cordsT, 0) == self.getCordTypeBit(cords2T, 1) == '1':

                        if (cordsX, cordsY) not in outerProvincesBordersDict:
                            outerProvincesBordersDict[(cordsX, cordsY)] = (self.changeCordTypeBit(cordsT, 0), province, (cordsX, cordsY))
                        else:
                            dictType, dictProvince, dictCords = outerProvincesBordersDict[(cordsX, cordsY)]
                            mergedType = self.mergeTypes(self.changeCordTypeBit(cordsT, 0), dictType)
                            outerProvincesBordersDict.pop((cordsX, cordsY))
                            outerProvincesBordersDict[(cordsX, cordsY)] = (mergedType, dictProvince, (cordsX, cordsY))

                        if (cords2X, cords2Y) not in outerProvincesBordersDict:
                            outerProvincesBordersDict[(cords2X, cords2Y)] = (self.changeCordTypeBit(cords2T, 1), province2, (cords2X, cords2Y))
                        else:
                            dictType, dictProvince, dictCords = outerProvincesBordersDict[(cords2X, cords2Y)]
                            mergedType = self.mergeTypes(self.changeCordTypeBit(cords2T, 1), dictType)
                            outerProvincesBordersDict.pop((cords2X, cords2Y))
                            outerProvincesBordersDict[(cords2X, cords2Y)] = (mergedType, dictProvince, (cords2X, cords2Y))

                    elif cordsY + 1 == cords2Y and cordsX == cords2X and self.getCordTypeBit(cordsT, 3) == self.getCordTypeBit(cords2T, 2) == '1':

                        if (cordsX, cordsY) not in outerProvincesBordersDict:
                            outerProvincesBordersDict[(cordsX, cordsY)] = (self.changeCordTypeBit(cordsT, 3), province, (cordsX, cordsY))
                        else:
                            dictType, dictProvince, dictCords = outerProvincesBordersDict[(cordsX, cordsY)]
                            mergedType = self.mergeTypes(self.changeCordTypeBit(cordsT, 3), dictType)
                            outerProvincesBordersDict.pop((cordsX, cordsY))
                            outerProvincesBordersDict[(cordsX, cordsY)] = (mergedType, dictProvince, (cordsX, cordsY))

                        if (cords2X, cords2Y) not in outerProvincesBordersDict:
                            outerProvincesBordersDict[(cords2X, cords2Y)] = (self.changeCordTypeBit(cords2T, 2), province2, (cords2X, cords2Y))
                        else:
                            dictType, dictProvince, dictCords = outerProvincesBordersDict[(cords2X, cords2Y)]
                            mergedType = self.mergeTypes(self.changeCordTypeBit(cords2T, 2), dictType)
                            outerProvincesBordersDict.pop((cords2X, cords2Y))
                            outerProvincesBordersDict[(cords2X, cords2Y)] = (mergedType, dictProvince, (cords2X, cords2Y))


                    elif cordsY - 1 == cords2Y and cordsX == cords2X and self.getCordTypeBit(cordsT, 2) == self.getCordTypeBit(cords2T, 3) == '1':

                        if (cordsX, cordsY) not in outerProvincesBordersDict:
                            outerProvincesBordersDict[(cordsX, cordsY)] = (self.changeCordTypeBit(cordsT, 2), province, (cordsX, cordsY))
                        else:
                            dictType, dictProvince, dictCords = outerProvincesBordersDict[(cordsX, cordsY)]
                            mergedType = self.mergeTypes(self.changeCordTypeBit(cordsT, 2), dictType)
                            outerProvincesBordersDict.pop((cordsX, cordsY))
                            outerProvincesBordersDict[(cordsX, cordsY)] = (mergedType, dictProvince, (cordsX, cordsY))

                        if (cords2X, cords2Y) not in outerProvincesBordersDict:
                            outerProvincesBordersDict[(cords2X, cords2Y)] = (self.changeCordTypeBit(cords2T, 3), province2, (cords2X, cords2Y))
                        else:
                            dictType, dictProvince, dictCords = outerProvincesBordersDict[(cords2X, cords2Y)]
                            mergedType = self.mergeTypes(self.changeCordTypeBit(cords2T, 3), dictType)
                            outerProvincesBordersDict.pop((cords2X, cords2Y))
                            outerProvincesBordersDict[(cords2X, cords2Y)] = (mergedType, dictProvince, (cords2X, cords2Y))


                    else:
                        if (cordsX, cordsY) not in outerProvincesBordersDict:
                            outerProvincesBordersDict[(cordsX, cordsY)] = (cordsT, province, (cordsX, cordsY))
                        else:
                            dictType, dictProvince, dictCords = outerProvincesBordersDict[(cordsX, cordsY)]
                            mergedType = self.mergeTypes(cordsT, dictType)
                            outerProvincesBordersDict[(cordsX, cordsY)] = (mergedType, province, (cordsX, cordsY))

                    cordsUsed.add((cords, cords2))
        zeroCount = 0
        for key, element in outerProvincesBordersDict.items():
            cordsT, province, cords = element
            cordsX, cordsY = cords

            if cordsT != 0:
                self.outerProvincesBorders.add(((cordsX, cordsY, cordsT), province))
                worldMapObjClass = WorldMapObjClass(colors=(self.getRegionColor(), province.getColor()), cords=(cordsX, cordsY), objectVar=province, isInner=False, outerType=cordsT)
                world.getWorldMap().addField(worldMapObjClass, weight=1)
            else:
                zeroCount +=1
        # print(f'Cords used: {len(cordsUsed)}')
        # print(f'Outer provinces: {len(self.outerProvincesBorders)}')
        # #print(self.outerProvincesBorders)
        # print(f'Zero count: {zeroCount}')
        # print(f'DIF : {len(outerTempProvinceBorders)-len(self.outerProvincesBorders)}')
    def getMiddleCords(self):
        return self.provincesInnerCords

    def caltulateMiddleCords(self, provinceInnerCordsList):

        mean0 = sum(elt[0] for elt in provinceInnerCordsList) // len(provinceInnerCordsList)
        mean1 = sum(elt[1] for elt in provinceInnerCordsList) // len(provinceInnerCordsList)
        self.provincesInnerCords = (mean0, mean1)
