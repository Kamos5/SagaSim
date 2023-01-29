import HouseFunctions
from Enums import LifeStatus, MaritalStatus, CauseOfDeath, Sexes, Settlements, Traits
import Utils
from Family import Family as Family
import Parameters
import FamilyNameGenerator as FNG
import PeopleFunctions as PF
import PersonLifeEventsHistory as PLEH
from Enums import MaritalStatus as MS
import SettlementsFunctions as SF
import SettlementFeatures as SFeat

def increaseAge (world):

    for person in world.getAlivePeople():
        if person.lifeStatus != LifeStatus.DEAD:
            person.increaseAge()
            if person.age < 15:
                person.increaseHeight()
            if person.age == 15:
                person.height = person.heightGen
                person.familyObjRef.moveChildToAdultMembers(person)
                person.changeMaritalStatus(MS.SINGLE)
                PLEH.adulthoodReached(person, world)
            if deathChanceFromAge(person) or person.age >= person.modifiedLifespan:
                PF.deathProcedures(person, world)

            if person.age > 50:
                PF.retirement(person, world)

def birthPeople (world):

    births = 0
    for person in world.getAlivePeople():

        # person here is MOTHER
        # only Females can give birth beetween 15 and 45y old + must be alive and have spouse
        if person.sex == Sexes.FEMALE and 15 <= person.age <= 45 and person.spouse is not None and person.lifeStatus == LifeStatus.ALIVE:

            # change spouseRelation based on liked/disliked traits
            changeRelationToFromSpouse(person)
            # is spouse alive
            if person.getSpouse().lifeStatus == LifeStatus.ALIVE:
                chanceOfBirth = Utils.randomRange(1, 100)

                if person.sexuality == 'homo':
                    person.setSpouseRelation(-5)
                if person.getSpouse().sexuality == 'homo':
                    person.getSpouse().setSpouseRelation(-5)

                if (chanceOfBirth <= min(person.fertility, person.getSpouse().fertility) * person.getSpouse().getSettlement().getBaseFertility() * person.getSpouse().getSettlement().getFertilityModifier() * person.getPersonalSexualModifier() * person.getSpouse().getPersonalSexualModifier()) and person.spouseRelation > 0:
                    # CHILD object
                    person.changeSpouseRelation(25)
                    person.getSpouse().changeSpouseRelation(25)
                    childObj = PF.birthChild(world, person, person.getSpouse())
                    # add child to proper family
                    childObj.familyObjRef.addNewMember(childObj)
                    world.addPerson(childObj)
                    world.addAlivePerson(childObj)
                    PLEH.beenBorn(childObj, world)
                    person.numberOfChildren += 1
                    person.getSpouse().numberOfChildren += 1
                    if person.modifiedLifespan-person.age > 1:
                        if Utils.randomRange(1, 2) == 1:
                            person.modifiedLifespan -= 1
                    person.appendAliveChildrenList(childObj)
                    person.getSpouse().appendAliveChildrenList(childObj)
                    childObj.changeMaritalStatus(MS.CHILD)
                    person.getAccommodation().addHouseResident(childObj)

                    # change of dying from childbirth (mother and child)
                    motherDeath, childdeath = deathChangeFromGivingBirth(person, childObj)

                    if motherDeath:
                        PF.deathProcedures(person, world)

                    if childdeath:
                        #parameters: child
                        PF.deathProcedures(childObj, world)

                    births += 1

    world.appendBirthsPerYear(births)


    return

def changeRelationToFromSpouse(person):

    person.spouseRelation += person.getSpouseNumberOfLikedTraits()*5
    person.spouseRelation += -person.getSpouseNumberOfDislikedTraits() * 5
    person.getSpouse().spouseRelation += person.getSpouse().getSpouseNumberOfLikedTraits() * 5
    person.getSpouse().spouseRelation += -person.getSpouse().getSpouseNumberOfDislikedTraits() * 5


