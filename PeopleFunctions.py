from Member import Person as PersonObj
import Utils
import PeopleInterface as PI
import NameGenerator
from Enums import LifeStatus,MaritalStatus, HairColor, Sexes

def birthChild (world, parent1, parent2, trueParent1 = '', trueParent2 = ''):

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
    person.addNewPerson(firstName, trueParent2.familyName, trueParent2.familyName, world.getYear(), lifespan, sex, sexGen1, sexGen2, fertility, hairColor, hairColorGen1, hairColorGen2, parent1.personUUID, parent2.personUUID, trueParent1.personUUID, trueParent2.personUUID)

    return person

def deathProcedures(people, person):

    #Todo optymalization for not calling PersonInterface

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
