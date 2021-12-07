

def adulthoodReached(person):

    person.lifeEvents.append(str(person.firstName) + " reached adulthood at the age of " + str(person.age))


def beenBorn(person, world):
    person.lifeEvents.append(str(person.firstName) + " had been born into " + str(person.familyName) + " in the year" + str(world.getYear()) + " to " + str(person.father.firstName) + " and " + str(person.mother.firstname))


def died(person):
    person.lifeEvents.append(str(person.firstName) + " died at the age of " + str(person.age) + " from " + str(person.causeOfDeath.value))

