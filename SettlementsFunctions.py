import Enums
import HouseFunctions
import Parameters
import Utils
import SettlementFeatures as SFeat
from Enums import Settlements, LifeStatus
import PersonLifeEventsHistory as PLEH
import FamilyFunctions as FF
from Family import Family
import FamilyNameGenerator as FNG

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

def prepareMigration(settlement, newTargetSettlement, world):

    migrantFamilies = 0
    if settlement.getSettlementType() == Settlements.TOWN:
        mirgrationWave = Parameters.migrationWaveForTown
    else:
        mirgrationWave = Parameters.migrationWaveForVillage

    randomMigrantsList = []
    complexRandomMigrantList = []
    # random x people with their alive children move to new Village
    for migrantFamilies in range(mirgrationWave):
        randomPerson = Utils.randomFromCollection(settlement.getResidents())
        if randomPerson not in randomMigrantsList:
            # for MINOR
            if randomPerson.age < 15:
                getRandomMigrantListForSingleRandomPerson(randomPerson, "Father", randomMigrantsList, settlement, world)
                getRandomMigrantListForSingleRandomPerson(randomPerson, "Mother", randomMigrantsList, settlement, world)
            else:
                # for Adult
                getRandomMigrantListForSingleRandomPerson(randomPerson, "Adult", randomMigrantsList, settlement, world)
            if len(randomMigrantsList) > 0:
                complexRandomMigrantList.append(randomMigrantsList)
                migrantFamilies += 1
                randomMigrantsList = []


    return complexRandomMigrantList

def iniciateMigration(complexMigrantList, settlementTarget, world):

    for migrantList in complexMigrantList:
        for migrant in migrantList:
            PLEH.movedHome(migrant, migrant.getSettlement(), settlementTarget, world)
            FF.fireSingleEmployee(migrant, world)
            migrant.getSettlement().decreasePopulation()
            migrant.getSettlement().removeResident(migrant)
            migrant.setSettlement(settlementTarget)
            settlementTarget.increasePopulation()
            settlementTarget.addResident(migrant)
            FF.fireSingleEmployee(migrant, world)

def getRandomMigrantListForSingleRandomPerson(person, parent, randomMigrantsList, settlement, world):

    getParent = ''
    if person.getFather() is not None and person.getFather() != '' and person.getFather().lifeStatus != LifeStatus.DEAD:
        if parent == "Father":
            getParent = person.getFather()
    if person.getFather() is not None and person.getMother() != '' and person.getMother().lifeStatus != LifeStatus.DEAD:
        if parent == "Mother":
            getParent = person.getMother()
    if parent == "Adult":
        getParent = person

    if getParent != '':
        if getParent not in randomMigrantsList:
            # if newLastName != '':
            #     getParent.lastName = newLastName
            randomMigrantsList.append(getParent)

        parentChildrensList = getParent.getAliveChildrenList()
        for parentChildren in parentChildrensList:
            if parentChildren.age < 15:
                if parentChildren not in randomMigrantsList:
                    randomMigrantsList.append(parentChildren)
                    #PLEH.movedHome(parentChildren, settlement, world)

        if getParent.spouse is not None:
            if getParent.spouse not in randomMigrantsList:
                randomMigrantsList.append(getParent.spouse)
                #PLEH.movedHome(getParent.spouse, settlement, world)
                # if newLastName != '':
                #     getParent.lastName = newLastName

            parentSpouseChildrensList = getParent.spouse.aliveChildren
            for parentSpouseChildren in parentSpouseChildrensList:
                if parentSpouseChildren.age < 15:
                    if parentSpouseChildren not in randomMigrantsList:
                        randomMigrantsList.append(parentSpouseChildren)
                        #PLEH.movedHome(parentSpouseChildren, settlement, world)
                        # if newLastName != '':
                        #     getParent.lastName = newLastName

