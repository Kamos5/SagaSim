import Enums
import SettlementNameGenerator as SNG
import RegionNameGenerator as RNG
import Parameters
import Utils
import SettlementFeatures as SF
import FoundationTypes as FoundationTypes
import PersonLifeEventsHistory as PLEH

def takeFeatureNumber(elem):
    return elem.getFeatureNumber()

class Settlements:

    def __init__(self, regionNumber, year=Parameters.startingYear, rebuildFlag = False):
        self.settlementType = Enums.Settlements.VILLAGE

        self.name = SNG.randomSettlementsName(regionNumber=regionNumber, rebuildOldSettlement=rebuildFlag)

        self.region = None
        self.province = None
        self.population = 0
        self.foundedIn = year
        self.baseFertility = Parameters.baseVillageFertility
        self.fertilityModifier = 0
        self.foodTiles = 7
        self.prodTiles = 1
        self.foodProduced = 0
        self.prodProduced = 0
        self.foodConsumed = 0
        self.prodConsumed = 0
        self.foodProducedLastYear = 0
        self.prodProducedLastYear = 0
        self.foodConsumedLastYear = 0
        self.prodConsumedLastYear = 0
        self.foodNetLastYear = 0
        self.freeFood = 100
        self.freeProd = 0
        self.residents = []
        self.foodFeatures = []
        self.prodFeatures = []
        self.adminFeatures = []
        self.unemployedRes = []
        self.employedRes = []
        self.providesTo = None
        self.providedFrom = []
        self.maxPopulation = 0
        self.uiExpand = False
        self.freeWealth = 0
        self.localIncomeTax = Utils.randomRange(1, 20)
        self.avarageResidentsWealth = 0
        self.housings = []
        self.createStartingVillageFeatures()
        self.timeSinceMigration = 0 #in days
        self.adjustFertilityModifier()
        self.migrationMonth = Utils.randomFromEnumCollection(Enums.Months)
        self.migrationDay = Utils.randomRange(1, self.migrationMonth.value[2])

    def getRegion(self):
        return self.region

    def setRegion(self, newRegion):
        self.region = newRegion

    def getProvince(self):
        return self.province

    def setProvince(self, newProvince):
        self.province = newProvince

    def updateFeaturesForTown(self):
        self.createUpdateVillageFeaturesForTown()

    def getUIExpand(self):
        return self.uiExpand

    def setUIExpand(self, newValue):
        self.uiExpand = newValue

    def getPopulation(self):
        return self.population

    def increasePopulation(self):
        self.population += 1

    def decreasePopulation(self):
        self.population -= 1

    def getMaxPopulation(self):
        return self.maxPopulation

    def setMaxPopulation(self, newMax):
        self.maxPopulation = newMax

    def getBaseFertility(self):
        return self.baseFertility

    def setBaseFertility(self, newFertility):
        self.baseFertility = newFertility

    def getFoodFeatures(self):
        return sorted(self.foodFeatures, key=lambda feature: feature.getFeatureNumber())

    def removeFoodFeature(self, feature):
        self.foodFeatures.remove(feature)

    def addFoodFeature(self, feature):
        self.foodFeatures.append(feature)

    def getAdminFeatures(self):
        return self.adminFeatures

    def addAdminFeature(self, feature):
        self.adminFeatures.append(feature)

    def removeAdminFeature(self, feature):
        self.adminFeatures.remove(feature)


    def getProdFeatures(self):
        return self.prodFeatures

    def addProdFeature(self, feature):
        self.prodFeatures.append(feature)

    def removeProdFeature(self, feature):
        self.prodFeatures.remove(feature)

    def getFertilityModifier(self):
        return self.fertilityModifier

    def setFertilityModifier(self, modifier):
        self.fertilityModifier = modifier

    def adjustFertilityModifier(self):
        if self.getFreeFood() < self.getPopulation() * 1:
            self.setFertilityModifier(Parameters.settlementLowFoodFertilityModifier)
            return
        if self.getFreeFood() > self.getPopulation() * 3:
            self.setFertilityModifier(Parameters.settlementHighFoodFertilityModifier)
            return
        else:
            self.setFertilityModifier(Parameters.settlementNormalFoodFertilityModifier)
            return

    def changeSettlementName(self, newName):
        self.name = newName

    def getSettlementName(self):
        return self.name

    def getSettlementFoodProduced(self):
        return self.foodProduced

    def increaseSettlementFoodProduced(self, value):
        self.foodProduced += value
        self.foodProduced = round(self.foodProduced, 2)

    def getSettlementFoodProducedLastYear(self):
        return round(self.foodProducedLastYear, 2)

    def setSettlementFoodProducedLastYear(self, value):
        self.foodProducedLastYear = value

    def getSettlementProdProduced(self):
        return round(self.prodProduced, 2)

    def increaseSettlementProdProduced(self, value):
        self.prodProduced += value
        self.prodProduced = round(self.prodProduced, 2)

    def getSettlementProdProducedLastYear(self):
        return round(self.prodProducedLastYear, 2)

    def setSettlementProdProducedLastYear(self, value):
        self.prodProducedLastYear = value

    def getSettlementFoodConsumed(self):
        return self.foodConsumed

    def increaseSettlementFoodConsumed(self, value):
        self.foodConsumed += value
        self.foodConsumed = round(self.foodConsumed, 2)

    def getSettlementFoodConsumedLastYear(self):
        return round(self.foodConsumedLastYear, 2)

    def setSettlementFoodConsumedLastYear(self, value):
        self.foodConsumedLastYear = value

    def getSettlementProdConsumed(self):
        return round(self.prodConsumed, 2)

    def increaseSettlementProdConsumed(self, value):
        self.prodConsumed += value
        self.prodConsumed = round(self.prodConsumed, 2)

    def getSettlementProodConsumedLastYear(self):
        return round(self.prodConsumedLastYear, 2)

    def setSettlementProdConsumedLastYear(self, value):
        self.prodConsumedLastYear = value

    def getNetFoodLastYear(self):
        return self.foodNetLastYear

    def setNetFoodLastYear(self, value):
        self.foodNetLastYear = round(value, 2)

    def getFreeFood(self):
        return self.freeFood

    def setFreeFood(self, value):
        self.freeFood = value
        self.freeFood = round(self.freeFood, 2)

    def changeFreeFood(self, value):
        self.freeFood += value
        self.freeFood = round(self.freeFood, 2)
        # if self.freeFood > 1000:
        #     self.freeFood = 1000
        self.adjustFertilityModifier()

    def getFreeProd(self):
        return self.freeProd

    def setFreeProd(self, value):
        self.freeProd = value
        self.freeProd = round(self.freeProd, 2)

    def changeFreeProd(self, value):
        self.freeProd += value
        self.freeProd = round(self.freeProd, 2)

    def getFoodTilesNumber(self):
        return self.foodTiles

    def getProdFeatureNumber(self):
        return self.prodTiles

    def getSettlementType(self):
        return self.settlementType

    def changeSettlementType(self, newType):
        self.settlementType = newType
        if newType == Enums.Settlements.VILLAGE:
            self.setBaseFertility(Parameters.baseVillageFertility)
            self.maxPopulation = Parameters.baseVillageSize
            #self.recalculatePopWithFeatures()
            self.foodTiles = 7
            self.prodTiles = 1
        else:
            self.setBaseFertility(Parameters.baseCityFertility)
            self.maxPopulation = Parameters.baseCitySize
            #self.recalculatePopWithFeatures()
            self.foodTiles = 8
            self.prodTiles = 16
            self.updateFeaturesForTown()
            self.setProvision(None)

        # for number in range(self.getFoodTilesNumber()-len(self.getFoodFeatures())):
        #     feature = Utils.randomFromCollection(SF.getListOfTier0FoodFeatures())
        #     feature.value.setFoundationType(Utils.randomFromEnumCollection(FoundationTypes.FoundationEnums))
        #     self.addFoodFeature(feature)
        #
        # for number in range(self.getProductionTilesNumber()-len(self.getProdFeatures())):
        #
        #     feature = Utils.randomFromCollection(SF.getListOfTier0ProdFeatures())
        #     feature.value.setFoundationType(Utils.randomFromEnumCollection(FoundationTypes.FoundationEnums))
        #     self.addProdFeature(feature)

    def getFounedIn(self):
        return self.foundedIn
    def getResidents (self):
        return self.residents
    def addResident (self, person):
        self.residents.append(person)
    def removeResident(self, person):
        self.residents.remove(person)

    def getCivilianWorkplaces(self):
        workplaces = 0
        for workplace in self.getAdminFeatures():
            workplaces += workplace.getMaxWorkersNumber()
        for workplace in self.getFoodFeatures():
            workplaces += workplace.getMaxWorkersNumber()
        for workplace in self.getProdFeatures():
            workplaces += workplace.getMaxWorkersNumber()
        return workplaces

    def getUnemployedResidentsList(self):

        self.unemployedRes = []
        for res in self.residents:
            if res.getAge() >= 15 and res.getOccupation() is None and res not in self.unemployedRes and res.getAge() < 50 and res.getSex() == Enums.Sexes.MALE:
                self.unemployedRes.append(res)
        return self.unemployedRes


    # TODO BUG MOGA BYC EMPLOYED ALE POPULATION = 0 - MAYBE FIX???
    def getEmployedResidentsList(self):

        self.employedRes = []
        for res in self.getResidents():
            if res.getOccupation() is not None:
                self.employedRes.append(res)
        return self.employedRes

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

    def createStartingVillageFeatures(self):

        adminFeature = SF.createAdminZones()[0]
        adminFeature.setFoundationType(FoundationTypes.foundations['medium'])#FoundationTypes.FoundationEnums.MEDIUM)
        self.addAdminFeature(adminFeature)
        adminFeature = SF.createAdminZones()[2]
        adminFeature.setFoundationType(FoundationTypes.foundations['medium'])#FoundationTypes.FoundationEnums.MEDIUM)
        self.addAdminFeature(adminFeature)

        for i in range(7):
            randomBasicFeature = Utils.randomRange(0, 4)
            feature = SF.createZones()[randomBasicFeature]
            feature.setFoundationType(Utils.randomFromFoundationDictionaryWithWeight(FoundationTypes.foundations))
            #feature.setFoundationType(Utils.randomFromEnumCollectionWithWeights(FoundationTypes.FoundationEnums))
            feature.setFeatureNumber(i)
            self.addFoodFeature(feature)
        randomBasicFeature = Utils.randomRange(5, 6)
        feature = SF.createZones()[randomBasicFeature]
        feature.setFoundationType(FoundationTypes.foundations['medium'])
        feature.setFeatureNumber(7)
        self.addProdFeature(feature)

    def createUpdateVillageFeaturesForTown(self):

        feature = SF.createZones()[4]
        feature.setFoundationType(Utils.randomFromFoundationDictionaryWithWeight(FoundationTypes.foundations))
        #feature.setFoundationType(Utils.randomFromEnumCollectionWithWeights(FoundationTypes.FoundationEnums))
        feature.setFeatureNumber(8)
        self.addFoodFeature(feature)

        for i in range(15):
            randomBasicFeature = Utils.randomRange(5, 6)
            feature = SF.createZones()[randomBasicFeature]
            feature.setFoundationType(Utils.randomFromFoundationDictionaryWithWeight(FoundationTypes.foundations))
            #feature.setFoundationType(Utils.randomFromEnumCollectionWithWeights(FoundationTypes.FoundationEnums))
            feature.setFeatureNumber(9+i)
            self.addProdFeature(feature)


    def upgradeTile(self, oldFeature, newFeature, world):

        if oldFeature.getFeatureType() == SF.FeatureTypes.FOODTYPE:
            self.removeFoodFeature(oldFeature)
            newFeature.setFoundationType(oldFeature.getFoundationType())
            newFeature.setFeatureNumber(oldFeature.getFeatureNumber())
            self.addFoodFeature(newFeature)
        if oldFeature.getFeatureType() == SF.FeatureTypes.PRODTYPE:
            self.removeProdFeature(oldFeature)
            newFeature.setFoundationType(oldFeature.getFoundationType())
            newFeature.setFeatureNumber(oldFeature.getFeatureNumber())
            self.addProdFeature(newFeature)

        workersToRemove = []
        for worker in oldFeature.getWorkerList():
            workersToRemove.append(worker)
            newFeature.addWorker(worker)
            worker.setOccupation(newFeature)
            worker.setOccupationName(newFeature.getOccupationName())
            PLEH.gotPromotion(worker, world)
        for worker in workersToRemove:
            oldFeature.removeWorker(worker)

    def getFreeWealth(self):
        return self.freeWealth

    def setFreeWealth(self, newValue):
        self.freeWealth = round(newValue, 2)

    def changeFreeWealth(self, modifier):
        self.freeWealth += modifier
        self.freeWealth = round(self.freeWealth, 2)

    def buildNewHouse(self, newHouse):
        self.housings.append(newHouse)

    def getHousing(self):
        return self.housings

    def removeHouse(self, house):
        self.housings.remove(house)

    def getLocalIncomeTax(self):
        return self.localIncomeTax

    def getTimeSinceMigration(self):
        return self.timeSinceMigration

    def increaseTimeSinceMigration(self):
        self.timeSinceMigration += 1

    def resetTimeSinceMigration(self):
        self.timeSinceMigration = 0

    def getAvarageResidentsWealth(self):

        tempSumWealth = 0

        for resident in self.getResidents():
            tempSumWealth += resident.getFreeWealth()

        return round(tempSumWealth/len(self.getResidents()), 3)

    def getMigrationDay(self):
        return self.migrationDay

    def getMigrationMonth(self):
        return self.migrationMonth


