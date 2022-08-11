from enum import Enum

import Utils

features = []

class FeatureType():

    def __init__(self, name, description):
        self.name = name
        self.description = description


class FeatureTypes(Enum):

    FOODTYPE = FeatureType("Food type", "produces food resource")
    PRODTYPE = FeatureType("Production type", "produces production resource")

    # POORSOIL = FundationType("Poor Soil", "Soil here is very poor.", 80)
    # GOODSOIL = FundationType("Good Soil", "Soil here is quite good.", 100)
    # RICHSOIL = FundationType("Rich Soil", "Soil here is very enriched.", 120)
    #
    # POLLUTEDWATER = FundationType("Polluted Water", "This water is polluted and is regarded as low quality", 80)
    # CLEANWATER = FundationType("Clean Water", "This water source is clean and regarded as good quality", 100)
    # PUREWATER = FundationType("Purified Water", "This water is very clean and naturally filtered from impurities", 120)
    #
    # POORQUALITYROCK = FundationType("Poor Quality Rock Layer", "Rock layer underneath is poor", 80)
    # MEDIUMQUALITYROCK = FundationType("Medium Quality Rock Layer", "Rock layer underneath is normal", 100)
    # HIGHQUALITYROCK = FundationType("Rich Quality Rock Layer", "Rock layer underneath is dense", 120)


class Feature:

    def __init__(self, featureType=None, prodYield=0, maxWorkers=0, name='', desc='', occupationName='', upgrCost=0, upgrFrom=None, cordx=0, cordy=0, featureNumber=0):
        self.featureType = featureType
        self.prodYield = prodYield
        self.workers = 0
        self.workersList = []
        self.maxWorkers = maxWorkers
        self.foundationType = None
        self.occupationName = occupationName
        self.name = name
        self.description = desc
        self.upgradeCost = upgrCost
        self.upgrFrom = upgrFrom
        self.cordX = cordx
        self.cordY = cordy
        self.featureNumber = featureNumber
        self.uiExpand = False

    def setFoundationType(self, newType):
        self.foundationType = newType

    def getFeatureType(self):
        return self.featureType

    def getFoundationType(self):
        return self.foundationType

    def getUpgrFrom(self):
        return self.upgrFrom

    def getName(self):
        return self.name

    def getProdYield(self):
        return self.prodYield

    def getWorkersNumber(self):
        return self.workers

    def getMaxWorkersNumber(self):
        return self.maxWorkers

    def getFreeWorkersSlots(self):
        return self.maxWorkers - self.workers

    def getOccupationName(self):
        return self.occupationName

    def getWorkerList(self):
        return self.workersList

    def getWorkerListNumber(self):
        return len(self.workersList)

    def addWorker(self, worker):
        self.workers += 1
        self.workersList.append(worker)

    def removeWorker(self, worker):
        self.workers -= 1
        self.workersList.remove(worker)

    def getUpgradeCost(self):
        return self.upgradeCost

    def getCordX(self):
        return self.cordX

    def setCordX(self, newValue):
        self.cordX = newValue

    def getCordY(self):
        return self.cordY

    def setCordY(self, newValue):
        self.cordY = newValue

    def getFeatureNumber(self):
        return self.featureNumber

    def setFeatureNumber(self, number):
        self.featureNumber = number

    def getUIExpand(self):
        return self.uiExpand

    def changeExpandedUI(self):
        self.uiExpand = not self.uiExpand

    def setUIExpand(self, newValue):
        self.uiExpand = newValue
