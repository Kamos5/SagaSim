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
        injury = Utils.randomFromFileDictionaryWithWeightInjuries(world.getInjuries())[1]
    else:
        injury = world.getInjuries()[0] ##TODO ZDEFINIOWAC OBRAZENIA
    if injury == world.getInjuries()[0][1]:
        world.organFailure += 1
    if injury == world.getInjuries()[1][1]:
        world.deepWounds += 1
    if injury == world.getInjuries()[2][1]:
        world.concussion += 1
    if injury == world.getInjuries()[3][1]:
        world.brokenBones += 1
    if injury == world.getInjuries()[4][1]:
        world.fleshWounds += 1

    randomPerson.addCurrentInjuries([injury, world.getDayOfTheYear(), 0])
    randomPerson.increaseHappiness(-5)
    PLEH.gotInjured(randomPerson, injury, world)
    offsetHealth(randomPerson, injury, world)

def toRemoveDisease(person, disease, world):

    if disease[2] < 100:
        disease[2] += round(100 / disease[0]["daysToCure"], 2)
        if disease[2] >= 100:
            disease[2] = 100  ######TODO TO COS JEST NIE TAK -> rozkminic te tablice
            person.setInfections([infection for infection in person.getInfections() if not infection[0] == disease[0]])
            person.setGeneralHelth(Enums.getGeneralHealthArray()[person.getGeneralHealth().value[0] - disease[0]['effectOnHealth'] + person.getHealthFromAge().value[0]])
            person.addImmunityTo([disease, world.getDayOfTheYear()])
            PLEH.gotImmunityTo(person, disease[0], world)
            return disease

def toRemoveInjury(person, injury, world):

    if injury[2] < 100:
        injury[2] += round(100 / injury[0]["daysToCure"], 2)
        if injury[2] >= 100:
            injury[2] = 100  ######TODO TO COS JEST NIE TAK -> rozkminic te tablice
            person.setGeneralHelth(Enums.getGeneralHealthArray()[person.getGeneralHealth().value[0] - injury[0]['effectOnHealth'] + person.getHealthFromAge().value[0]])
            return injury
