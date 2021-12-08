from Enums import Sexes

def adulthoodReached(person, world):

    person.lifeEvents.append(str(person.firstName) + " reached adulthood at the age of " + str(person.age) + " in the year " + str(world.getYear()))


def hadKid(person, child, world):

    if child.sex == Sexes.FEMALE:
        sex = 'girl'
    else:
        sex = 'boy'
    person.lifeEvents.append(str(person.firstName) + ' mothered a ' + str(sex) + ' named ' + str(child.firstName) + ' in the year ' + str(world.getYear()))
    if person.spouse != '':
        person.spouse.lifeEvents.append(str(person.spouse.firstName) + ' fathered a ' + str(sex) + ' named ' + str(child.firstName) + ' in the year ' + str(world.getYear()))


def lostChild(person, child, world):

    if child.sex == Sexes.FEMALE:
        sex = 'girl'
    else:
        sex = 'boy'
    person.lifeEvents.append(str(person.firstName) + ' had lost a ' + str(sex) + ' named ' + str(child.firstName) + ' in the year ' + str(world.getYear()) + ' due to ' + str(child.causeOfDeath.value))


def beenBorn(person, world):

    if person.father != '':
        fatherString = str(person.father.firstName)
    else:
        fatherString = 'unknown father'
    if person.mother != '':
        motherString = str(person.mother.firstName)
    else:
        motherString = 'unknown mother'

    person.lifeEvents.append(str(person.firstName) + " had been born into " + str(person.familyName) + " family in the year " + str(world.getYear()) + " to " + str(fatherString) + " and " + str(motherString) + " in the " + str(person.settlement.getSettlementType().value) + " of " + str(person.settlement.getSettlementName()))
    hadKid(person.mother, person, world)

def died(person, world):
    person.lifeEvents.append(str(person.firstName) + " died at the age of " + str(person.age) + " from " + str(person.causeOfDeath.value) + ' in the year ' + str(world.getYear()))

def movedHome(person, movedFrom, world):

    if person.sex == Sexes.FEMALE:
        preverb = 'hers'
    else:
        preverb = 'his'
    person.lifeEvents.append(str(person.firstName) + " moved with " + str(preverb) + " family from " + str(movedFrom.getSettlementName()) + " to " + str(person.getSettlement().getSettlementName()) + ' in the year ' + str(world.getYear()))


def married(person, world):

    person.lifeEvents.append(str(person.firstName) + " married " + str(person.spouse.firstName) + " " + str(person.spouse.lastName) + " in the year: " + str(world.getYear()))

def lostSpouse(person, world):

    if person.sex == Sexes.FEMALE:
        sex = 'husband'
    else:
        sex = 'wife'
    person.lifeEvents.append(str(person.firstName) + ' had lost a ' + str(sex) + ' named ' + str(person.spouse.firstName) + ' due to ' + str(person.spouse.causeOfDeath.value + ' in the year ' + str(world.getYear())))