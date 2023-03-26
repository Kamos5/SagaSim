import Utils
from House import House
from HouseTypes import HouseEnums


def getNewHouse():
    return House().getBasicHouse()

def setNewHouseToPerson(person, house):
    person.setAccommodation(house)

# def addNewOwner(person, house):
#     house.setHouseFirstOwner(person)
#     person.addRealEstate(house)

def setHouseDurability(house, newValue):
    house.setHouseDurability(newValue)

def payForUpkeep (house):

    upkeepWasPaid = False
    for resident in house.getHouseResidents():
        upkeep = house.getHouseType().value.getHouseUpkeep()
        if house.getHouseDurability() == 100 and resident.getFreeWealth() >= upkeep/2:
            resident.changeFreeWealth(-upkeep/2)
            upkeepWasPaid = True
            break
        if resident.getFreeWealth() >= upkeep:
            resident.changeFreeWealth(-upkeep)
            house.changeHouseDurability(round((100-house.getHouseDurability())/4)+1)
            upkeepWasPaid = True
            break

    if not upkeepWasPaid:
        house.changeHouseDurability(-5)

def payForUpgrade (house):

    for resident in house.getHouseResidents():
        costToPay = house.getHouseType().value.getCostToUpgrade()
        if resident.getSpouse() is not None and resident.getFreeWealth() + resident.getSpouse().getFreeWealth() >= costToPay:
            if resident.getFreeWealth() > costToPay:
                resident.changeFreeWealth(-costToPay)
            if resident.getSpouse().getFreeWealth() > costToPay:
                resident.getSpouse().changeFreeWealth(-costToPay)
            randomPerson = Utils.randomFromCollection([resident, resident.getSpouse()])
            costToPay -= randomPerson.getFreeWealth()
            randomPerson.changeFreeWealth(-randomPerson.getFreeWealth())
            costToPay -= randomPerson.getSpouse().getFreeWealth()
            upgradeHouse(house)
            break
        else:
            if resident.getFreeWealth() > costToPay:
                resident.changeFreeWealth(-costToPay)
                upgradeHouse(house)
                break


def downgradeHouse (house):

    if house.getHouseType().value.getTier() == 2:
        house.setHouseType(HouseEnums.TENT)
        return
    if house.getHouseType().value.getTier() == 3:
        house.setHouseType(HouseEnums.SHACK)
        return
    if house.getHouseType().value.getTier() == 4:
        house.setHouseType(HouseEnums.WOODENHOUSE)
        return
    if house.getHouseType().value.getTier() == 5:
        house.setHouseType(HouseEnums.STONEHOUSE)
        return
    if house.getHouseType().value.getTier() == 6:
        house.setHouseType(HouseEnums.BRICKHOUSE)
        return
    if house.getHouseType().value.getTier() == 7:
        house.setHouseType(HouseEnums.MANOR)
        return

def upgradeHouse (house):

    if house.getHouseType().value.getTier() == 1:
        house.setHouseType(HouseEnums.SHACK)
        return
    if house.getHouseType().value.getTier() == 2:
        house.setHouseType(HouseEnums.WOODENHOUSE)
        return
    if house.getHouseType().value.getTier() == 3:
        house.setHouseType(HouseEnums.STONEHOUSE)
        return
    if house.getHouseType().value.getTier() == 4:
        house.setHouseType(HouseEnums.BRICKHOUSE)
        return
    if house.getHouseType().value.getTier() == 5:
        house.setHouseType(HouseEnums.MANOR)
        return
    if house.getHouseType().value.getTier() == 6:
        house.setHouseType(HouseEnums.PALACE)
        return