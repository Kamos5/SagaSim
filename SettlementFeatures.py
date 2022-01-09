from enum import Enum

class FeatureType():

    def __init__(self, name, description):
        self.name = name
        self.description = description


class FundationType():

    def __init__(self, name, description, yieldModifier):
        self.name = name
        self.description = description
        self.yieldModifier = yieldModifier

class FundationEnums(Enum):

    poorSoil = FundationType("Poor Soil", "Soil here is very poor.", 80)
    goodSoil = FundationType("Good Soil", "Soil here is quite good.", 100)
    richSoil = FundationType("Rich Soil", "Soil here is very enriched.", 120)
    pollutedWater = FundationType("Polluted Water", "This water is polluted and is regarded as low quality", 80)
    cleanWater = FundationType("Clean Water", "This water source is clean and regarded as good quality", 100)
    pureWater = FundationType("Purified Water", "This water is very clean and naturally filtered from impurities", 120)

class Feature():

    def __init__(self, prodYield=0, maxWorkers=0, desc='', upgrCost=0, upgrTo=None):
        self.prodYield = prodYield
        self.workers = 0
        self.maxWorkers = maxWorkers
        self.foundationType = None
        self.description = desc
        self.upgradeCost = upgrCost
        self.upgradesTo = upgrTo

    def setType(self, newType):
        self.foundationType = newType

class FoodZones(Enum):

    #production yield, description, upgr cost, upgrades to
    SIMPLEFARM = Feature(2, 10, 'simple farm', 40, None)
    FALLOW = Feature(0, 0, 'fallow land', 20, SIMPLEFARM)

    RIVER = Feature()

    #bonus to max pop, description
    FARMS = 20, 'farms'
    RICHSOIL = 100, 'rich soil',
    RIVER = 50, 'river'
    FISHSCHOOLS = 50, 'school of fish'
    ORCHARD = 50, 'oarchard'
    SILO = 25, 'silo'
    MILL = 25, 'mill'
    BARN = 25, 'barn'
    FOREST = 20, 'forest'
    BIGGAME = 20, 'big game'
    MEADOWBEES = 15, 'meadow bees'

class ProdZone(Enum):
    QUARRY = 10, 'quarry'
