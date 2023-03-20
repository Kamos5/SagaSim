from Enums import Sexes

def adulthoodReached(person, world):

    person.lifeEvents.append(str(person.firstName) + " reached adulthood at the age of " + str(person.age) + " on the " + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()))


def hadKid(person, child, world):

    if child.sex == Sexes.FEMALE:
        sex = 'girl'
    else:
        sex = 'boy'
    person.lifeEvents.append(str(person.firstName) + ' mothered a ' + str(sex) + ' named ' + str(child.firstName) + ' on the year ' + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()))
    if person.spouse != None:
        person.spouse.lifeEvents.append(str(person.spouse.firstName) + ' fathered a ' + str(sex) + ' named ' + str(child.firstName) + ' on the year ' + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()))

def miscarriage(person, world):

    person.lifeEvents.append(str(person.firstName) + ' had lost a child on the ' + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()) + ' due to miscarriage')

def stillborn(person, world):

    person.lifeEvents.append(str(person.firstName) + ' had given birth to a stillborn child on the ' + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()))

def lostChild(person, child, world):

    if child.sex == Sexes.FEMALE:
        sex = 'girl'
    else:
        sex = 'boy'
    person.lifeEvents.append(str(person.firstName) + ' had lost a ' + str(sex) + ' named ' + str(child.firstName) + ' on the ' + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()) + ' due to ' + str(child.causeOfDeath.value))


def killedByDuringCrime(victim, offender, world):

    offenderString = ""
    if offender is None:
        offenderString = "Unknown"

    else:
        offenderString = offender.getFirstName() + " " + offender.getLastName()

    victim.lifeEvents.append(str(victim.firstName) + " was killed by" + offenderString + " during crime " + ' on the year ' + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()))

def killedSMBDuringCrime(offender, victim, world):

    offender.lifeEvents.append(str(offender.firstName) + " killed " + victim.getFirstName() + " " + victim.getLastName() + " while committing crime on the year " + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()))

def beenBorn(person, world):

    if person.father is not None:
        fatherString = str(person.father.firstName)
    else:
        fatherString = 'unknown father'
    if person.mother is not None:
        motherString = str(person.mother.firstName)
    else:
        motherString = 'unknown mother'

    person.lifeEvents.append(str(person.firstName) + " had been born into " + str(person.familyName) + " family on the " + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()) + " to " + str(fatherString) + " and " + str(motherString) + " in the " + str(person.settlement.getSettlementType().value) + " of " + str(person.settlement.getSettlementName()))
    hadKid(person.mother, person, world)

def died(person, world):
    person.lifeEvents.append(str(person.firstName) + " died at the age of " + str(person.age) + " from " + str(person.causeOfDeath.value) + ' on the ' + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()))

def movedHome(person, movedFrom, movedTo, world):

    if person.sex == Sexes.FEMALE:
        preverb = 'hers'
    else:
        preverb = 'his'
    person.lifeEvents.append(str(person.firstName) + " moved with " + str(preverb) + " family from " + str(movedFrom.getSettlementName()) + " to " + str(movedTo.getSettlementName()) + ' on the ' + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()))

def married(person, world):

    person.lifeEvents.append(str(person.firstName) + " married " + str(person.spouse.firstName) + " " + str(person.spouse.lastName) + " on the " + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()))

def divorced(person, world):

    person.lifeEvents.append(str(person.firstName) + " divorced " + str(person.spouse.firstName) + " " + str(person.spouse.familyName) + " on the " + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()))

def changedLastName(person, world, newFamilyName):
    person.lifeEvents.append(str(person.firstName) + " " + str(person.lastName) + " changed family name to " + str(newFamilyName) + " on the " + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()))

def lostSpouse(person, world):

    if person.sex == Sexes.FEMALE:
        sex = 'husband'
    else:
        sex = 'wife'
    person.lifeEvents.append(str(person.firstName) + ' had lost a ' + str(sex) + ' named ' + str(person.spouse.firstName) + ' due to ' + str(person.spouse.causeOfDeath.value) + ' on the ' + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()))

def foundEmpoyment(person, world):

    person.lifeEvents.append(str(person.getFirstName()) + ' starts workings as ' + str(person.getOccupationName()) + ' in the town of ' + str(person.getSettlement().getSettlementName()) + ' on the ' + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()))

def lostEmpoyment(person, world):

    person.lifeEvents.append(str(person.getFirstName()) + ' lost job as ' + str(person.getOccupationName()) + ' in the town of ' + str(person.getSettlement().getSettlementName()) + ' on the ' + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()))

def retired(person, world):

    person.lifeEvents.append(str(person.getFirstName()) + ' retired from working as ' + str(person.getOccupationName()) + ' on the ' + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()))

def gotPromotion(person, world):

    person.lifeEvents.append(str(person.getFirstName()) + ' got promotion workings to ' + str(person.getOccupationName()) + ' in the town of ' + str(person.getSettlement().getSettlementName()) + ' on the ' + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()))

def gotInfectedWithDisease(person, disease, world, carrier=None):

    infectedByString = ''
    if carrier is not None:
        infectedByString = ' by ' + str(carrier.getFirstName()) + ' ' + str(carrier.getLastName())
    person.lifeEvents.append(str(person.getFirstName()) + ' got infected with ' + str(disease['name']) + ' on the ' + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()) + infectedByString)

def showingSymptomsOf(person, disease, world):

    person.lifeEvents.append(str(person.getFirstName()) + ' started to show symptoms of ' + str(disease['name']) + ' on the ' + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()))

def gotImmunityTo(person, disease, world):

    person.lifeEvents.append(str(person.getFirstName()) + ' got healed and got immunity from ' + str(disease['name']) + ' on the ' + str(world.getDay()) + '/' + str(world.getMonth().value[1]) + '/' + str(world.getYear()))