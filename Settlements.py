import Enums
import SettlementNameGenerator as SNG
from Utils import randomFromCollection


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
        self.baseFertility = 80
        self.fertilityModifier = 0
        self.residents = []

    def getPopulation(self):
        return self.population

    def increasePopulation(self):
        self.population += 1
        self.adjustFertilityModifier()

    def decreasePopulation(self):
        self.population -= 1
        self.adjustFertilityModifier()

    def getBaseFertility(self):
        return self.baseFertility

    def setBaseFertility(self, newFertility):
        self.baseFertility = newFertility

    def getFertilityModifier(self):
        return self.fertilityModifier
    def setFertilityModifier(self, modifier):
        self.fertilityModifier = modifier

    def adjustFertilityModifier(self):
        if self.getSettlementType() == Enums.Settlements.TOWN and self.getPopulation() >= 1000:
            self.setFertilityModifier(0.5)
        elif self.getSettlementType() == Enums.Settlements.VILLAGE and self.getPopulation() >= 200:
            self.setFertilityModifier(0.5)
        else:
            self.setFertilityModifier(1)

    def changeSettlementName(self, newName):
        self.name = newName
    def getSettlementType(self):
        return self.settlementType
    def changeSettlementType(self, newType):
        self.settlementType = newType

    def getResidents (self):
        return self.residents
    def addResident (self, person):
        self.residents.append(person)
    def removeResident(self, person):
        self.residents.remove(person)