def settlementsPopulationManagement (world):

    for region in world.getRegions():

        for settlement in region.getSettlements():
            villagesList = SF.getVillages(region.getSettlements())
            townList = SF.getCities(region.getSettlements())

            #Treshhold to create migration wave
            if settlement.getPopulation() >= int(settlement.getMaxPopulation() * Parameters.percentagePopulationThresholdForMigration):
                chanceOfMigration = Utils.randomRange(1, 100)
                #Chance of migration happening
                if chanceOfMigration < Parameters.chanceForMigration:
                    #Check for max size of region
                    if len(region.getSettlements()) == region.regionSize:
                        newTargetSettlement = Utils.randomFromCollection(region.getSettlements())

                    else:
                        # TODO FIX PEOPLE CAN MOVE TO THE SAME VILLAGE
                        #Take lowest population as dest
                        lowestSettlementInRegion = region.getLowestPopulatedSettlement()
                        newTargetSettlement = lowestSettlementInRegion
                        #If lowest pop > lowest max pop * modifier create new setttlement
                        if lowestSettlementInRegion.getPopulation() > int(lowestSettlementInRegion.getMaxPopulation() * Parameters.percentageVillagePopulationThresholdForCreatingNewVillage):
                            newSettlement = region.addSettlement(world)
                            newSettlement.setRegion(settlement.getRegion())
                            newSettlement.setMaxPopulation = Parameters.baseVillageSize
                            newTargetSettlement = newSettlement

                    #Migration Wave
                    complexRandomMigrantsList = prepareMigration(settlement, newTargetSettlement, world)
                    iniciateMigration(complexRandomMigrantsList, newTargetSettlement, world)
                    splitFamiliesInMigration(world, region, newTargetSettlement, complexRandomMigrantsList)

            #Upgrading from Village to City
            randomVillage = Utils.randomFromCollection(villagesList)
            if len(villagesList) >= (len(townList)+1) * (Parameters.villageToTownMultiplier + 1) - len(townList) and randomVillage.getPopulation() > int(randomVillage.getMaxPopulation() * Parameters.percentageVillagePopulationThresholdForUpgradeToTown):

                chanceOfUpgradingToCity = Utils.randomRange(1, 100)
                if chanceOfUpgradingToCity < Parameters.chancePerYearToUpgradeVillageToTown:
                    randomVillage.changeSettlementType(Settlements.TOWN)
                    Utils.randomFromCollection(randomVillage.getRegion().getVillagesExProvisionToThisTown(randomVillage)).setProvision(randomVillage)
                    Utils.randomFromCollection(randomVillage.getRegion().getVillagesExProvisionToThisTown(randomVillage)).setProvision(randomVillage)
                    Utils.randomFromCollection(randomVillage.getRegion().getVillagesExProvisionToThisTown(randomVillage)).setProvision(randomVillage)

def settlementGoodsProduction(world):

    for region in world.getRegions():

        for settlement in region.getSettlements():

            ##FOOD PRODUCTION
            foodProd0 = settlement.getSettlementFoodProduced()
            for foodTile in settlement.getFoodFeatures():

                foodProd = foodTile.prodYield * foodTile.foundationType.value.yieldModifier / 100 * foodTile.getWorkersNumber()

                if settlement.getProvision() is not None:
                    settlement.getProvision().increaseSettlementFoodProduced(foodProd*Parameters.socage)
                    settlement.increaseSettlementFoodProduced(foodProd*(1-Parameters.socage))
                else:
                    settlement.increaseSettlementFoodProduced(foodProd)

                for worker in foodTile.getWorkerList():
                    workerModifier = 0
                    if Traits.LAZY in worker.getTraits():
                        workerModifier = -10
                    if Traits.DILIGENT in worker.getTraits():
                        workerModifier = 10
                    goodProduced = foodTile.prodYield * (foodTile.foundationType.value.yieldModifier + workerModifier) / 100
                    worker.changeFreeWealth(goodProduced * (100 - settlement.getLocalIncomeTax()) / 100)
                    settlement.changeFreeWealth(goodProduced * (settlement.getLocalIncomeTax()) / 100)

            foodProd1 = settlement.getSettlementFoodProduced()
            settlement.setSettlementFoodProducedLastYear(foodProd1-foodProd0)

            foodConsumed = 0
            for resident in settlement.getResidents():
                if resident.getAge() < 10:
                    foodConsumed += 0.5
                    settlement.increaseSettlementFoodConsumed(0.5)
                elif 10 <= resident.getAge() < 15:
                    foodConsumed += 0.75
                    settlement.increaseSettlementFoodConsumed(0.75)
                else:
                    foodConsumed += 1
                    settlement.increaseSettlementFoodConsumed(1)
            settlement.setSettlementFoodConsumedLastYear(foodConsumed)
            if settlement.getFreeFood() + (foodProd1 - foodProd0) - foodConsumed < 0:
                settlement.setFreeFood(0)
            else:
                settlement.changeFreeFood(foodProd1 - foodProd0 - foodConsumed)

            settlement.setNetFoodLastYear(foodProd1-foodProd0-foodConsumed)

            ##PRODUCTION PRODUCTION
            prodProd0 = settlement.getSettlementProdProduced()

            for prodTile in settlement.getProdFeatures():

                prodProd = prodTile.prodYield * prodTile.foundationType.value.yieldModifier / 100 * prodTile.getWorkersNumber()

                if settlement.getProvision() is not None:
                    settlement.getProvision().increaseSettlementFoodProduced(prodProd*Parameters.socage)
                    settlement.increaseSettlementFoodProduced(prodProd*(1-Parameters.socage))
                else:
                    settlement.increaseSettlementFoodProduced(prodProd)
                for worker in prodTile.getWorkerList():
                    workerModifier = 0
                    if Traits.LAZY in worker.getTraits():
                        workerModifier = -10
                    if Traits.DILIGENT in worker.getTraits():
                        workerModifier = 10
                    goodProduced = prodTile.prodYield * (prodTile.foundationType.value.yieldModifier + workerModifier) / 100
                    worker.changeFreeWealth(goodProduced * (100-settlement.getLocalIncomeTax())/100)
                    settlement.changeFreeWealth(goodProduced * (settlement.getLocalIncomeTax())/100)

            prodProd1 = settlement.getSettlementProdProduced()
            settlement.changeFreeProd(prodProd1 - prodProd0)
            settlement.setSettlementProdProducedLastYear(prodProd1 - prodProd0)


            #UPGRADING FEATURES

            if float(settlement.getFreeProd()) > 0:
#                if settlement.getSettlementFoodProducedLastYear() - settlement.getSettlementFoodConsumedLastYear() < int(round(len(settlement.getResidents())/2)):
                    for tile in settlement.getFoodFeatures():
                        if len(SFeat.getPotencialUpgradesForZone(tile.getName())) > 0:
                            upgradable = Utils.randomFromCollectionWithWeight(SFeat.getPotencialUpgradesForZone(tile.getName()))
                            #for upgradable in (SFeat.getPotencialUpgradesForZone(tile.getName())):
                            if float(settlement.getFreeProd()) >= float(upgradable.value.getUpgradeCost()):
                                settlement.changeFreeProd(-upgradable.value.getUpgradeCost())
                                newFeature = SFeat.createZones()[SFeat.getFeatureIndexFromName(upgradable.value.getName())]
                                settlement.upgradeTile(tile, newFeature)
                                return

                    for tile in settlement.getProdFeatures():
                        if len(SFeat.getPotencialUpgradesForZone(tile.getName())) > 0:
                            upgradable = Utils.randomFromCollectionWithWeight(SFeat.getPotencialUpgradesForZone(tile.getName()))
    #                        for upgradable in (SFeat.getPotencialUpgradesForZone(tile.getName())):
                            if float(settlement.getFreeProd()) >= float(upgradable.value.getUpgradeCost()):
                                settlement.changeFreeProd(-upgradable.value.getUpgradeCost())
                                newFeature = SFeat.createZones()[SFeat.getFeatureIndexFromName(upgradable.value.getName())]
                                settlement.upgradeTile(tile, newFeature)
                                return


def accommodationManagment(world):

    for region in world.getRegions():

        for settlement in region.getSettlements():

            for house in settlement.getHousing():

                HouseFunctions.payForUpkeep(house)

                if house.getHouseDurability() == 0:
                    if len(house.getHouseResidents()) == 0:
                        settlement.removeHouse(house)
                    else:
                        HouseFunctions.downgradeHouse(house)

                HouseFunctions.payForUpgrade(house)


