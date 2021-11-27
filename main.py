import FamilyInitGenerator as FIG
import MembersInitGenerator as MIG
from World import World as World
import Events
import Enums
import PeopleFunctions as MF
import FamilyFunctions as FF
import PeopleInterface as PIF
import random
import time

world = World()

def initFamilies():

    families = FIG.Init(world)

    return families

def initPeople(families):

    people = MIG.Init(families, world)
    for family in families:
        MIG.initInitMarrieges(family, people)

    return people

def running (world, families, people, manualOverride):

    start = time.time()
    print(world.getYear())

    # for val in families:
    #     print(val.familyName)
    #     print("Children Number: " + str(val.getChildrenNumber()))
    #     print("Male Adults:" + str(len(val.adultMaleList)))
    #     print("Female Adults:" + str(len(val.adultFemaleList)))
    #     print("Members Number:" + str(val.getFamilyMembersNumber()))
    #     print("Female Number:" + str(val.getFemaleNumber()))
    #     print("Male Number:" + str(val.getMaleNumber()))
    #     print("LEN UAM: " + str(len(val.unmarriedAdultMaleList)))
    #     print("LEN UAF: " + str(len(val.unmarriedAdultFemaleList)))
    # for UAM in val.unmarriedAdultMaleList:
    #     print("Unmarried male family member: " + " " + UAM)
    # for UAF in val.unmarriedAdultFemaleList:
    #     print("Unmarried female family member: " + " " + UAF)

    isAliveFlag = True
    personUUIDFLAG = True
    personFirstNameFLAG = True
    personLastNameFLAG = True
    personSexFLAG = True
    personAgeFLAG = True
    personLifeSpanFLAG = False
    personModLifeSpanFLAG = True
    personLifeStatFLAG = False
    fatherFLAG = True
    fatherIDFLAG = True
    motherFLAG = True
    motherIDFLAG = True
    spouseFLAG = True
    causeOfDeathFLAG = False
    hairColorFLAG = True

    blackCount = 0
    brownCount = 0
    yellowCount = 0
    redCount = 0
    whiteCount = 0

    for person in people:
        printString = ''
        if (person.lifeStatus == Enums.LifeStatus.ALIVE or not isAliveFlag):
            if (personUUIDFLAG):
                printString += "UUID: " + person.personUUID + " "
            if (personFirstNameFLAG):
                printString += "FirstName: " + person.firstName + " "
            if (personLastNameFLAG):
                printString += "LastName: " + person.lastName + " "
            if (personSexFLAG):
                printString += "Sex: " + str(person.sex) + " "
            if personAgeFLAG:
                printString += "Age: " + str(person.age) + " "
            if (personLifeSpanFLAG):
                printString += "Lifespan: " + str(person.lifespan) + " "
            if (personModLifeSpanFLAG):
                printString += "ModLifespan: " + str(person.modifiedLifespan) + " "
            if (personLifeStatFLAG):
                printString += "Status: " + person.lifeStatus.value + " "
            if (fatherFLAG):
                printString += "Father: " + PIF.findOneFirstName(people, person.father) + " "
            if (fatherIDFLAG):
                printString += "Father-id: " + person.father + " "
            if (motherFLAG):
                printString += "Mother: " + PIF.findOneFirstName(people, person.mother) + " "
            if (motherIDFLAG):
                printString += "Mother-id: " + person.mother + " "
            if (spouseFLAG):
                printString += "Spouse: " + PIF.findOneFirstName(people, person.spouse) + " "
            if (causeOfDeathFLAG):
                printString += "Status: " + person.causeOfDeath.value + " "
            if (hairColorFLAG):
                printString += "HairColor: " + person.hairColor.value[1] + " "
                if (person.hairColor == Enums.HairColor.BLACK):
                    blackCount += 1
                if (person.hairColor == Enums.HairColor.BROWN):
                    brownCount += 1
                if (person.hairColor == Enums.HairColor.RED):
                    redCount += 1
                if (person.hairColor == Enums.HairColor.YELLOW):
                    yellowCount += 1
                if (person.hairColor == Enums.HairColor.WHITE):
                    whiteCount += 1

        # if len(printString) > 0:
        #    print(printString)

    print("Black count: " + str(blackCount))
    print("Brown count: " + str(brownCount))
    print("Yellow count: " + str(yellowCount))
    print("Red count: " + str(redCount))
    print("White count: " + str(whiteCount))

    # if len(person.deadSpouses) > 0:
    #     print("   Dead spouses:")
    #     for dspouse in person.deadSpouses:
    #         print("      " + PIF.findOneFirstName(people, dspouse))
    # if person.lifeStatus == Enums.LifeStatus.ALIVE and person.spouse == '':
    #     print(FF.FindAvailableSpouses(families, person))

    if manualOverride:
        input()

    world.increaseYear()
    Events.increaseAge(people)
    Events.birthPeople(world, families, people)
    FF.UpdateLists(families, people)
    FF.SpouseMatchmaking(families, people)
    FF.UpdateLists(families, people)

    end = time.time()
    print(end - start)


def main():

    families = []

    world = World()
    families = initFamilies()
    people = initPeople(families)
    manualOverride = False

    sun = 'true'

    pCount = 30
    pTime = 1000 / pCount

    tickStartTime = time.time() * 1000.0

    while (sun):

        tickCurrentTime = time.time() * 1000.0

        if tickCurrentTime - tickStartTime >= pTime or not manualOverride:
            running(world, families, people, manualOverride)
            tickStartTime = time.time() * 1000.0
        else:
            running(world, families, people, manualOverride)

        if world.getYear() == 700:
            return

def menuCall():

    input = input()












main()

