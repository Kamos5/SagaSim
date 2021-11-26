import FamilyInitGenerator as FIG
import MembersInitGenerator as MIG
from World import World as World
import Events
import Enums
import PeopleFunctions as MF
import FamilyFunctions as FF
import PeopleInterface as PIF
import random

world = World()

def initFamilies():

    families = FIG.Init(world)

    return families

def initPeople(families):

    people = MIG.Init(families, world)
    for family in families:
        MIG.initInitMarrieges(family, people)

    return people

def main():

    families = []

    world = World()
    families = initFamilies()
    people = initPeople(families)

    sun = 'true'

    while (sun):
        print(world.getYear())

        # for val in families:
        #     print(val.familyName)
        #     print("Female Number:" + " " + str(val.getFemaleNumber()))
        #     print("Male Number:" + " " + str(val.getMaleNumber()))
        #     print("Children Number: " + " " + str(val.getChildrenNumber()))
        #     print("Members Number:" + " " + str(val.getFamilyMembersNumber()))
        #     print("LEN UAM: " + str(len(val.unmarriedAdultMaleList)))
        #     print("LEN UAF: " + str(len(val.unmarriedAdultFemaleList)))
            # for UAM in val.unmarriedAdultMaleList:
            #     print("Unmarried male family member: " + " " + UAM)
            # for UAF in val.unmarriedAdultFemaleList:
            #     print("Unmarried female family member: " + " " + UAF)


        isAliveFlag = False
        personUUIDFLAG = True
        personFirstNameFLAG = True
        personLastNameFLAG = True
        personSexFLAG = True
        personAgeFLAG = True
        personLifeSpanFLAG = False
        personModLifeSpanFLAG = False
        personLifeStatFLAG = True
        fatherFLAG = True
        motherFLAG = True
        spouseFLAG = True
        causeOfDeathFLAG = True
        hairColorFLAG = True

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
                if (motherFLAG):
                    printString += "Mother: " + PIF.findOneFirstName(people, person.mother) + " "
                if (spouseFLAG):
                    printString += "Spouse: " + PIF.findOneFirstName(people, person.spouse) + " "
                if (causeOfDeathFLAG):
                    printString += "Status: " + person.causeOfDeath.value + " "
                if (hairColorFLAG):
                    printString += "HairColor: " + person.hairColor.value[1] + " "

            print(printString)

            # if len(person.deadSpouses) > 0:
            #     print("   Dead spouses:")
            #     for dspouse in person.deadSpouses:
            #         print("      " + PIF.findOneFirstName(people, dspouse))
            # if person.lifeStatus == Enums.LifeStatus.ALIVE and person.spouse == '':
            #     print(FF.FindAvailableSpouses(families, person))
        input()

        world.increaseYear()
        Events.increaseAge(people)
        Events.birthPeople(world, families, people)
        FF.UpdateLists(families, people)
        FF.SpouseMatchmaking(families, people)
        FF.UpdateLists(families, people)

        if world.getYear() == 535:
            break


def menuCall():

    input = input()












main()