def settlementWorkersManagement(world):

    for region in world.getRegions():

        for settlement in region.getSettlements():

                unemployedWorkerList = settlement.getUnemployedResidentsList()

            #if settlement.getSettlementFoodProducedLastYear() - settlement.getSettlementFoodConsumedLastYear() < int(round(len(settlement.getResidents())/2)):
                for foodTile in settlement.getFoodFeatures():

                    for occupations in range(foodTile.getFreeWorkersSlots()):
                        if len(unemployedWorkerList) > 0:
                            newWorker = Utils.randomFromCollection(unemployedWorkerList)
                            unemployedWorkerList.remove(newWorker)
                            foodTile.addWorker(newWorker)
                            newWorker.setOccupation(foodTile)
                            newWorker.setOccupationName(foodTile.getOccupationName())
                            PLEH.foundEmpoyment(newWorker, world)
            #else:
                for prodTile in settlement.getProdFeatures():

                    for occupations in range(prodTile.getFreeWorkersSlots()):

                        if len(unemployedWorkerList) > 0:
                            newWorker = Utils.randomFromCollection(unemployedWorkerList)
                            unemployedWorkerList.remove(newWorker)
                            prodTile.addWorker(newWorker)
                            newWorker.setOccupation(prodTile)
                            newWorker.setOccupationName(prodTile.getOccupationName())
                            PLEH.foundEmpoyment(newWorker, world)


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

def splitFamiliesInMigration(world, region, newTargetSettlement, complexRandomMigrantsList):


    for randomMigrantList in complexRandomMigrantsList:
        chanceOfChangingLastName = Utils.randomRange(1, 100)
        #won't change last name if only 1 person will be in migrant list whose culture sex is not to inherite
        if (chanceOfChangingLastName < Parameters.chanceForChangingLastNameDuringMigration and
                len(randomMigrantList) > 1 and
                randomMigrantList[0].familyObjRef.aliveMemberNumber > 1 and
                randomMigrantList[0].familyObjRef.getOriginCulture().getInheritanceBy() != randomMigrantList[0].sex):
            chanceForRevingAncestralFamily = Utils.randomRange(1, 100)

            if chanceForRevingAncestralFamily > 20:
                newFamilyName = FNG.getNewRandomLastName()
                family = Family(newFamilyName)
                family.setFoundingYear(world.getYear())
                family.setOriginRegion(region)
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
                    newFamilyName = FNG.getNewRandomLastName()
                    family = Family(newFamilyName)
                    family.setFoundingYear(world.getYear())
                    family.setOriginRegion(region)
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

def crime(world):

    crimeLevel = 0
    crimeHomicideTemp = 0
    crimeAssaultTemp = 0
    crimeBurglaryTemp = 0
    crimeTheftTemp = 0
    crimeFailedTemp = 0

    for person in world.getAlivePeople():
        randomChanceForCrime = Utils.randomRange(1, 100)
        if randomChanceForCrime < 5 and (Traits.VENGEFUL in person.getTraits() or Traits.GREEDY in person.getTraits() or Traits.DECEITFUL in person.getTraits() and person.getOccupation() is None) and person.getAge() > 15 and person.getLifeStatus() == LifeStatus.ALIVE and person.getFreeWealth() < person.getSettlement().getAvarageResidentsWealth():
            randomPerson = Utils.randomFromCollection(person.getSettlement().getResidents())
            if randomPerson != person and randomPerson != person.spouse and randomPerson not in person.getAliveChildrenList():
                randomCrime = Utils.randomRange(1, 100)
                #homicide
                if randomCrime < 10:
                    # print("Homicide")
                    PF.deathProcedures(randomPerson, world)
                    offenderIdentified = Utils.randomRange(1, 100)
                    if offenderIdentified > 50:
                        PLEH.killedByDuringCrime(randomPerson, person, world)
                    else:
                        PLEH.killedByDuringCrime(randomPerson, None, world)
                    PLEH.killedSMBDuringCrime(person, randomPerson, world)
                    loot = randomPerson.getFreeWealth()
                    randomPerson.setFreeWealth(loot / 2)
                    person.changeFreeWealth(loot)
                    crimeLevel += 1
                    crimeHomicideTemp += 1
                    continue
                if randomCrime < 30:
                    # print("Assault")
                    loot = randomPerson.getFreeWealth()
                    randomPerson.setFreeWealth(loot / 3)
                    person.changeFreeWealth(loot)
                    crimeLevel += 1
                    crimeAssaultTemp += 1
                    continue
                if randomCrime < 70:
                    # print("Burglary")
                    loot = randomPerson.getFreeWealth()
                    randomPerson.setFreeWealth(loot / 4)
                    person.changeFreeWealth(loot)
                    crimeLevel += 1
                    crimeBurglaryTemp += 1
                    continue
                if randomCrime < 90:
                    # print("Theft")
                    loot = randomPerson.getFreeWealth()
                    randomPerson.setFreeWealth(loot / 5)
                    person.changeFreeWealth(loot)
                    crimeLevel += 1
                    crimeTheftTemp += 1
                    continue
                if randomCrime <= 100:
                    # print("Crime failed")
                    crimeLevel += 1
                    crimeFailedTemp += 1
                    continue

    world.appendCrimesPerYear(crimeLevel, [crimeHomicideTemp, crimeAssaultTemp, crimeBurglaryTemp, crimeTheftTemp,crimeFailedTemp])