# def setFeatures():
#
#     #production yield, description, upgr cost, upgrades to
#     # TIER 0 (BASIC)
#     FALLOW = Feature(FeatureTypes.FOODTYPE, 10, 1, 'fallow farmer', 'Fallow', 'fallow land')
#     WILDERNESS = Feature(FeatureTypes.FOODTYPE, 10, 1, 'primitive gatherer', 'Wilderness', 'unpassable terrain')
#     RIVER = Feature(FeatureTypes.FOODTYPE, 4, 5, 'river fisher', 'River', 'running volume of not sparkling water')
#     SEASIDE = Feature(FeatureTypes.FOODTYPE, 3, 3, 'sea fisher', 'Sea side', 'running volume of not sparkling salt water')
#     WILDLIFE = Feature(FeatureTypes.FOODTYPE, 3, 5, 'primitive hunter', 'Wild animals', 'Packs of wild animals are roaming around')
#     ROCKYTERRAIN = Feature(FeatureTypes.PRODTYPE, 1, 10, 'rock gatherer', 'Rocky Terrain', 'Piece of terrain that has high concentration of rock within.')
#
#     # TIER 1
#     SIMPLEFARM = Feature(FeatureTypes.FOODTYPE, 2, 10, 'farmer', 'Simple farm', 'simple farm', 20, FALLOW)
#     ORCHARD = Feature(FeatureTypes.FOODTYPE, 3, 20, 'fruit grower', 'Orchard', 'fruit tree paradise', 20, FALLOW)
#     FOREST = Feature(FeatureTypes.FOODTYPE, 2, 8, 'gatherer', 'Forest', 'forest with wild life and forage supply', 20, WILDERNESS)
#     MILL = Feature(FeatureTypes.FOODTYPE, 6, 4, 'miller', 'Mill', 'running volume of not sparkling water', 20, RIVER)
#     BIGGAME = Feature(FeatureTypes.FOODTYPE, 4, 5, 'hunter', 'Big Game', 'there are signs of big hunter game in the area', 20, WILDLIFE)
#     LUMBERMILL = Feature(FeatureTypes.PRODTYPE, 3, 10, 'logger', 'Lumber mill', 'Mill that produces lumber', 20, WILDERNESS)
#     QUARRY = Feature(FeatureTypes.PRODTYPE, 3, 10, 'miner', 'Quarry', 'Man made rock farm', 20, ROCKYTERRAIN)
#
#     features.append(FALLOW)
#     features.append(WILDERNESS)
#     features.append(RIVER)
#     features.append(SEASIDE)
#     features.append(WILDLIFE)
#     features.append(ROCKYTERRAIN)
#     features.append(SIMPLEFARM)
#     features.append(ORCHARD)
#     features.append(FOREST)
#     features.append(MILL)
#     features.append(BIGGAME)
#     features.append(LUMBERMILL)
#     features.append(QUARRY)

def get0FoodZone():

    returnArray = []
    for feature in features:
        if feature.foundationType == FeatureTypes.FOODTYPE and feature.upgrFrom == None:
            returnArray.append(feature)
    return returnArray


def get0ProdZone():
    returnArray = []
    for feature in features:
        if feature.foundationType == FeatureTypes.PRODTYPE and feature.upgrFrom == None:
            returnArray.append(feature)
    return returnArray


def getNewFallow():
    return Feature(FeatureTypes.FOODTYPE, 10, 1, 'Fallow', 'fallow land', 'Fallow farmer')
def getNewWildrness():
    return Feature(FeatureTypes.FOODTYPE, 10, 1, 'Wilderness', 'unpassable terrain', 'Primitive gatherer')
def getNewRiver():
    return Feature(FeatureTypes.FOODTYPE, 4, 5, 'River', 'running volume of not sparkling water', 'River fisher')
def getNewSeaSide():
    return Feature(FeatureTypes.FOODTYPE, 3, 3, 'Sea side', 'running volume of not sparkling salt water', 'Sea fisher')
def getNewWildlife():
    return Feature(FeatureTypes.FOODTYPE, 3, 5, 'Wild animals', 'Packs of wild animals are roaming around', 'Primitive hunter')
def getNewRockyTerrain():
    return Feature(FeatureTypes.PRODTYPE, 1, 5, 'Rocky Terrain', 'Piece of terrain that has high concentration of rock within.', 'Rock gatherer')
def getNewFallenLogs():
    return Feature(FeatureTypes.PRODTYPE, 1, 8, 'Fallen Logs', 'Trees that took a bit to long nap', 'Wood hawler')
