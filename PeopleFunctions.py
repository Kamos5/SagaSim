from Person import Person as PersonObj
import Utils
import NameGenerator
from Enums import LifeStatus, MaritalStatus, HairColor, Sexes
import PersonLifeEventsHistory as PLEH

#mother, mother's spouse, trueMother, trueFather


def birthChild(world, parent1, parent2=None, trueParent1=None, trueParent2=None):

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

    if sex == Sexes.MALE:
        firstName = NameGenerator.getRandomMNameForRegion(parent1.getSettlement().getRegion())
    else:
        firstName = NameGenerator.getRandomFNameForRegion(parent1.getSettlement().getRegion())

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

    person = PersonObj()

    #Child goes to father's family
    person.birthNewPerson(firstName, secondParent.familyName, secondParent.familyName, world.getDay(), world.getMonth(), world.getYear(), lifespan, sex,
                          sexGen1, sexGen2, sexuality, fertility, offspringHeight, hairColor, hairColorGen1, hairColorGen2, eyeColor, eyeColorGen1, eyeColorGen2,
                          parent1, parent2, trueParent1, trueParent2, secondParent.familyObjRef)

    Utils.inheretTraits(person, parent1, secondParent, trueParent1, trueParent2)

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
        child.changeFreeWealth(person.getFreeWealth() / len(person.getAliveChildrenList()))

    #If no alive children city takes it all
    if len(person.getAliveChildrenList()) == 0:
        person.getSettlement().changeFreeWealth(person.getFreeWealth())

    person.setFreeWealth(0)

    person.getSettlement().decreasePopulation()
    person.getSettlement().removeResident(person)

    person.getAccommodation().removeHouseResident(person)
    person.setAccommodation(None)

    # adding dead kids to the list od dead children
    # not needed. all kids that have Status.DEAD in child list is what we need

    return

def retirement(person,world):

    if person.getOccupation() is not None:
        person.getOccupation().removeWorker(person)
        person.setOccupation(None)
        person.setOccupationName("Retired")
        PLEH.retired(person, world)
