import uuid
from enum import Enum

import Enums
import Utils

features = []

class FeatureType():

    def __init__(self, name, description):
        self.name = name
        self.description = description


class FeatureTypes(Enum):

    FOODTYPE = FeatureType("Food type", "produces food resource")
    PRODTYPE = FeatureType("Production type", "produces production resource")
    ADMINTYPE = FeatureType("Administrative type", "administering stuff")
    MILITARYTYPE = FeatureType("Military type", "fending of bad people")
    MISC = FeatureType("Misc type", "random type")
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

    def __init__(self, featureType=None, prodYield=0, maxWorkers=0, name='', desc='', occupationName='', upgrCost=0, upgrFrom=None, upgrWeightValue=100, cordx=0, cordy=0, featureNumber=0, skillUsed=Enums.SkillNames.LABOR):
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
        self.upgrWeightValue = upgrWeightValue
        self.cordX = cordx
        self.cordY = cordy
        self.featureNumber = featureNumber
        self.skillUsed = skillUsed
        self.uiExpand = False

    def setFoundationType(self, newType):
        self.foundationType = newType

    def getFoundationType(self):
        return self.foundationType

    def getFeatureType(self):
        return self.featureType

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

    def getUpgrWeightValue(self):
        return self.upgrWeightValue

    def getUIExpand(self):
        return self.uiExpand

    def getSkillUsed(self):
        return self.skillUsed

    def changeSkillUsed(self, newSkill):
        self.skillUsed = newSkill

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


#foundation type, productionValue, workersNumber, name, descr, workerName, upgrCost, upgrFrom, weightUpgrValue, skill
def getNewFallow():
    return Feature(FeatureTypes.FOODTYPE, 2, 5, 'Fallow', 'fallow land', 'Fallow farmer', skillUsed=Enums.SkillNames.LABOR)
def getNewWildrness():
    return Feature(FeatureTypes.FOODTYPE, 2, 5, 'Wilderness', 'unpassable terrain', 'Primitive gatherer', skillUsed=Enums.SkillNames.LABOR)
def getNewRiver():
    return Feature(FeatureTypes.FOODTYPE, 3, 5, 'River', 'running volume of not sparkling water', 'River fisher', skillUsed=Enums.SkillNames.LABOR)
def getNewSeaSide():
    return Feature(FeatureTypes.FOODTYPE, 3, 5, 'Sea side', 'running volume of not sparkling salt water', 'Sea fisher', skillUsed=Enums.SkillNames.LABOR)
def getNewWildlife():
    return Feature(FeatureTypes.FOODTYPE, 3, 3, 'Wild animals', 'Packs of wild animals are roaming around', 'Primitive hunter', skillUsed=Enums.SkillNames.LABOR)
def getNewRockyTerrain():
    return Feature(FeatureTypes.PRODTYPE, 1, 5, 'Rocky Terrain', 'Piece of terrain that has high concentration of rock within.', 'Rock gatherer', skillUsed=Enums.SkillNames.LABOR)
def getNewFallenLogs():
    return Feature(FeatureTypes.PRODTYPE, 2, 3, 'Fallen Logs', 'Trees that took a bit to long nap', 'Wood howler', skillUsed=Enums.SkillNames.LABOR)
def getNewSimplefarm():
    return Feature(FeatureTypes.FOODTYPE, 3, 7, 'Simple farm', 'simple farm', 'Farmer', 200, 'Fallow', 100, skillUsed=Enums.SkillNames.LABOR)
def getNewOrchard():
    return Feature(FeatureTypes.FOODTYPE, 3, 7, 'Orchard', 'fruit tree paradise', 'Fruit grower', 200, 'Fallow', 100, skillUsed=Enums.SkillNames.LABOR)
def getNewWindmill():
    return Feature(FeatureTypes.FOODTYPE, 4, 7, 'Wind Mill', 'wind make it go brrr', 'Miller', 200, 'Fallow', skillUsed=Enums.SkillNames.LABOR)
def getNewForest():
    return Feature(FeatureTypes.FOODTYPE, 3, 7, 'Forest', 'forest with wild life and forage supply', 'Gatherer', 200, 'Wilderness', skillUsed=Enums.SkillNames.LABOR)
def getNewWatermill():
    return Feature(FeatureTypes.FOODTYPE, 4, 7, 'Water Mill', 'running volume of not sparkling water', 'Miller', 200, 'River', skillUsed=Enums.SkillNames.LABOR)
def getNewBigGame():
    return Feature(FeatureTypes.FOODTYPE, 4, 5, 'Big Game', 'there are signs of big hunter game in the area', 'Hunter', 200, 'Wild animals', skillUsed=Enums.SkillNames.LABOR)
def getNewLumberMill():
    return Feature(FeatureTypes.PRODTYPE, 3, 5, 'Lumber mill', 'Mill that produces lumber', 'Logger', 200, 'Fallen Logs', skillUsed=Enums.SkillNames.LABOR)
def getNewQuarry():
    return Feature(FeatureTypes.PRODTYPE, 2, 7, 'Quarry', 'Man made rock farm', 'Miner', 250, 'Rocky Terrain', 100, skillUsed=Enums.SkillNames.LABOR)