def moveFoodAndProduction(migrantSize, oldSettlement, newSettlement):

    foodPackages = 2 * migrantSize
    if oldSettlement.getFreeFood() > foodPackages:
        oldSettlement.changeFreeFood(foodPackages)
        newSettlement.changeFreeFood(foodPackages)

def iniciateMigration(complexMigrantList, settlementTarget, world):

    for migrantList in complexMigrantList:
        for migrant in migrantList:
            PLEH.movedHome(migrant, migrant.getSettlement(), settlementTarget, world)
            migrant.getSettlement().decreasePopulation()
            migrant.getSettlement().removeResident(migrant)
            migrant.setSettlement(settlementTarget)
            settlementTarget.increasePopulation()
            settlementTarget.addResident(migrant)


def getRandomMigrantListForSingleRandomPerson(person, parent, randomMigrantsList, settlement, world):

    getParent = ''
    if person.getFather() is not None and person.getFather().lifeStatus != LifeStatus.DEAD:
        if parent == "Father":
            getParent = person.getFather()
    if person.getFather() is not None and person.getMother().lifeStatus != LifeStatus.DEAD:
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




def deathFromNegligence(person):

    if person.father != '' and person.mother != '':
        if person.father.lifeStatus == LifeStatus.DEAD and person.mother.lifeStatus == LifeStatus.DEAD:
            chanceOfDeath = Utils.randomRange(1, 100)
            triangChance = (Utils.triangularNumber(person.age-1))
            if chanceOfDeath < 100 - triangChance:
                person.causeOfDeath = CauseOfDeath.NEGLIGENCE
                return True
    return False


def deathChanceFromAge(person):

    chanceOfDeath = Utils.randomRange(1, 100)
    dead = False

    age = person.age
    modifiedLifespan = person.modifiedLifespan

    if age == 1:
        if chanceOfDeath <= 20:
            dead = True
            person.causeOfDeath = CauseOfDeath.SICKNESS
    elif age == 2:
        if chanceOfDeath <= 15:
            person.causeOfDeath = CauseOfDeath.SICKNESS
            dead = True
    elif age == 3:
        if chanceOfDeath <= 10:
            person.causeOfDeath = CauseOfDeath.SICKNESS
            dead = True
    elif age == 4:
        if chanceOfDeath <= 5:
            person.causeOfDeath = CauseOfDeath.SICKNESS
            dead = True
    elif age == 5:
        if chanceOfDeath <= 3:
            person.causeOfDeath = CauseOfDeath.SICKNESS
            dead = True
    elif modifiedLifespan-age <= 5:
        if chanceOfDeath <= 100 - (modifiedLifespan-age) * 4:
            person.causeOfDeath = CauseOfDeath.AGE
            dead = True

    if person.age < 15:
        if deathFromNegligence(person):
            dead = True

    return dead


def deathChangeFromGivingBirth(person, child, modifier=0):

    motherDeath = False
    childDeath = False
    numberOfChildren = person.numberOfChildren
    chanceOfMotherDeath = 0

    if numberOfChildren == 0:
        chanceOfMotherDeath = Utils.randomRange(1, 100)
    elif numberOfChildren == 1:
        chanceOfMotherDeath = Utils.randomRange(1, 98)
    elif numberOfChildren == 2:
        chanceOfMotherDeath = Utils.randomRange(1, 95)
    else:
        chanceOfMotherDeath = Utils.randomRange(1, 90)

    if chanceOfMotherDeath > 88 + modifier:
        person.causeOfDeath = CauseOfDeath.CHILDBIRTH
        motherDeath = True

    chanceOfChildsDeath = Utils.randomRange(1, 100)

    if chanceOfChildsDeath > 90 + modifier:
        child.causeOfDeath = CauseOfDeath.CHILDBIRTH
        childDeath = True

    return motherDeath, childDeath

