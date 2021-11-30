import Enums
import SettlementNameGenerator as SNG
from Utils import randomFromCollection


class Settlements:

    def __init__(self, region):
        self.settlementType = Enums.Settlements.VILLAGE

        if region == "Region 0":
            self.name = SNG.randomEnglishSettlementsName()
        elif region == "Region 1":
            self.name = SNG.randomEnglishSettlementsName()
        elif region == "Region 2":
            self.name = SNG.randomEnglishSettlementsName()
        elif region == "Region 3":
            self.name = SNG.randomEnglishSettlementsName()
        elif region == "Region 4":
            self.name = SNG.randomEnglishSettlementsName()
        else:
            self.name = SNG.randomEnglishSettlementsName()

        self.region = ''
        self.population = 0


    def increasePopulation(self):
        self.population += 1
    def decreasePopulation(self):
        self.population -= 1

    def changeSettlementName(self, newName):
        self.name = newName

    def changeSettlementType(self, newType):
        self.settlementType = newType
