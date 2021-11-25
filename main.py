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

        for val in families:
            print(val.familyName)
            print("Female Number:" + " " + str(val.getFemaleNumber()))
            print("Male Number:" + " " + str(val.getMaleNumber()))
            print("Children Number: " + " " + str(val.getChildrenNumber()))
            print("Members Number:" + " " + str(val.getFamilyMembersNumber()))
        #     print("LEN UAM: " + str(len(val.unmarriedAdultMaleList)))
        #     print("LEN UAF: " + str(len(val.unmarriedAdultFemaleList)))
            # for UAM in val.unmarriedAdultMaleList:
            #     print("Unmarried male family member: " + " " + UAM)
            # for UAF in val.unmarriedAdultFemaleList:
            #     print("Unmarried female family member: " + " " + UAF)

        for person in people:
            stringText = ''
            personSuperObj = person
            if (person.lifeStatus == Enums.LifeStatus.ALIVE):
                print(stringText + " " + person.personUUID + " " + person.firstName + " " + person.lastName + " Sex:" + person.sex + " Age:" + str(person.age) + " Lifespan:" + str(person.lifespan) + " ModLifespan:" + str(person.modifiedLifespan) + " Status:" + str(person.lifeStatus.value) + " Parents: " + PIF.findOneFirstName(people, person.father) + ";" + PIF.findOneFirstName(people, person.mother) + "-" + PIF.findOneFamilyName(people, person.father) + " Spouse:" + PIF.findOneFirstName(people, person.spouse))
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

