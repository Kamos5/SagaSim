import Enums
import PersonLifeEventsHistory as PLEH
import Utils
import PeopleFunctions as PF

def getDiseases(afflictions):

    diseases = []
    for affliction in afflictions:
        if affliction[1]['type'] == 'sickness':
            diseases.append(affliction)
    return diseases

def getInjuries(afflictions):

    injures = []
    for affliction in afflictions:
        if affliction[1]['type'] == 'injury':
            injures.append(affliction)
    return injures

def checkIfInfected(infected, infection):

    if len(infected.getInfections()) == 0:
        return True
    else:
        infections, infDate = zip(*infected.getInfections())
        if infection not in infections:
            return True
        else:
            return False

def addInfectionToPerson(infected, infection, world, carrier=None):

    infectionsPerDay = 0
    infected.addInfection([infection, world.getDayOfTheYear()])
    PLEH.gotInfectedWithDisease(infected, infection, world, carrier)
    infectionsPerDay += 1
    return infectionsPerDay

def checkIfWillInfect(potentiallyInfected, infection):

    spreadingChance = Utils.randomRange(1, 500)
    if spreadingChance < infection['contagionChange']:
        if len(potentiallyInfected.getInfections()) == 0:
            return True
        else:
            infections, infDate = zip(*potentiallyInfected.getInfections())
            if infection not in infections:
                return True
            else:
                return False


def tryToInfectPeopleFromList(carrier, list, infection, world):

    infectionsPerDay = 0
    for memberOfList in list:
        if memberOfList is not carrier:
            if len(memberOfList.getImmunityTo()) > 0:
                isImmune = False
                for immunityTo in memberOfList.getImmunityTo():
                    if infection == immunityTo[0][0]:
                        isImmune = True
                        break
                if not isImmune:
                    if checkIfWillInfect(memberOfList, infection):
                        infectionsPerDay += addInfectionToPerson(memberOfList, infection, world, carrier)
                        break
            else:
                if checkIfWillInfect(memberOfList, infection):
                    infectionsPerDay += addInfectionToPerson(memberOfList, infection, world, carrier)
        else:
            continue

    return infectionsPerDay

def offsetHealth(person, affliction, world):

    offsetHealth = person.getGeneralHealth().value[0] + affliction['effectOnHealth'] + person.getHealthFromAge().value[0]
    if offsetHealth >= len(Enums.getGeneralHealthArray()):
        offsetHealth = len(Enums.getGeneralHealthArray()) - 1
    person.setGeneralHelth(Enums.getGeneralHealthArray()[offsetHealth])
    if person.getGeneralHealth() == Enums.GeneralHealth.DEATH:
        person.causeOfDeath = Enums.CauseOfDeath.SICKNESS
        PF.deathProcedures(person, world)
        return True
    else:
        return False

def injureSomeone(randomPerson, world, randomInjury = True):
    if randomInjury:
        injury = Utils.randomFromCollection(world.getInjuries())[1]
    else:
        injury = world.getInjuries()[0] #TODO ZDEFINIOWAC OBRAZENIA
    randomPerson.addCurrentInjuries([injury, world.getDayOfTheYear(), 0])
    PLEH.gotInjured(randomPerson, injury, world)
    offsetHealth(randomPerson, injury, world)
