from Person import Person as PersonObj
import Utils
import PeopleInterface as PI
import NameGenerator
from Enums import LifeStatus, MaritalStatus, HairColor, Sexes


def birthChild(world, parent1, parent2, trueParent1='', trueParent2=''):
    # parent2 is father
    if trueParent1 == '':
        trueParent1 = parent1
    if trueParent2 == '':
        trueParent2 = parent2

    sex, sexGen1, sexGen2 = Utils.geneticSex(trueParent1, trueParent2)

    if sex == Sexes.MALE:
        firstName = NameGenerator.randomMName()
    else:
        firstName = NameGenerator.randomFName()

    lifespan = Utils.geneticRandomFromValues(trueParent1.lifespan, trueParent2.lifespan)

    if lifespan > 100:
        lifespan = 100

    fertility = Utils.geneticRandomFromValues(trueParent1.fertility, trueParent2.fertility)

    hairColor, hairColorGen1, hairColorGen2 = Utils.geneticHairColor(trueParent1, trueParent2)

    person = PersonObj()

    #Child goes to father's family
    person.addNewPerson(firstName, trueParent2.familyName, trueParent2.familyName, world.getYear(), lifespan, sex,
                        sexGen1, sexGen2, fertility, hairColor, hairColorGen1, hairColorGen2, parent1, parent2,
                        trueParent1, trueParent2, trueParent2.familyObjRef)

    return person


def deathProcedures(person):

    if person.spouse is not None:
        person.spouse.deadSpouses.append(person)
        # changing status of the spouse to WIDOW* and clearing spouse field
        if person.spouse.sex == Sexes.MALE:
            person.spouse.maritalStatus = MaritalStatus.WIDOWER
        else:
            person.spouse.maritalStatus = MaritalStatus.WIDOW

        person.spouse.familyObjRef.removeMarriedMember(person.spouse)
        person.spouse.familyObjRef.addUnmarriedMember(person.spouse)
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

    if person.age < 15:
        person.getMother().childrens.remove(person)
        person.getFather().childrens.remove(person)
        person.getMother().deadChildrens.append(person)
        person.getFather().deadChildrens.append(person)
    # adding dead kids to the list od dead children
    # not needed. all kids that have Status.DEAD in child list is what we need

    return
