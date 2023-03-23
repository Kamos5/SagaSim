from Enums import Sexes

def adulthoodReached(person, world):

    person.lifeEvents.append(f'{person.firstName} reached adulthood at the age of {person.age} on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')


def hadKid(person, child, world):

    if child.sex == Sexes.FEMALE:
        sex = 'girl'
    else:
        sex = 'boy'
    person.lifeEvents.append(f'{person.firstName} mothered a {sex} named {child.firstName} on the year {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')
    if person.spouse != None:
        person.spouse.lifeEvents.append(f'{person.spouse.firstName} fathered a {sex} named {child.firstName} on the year {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def miscarriage(person, world):

    person.lifeEvents.append(f'{person.firstName} had lost a child on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()} due to miscarriage')

def stillborn(person, world):

    person.lifeEvents.append(f'{person.firstName} had given birth to a stillborn child on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def lostChild(person, child, world):

    if child.sex == Sexes.FEMALE:
        sex = 'girl'
    else:
        sex = 'boy'
    person.lifeEvents.append(f'{person.firstName} had lost a {sex} named {child.firstName} on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()} due to {child.causeOfDeath.value}')


def killedByDuringCrime(victim, offender, world):

    offenderString = ""
    if offender is None:
        offenderString = "Unknown"

    else:
        offenderString = offender.getFirstName() + " " + offender.getLastName()

    victim.lifeEvents.append(f'{victim.firstName} was killed by {offenderString} + " during crime {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def killedSMBDuringCrime(offender, victim, world):

    offender.lifeEvents.append(f'{offender.firstName} killed {victim.getFirstName()} {victim.getLastName()} while committing crime on the year {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def beenBorn(person, world):

    if person.father is not None:
        fatherString = str(person.father.firstName)
    else:
        fatherString = 'unknown father'
    if person.mother is not None:
        motherString = str(person.mother.firstName)
    else:
        motherString = 'unknown mother'

    person.lifeEvents.append(f'{person.firstName} had been born into {person.familyName} family on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()} to {fatherString} and {motherString} in the {person.settlement.getSettlementType().value} of {person.settlement.getSettlementName()}')
    hadKid(person.mother, person, world)

def died(person, world):
    person.lifeEvents.append(f'{person.firstName} died at the age of {person.age} from {person.causeOfDeath.value} on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def movedHome(person, movedFrom, movedTo, world):

    if person.sex == Sexes.FEMALE:
        preverb = 'hers'
    else:
        preverb = 'his'
    person.lifeEvents.append(f'{person.firstName} moved with {preverb} family from {movedFrom.getSettlementName()} to {movedTo.getSettlementName()} on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def married(person, world):

    person.lifeEvents.append(f'{person.firstName} married {person.spouse.firstName} {person.spouse.lastName} on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def divorced(person, world):

    person.lifeEvents.append(f'{person.firstName} divorced {person.spouse.firstName} {person.spouse.familyName} on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def changedLastName(person, world, newFamilyName):
    person.lifeEvents.append(f'{person.firstName} {person.lastName} changed family name to {newFamilyName} on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def lostSpouse(person, world):

    if person.sex == Sexes.FEMALE:
        sex = 'husband'
    else:
        sex = 'wife'
    person.lifeEvents.append(f'{person.firstName} had lost a {sex} named {person.spouse.firstName} due to {person.spouse.causeOfDeath.value} on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def foundEmpoyment(person, world):

    person.lifeEvents.append(f'{person.getFirstName()} starts workings as {person.getOccupationName()} in the town of {person.getSettlement().getSettlementName()} on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def lostEmpoyment(person, world):

    person.lifeEvents.append(f'{person.getFirstName()} lost job as {person.getOccupationName()} in the town of {person.getSettlement().getSettlementName()} on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def retired(person, world):

    person.lifeEvents.append(f'{person.getFirstName()} retired from working as {person.getOccupationName()} on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def gotPromotion(person, world):

    person.lifeEvents.append(f'{person.getFirstName()} got promotion workings to {person.getOccupationName()} in the town of {person.getSettlement().getSettlementName()} on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def gotInfectedWithDisease(person, disease, world, carrier=None):

    infectedByString = ''
    if carrier is not None:
        infectedByString = f' by {carrier.getFirstName()} {carrier.getLastName()}'
    person.lifeEvents.append(f'{person.getFirstName()} got infected with {disease["name"]} on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}{infectedByString}')

def showingSymptomsOf(person, disease, world):

    person.lifeEvents.append(f'{person.getFirstName()} started to show symptoms of {disease["name"]} on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def gotImmunityTo(person, disease, world):

    person.lifeEvents.append(f'{person.getFirstName()} got healed and got immunity from {disease["name"]} on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def gotFriend(person, friend, world):

    person.lifeEvents.append(f'{person.getFirstName()} found a friend {friend.getFirstName()} {friend.getLastName()} on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def gotRival(person, rival, world):
    person.lifeEvents.append(f'{person.getFirstName()} found a rival {rival.getFirstName()} {rival.getLastName()} on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def lostFriend(person, friend, world):

    person.lifeEvents.append(f'{person.getFirstName()} lost a friend {friend.getFirstName()} {friend.getLastName()} on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def lostRival(person, rival, world):
    person.lifeEvents.append(f'{person.getFirstName()} lost a rival {rival.getFirstName()} {rival.getLastName()} on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')
