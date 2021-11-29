from Enums import LifeStatus, MaritalStatus, CauseOfDeath, Sexes
import Utils
import time
import PeopleFunctions as PF
import PeopleInterface as PI
import FamilyFunctions as FF

def increaseAge (people):

    for person in people:
        if person.lifeStatus != LifeStatus.DEAD:
            person.increaseAge()
            if person.age == 15:
                person.familyObjRef.moveChildToAdultMembers(person)
        if deathChanceFromAge(person) or person.age >= person.modifiedLifespan:
            PF.deathProcedures(person)

def birthPeople (world, families, people):

    for person in people:

        # person here is MOTHER
        # only Females can give birth beetween 15 and 45y old + must be alive and have spouse
        if person.lifeStatus == LifeStatus.ALIVE and person.sex == Sexes.FEMALE and 15 <= person.age <= 45 and person.spouse is not None:

            #spouseObj for simplicity
            spouseObj = person.spouse
            # is spouse alive
            if spouseObj.lifeStatus == LifeStatus.ALIVE:
                chanceOfBirth = Utils.randomRange(1, 100)
                if chanceOfBirth <= min(person.fertility, spouseObj.fertility):
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
                        PF.deathProcedures(person)

                    break

    return


def deathChanceFromAge (person):

    chanceOfDeath = Utils.randomRange(1, 100)
    dead = False

    age = person.age
    lifespan = person.lifespan

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
    elif lifespan-age <= 5:
        if chanceOfDeath >= 100 - (lifespan-age) * 2:
            person.causeOfDeath = CauseOfDeath.AGE
            dead = True

    return dead

def deathChangeFromGivingBirth (person, child, modifier=0):

    motherDeath = False
    childDeath = False
    numberOfChildren = person.childrenNumber
    chanceOfMotherDeath = 100

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