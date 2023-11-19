import Utils
import SettlementFeatures as SFeat
from Enums import Settlements

def getCities (settlements):

    citiesList = []

    for settlement in settlements:
        if settlement.settlementType == Settlements.TOWN:
            citiesList.append(settlement)
    return citiesList


def getVillages(settlements):
    villagesList = []

    for settlement in settlements:
        if settlement.settlementType == Settlements.VILLAGE:
            villagesList.append(settlement)
    return villagesList

def produceFood (settlement):

    if settlement.settlementType==  Settlements.VILLAGE:
        return 0


def checkForTileUpgrades(settlement, featuresType, world):


    for tile in featuresType: #food/prod/admin
        if len(SFeat.getPotencialUpgradesForZone(tile.getName())) > 0:
            upgradable = Utils.randomFromCollectionWithWeight(SFeat.getPotencialUpgradesForZone(tile.getName()))
            # for upgradable in (SFeat.getPotencialUpgradesForZone(tile.getName())):
            if float(settlement.getFreeProd()) >= float(upgradable.value.getUpgradeCost()):
                settlement.changeFreeProd(-upgradable.value.getUpgradeCost())
                newFeature = SFeat.createZones()[SFeat.getFeatureIndexFromName(upgradable.value.getName())]
                settlement.upgradeTile(tile, newFeature, world)
                return