def getNewSimplefarm():
    return Feature(FeatureTypes.FOODTYPE, 2, 10, 'Simple farm', 'simple farm', 'Farmer', 20, 'Fallow')
def getNewOrchard():
    return Feature(FeatureTypes.FOODTYPE, 3, 20, 'Orchard', 'fruit tree paradise', 'Fruit grower', 20, 'Fallow')
def getNewForest():
    return Feature(FeatureTypes.FOODTYPE, 2, 8, 'Forest', 'forest with wild life and forage supply', 'Gatherer', 20, 'Wilderness')
def getNewMill():
    return Feature(FeatureTypes.FOODTYPE, 6, 4, 'Mill', 'running volume of not sparkling water', 'Miller', 20, 'River')
def getNewBigGame():
    return Feature(FeatureTypes.FOODTYPE, 4, 5, 'Big Game', 'there are signs of big hunter game in the area', 'Hunter', 20, 'Wild animals')
def getNewLumberMill():
    return Feature(FeatureTypes.PRODTYPE, 3, 10, 'Lumber mill', 'Mill that produces lumber', 'Logger', 20, 'Fallen Logs')
def getNewQuarry():
    return Feature(FeatureTypes.PRODTYPE, 3, 10, 'Quarry', 'Man made rock farm', 'Miner', 20, 'Rocky Terrain')


def createZones():

    zones = []

    zones.append(getNewFallow())
    zones.append(getNewWildrness())
    zones.append(getNewRiver())
    zones.append(getNewSeaSide())
    zones.append(getNewWildlife())
    zones.append(getNewRockyTerrain())
    zones.append(getNewFallenLogs())
    zones.append(getNewSimplefarm())
    zones.append(getNewOrchard())
    zones.append(getNewForest())
    zones.append(getNewMill())
    zones.append(getNewBigGame())
    zones.append(getNewLumberMill())
    zones.append(getNewQuarry())

    return zones

class Zones(Enum):

    #production yield, description, upgr cost, upgrades to
    # TIER 0 (BASIC)
    FALLOW = getNewFallow()
    WILDERNESS = getNewWildrness()
    RIVER = getNewRiver()
    SEASIDE = getNewSeaSide()
    WILDLIFE = getNewWildlife()
    ROCKYTERRAIN = getNewRockyTerrain()
    FALLENLOGS = getNewFallenLogs()

    # TIER 1
    SIMPLEFARM = getNewSimplefarm()
    ORCHARD = getNewOrchard()
    FOREST = getNewForest()
    MILL = getNewMill()
    BIGGAME = getNewBigGame()
    LUMBERMILL = getNewLumberMill()
    QUARRY = getNewQuarry()



    #bonus to max pop, description
    # FARMS = 20, 'farms'
    # RICHSOIL = 100, 'rich soil',
    # RIVER = 50, 'river'
    # FISHSCHOOLS = 50, 'school of fish'
    # ORCHARD = 50, 'oarchard'
    # SILO = 25, 'silo'
    # MILL = 25, 'mill'
    # BARN = 25, 'barn'
    # FOREST = 20, 'forest'
    # BIGGAME = 20, 'big game'
    # MEADOWBEES = 15, 'meadow bees'

def getFeatureIndexFromName(name):
    index = 0
    for feature in Zones:
        if feature.value.getName() == name:
            return index
        else:
            index +=1

    return -1

def getListOfTier0FoodFeatures():
    returnArray = []
    for enum in Zones:
        if enum.value.upgrFrom == None and enum.value.featureType == FeatureTypes.FOODTYPE:
            returnArray.append(enum)
    return returnArray

def getListOfTier0ProdFeatures():
    returnArray = []
    for enum in Zones:
        if enum.value.upgrFrom == None  and enum.value.featureType == FeatureTypes.PRODTYPE:
            returnArray.append(enum)
    return returnArray

def getPotencialUpgradesForZone(zone):

    returnArray = []
    for enum in Zones:
        if enum.value.upgrFrom == zone:
            returnArray.append(enum)
    return returnArray

