import Enums
from Person import Person as PersonObj
import Utils
import NameGenerator
from Enums import LifeStatus, MaritalStatus, HairColor, Sexes
import PersonLifeEventsHistory as PLEH

#mother, mother's spouse, trueMother, trueFather


def birthChild(world, parent1, parent2=None, trueParent1=None, trueParent2=None):

    firstName = []
    person = []
    numberOfChildren = 1
    if parent2 is None:
        secondParent = parent1
    else:
        secondParent = parent2

    sex, sexGen1, sexGen2 = Utils.geneticSex(trueParent1, trueParent2)

    randomChanceForBeingGay = Utils.randomRange(1, 100)

    if randomChanceForBeingGay < 10:
        sexuality = 'homo'
    else:
        sexuality = 'hetero'
    randomChanceForMultipleChildren = Utils.randomRange(1, 100)
    if randomChanceForMultipleChildren < 10:
        numberOfChildren += 1
    if randomChanceForMultipleChildren < 5:
        numberOfChildren += 1
    if randomChanceForMultipleChildren < 2:
        numberOfChildren += 1
    if randomChanceForMultipleChildren < 1:
        numberOfChildren += 1

    for number in range(numberOfChildren):
        if sex == Sexes.MALE:
            firstName.append(NameGenerator.getRandomMNameForRegion(parent1.getSettlement().getRegion().getRegionNumber()))
        else:
            firstName.append(NameGenerator.getRandomFNameForRegion(parent1.getSettlement().getRegion().getRegionNumber()))

    lifespan = Utils.geneticRandomFromValues(trueParent1.lifespan, trueParent2.lifespan)

    if lifespan > 100:
        lifespan = 100

    fertility = Utils.geneticRandomFromValues(trueParent1.fertility, trueParent2.fertility)

    #offspringHeight = Utils.geneticRandomFromValuesForHeight(trueParent1.height, trueParent2.height)
    if sex == Sexes.MALE:
        offspringHeight = int(trueParent2.height * Utils.randomRange(98, 103) / 100)
    else:
        offspringHeight = int(trueParent1.height * Utils.randomRange(98, 103) / 100)

    hairColor, hairColorGen1, hairColorGen2 = Utils.geneticHairColor(trueParent1, trueParent2)
    eyeColor, eyeColorGen1, eyeColorGen2 = Utils.geneticEyeColor(trueParent1, trueParent2)
    skinColor, skinColorGen1, skinColorGen2 = Utils.geneticSkinColor(trueParent1, trueParent2)

    for childFirstName in firstName:
        person.append(PersonObj())

    immunities = []
    for immunity in parent1.getImmunityTo():
        chanceToInheritImmunity = Utils.randomRange(1,2)
        if chanceToInheritImmunity == 1:
            immunities.append(immunity)

    for personObj, childFirstName in zip(person, firstName):
    #Child goes to father's family
        personObj.birthNewPerson(childFirstName, secondParent.familyName, secondParent.familyName, world.getDay(), world.getMonth(), world.getYear(), lifespan, sex,
                              sexGen1, sexGen2, sexuality, fertility, offspringHeight, hairColor, hairColorGen1, hairColorGen2, eyeColor, eyeColorGen1, eyeColorGen2,
                              skinColor, skinColorGen1, skinColorGen2, parent1, parent2, trueParent1, trueParent2, secondParent.familyObjRef, immunities)

        Utils.inheretTraits(personObj, parent1, secondParent, trueParent1, trueParent2)

    return person


