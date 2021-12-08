from Enums import LifeStatus, MaritalStatus, CauseOfDeath, Sexes, Settlements
import Utils
import time
from Family import Family as Family
import Parameters
import FamilyNameGenerator as FNG
import PeopleFunctions as PF
import PersonLifeEventsHistory as PLEH
import PeopleInterface as PI
import FamilyFunctions as FF
import SettlementsFunctions as SF

def increaseAge (people, world):

    for person in people:
        if person.lifeStatus != LifeStatus.DEAD:
            person.increaseAge()
            if person.age == 15:
                person.familyObjRef.moveChildToAdultMembers(person)
                PLEH.adulthoodReached(person, world)
            if deathChanceFromAge(person) or person.age >= person.modifiedLifespan:
                PF.deathProcedures(person, world)

def birthPeople (world, people):

    births = 0
    for person in people:

        # person here is MOTHER
        # only Females can give birth beetween 15 and 45y old + must be alive and have spouse
        if person.lifeStatus == LifeStatus.ALIVE and person.sex == Sexes.FEMALE and 15 <= person.age <= 45 and person.spouse is not None:

            #spouseObj for simplicity
            spouseObj = person.spouse
            # is spouse alive
            if spouseObj.lifeStatus == LifeStatus.ALIVE:
                chanceOfBirth = Utils.randomRange(1, 100)
                personSexualityModifier = 1
                spouseObjSexualityModifier = 1
                if person.sexuality == 'homo':
                    personSexualityModifier = 0.66
                if spouseObj.sexuality == 'homo':
                    spouseObjSexualityModifier = 0.33

                if chanceOfBirth <= min(person.fertility, spouseObj.fertility) * spouseObj.getSettlement().getBaseFertility() * spouseObj.getSettlement().getFertilityModifier() * personSexualityModifier * spouseObjSexualityModifier/ 100:
                    # CHILD object
                    personObj = PF.birthChild(world, person, spouseObj)
                    # add child to proper family
                    personObj.familyObjRef.addNewMember(personObj)
                    people.append(personObj)
                    PLEH.beenBorn(personObj, world)
                    person.numberOfChildren += 1
                    spouseObj.numberOfChildren += 1
                    if person.modifiedLifespan-person.age > 1:
                        person.modifiedLifespan -= 1
                    person.childrens.append(personObj)
                    spouseObj.childrens.append(personObj)

                    # change of dying from childbirth (mother and child)
                    motherDeath, childdeath = deathChangeFromGivingBirth(person, personObj)

                    if motherDeath:
                        PF.deathProcedures(person, world)

                    if childdeath:
                        #parameters: child
                        PF.deathProcedures(personObj, world)

                    births += 1

    print("Births per year:" + str(births))


    return

def settlementsPopulationManagement (world, families):

    for region in world.getRegions():

        for settlement in region.getSettlements():

            villagesList = SF.getVillages(region.getSettlements())
            townList = SF.getCities(region.getSettlements())

            if settlement.getPopulation() >= int(settlement.getMaxPopulation() * Parameters.percentagePopulationThresholdForMigration):
                chanceOfMigration = Utils.randomRange(1, 100)
                if chanceOfMigration < Parameters.chanceForMigration:
                    if len(region.getSettlements()) == region.regionSize:
                        newTargetSettlement = Utils.randomFromCollection(townList)
                    else:
                        lowestSettlementInRegion = region.getLowestPopulatedSettlement(world)
                        newTargetSettlement = lowestSettlementInRegion
                        if lowestSettlementInRegion.getPopulation() > int(lowestSettlementInRegion.getMaxPopulation() * Parameters.percentageVillagePopulationThresholdForCreatingNewVillage):
                            if region.canAddSettlement():
                                newSettlement = region.addSettlement(world)
                                newSettlement.setMaxPopulation = Parameters.baseVillageSize
                                newTargetSettlement = newSettlement
                    complexRandomMigrantsList = prepareMigration(settlement, world)
                    iniciateMigration(complexRandomMigrantsList, newTargetSettlement)
                    splitFamilies(world, region, families, newTargetSettlement, complexRandomMigrantsList)

        randomVillage = Utils.randomFromCollection(villagesList)
        if len(villagesList) >= (len(townList)+1) * (Parameters.villageToTownMultiplier + 1) - len(townList) and randomVillage.getPopulation() > int(randomVillage.getMaxPopulation() * Parameters.percentageVillagePopulationThresholdForUpgradeToTown):

            chanceOfUpgradingToCity = Utils.randomRange(1, 100)
            if chanceOfUpgradingToCity < Parameters.chancePerYearToUpgradeVillageToTown:
                randomVillage.changeSettlementType(Settlements.TOWN)



