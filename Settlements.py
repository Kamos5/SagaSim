import Enums
import SettlementNameGenerator as SNG
from Utils import randomFromCollection
import Parameters


class Settlements:

    def __init__(self, region, rebuildFlag = False):
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
        self.baseFertility = Parameters.baseVillageFertility
        self.fertilityModifier = 0
        self.residents = []
        self.features = []
        self.maxPopulation = 0

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

    def addFeature(self, feature):
        self.features.append(feature)

    def getFertilityModifier(self):
        return self.fertilityModifier
    def setFertilityModifier(self, modifier):
        self.fertilityModifier = modifier

    def adjustFertilityModifier(self):
        if self.getPopulation() >= self.maxPopulation:
            self.setFertilityModifier(0.25)
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
        else:
            self.setBaseFertility(Parameters.baseCityFertility)
            self.maxPopulation = Parameters.baseCitySize
            self.recalculatePopWithFeatures()

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
