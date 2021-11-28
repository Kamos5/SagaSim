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
    personLastNameFLAG = False
    personSexFLAG = True
    personSexGen1FLAG = True
    personSexGen2FLAG = True
    personAgeFLAG = False
    personLifeSpanFLAG = False
    personModLifeSpanFLAG = False
    personLifeStatFLAG = True
    fatherFLAG = False
    fatherIDFLAG = True
    motherFLAG = False
    motherIDFLAG = True
    spouseFLAG = True
    causeOfDeathFLAG = False
    hairColorFLAG = True
    personHairColorGensFLAG = True
    deadChildrenListFLAG = True

    blackCount = 0
    brownCount = 0
    yellowCount = 0
    redCount = 0
    whiteCount = 0
    grayCount = 0
    timers = False

    isAlive = 0
    isDead = 0
    for person in people:

        printString = ''
        if person.lifeStatus == Enums.LifeStatus.ALIVE:
            isAlive += 1
        else:
            isDead += 1

        if (person.lifeStatus == Enums.LifeStatus.ALIVE or not isAliveFlag):
            if (personUUIDFLAG):
                printString += "UUID: " + person.personUUID + " "
            if (personFirstNameFLAG):
                printString += "FirstName: " + person.firstName + " "
            if (personLastNameFLAG):
                printString += "LastName: " + person.lastName + " "
            if (personSexFLAG):
                printString += "Sex: " + str(person.sex.value[1]) + " "
            if (personSexGen1FLAG):
                printString += "SexGen1: " + str(person.sexGen1[0].value[1]) + " "
            if (personSexGen2FLAG):
                printString += "SexGen2: " + str(person.sexGen2[0].value[1]) + " "
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
                printString += "HairColor: " + str(person.hairColor) + " "
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
                if (person.hairColor == Enums.HairColor.GRAY):
                    grayCount += 1
            if (personHairColorGensFLAG):
                printString += "HairColorGen1: " + str(person.hairColorGen1) + " "
                printString += "HairColorGen2: " + str(person.hairColorGen2) + " "
            if (deadChildrenListFLAG):
                printString += "DeadChildrenList: " + str(person.deadChildrens) + " "
        #if len(printString) > 0:
        #  print(printString)

    # print("Black count: " + str(blackCount))
    # print("Brown count: " + str(brownCount))
    # print("Yellow count: " + str(yellowCount))
    # print("Red count: " + str(redCount))
    # print("White count: " + str(whiteCount))
    # print("Gray count: " + str(grayCount))
    # print("Sum: " + str(blackCount + brownCount + yellowCount + redCount + whiteCount + grayCount))

    #print("People Alive: " + str(isAlive))
    #print("People Dead: " + str(isDead))
    print("Population: " + str(isAlive + isDead))

    # if len(person.deadSpouses) > 0:
    #     print("   Dead spouses:")
    #     for dspouse in person.deadSpouses:
    #         print("      " + PIF.findOneFirstName(people, dspouse))
    # if person.lifeStatus == Enums.LifeStatus.ALIVE and person.spouse == '':
    #     print(FF.FindAvailableSpouses(families, person))

    if manualOverride:
        input()

    if timers:
        start1 = time.time()
    world.increaseYear()
    if timers:
        end1 = time.time()
        print("WorldTime: " + str(end1 - start1))
        start1 = time.time()
    Events.increaseAge(people)
    if timers:
        end1 = time.time()
        print("IncAgeTime: " + str(end1 - start1))
        start1 = time.time()
    Events.birthPeople(world, families, people)
    if timers:
        end1 = time.time()
        print("BirthTime: " + str(end1 - start1))
        start1 = time.time()
    FF.UpdateLists(families, people)
    if timers:
        end1 = time.time()
        print("UPD1Time: " + str(end1 - start1))
        start1 = time.time()
    FF.SpouseMatchmaking(families, people)
    if timers:
        end1 = time.time()
        print("SpouseMMTime: " + str(end1 - start1))
        start1 = time.time()
    FF.UpdateLists(families, people)
    if timers:
        end1 = time.time()
        print("UDP2Time: " + str(end1 - start1))

    end = time.time()
    print(end - start)


def main():

    families = []

    world = World()
    families = initFamilies()
    people = initPeople(families)
    manualOverride = False

    sun = True

    pCount = 30
    pTime = 1000 / pCount

    tickStartTime = time.time() * 1000.0

    while sun:

        tickCurrentTime = time.time() * 1000.0

        if tickCurrentTime - tickStartTime >= pTime or not manualOverride:
            running(world, families, people, manualOverride)
            tickStartTime = time.time() * 1000.0
        else:
            running(world, families, people, manualOverride)

        if world.getYear() == 700:

            return


main()

