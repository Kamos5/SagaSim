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