def deathProcedures(person, world):

    if person.spouse is not None:
        person.spouse.addDeadSpouse(person)
        person.getSpouse().setSpouseRelation(0)
        person.getSpouse().changeSpouseNumberOfLikedTraits(-person.getSpouse().getSpouseNumberOfLikedTraits())
        person.getSpouse().changeSpouseNumberOfDislikedTraits(-person.getSpouse().getSpouseNumberOfDislikedTraits())
        # changing status of the spouse to WIDOW* and clearing spouse field
        if person.spouse.sex == Sexes.MALE:
            person.spouse.maritalStatus = MaritalStatus.WIDOWER
        else:
            person.spouse.maritalStatus = MaritalStatus.WIDOW

        person.spouse.familyObjRef.removeMarriedMember(person.spouse)
        person.spouse.familyObjRef.addUnmarriedMember(person.spouse)
        PLEH.lostSpouse(person.spouse, world)
        person.spouse.spouse = None
        person.spouse = None

    # else:
    #     #cleaning widowers and widows if they are also dead
    #     if person.maritalStatus == MaritalStatus.WIDOWER or person.maritalStatus == MaritalStatus.WIDOW:
    #         person.maritalStatus = MaritalStatus.DEAD

    person.familyObjRef.appendDeadMembersList(person)
    person.setSpouseRelation(0)
    person.changeSpouseNumberOfLikedTraits(-person.getSpouseNumberOfLikedTraits())
    person.changeSpouseNumberOfDislikedTraits(-person.getSpouseNumberOfDislikedTraits())
    # changing statutes
    person.changeLifeStatus(LifeStatus.DEAD)
    person.maritalStatus = MaritalStatus.DEAD
    person.yearOfDeath = world.getYear()
    PLEH.died(person, world)

    if person.age < 15:
        PLEH.lostChild(person.mother, person, world)
        if person.getFather() is not None:
            PLEH.lostChild(person.father, person, world)
    if person.getFather() is not None:
        person.getFather().getAliveChildrenList().remove(person)
        person.getFather().appendDeadChildrenList(person)
    if person.getMother() is not None:
        person.getMother().getAliveChildrenList().remove(person)
        person.getMother().appendDeadChildrenList(person)

    if person.getOccupation() is not None:
        person.getOccupation().removeWorker(person)
        person.setOccupation(None)

    #wealth inheretance (to children only)
    for child in person.getAliveChildrenList():
        inheritance = person.getFreeWealth() / len(person.getAliveChildrenList())
        if inheritance > 0:
            child.changeFreeWealth(inheritance)
            PLEH.inheritFromParent(child, person, inheritance, world)

    #If no alive children city takes it all
    if len(person.getAliveChildrenList()) == 0:
        person.getSettlement().changeFreeWealth(person.getFreeWealth())

    person.setFreeWealth(0)

    person.getSettlement().decreasePopulation()
    person.getSettlement().removeResident(person)

    person.getAccommodation().removeHouseResident(person)
    person.setAccommodation(None)


    for friend in person.getFriends():
        friend.removeFriend(person)
        PLEH.lostFriend(friend, person, world)
        person.removeFriend(friend)

    for rival in person.getRivals():
        rival.removeRival(person)
        PLEH.lostRival(rival, person, world)
        person.removeRival(rival)

    for lover in person.getLovers():
        PLEH.lostLover(lover, person, world)
        lover.removeLover(person)
        person.removeLover(lover)


    # adding dead kids to the list od dead children
    # not needed. all kids that have Status.DEAD in child list is what we need

    return

def retirement(person,world):

    if person.getOccupation() is not None:
        person.getOccupation().removeWorker(person)
        person.setOccupation(None)
        person.setOccupationName("Retired")
        PLEH.retired(person, world)

def canBeLover(person1, person2):

    if person1 == person2:
        return False

    if person1.getSexuality() == 'homo' and person2.getSexuality() == person1.getSexuality() and person2.getSex() == person1.getSex():
        return True

    if person1.getSexuality() == 'hetero' and person2.getSexuality() == person2.getSexuality() and person1.getSex() != person2.getSex():
        if toBeLoverCounter(person1) > 0 and toBeLoverCounter(person2) > 0:
            return True
        else:
            return False

def toBeLoverCounter(person):

    loverCounter = 0
    if Enums.Traits.LUSTFUL in person.getTraits():
        loverCounter += 3

    if Enums.Traits.CHASTE in person.getTraits():
        loverCounter -= 3

    if Enums.Traits.DECEITFUL in person.getTraits():
        loverCounter += 2

    if Enums.Traits.HONEST in person.getTraits():
        loverCounter += 2

    if Enums.Traits.AMBITIOUS in person.getTraits():
        loverCounter += 1

    if Enums.Traits.CONTENT in person.getTraits():
        loverCounter -= 1

    if Enums.Traits.GLUTTONOUS in person.getTraits():
        loverCounter += 1

    if Enums.Traits.TEMPERATE in person.getTraits():
        loverCounter -= 1

    if Enums.Traits.TRUSTING in person.getTraits():
        loverCounter += 1

    if Enums.Traits.PARANOID in person.getTraits():
        loverCounter -= 1

    if Enums.Traits.CYNICAL in person.getTraits():
        loverCounter += 2

    if Enums.Traits.ZEALOUS in person.getTraits():
        loverCounter -= 2

    return loverCounter

def checkAndAddPersonToLovers(person, lover, world):
    if lover not in person.getLovers():
        person.addLover(lover)
        PLEH.gotLover(person, lover, world)
    if person not in lover.getLovers():
        lover.addLover(person)
        PLEH.gotLover(lover, person, world)