def getNewCoalMine():
    return Feature(FeatureTypes.PRODTYPE, 3, 7, 'Coal mine', 'Dirty rocks', 'Coal miner', 250, 'Rocky Terrain', 80, skillUsed=Enums.SkillNames.LABOR)
def getNewTinMine():
    return Feature(FeatureTypes.PRODTYPE, 2, 7, 'Tin mine', 'Grayish rocks', 'Tin miner', 250, 'Rocky Terrain', 50, skillUsed=Enums.SkillNames.LABOR)
def getNewLeadMine():
    return Feature(FeatureTypes.PRODTYPE, 2, 7, 'Lead mine', 'Almost silver rocks', 'Lead miner', 250, 'Rocky Terrain', 50, skillUsed=Enums.SkillNames.LABOR)
def getNewCopperMine():
    return Feature(FeatureTypes.PRODTYPE, 3, 7, 'Copper mine', 'Green rocks', 'Copper miner', 250, 'Rocky Terrain', 50, skillUsed=Enums.SkillNames.LABOR)
def getNewIronMine():
    return Feature(FeatureTypes.PRODTYPE, 4, 7, 'Iron mine', 'Hard rocks', 'Iron miner', 250, 'Rocky Terrain', 50, skillUsed=Enums.SkillNames.LABOR)
def getNewSilverMine():
    return Feature(FeatureTypes.PRODTYPE, 5, 7, 'Silver mine', 'Shiny white rocks', 'Silver miner', 250, 'Rocky Terrain', 25, skillUsed=Enums.SkillNames.LABOR)
def getNewGoldMine():
    return Feature(FeatureTypes.PRODTYPE, 6, 7, 'Gold mine', 'Shiny rocks', 'Gold miner', 250, 'Rocky Terrain', 10, skillUsed=Enums.SkillNames.LABOR)
def getEltersHut():
    return Feature(FeatureTypes.ADMINTYPE, 1, 1, 'Elders hut', 'Place of meeting of old important village people', 'Village Elder', skillUsed=Enums.SkillNames.ADMIN)
def getVillageHall():
    return Feature(FeatureTypes.ADMINTYPE, 1, 1, 'Village hall', 'Place of meeting for village people', 'Village Mayor', skillUsed=Enums.SkillNames.ADMIN)
def getTownHall():
    return Feature(FeatureTypes.ADMINTYPE, 1, 1, 'City hall', 'Place of meeting for town people', 'Mayor', skillUsed=Enums.SkillNames.ADMIN)
def getShrine():
    return Feature(FeatureTypes.ADMINTYPE, 1, 1, 'Shrine', 'Place of basic worship', 'Priest', skillUsed=Enums.SkillNames.ADMIN)
def getMilitiaHut():
    return Feature(FeatureTypes.MILITARYTYPE, 0, 15, 'Militia Hut', 'Place for peasants with pitchforks and axes', 'Militiaman', skillUsed=Enums.SkillNames.FIGHTER)
def getArcherHut():
    return Feature(FeatureTypes.MILITARYTYPE, 0, 10, 'Archer\'s Hut', 'Place for people with flying sharp sticks', 'Archer', skillUsed=Enums.SkillNames.FIGHTER)
def getSwordsmansGuild():
    return Feature(FeatureTypes.MILITARYTYPE, 0, 10, 'Swordsman\'sGuild', 'Place from where people with big metal sticks are coming from', 'Swordsman', skillUsed=Enums.SkillNames.FIGHTER)

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
    zones.append(getNewWatermill())
    zones.append(getNewWindmill())
    zones.append(getNewBigGame())
    zones.append(getNewLumberMill())
    zones.append(getNewQuarry())
    zones.append(getNewGoldMine())
    zones.append(getNewCoalMine())
    zones.append(getNewIronMine())
    zones.append(getNewTinMine())
    zones.append(getNewLeadMine())
    zones.append(getNewCopperMine())
    zones.append(getNewSilverMine())

    return zones

def createAdminZones():

    zones = []

    zones.append(getEltersHut())
    zones.append(getVillageHall())
    zones.append(getTownHall())
    zones.append(getShrine())

    return zones

def createMilitaryZones():

    zones = []

    zones.append(getMilitiaHut())
    zones.append(getArcherHut())
    zones.append(getSwordsmansGuild())

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
    WATERMILL = getNewWatermill()
    WINDMILL = getNewWindmill()
    BIGGAME = getNewBigGame()
    LUMBERMILL = getNewLumberMill()
    QUARRY = getNewQuarry()

    GOLDMINE = getNewGoldMine()
    COALMINE = getNewCoalMine()
    IRONMINE = getNewIronMine()
    SILVERMINE = getNewSilverMine()
    TINMINE = getNewTinMine()
    LEADMINE = getNewLeadMine()
    COPPERMINE = getNewCopperMine()


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
    indexList = []
    for feature in Zones:
        if feature.value.getName() == name:
            indexList.append(index)
        else:
            index +=1

    if len(indexList) > 0:
        return Utils.randomFromCollection(indexList)
    else:
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

