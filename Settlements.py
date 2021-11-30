import Enums
import NameGenerator as NG
from Utils import randomFromCollection


class Settlements:

    def __init__(self):
        self.settlementType = Enums.Settlements.VILLAGE
        self.name = NG.randomsettlementsVillageName()
        self.region = ''
        self.population = 0


    def increasePopulation(self):
        self.population += 1
    def decreasePopulation(self):
        self.population -= 1
