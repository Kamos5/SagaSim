from Enums import LifeStatus, MaritalStatus, CauseOfDeath, Sexes, Settlements
import Utils
import time
import Family as Family
import Parameters
import FamilyNameGenerator as FNG
import PeopleFunctions as PF
import PeopleInterface as PI
import FamilyFunctions as FF

def increaseAge (people):

    for person in people:
        if person.lifeStatus != LifeStatus.DEAD:
            person.increaseAge()
            #if person.age < 15:
            #    deathFromNegligence(person)
            if person.age == 15:
                person.familyObjRef.moveChildToAdultMembers(person)
            if deathChanceFromAge(person) or person.age >= person.modifiedLifespan:
                PF.deathProcedures(person)

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
                if chanceOfBirth <= min(person.fertility, spouseObj.fertility) * spouseObj.getSettlement().getBaseFertility()*spouseObj.getSettlement().getFertilityModifier() / 100:
                    # CHILD object
                    personObj = PF.birthChild(world, person, spouseObj)
                    # add child to proper family
                    personObj.familyObjRef.addNewMember(personObj)
                    people.append(personObj)
                    person.numberOfChildren += 1
                    spouseObj.numberOfChildren += 1
                    if person.modifiedLifespan-person.age > 1:
                        person.modifiedLifespan -= 1
                    person.childrens.append(personObj)
                    spouseObj.childrens.append(personObj)

                    # change of dying from childbirth (mother and child)
                    motherDeath, childdeath = deathChangeFromGivingBirth(person, personObj)

                    if motherDeath:
                        PF.deathProcedures(person)
                        #FF.RemoveFromAdultMemberList(families, person)

                    if childdeath:
                        #parameters: child
                        PF.deathProcedures(personObj)

                    births += 1

    print("Births per year:" + str(births))


    return

def settlementsPopulationManagement (world):

    for region in world.getRegions():
        for settlement in region.getSettlements():
            #TODO WHAT IF CITY DIES OFF? WILL IT CONVERT INTO VILLAGE
            if settlement.getPopulation() >= int(settlement.getMaxPopulation() * 0.75):
                #TODO CHANCE FOR MIGRATION??
                chanceOfMigration = Utils.randomRange(1, 100)
                if chanceOfMigration < 20:
                    lowestSettlementInRegion = region.getLowestPopulatedSettlement(world)
                    newTargetSettlement = lowestSettlementInRegion
                    if lowestSettlementInRegion.getPopulation() > int(lowestSettlementInRegion.getMaxPopulation() * 0.50):
                        if region.canAddSettlement():
                            newSettlement = region.addSettlement()
                            newSettlement.setMaxPopulation = Parameters.baseVillageSize
                            newTargetSettlement = newSettlement
                    randomMigrantsList = prepareMigration(settlement)
                    iniciateMigration(randomMigrantsList, newTargetSettlement)

def prepareMigration(settlement):

    migrantFamilies = 0
    if settlement.getSettlementType() == Settlements.TOWN:
        mirgrationWave = 15
    else:
        mirgrationWave = 10

    randomMigrantsList = []
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
        migrantFamilies += 1


    return randomMigrantsList

def iniciateMigration(migrantList, settlementTarget):

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

    chanceOfChaningLastName = Utils.randomRange(1, 100)

    # newLastName = ''
    # if chanceOfChaningLastName < 10:
    #     newFamilyName = FNG.getNewRandomLastName()
    #     family = Family(newFamilyName)
    #     family.setFoundingYear(world.getYear())
    #     family.setOriginRegion(world.getRegionFromIndex(0))

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

    if person.father.lifeStatus == LifeStatus.DEAD and person.mother.lifeStatus == LifeStatus.DEAD:
        chanceOfDeath = Utils.randomRange(1, 100)
        if chanceOfDeath > 100 - (Utils.triangularNumber(person.age-1)):
            person.causeOfDeath = CauseOfDeath.NEGLIGENCE

        PF.deathProcedures(person)

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
        if chanceOfDeath <= 100 - (modifiedLifespan-age) * 2:
            person.causeOfDeath = CauseOfDeath.AGE
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

