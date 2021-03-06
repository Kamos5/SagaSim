from Person import Person as PersonObj
import Utils
import PeopleInterface as PI
import NameGenerator
from Enums import LifeStatus, MaritalStatus, HairColor, Sexes
import PersonLifeEventsHistory as PLEH


def birthChild(world, parent1, parent2, trueParent1='', trueParent2=''):
    # parent2 is father
    if trueParent1 == '':
        trueParent1 = parent1
    if trueParent2 == '':
        trueParent2 = parent2

    sex, sexGen1, sexGen2 = Utils.geneticSex(trueParent1, trueParent2)

    randomChanceForBeingGay = Utils.randomRange(1, 100)

    if randomChanceForBeingGay < 5:
        sexuality = 'homo'
    else:
        sexuality = 'hetero'

    if sex == Sexes.MALE:
        firstName = NameGenerator.randomMName()
    else:
        firstName = NameGenerator.randomFName()

    lifespan = Utils.geneticRandomFromValues(trueParent1.lifespan, trueParent2.lifespan)

    if lifespan > 100:
        lifespan = 100

    fertility = Utils.geneticRandomFromValues(trueParent1.fertility, trueParent2.fertility)

    offspringHeight = Utils.geneticRandomFromValuesForHeight(trueParent1.height, trueParent2.height)
    if sex == Sexes.MALE:
        offspringHeight = int(offspringHeight*Utils.randomRange(101, 102)/100)

    hairColor, hairColorGen1, hairColorGen2 = Utils.geneticHairColor(trueParent1, trueParent2)
    eyeColor, eyeColorGen1, eyeColorGen2 = Utils.geneticEyeColor(trueParent1, trueParent2)

    person = PersonObj()

    #Child goes to father's family
    person.birthNewPerson(firstName, trueParent2.familyName, trueParent2.familyName, world.getYear(), lifespan, sex,
                          sexGen1, sexGen2, sexuality, fertility, offspringHeight, hairColor, hairColorGen1, hairColorGen2, eyeColor, eyeColorGen1, eyeColorGen2,
                          parent1, parent2, trueParent1, trueParent2, trueParent2.familyObjRef)

    Utils.inheretTraits(person, parent1, parent2, trueParent1, trueParent2)

    return person


def deathProcedures(person, world):

    if person.spouse is not None:
        person.spouse.deadSpouses.append(person)
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

    # changing statutes
    person.changeLifeStatus(LifeStatus.DEAD)
    person.maritalStatus = MaritalStatus.DEAD
    PLEH.died(person, world)

    if person.age < 15:
        PLEH.lostChild(person.mother, person, world)
    if person.getFather() != '':
        person.getFather().getChildrensList().remove(person)
        person.getFather().getDeadChildrens().append(person)
    if person.getMother() != '':
        person.getMother().getChildrensList().remove(person)
        person.getMother().getDeadChildrens().append(person)

    # adding dead kids to the list od dead children
    # not needed. all kids that have Status.DEAD in child list is what we need

    return