def splitFamiliesInMigration(world, region, province, newTargetSettlement, complexRandomMigrantsList):


    for randomMigrantList in complexRandomMigrantsList:
        chanceOfChangingLastName = Utils.randomRange(1, 100)
        #won't change last name if only 1 person will be in migrant list whose culture sex is not to inherite
        if (chanceOfChangingLastName < Parameters.chanceForChangingLastNameDuringMigration and
                len(randomMigrantList) > 1 and
                randomMigrantList[0].familyObjRef.aliveMemberNumber > 1 and
                randomMigrantList[0].familyObjRef.getOriginCulture().getInheritanceBy() != randomMigrantList[0].sex):



            chanceForRevingAncestralFamily = Utils.randomRange(1, 100)

            if chanceForRevingAncestralFamily > 20:
                newFamilyName = FNG.getNewLastNameBasedOnCulture(region.getOriginalCulture(), world=world)
#                newFamilyName = FNG.getNewLastNameBasedOnRegion(region)
                family = Family(newFamilyName)
                family.setFoundingYear(world.getYear())
                family.setOriginRegion(region)
                family.setOriginProvince(province)
                family.setOriginSettlement(newTargetSettlement)
                family.setOriginCulture(randomMigrantList[0].familyObjRef.getOriginCulture())
                family.setFamilyBranchedFrom(randomMigrantList[0].familyObjRef)
                randomMigrantList[0].familyObjRef.addOffspringBranch(family)
                world.addFamily(family)
            else:
                ancestralFamilies = randomMigrantList[0].getAncestralFamilies()
                if len(ancestralFamilies) > 1:
                    ancestralFamilies.pop(0)
                    family = Utils.randomFromCollection(ancestralFamilies)
                    newFamilyName = family.getFamilyName()
                else:
                    newFamilyName = FNG.getNewLastNameBasedOnCulture(region.getOriginalCulture(), world=world)
#                    newFamilyName = FNG.getNewLastNameBasedOnRegion(region)
                    family = Family(newFamilyName)
                    family.setFoundingYear(world.getYear())
                    family.setOriginRegion(region)
                    family.setOriginProvince(province)
                    family.setOriginSettlement(newTargetSettlement)
                    family.setOriginCulture(randomMigrantList[0].familyObjRef.getOriginCulture())
                    family.setFamilyBranchedFrom(randomMigrantList[0].familyObjRef)
                    randomMigrantList[0].familyObjRef.addOffspringBranch(family)
                    world.addFamily(family)

            newHouse = HouseFunctions.getNewHouse()
            newTargetSettlement.buildNewHouse(newHouse)
            HouseFunctions.setHouseDurability(newHouse, Utils.randomRange(60, 90))

            for person in randomMigrantList:

                person.getAccommodation().removeHouseResident(person)
                HouseFunctions.setNewHouseToPerson(person, newHouse)
                newHouse.addHouseResident(person)

                person.familyObjRef.removeFromFamily(person)
                person.familyName = newFamilyName
                person.lastName = newFamilyName
                person.familyObjRef = family
                person.setOriginFamilyObjectRef(family)
                if family.getFemaleNumber() == 0 and family.getMaleNumber() == 0:
                    family.setFoundedBy(person)
                    #HouseFunctions.addNewOwner(person, newHouse)
                family.addNewMember(person)
                PLEH.changedLastName(person, world, person.getFamilyName())

def hireEmployee(employee, tile, world):

    tile.addWorker(employee)
    employee.setOccupation(tile)
    employee.setOccupationName(tile.getOccupationName())
    employee.increaseHappiness(15)
    PLEH.foundEmpoyment(employee, world)

    return

def fireAllEmployees(tile, world):

    for worker in tile.getWorkerList():
        worker.getOccupation().removeWorker(worker)
        worker.setOccupation(None)
        worker.setOccupationName('')
        worker.increaseHappiness(-15)
        PLEH.lostEmpoyment(worker, world)

    return

def fireEmployeesWithPoorHealth(tile, world):

    for worker in tile.getWorkerList():
        if worker.getGeneralHealth().value[0] >= Enums.GeneralHealth.POOR.value[0]:
            PLEH.lostEmpoymentDueToHealth(worker, world)
            worker.getOccupation().removeWorker(worker)
            worker.setOccupation(None)
            worker.setOccupationName('')
            worker.increaseHappiness(-15)

    return