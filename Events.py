from Enums import LifeStatus, MaritalStatus,CauseOfDeath
import Utils
import PeopleFunctions as PF
import PeopleInterface as PI
import FamilyFunctions as FF

def increaseAge (people):

    for person in people:
        if person.lifeStatus != LifeStatus.DEAD:
            person.increaseAge()
        if deathChanceFromAge(person.age, person.modifiedLifespan, person) or person.age >= person.modifiedLifespan:
            PF.deathProcedures(people, person)


def birthPeople (world, families, people):

    for person in people:

        # only Females can give birth beetween 15 and 45y old + must be alive and have spouse
        if person.sex == "F" and 15 <= person.age <= 45 and person.lifeStatus == LifeStatus.ALIVE and person.spouse != '':
            # is spouse alive
            if (PI.findOnePersonObj(people, person.spouse).lifeStatus == LifeStatus.ALIVE):
                chanceOfBirth = Utils.randomRange(1, 100)
                if chanceOfBirth <= min(person.fertility, PI.findOnePersonObj(people, person.spouse).fertility):
                    # child object
                    personObj = PF.birthChild(world, people, person.personUUID, person.spouse)
                    # add child to proper family
                    for family in families:
                        if family.familyName == personObj.familyName:
                            family.addNewMember(personObj)
                            family.increaseChildrenNumber()
                            people.append(personObj)
                            person.numberOfChildren += 1
                            PI.findOnePersonObj(people, person.spouse).numberOfChildren += 1
                            if person.modifiedLifespan-person.age > 1:
                                person.modifiedLifespan -= 1
                            person.childrens.append(personObj.personUUID)
                            PI.findOnePersonObj(people, person.spouse).childrens.append(personObj.personUUID)

                            # change of dying from childbirth (mother and child)
                            motherDeath, childdeath = deathChangeFromGivingBirth (person, personObj)

                            if (motherDeath):
                                PF.deathProcedures(people, person)
                                #FF.RemoveFromAdultMemberList(families, person)
                            if (childdeath):
                                PF.deathProcedures(people, personObj)

    return


def deathChanceFromAge (age, lifespan, person):

    chanceOfDeath = Utils.randomRange(1, 100)

    dead = False

    if age == 1:
        if chanceOfDeath <= 20:
            dead = True
            person.causeOfDeath = CauseOfDeath.SICKNESS
    if age == 2:
        if chanceOfDeath <= 15:
            person.causeOfDeath = CauseOfDeath.SICKNESS
            dead = True
    if age == 3:
        if chanceOfDeath <= 10:
            person.causeOfDeath = CauseOfDeath.SICKNESS
            dead = True
    if age == 4:
        if chanceOfDeath <= 5:
            person.causeOfDeath = CauseOfDeath.SICKNESS
            dead = True
    if age == 5:
        if chanceOfDeath <= 3:
            person.causeOfDeath = CauseOfDeath.SICKNESS
            dead = True
    if lifespan-age <= 5:
        if chanceOfDeath >= 100 - (lifespan-age) * 2:
            person.causeOfDeath = CauseOfDeath.AGE
            dead = True

    return dead

def deathChangeFromGivingBirth (person, child, modifier=0):

    motherDeath = False
    childDeath = False
    numberOfChildren = person.childrenNumber
    chanceOfMotherDeath = 0

    if numberOfChildren == 0:
        chanceOfMotherDeath = Utils.randomRange(1, 100)
    if numberOfChildren == 1:
        chanceOfMotherDeath = Utils.randomRange(1, 95)
    if numberOfChildren == 2:
        chanceOfMotherDeath = Utils.randomRange(1, 90)
    if numberOfChildren >= 3:
        chanceOfMotherDeath = Utils.randomRange(1, 85)

    if chanceOfMotherDeath > 80 + modifier:
        person.causeOfDeath = CauseOfDeath.CHILDBIRTH
        motherDeath = True

    chanceOfChildsDeath = Utils.randomRange(1, 100)

    if chanceOfChildsDeath > 90 + modifier:
        child.causeOfDeath = CauseOfDeath.CHILDBIRTH
        childDeath = True

    return motherDeath, childDeath

#
# def gettingSickness (person):
#     chanceOfGettingSick = Utils.randomRange(1, 100)
#     Sick = False
#
#     if chanceOfGettingSick <= 2:
#         Sick = True
#
#     return True
#