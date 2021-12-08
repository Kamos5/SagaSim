import FamilyInitGenerator as FIG
import MembersInitGenerator as MIG
from World import World as World
import Events
from Settlements import Settlements
import Enums
import PeopleFunctions as MF
import FamilyFunctions as FF
import PeopleInterface as PIF
import random
import time
import Parameters

world = World()

def initFamilies():

    families = FIG.Init(world)

    return families

def initPeople(families):

    people = MIG.Init(families, world)

    for family in families:
        MIG.initInitMarrieges(family)

    return people

def running (world, families, people, manualOverride):

    start = time.time()
    print(world.getYear())

    isAliveFlag = False
    personUUIDFLAG = False
    personFirstNameFLAG = False
    personLastNameFLAG = False
    personSexFLAG = False
    personSexGen1FLAG = False
    personSexGen2FLAG = False
    personAgeFLAG = False
    personLifeSpanFLAG = False
    personModLifeSpanFLAG = False
    personLifeStatFLAG = False
    fatherFLAG = False
    fatherIDFLAG = False
    motherFLAG = False
    motherIDFLAG = False
    spouseFLAG = False
    causeOfDeathFLAG = False
    hairColorFLAG = False
    personHairColorGensFLAG = False
    deadChildrenListFLAG = False

    blackCount = 0
    brownCount = 0
    yellowCount = 0
    redCount = 0
    whiteCount = 0
    grayCount = 0
    timers = True

    # for person in people:
    #
    #     printString = ''
    #     if (person.lifeStatus == Enums.LifeStatus.ALIVE or not isAliveFlag):
    #         if (personUUIDFLAG):
    #             printString += "UUID: " + person.personUUID + " "
    #         if (personFirstNameFLAG):
    #             printString += "FirstName: " + person.firstName + " "
    #         if (personLastNameFLAG):
    #             printString += "LastName: " + person.lastName + " "
    #         if (personSexFLAG):
    #             printString += "Sex: " + str(person.sex.value[1]) + " "
    #         if (personSexGen1FLAG):
    #             printString += "SexGen1: " + str(person.sexGen1[0].value[1]) + " "
    #         if (personSexGen2FLAG):
    #             printString += "SexGen2: " + str(person.sexGen2[0].value[1]) + " "
    #         if personAgeFLAG:
    #             printString += "Age: " + str(person.age) + " "
    #         if (personLifeSpanFLAG):
    #             printString += "Lifespan: " + str(person.lifespan) + " "
    #         if (personModLifeSpanFLAG):
    #             printString += "ModLifespan: " + str(person.modifiedLifespan) + " "
    #         if (personLifeStatFLAG):
    #             printString += "Status: " + person.lifeStatus.value + " "
    #         if (fatherFLAG):
    #             printString += "Father: " + PIF.findOneFirstName(people, person.father) + " "
    #         if (fatherIDFLAG):
    #             printString += "Father-id: " + person.father + " "
    #         if (motherFLAG):
    #             printString += "Mother: " + PIF.findOneFirstName(people, person.mother) + " "
    #         if (motherIDFLAG):
    #             printString += "Mother-id: " + person.mother + " "
    #         if (spouseFLAG):
    #             printString += "Spouse: " + PIF.findOneFirstName(people, person.spouse) + " "
    #         if (causeOfDeathFLAG):
    #             printString += "Status: " + person.causeOfDeath.value + " "
    #         if (hairColorFLAG):
    #             printString += "HairColor: " + str(person.hairColor) + " "
    #             if (person.hairColor == Enums.HairColor.BLACK):
    #                 blackCount += 1
    #             if (person.hairColor == Enums.HairColor.BROWN):
    #                 brownCount += 1
    #             if (person.hairColor == Enums.HairColor.RED):
    #                 redCount += 1
    #             if (person.hairColor == Enums.HairColor.YELLOW):
    #                 yellowCount += 1
    #             if (person.hairColor == Enums.HairColor.WHITE):
    #                 whiteCount += 1
    #             if (person.hairColor == Enums.HairColor.GRAY):
    #                 grayCount += 1
    #         if (personHairColorGensFLAG):
    #             printString += "HairColorGen1: " + str(person.hairColorGen1) + " "
    #             printString += "HairColorGen2: " + str(person.hairColorGen2) + " "
    #         if (deadChildrenListFLAG):
    #             printString += "DeadChildrenList: " + str(person.deadChildrens) + " "
        #if len(printString) > 0:
        #  print(printString)

    # print("Black count: " + str(blackCount))
    # print("Brown count: " + str(brownCount))
    # print("Yellow count: " + str(yellowCount))
    # print("Red count: " + str(redCount))
    # print("White count: " + str(whiteCount))
    # print("Gray count: " + str(grayCount))
    # print("Sum: " + str(blackCount + brownCount + yellowCount + redCount + whiteCount + grayCount))

    isAlive = 0
    isDead = 0

    if manualOverride:
        input()

    if timers:
        start1 = time.time()
    world.increaseYear()
    if timers:
        end1 = time.time()
        worldtime = end1 - start1
        start1 = time.time()
    Events.increaseAge(people, world)
    if timers:
        end1 = time.time()
        incAgeTime = end1 - start1
        start1 = time.time()
    Events.birthPeople(world, people)
    if timers:
        end1 = time.time()
        birthtime = end1 - start1
        start1 = time.time()
    FF.SpouseMatchmaking(families, people, world)
    if timers:
        end1 = time.time()
        spouseMMTime = end1 - start1
        start1 = time.time()
    Events.settlementsPopulationManagement(world, families)
    if timers:
        end1 = time.time()
        breakSettlementsPopTime = end1 - start1
        end = time.time()
        fullTime = end-start
        if fullTime > 0.0:
            print("WorldTime: " + str(worldtime) + " %: " + str(worldtime/fullTime))
            print("IncAgeTime: " + str(incAgeTime) + " %: " + str(incAgeTime/fullTime))
            print("BirthTime: " + str(birthtime) + " %: " + str(birthtime/fullTime))
            print("SpouseMMTime: " + str(spouseMMTime) + " %: " + str(spouseMMTime/fullTime))
            print("breakSettlementsPopTime: " + str(breakSettlementsPopTime) + " %: " + str(breakSettlementsPopTime/fullTime))
        print(fullTime)

    for family in families:
        isAlive += family.getAliveMemberNumber()
        isDead += family.getDeadMemberNumber()

    print("PeopleOBJNUMBER: " + str(len(people)))
    print("Population alive: " + str(isAlive))
    print("Population dead: " + str(isDead))
    print("Population sum: " + str(isAlive+isDead))
    print("Settlement 0 pop: " + str(world.getRegionFromIndex(0).getSettlementFromIndex(0).getPopulation()))
    #print("Settlement 0 residents: " + str(len(world.getRegionFromIndex(0).getSettlementFromIndex(0).getResidents())))
    print("Settlement 1 pop: " + str(world.getRegionFromIndex(0).getSettlementFromIndex(1).getPopulation()))
    #print("Settlement 1 residents: " + str(len(world.getRegionFromIndex(0).getSettlementFromIndex(1).getResidents())))
    if len(world.getRegionFromIndex(0).getSettlements()) >= 3:
        print("Settlement 2 pop: " + str(world.getRegionFromIndex(0).getSettlementFromIndex(2).getPopulation()))
        #print("Settlement 2 residents: " + str(len(world.getRegionFromIndex(0).getSettlementFromIndex(2).getResidents())))
    if len(world.getRegionFromIndex(0).getSettlements()) >= 4:
        print("Settlement 3 pop: " + str(world.getRegionFromIndex(0).getSettlementFromIndex(3).getPopulation()))
        #print("Settlement 3 residents: " + str(len(world.getRegionFromIndex(0).getSettlementFromIndex(3).getResidents())))
    if len(world.getRegionFromIndex(0).getSettlements()) >= 5:
        print("Settlement 4 pop: " + str(world.getRegionFromIndex(0).getSettlementFromIndex(4).getPopulation()))
        #print("Settlement 4 residents: " + str(len(world.getRegionFromIndex(0).getSettlementFromIndex(4).getResidents())))
    if len(world.getRegionFromIndex(0).getSettlements()) >= 6:
        print("Settlement 5 pop: " + str(world.getRegionFromIndex(0).getSettlementFromIndex(5).getPopulation()))
        #print("Settlement 5 residents: " + str(len(world.getRegionFromIndex(0).getSettlementFromIndex(5).getResidents())))
    if len(world.getRegionFromIndex(0).getSettlements()) >= 7:
        print("Settlement 6 pop: " + str(world.getRegionFromIndex(0).getSettlementFromIndex(6).getPopulation()))
        #print("Settlement 6 residents: " + str(len(world.getRegionFromIndex(0).getSettlementFromIndex(6).getResidents())))
    if len(world.getRegionFromIndex(0).getSettlements()) >= 8:
        print("Settlement 7 pop: " + str(world.getRegionFromIndex(0).getSettlementFromIndex(7).getPopulation()))
        #print("Settlement 7 residents: " + str(len(world.getRegionFromIndex(0).getSettlementFromIndex(7).getResidents())))
    if len(world.getRegionFromIndex(0).getSettlements()) >= 9:
        print("Settlement 8 pop: " + str(world.getRegionFromIndex(0).getSettlementFromIndex(8).getPopulation()))
        #print("Settlement 8 residents: " + str(len(world.getRegionFromIndex(0).getSettlementFromIndex(8).getResidents())))
    if len(world.getRegionFromIndex(0).getSettlements()) >= 10:
        print("Settlement 9 pop: " + str(world.getRegionFromIndex(0).getSettlementFromIndex(9).getPopulation()))
        #print("Settlement 9 residents: " + str(len(world.getRegionFromIndex(0).getSettlementFromIndex(9).getResidents())))
    if len(world.getRegionFromIndex(0).getSettlements()) >= 11:
        print("Settlement 10 pop: " + str(world.getRegionFromIndex(0).getSettlementFromIndex(10).getPopulation()))
        #print("Settlement 9 residents: " + str(len(world.getRegionFromIndex(0).getSettlementFromIndex(9).getResidents())))
    if len(world.getRegionFromIndex(0).getSettlements()) >= 12:
        print("Settlement 11 pop: " + str(world.getRegionFromIndex(0).getSettlementFromIndex(11).getPopulation()))
        #print("Settlement 9 residents: " + str(len(world.getRegionFromIndex(0).getSettlementFromIndex(9).getResidents())))


def main():

    world.generateRegions(Parameters.startingNumberOfRegions)
    world.generateSettlements()
    families = initFamilies()
    people = initPeople(families)


    manualOverride = False

    sun = True

    pCount = 300
    pTime = 1000 / pCount

    tickStartTime = time.time() * 1000.0

    while sun:

        tickCurrentTime = time.time() * 1000.0

        if tickCurrentTime - tickStartTime >= pTime:
            running(world, families, people, manualOverride)

            tickStartTime = time.time() * 1000.0

        if world.getYear() == 700:
            # for region in world.getRegions():
            #     for settlement in region.getSettlements():
            #         print(settlement.getSettlementName())
            #         if len(settlement.getUniqueFamilies()) > 0:
            #             for uniqueFamily in settlement.getUniqueFamilies():
            #                 residentFamilyMember = filter(lambda person: person.lastName in uniqueFamily, settlement.getResidents())
            #                 print(uniqueFamily + " : " + str(len(list(residentFamilyMember))))

            return
main()

