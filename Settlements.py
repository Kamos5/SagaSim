import Enums
import SettlementNameGenerator as SNG
import Parameters


class Settlements:

    def __init__(self, region, year=Parameters.startingYear, rebuildFlag = False):
        self.settlementType = Enums.Settlements.VILLAGE

        if region == "Region 0":
            self.name = SNG.randomEnglishSettlementsName(rebuildFlag)
        elif region == "Region 1":
            self.name = SNG.randomEnglishSettlementsName(rebuildFlag)
        elif region == "Region 2":
            self.name = SNG.randomEnglishSettlementsName(rebuildFlag)
        elif region == "Region 3":
            self.name = SNG.randomEnglishSettlementsName(rebuildFlag)
        elif region == "Region 4":
            self.name = SNG.randomEnglishSettlementsName(rebuildFlag)
        else:
            self.name = SNG.randomEnglishSettlementsName(rebuildFlag)

        self.region = ''
        self.population = 0
        self.foundedIn = year
        self.baseFertility = Parameters.baseVillageFertility
        self.fertilityModifier = 0
        self.foodTiles = 0
        self.prodTiles = 0
        self.residents = []
        self.features = []
        self.providesTo = None
        self.providedFrom = []
        self.maxPopulation = 0
        self.uiExpand = False

    def getUIExpand(self):
        return self.uiExpand

    def setUIExpand(self, newValue):
        self.uiExpand = newValue

    def getPopulation(self):
        return self.population

    def increasePopulation(self):
        self.population += 1
        self.adjustFertilityModifier()

    def decreasePopulation(self):
        self.population -= 1
        self.adjustFertilityModifier()

    def getMaxPopulation(self):
        return self.maxPopulation

    def setMaxPopulation(self, newMax):
        self.maxPopulation = newMax

    def getBaseFertility(self):
        return self.baseFertility

    def setBaseFertility(self, newFertility):
        self.baseFertility = newFertility

    def getFeatures(self):
        return self.features

    def addFeature(self, feature):
        self.features.append(feature)

    def getFertilityModifier(self):
        return self.fertilityModifier
    def setFertilityModifier(self, modifier):
        self.fertilityModifier = modifier

    def adjustFertilityModifier(self):
        if self.getPopulation() >= self.maxPopulation:
            self.setFertilityModifier(0.5)
        elif self.getPopulation() <= int(self.maxPopulation * 0.5):
            self.setFertilityModifier(1.2)
        else:
            self.setFertilityModifier(1)

    def changeSettlementName(self, newName):
        self.name = newName

    def getSettlementName(self):
        return self.name

    def getSettlementType(self):
        return self.settlementType
    def changeSettlementType(self, newType):
        self.settlementType = newType
        if newType == Enums.Settlements.VILLAGE:
            self.setBaseFertility(Parameters.baseVillageFertility)
            self.maxPopulation = Parameters.baseVillageSize
            self.recalculatePopWithFeatures()
            self.foodTiles = 7
            self.prodTiles = 1
        else:
            self.setBaseFertility(Parameters.baseCityFertility)
            self.maxPopulation = Parameters.baseCitySize
            self.recalculatePopWithFeatures()
            self.foodTiles = 8
            self.prodTiles = 16

    def getFounedIn(self):
        return self.foundedIn
    def getResidents (self):
        return self.residents
    def addResident (self, person):
        self.residents.append(person)
    def removeResident(self, person):
        self.residents.remove(person)

    def recalculatePopWithFeatures(self):
        for feature in self.features:
            self.maxPopulation += feature.value[0]

    def getUniqueFamilies(self):
        uniqueFamilies = []
        for resident in self.residents:
            if resident.lastName not in uniqueFamilies:
                uniqueFamilies.append(resident.lastName)

        return uniqueFamilies

    def getProvision(self):
        return self.providesTo

    def setProvision(self, newSettlement):
        self.providesTo = newSettlement