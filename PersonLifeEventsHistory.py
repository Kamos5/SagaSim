

def adulthoodReached(person):

    person.lifeEvents.append(str(person.firstName) + " reached adulthood at the age of " + str(person.age))


def beenBorn(person, world):

    if person.father != '':
        fatherString = str(person.father.firstName)
    else:
        fatherString = 'unknown father'
    if person.mother != '':
        motherString = str(person.mother.firstName)
    else:
        motherString = 'unknown mother'

    person.lifeEvents.append(str(person.firstName) + " had been born into " + str(person.familyName) + " in the year" + str(world.getYear()) + " to " + fatherString + " and " + motherString)


def died(person):
    person.lifeEvents.append(str(person.firstName) + " died at the age of " + str(person.age) + " from " + str(person.causeOfDeath.value))