def prepareMigration(settlement, world):

    migrantFamilies = 0
    if settlement.getSettlementType() == Settlements.TOWN:
        mirgrationWave = Parameters.migrationWaveForTown
    else:
        mirgrationWave = Parameters.migrationWaveForTown

    randomMigrantsList = []
    complexRandomMigrantList = []
    # random 20 people with their alive children move to new Village
    for migrantFamilies in range(mirgrationWave):
        randomPerson = Utils.randomFromCollection(settlement.getResidents())
        if randomPerson not in randomMigrantsList:
            # for MINOR
            if randomPerson.age < 15:
                getRandomMigrantListForSingleRandomPerson(randomPerson, "Father", randomMigrantsList)
                getRandomMigrantListForSingleRandomPerson(randomPerson, "Mother", randomMigrantsList)
            else:
                # for Adult
                getRandomMigrantListForSingleRandomPerson(randomPerson, "Adult", randomMigrantsList)
            if len(randomMigrantsList) > 0:
                complexRandomMigrantList.append(randomMigrantsList)
                PLEH.movedHome(randomPerson, settlement, world)
                migrantFamilies += 1
                randomMigrantsList = []


    return complexRandomMigrantList

def splitFamilies(world, region, families, newTargetSettlement, complexRandomMigrantsList):


    for randomMigrantList in complexRandomMigrantsList:
        chanceOfChangingLastName = Utils.randomRange(1, 100)
        #won't change last name if only 1 person will be in migrant list whose culture sex is not to inherite
        if chanceOfChangingLastName < Parameters.chanceForChangingLastNameDuringMigration and (len(randomMigrantList) > 1 or randomMigrantList[0].familyObjRef.getOriginCulture().getInheritanceBy() != randomMigrantList[0].sex):
            newFamilyName = FNG.getNewRandomLastName()
            family = Family(newFamilyName)
            family.setFoundingYear(world.getYear())
            family.setOriginRegion(region)
            family.setOriginSettlement(newTargetSettlement)
            family.setOriginCulture(randomMigrantList[0].familyObjRef.getOriginCulture())
            family.setFamilyBranchedFrom(randomMigrantList[0].familyObjRef)
            randomMigrantList[0].familyObjRef.addOffspringBranch(family)
            families.append(family)

            for person in randomMigrantList:
                person.familyObjRef.removeFromFamily(person)
                person.familyName = newFamilyName
                person.lastName = newFamilyName
                person.familyObjRef = family
                if family.getFemaleNumber() == 0 and family.getMaleNumber() == 0:
                    family.setFoundedBy(person)
                family.addNewMember(person)





def iniciateMigration(complexMigrantList, settlementTarget):

    for migrantList in complexMigrantList:
        for migrant in migrantList:
            migrant.getSettlement().decreasePopulation()
            migrant.getSettlement().removeResident(migrant)
            migrant.setSettlement(settlementTarget)
            settlementTarget.increasePopulation()
            settlementTarget.addResident(migrant)


def getRandomMigrantListForSingleRandomPerson(person, parent, randomMigrantsList):

    getParent = ''
    if person.getFather().lifeStatus != LifeStatus.DEAD:
        if parent == "Father":
            getParent = person.getFather()
    if person.getMother().lifeStatus != LifeStatus.DEAD:
        if parent == "Mother":
            getParent = person.getMother()
    if parent == "Adult":
        getParent = person

    if getParent != '':
        if getParent not in randomMigrantsList:
            # if newLastName != '':
            #     getParent.lastName = newLastName
            randomMigrantsList.append(getParent)

        parentChildrensList = getParent.childrens
        for parentChildren in parentChildrensList:
            if parentChildren.age < 15:
                if parentChildren not in randomMigrantsList:
                    randomMigrantsList.append(parentChildren)

        if getParent.spouse is not None:
            if getParent.spouse not in randomMigrantsList:
                randomMigrantsList.append(getParent.spouse)
                # if newLastName != '':
                #     getParent.lastName = newLastName

            parentSpouseChildrensList = getParent.spouse.childrens
            for parentSpouseChildren in parentSpouseChildrensList:
                if parentSpouseChildren.age < 15:
                    if parentSpouseChildren not in randomMigrantsList:
                        randomMigrantsList.append(parentSpouseChildren)
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
        chanceOfMotherDeath = Utils.randomRange(1, 95)
    elif numberOfChildren == 2:
        chanceOfMotherDeath = Utils.randomRange(1, 90)
    else:
        chanceOfMotherDeath = Utils.randomRange(1, 85)

    if chanceOfMotherDeath > 80 + modifier:
        person.causeOfDeath = CauseOfDeath.CHILDBIRTH
        motherDeath = True

    chanceOfChildsDeath = Utils.randomRange(1, 100)

    if chanceOfChildsDeath > 90 + modifier:
        child.causeOfDeath = CauseOfDeath.CHILDBIRTH
        childDeath = True

    return motherDeath, childDeath

