from Member import Person as PersonObj
import Utils
import PeopleInterface as PI
import NameGenerator
from Enums import LifeStatus,MaritalStatus, HairColor, Sexes


def removeSpouses (person, spouse):



    return

def birthChild (world, people, parent1, parent2, trueParent1 = '', trueParent2 = ''):

    # parent2 is father

    if trueParent1 == '':
        trueParent1 = parent1
    if trueParent2 == '':
        trueParent2 = parent2

    parent1Obj = PI.findOnePersonObj(people, trueParent1)
    parent2Obj = PI.findOnePersonObj(people, trueParent2)

    sex, sexGen1, sexGen2 = Utils.geneticSex(parent1Obj, parent2Obj)

    if sex == Sexes.MALE:
        firstName = NameGenerator.randomMName()
    else:
        firstName = NameGenerator.randomFName()

    lifespan = Utils.geneticRandomFromValues(parent1Obj.lifespan, parent2Obj.lifespan)

    if lifespan > 100:
        lifespan = 100

    fertility = Utils.geneticRandomFromValues(parent1Obj.fertility, parent2Obj.fertility)

    hairColor, hairColorGen1, hairColorGen2 = Utils.geneticHairColor(people, trueParent1, trueParent2)

    person = PersonObj()
    person.addNewPerson(firstName, parent2Obj.familyName, parent2Obj.familyName, world.getYear(), lifespan, sex, sexGen1, sexGen2, fertility, hairColor, hairColorGen1, hairColorGen2, parent1, parent2, trueParent1, trueParent2)

    return person

def deathProcedures(people, person):

    # changing statutes
    person.changeLifeStatus(LifeStatus.DEAD)
    person.maritalStatus = MaritalStatus.DEAD

    if person.spouse != '':
        spouseObj = PI.findOnePersonObj(people, person.spouse)
        person.spouse = ''
        spouseObj.deadSpouses.append(person.spouse)
        spouseObj.spouse = ''

        # changing status of the spouse to WIDOW* and clearing spouse field
        if spouseObj.sex == Sexes.MALE:
            spouseObj.maritalStatus = MaritalStatus.WIDOWER
        else:
            spouseObj.maritalStatus = MaritalStatus.WIDOW

    # adding dead kids to the list od dead children
    if person.mother != '' and person.father != '':
        PI.findOnePersonObj(people, person.father).deadChildrens.append(person.personUUID)
        PI.findOnePersonObj(people, person.mother).deadChildrens.append(person.personUUID)

    return