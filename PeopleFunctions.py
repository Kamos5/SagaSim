from Member import Person as PersonObj
import Utils
import PeopleInterface as PI
import NameGenerator
from Enums import LifeStatus,MaritalStatus,HairColor

def removeSpouses (people, pip1, pip2):

    for person in people:
        if person.personUUID == pip1:
            person.spouse = ''
        if person.personUUID == pip2:
            person.deadSpouses.append(person.spouse)
            person.spouse = ''

    return


def birthChild (world, people, parent1, parent2, trueParent1 = '', trueParent2 = ''):

    sexes = ["M", "F"]

    if trueParent1 == '':
        trueParent1 = parent1
    if trueParent2 == '':
        trueParent2 = parent2

    sex = Utils.randomFromCollection(sexes)

    if sex == "M":
        firstName = NameGenerator.randomMName()
    else:
        firstName = NameGenerator.randomFName()

    lifespan = Utils.geneticRandomFromValues(PI.findOneLifeSpan(people, trueParent1), PI.findOneLifeSpan(people, trueParent2))

    if lifespan > 100:
        lifespan = 100

    fertility = Utils.geneticRandomFromValues(PI.findOneFertility(people, trueParent1), PI.findOneFertility(people, trueParent2))

    hairColor = Utils.geneticHairColor(PI.findOneHairColor(people, trueParent1), PI.findOneHairColor(people, trueParent2))

    person = PersonObj()
    person.addNewPerson(firstName, PI.findOneFamilyName(people, parent2), PI.findOneFamilyName(people, parent2), world.getYear(), lifespan, sex, fertility, hairColor, parent1, parent2, trueParent1, trueParent2)

    return person

def deathProcedures(people, person):

    # changing statutes
    person.changeLifeStatus(LifeStatus.DEAD)
    person.maritalStatus = MaritalStatus.DEAD

    # adding dead kids to the list od dead children
    if person.mother != '' and person.father != '':
        PI.findOnePersonObj(people, person.father).deadChildrens.append(person.personUUID)
        PI.findOnePersonObj(people, person.mother).deadChildrens.append(person.personUUID)

    # changing status of the spouse to WIDOW* and clearing spouse field
    if person.spouse != '':
        if PI.findOnePersonObj(people, person.spouse).sex == "M":
            PI.findOnePersonObj(people, person.spouse).maritalStatus = MaritalStatus.WIDOWER
        else:
            PI.findOnePersonObj(people, person.spouse).maritalStatus = MaritalStatus.WIDOW
    removeSpouses(people, person.personUUID, person.spouse)

    return