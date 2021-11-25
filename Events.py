from Enums import LifeStatus, MaritalStatus
import Utils
import PeopleFunctions as MF
import PeopleInterface as PI
import FamilyFunctions as FF

def increaseAge (people):

    for person in people:
        if person.lifeStatus != LifeStatus.DEAD:
            person.increaseAge()
        if deathChanceFromAge(person.age, person.modifiedLifespan) or person.age >= person.modifiedLifespan:
            person.changeAgeStatus(LifeStatus.DEAD)
            person.maritalStatus = MaritalStatus.DEAD
            person.lifeStatus = LifeStatus.DEAD
            if person.spouse != '':
                if PI.findOnePersonObj(people, person.spouse).sex == "M":
                    PI.findOnePersonObj(people, person.spouse).maritalStatus = MaritalStatus.WIDOWER
                else:
                    PI.findOnePersonObj(people, person.spouse).maritalStatus = MaritalStatus.WIDOW
            MF.removeSpouses(people, person.personUUID, person.spouse)


def birthPeople (world, families, people):

    for person in people:

        if person.sex == "F" and 15 <= person.age <= 45 and person.lifeStatus == LifeStatus.ALIVE and person.spouse != '':
            if (PI.findOnePersonObj(people, person.spouse).lifeStatus == LifeStatus.ALIVE):

                chanceOfBirth = Utils.randomRange(1, 100)
                if chanceOfBirth <= min(person.fertility, PI.findOnePersonObj(people, person.spouse).fertility):
                    personObj = MF.birthChild(world, people, person.personUUID, person.spouse)
                    for family in families:
                        if family.familyName == personObj.familyName:
                            family.addNewMember(personObj)
                            family.increaseChildrenNumber()
                            people.append(personObj)
                            person.numberOfChildren += 1
                            PI.findOnePersonObj(people, person.spouse).numberOfChildren += 1
                            if person.modifiedLifespan-person.age > 1:
                                person.modifiedLifespan -= 1

    return


def deathChanceFromAge (age, lifespan):

    chanceOfDeath = Utils.randomRange(1, 100)

    dead = False

    if age == 1:
        if chanceOfDeath <= 25:
            dead = True
    if age == 2:
        if chanceOfDeath <= 15:
            dead = True
    if age == 3:
        if chanceOfDeath <= 10:
            dead = True
    if age == 4:
        if chanceOfDeath <= 5:
            dead = True
    if age == 5:
        if chanceOfDeath <= 3:
            dead = True
    if lifespan-age <= 5:
        if chanceOfDeath >= 100 - (lifespan-age) * 2:
            dead = True

    return dead

