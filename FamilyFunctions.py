import random
import time

import HouseFunctions
from Enums import MaritalStatus, Sexes
import Enums
import Utils
import PersonLifeEventsHistory as PLEH

def FindAvailableSpouses (families, person):

    availableSpouses = []
    for family in families:
        if family.familyName != person.familyName and (family.getOriginRegion() == person.familyObjRef.getOriginRegion() or False): #temp flag
            if person.getSex() == Sexes.MALE:
                # availableSpouses.extend(family.getUnmarriedFemalesList())
                for eachFreeMember in family.getUnmarriedFemalesList():
                    availableSpouses.append(eachFreeMember)
            else:
                # availableSpouses.extend(family.getUnmarriedMalesList())
                for eachFreeMember in family.getUnmarriedMalesList():
                    availableSpouses.append(eachFreeMember)

    return availableSpouses

def RemoveFromUnmarriedList (person, spouse):

    person.familyObjRef.removeUnmarriedMember(person)
    spouse.familyObjRef.removeUnmarriedMember(spouse)


def AddToMarriedList (person, spouse):

    #if female change lastName => could be modified by culture
    #exception when it is only member of family, don't change
    if person.familyObjRef.getOriginCulture().getInheritanceBy() != person.sex:
        spouse.familyObjRef.addMarriedMember(person)
        spouse.familyObjRef.addMarriedMember(spouse)
    else:
        person.familyObjRef.addMarriedMember(person)
        person.familyObjRef.addMarriedMember(spouse)

def changeToOriginalFamilyNameAfterDivorce(person, spouse, world):

    spouseObj = spouse
    if person.familyObjRef.getOriginCulture().getInheritanceBy() != person.sex:
        PLEH.changedLastName(person, world, person.getFamilyName())
        person.lastName = person.getFamilyName()
        person.familyObjRef = person.getOriginFamilyObjectRef()
    else:
        PLEH.changedLastName(spouseObj, world, spouseObj.getFamilyName())
        spouseObj.lastName = spouse.getFamilyName()
        spouse.familyObjRef = spouse.getOriginFamilyObjectRef()

def ChangeFamilyName (person, spouse, world):

    spouseObj = spouse
    #if female change lastName => could be modified by culture
    #exception when it is only member of family, don't change
    #CULTURE MIX WHAT IF 2 DIFF CULTURES MEET? => random who is first as person


    if person.familyObjRef.getOriginCulture().getInheritanceBy() != person.sex:
        PLEH.changedLastName(person, world, spouseObj.getLastName())
        person.lastName = spouseObj.getLastName()
        person.familyObjRef = spouse.familyObjRef
    else:
        PLEH.changedLastName(spouseObj, world, person.getFamilyName())
        spouseObj.lastName = person.getLastName()
        spouse.familyObjRef = person.familyObjRef

def divorces (world):

    for person in world.getAlivePeople():
        if person.getSpouseRelation() < -25 and person.getMaritialStatus() == Enums.MaritalStatus.MARRIED and person.lifeStatus == Enums.LifeStatus.ALIVE:
            randomChance = Utils.randomRange(1, 10000)
            if randomChance < abs(person.getSpouseRelation()):
                person.changeMaritalStatus(Enums.MaritalStatus.DIVORCED)
                person.spouse.changeMaritalStatus(Enums.MaritalStatus.DIVORCED)
                PLEH.divorced(person, world)
                PLEH.divorced(person.getSpouse(), world)
                person.addExSpouse(person.getSpouse())
                person.getSpouse().addExSpouse(person)
                person.setSpouseRelation(0)
                person.changeSpouseNumberOfLikedTraits(0)
                person.changeSpouseNumberOfDislikedTraits(0)
                person.getSpouse().setSpouseRelation(0)
                person.getSpouse().changeSpouseNumberOfLikedTraits(0)
                person.getSpouse().changeSpouseNumberOfDislikedTraits(0)
                person.getFamilyObjectRef().removeMarriedMember(person)
                person.getSpouse().getFamilyObjectRef().removeMarriedMember(person.getSpouse())
                person.getOriginFamilyObjectRef().addUnmarriedMember(person)
                person.getSpouse().getOriginFamilyObjectRef().addUnmarriedMember(person.getSpouse())
                changeToOriginalFamilyNameAfterDivorce(person.getSpouse(), person, world)
                person.getSpouse().setSpouse(None)
                person.setSpouse(None)
                world.changeDivorcesNumber(1)

                newHouse = HouseFunctions.getNewHouse()
                person.getSettlement().buildNewHouse(newHouse)
                HouseFunctions.setHouseDurability(newHouse, Utils.randomRange(60, 90))
                person.getAccommodation().removeHouseResident(person)
                newHouse.addHouseResident(person)
                HouseFunctions.setNewHouseToPerson(person, newHouse)
                #HouseFunctions.addNewOwner(person, newHouse)


def spouseMatchmaking (params):

    world = params[0]
    timeTable = params[1]

    validMaritalStatuses = {Enums.MaritalStatus.SINGLE, Enums.MaritalStatus.WIDOW, Enums.MaritalStatus.WIDOWER, Enums.MaritalStatus.DIVORCED}

    #CANT USE PERSON IN UNMARIED LIST BECAUSE OF STRANGE ERRORS CONNECTED WITH PREVIOUS SPOUS DYING IN THE SAME YEAR AND LOOP family.getUnmarried list NOT RECOGNIZING IT!!!

    times = 0

    for person in world.getAlivePeople():

        if person.lifeStatus == Enums.LifeStatus.ALIVE and person.age >= 15 and person.spouse is None and validMaritalStatuses:

            if checkIfOccupationIsPriest(person):
                continue

            start = time.perf_counter()
            availableSpouesesList = FindAvailableSpouses(world.getFamilies(), person)
            end = time.perf_counter()
            findSpouseTime = end - start
            times += findSpouseTime
            if len(availableSpouesesList) > 0 and random.random() < 0.05:
                randomSpouse = Utils.randomFromCollection(availableSpouesesList)
                if checkIfOccupationIsPriest(randomSpouse):
                    continue
                person.spouse = randomSpouse
                spouseObj = person.spouse
                person.maritalStatus = Enums.MaritalStatus.MARRIED
                spouseObj.spouse = person
                spouseObj.maritalStatus = Enums.MaritalStatus.MARRIED
                PLEH.married(person, world)
                PLEH.married(spouseObj, world)
                checkLDTraitsNumber(person)
                person.changeSpouseRelation(50)
                spouseObj.changeSpouseRelation(50)

                newHouse = HouseFunctions.getNewHouse()
                HouseFunctions.setHouseDurability(newHouse, Utils.randomRange(60, 90))
                movingMarriedCoupleToNewHouse(person, newHouse, world)
                movingMarriedCoupleToNewHouse(spouseObj, newHouse, world)

                # if person.getSex() == Sexes.MALE:
                #     spouseObj.getAccommodation().removeHouseResident(spouseObj)
                #     spouseObj.setAccommodation(person.getAccommodation())
                #     spouseObj.getAccommodation().addHouseResident(spouseObj)
                #     spouseObj.getSettlement().decreasePopulation()
                #     spouseObj.getSettlement().removeResident(spouseObj)
                #     spouseObj.setSettlement(person.getSettlement())
                #     spouseObj.getSettlement().increasePopulation()
                #     spouseObj.getSettlement().addResident(spouseObj)
                #     fireSingleEmployee(spouseObj, world)
                #
                # else:
                #     person.getAccommodation().removeHouseResident(person)
                #     person.setAccommodation(spouseObj.getAccommodation())
                #     person.getAccommodation().addHouseResident(person)
                #     person.getSettlement().decreasePopulation()
                #     person.getSettlement().removeResident(person)
                #     person.setSettlement(spouseObj.getSettlement())
                #     person.getSettlement().increasePopulation()
                #     person.getSettlement().addResident(person)
                #     fireSingleEmployee(person, world)

                #TODO FIX ISSUE WHEN ONLY 1 FEMALE IS IN FAMILY
                RemoveFromUnmarriedList(person, spouseObj)
                AddToMarriedList(person, spouseObj)
                ChangeFamilyName(person, spouseObj, world)

                # #new House for marriage
                # newHouse = HouseFunctions.getNewHouse()
                # person.getSettlement().buildNewHouse(newHouse)
                # HouseFunctions.setHouseDurability(newHouse, Utils.randomRange(60, 90))
                # person.getAccommodation().removeHouseResident(person)
                # person.getSpouse().getAccommodation().removeHouseResident(spouseObj)
                # HouseFunctions.setNewHouseToPerson(person, newHouse)
                # #HouseFunctions.addNewOwner(person, newHouse)
                # HouseFunctions.setNewHouseToPerson(spouseObj, newHouse)
                # newHouse.addHouseResident(person)
                # newHouse.addHouseResident(person.getSpouse())

    timeTable.extend([times])
    print("SposesSumTime: " + str(times))

def checkIfOccupationIsPriest(person):

    if person.getOccupation() is not None and person.getOccupation().getOccupationName() == 'Priest':
        return True
    else:
        return False

def movingMarriedCoupleToNewHouse(person, newHouse, world):

    person.getAccommodation().removeHouseResident(person)
    person.setAccommodation(newHouse)
    person.getAccommodation().addHouseResident(person)

    if person.getSex() == Sexes.FEMALE:

        if person.getSettlement() != person.getSpouse().getSettlement():
            person.getSettlement().decreasePopulation()
            person.getSettlement().removeResident(person)
            person.setSettlement(person.spouse.getSettlement())
            person.getSettlement().increasePopulation()
            person.getSettlement().addResident(person)
            person.getSpouse().getSettlement().buildNewHouse(newHouse)
            fireSingleEmployee(person, world)

        # parentChildrensList = person.getAliveChildrenList()
        # for parentChild in parentChildrensList:
        #     if parentChild.age < 15:
        #         parentChild.getSettlement().decreasePopulation()
        #         parentChild.getSettlement().removeResident(person)
        #         parentChild.setSettlement(person.spouse.getSettlement())
        #         parentChild.getSettlement().increasePopulation()
        #         parentChild.getSettlement().addResident(person)


def checkLDTraitsNumber(person):

    person.setSpouseNumberOfLikedTraits(0)
    person.setSpouseNumberOfDislikedTraits(0)
    person.getSpouse().setSpouseNumberOfLikedTraits(0)
    person.getSpouse().setSpouseNumberOfDislikedTraits(0)

    for trait in person.getTraits():
        if trait in person.getSpouse().getLikedTraits():
            person.getSpouse().changeSpouseNumberOfLikedTraits(1)
        if trait in person.getSpouse().getDislikedTraits():
            person.getSpouse().changeSpouseNumberOfDislikedTraits(1)
    for trait in person.getSpouse().getTraits():
        if trait in person.getLikedTraits():
            person.changeSpouseNumberOfLikedTraits(1)
        if trait in person.getDislikedTraits():
            person.changeSpouseNumberOfDislikedTraits(1)

def FindNextHeir (families, people):

    return

def fireSingleEmployee(person, world):

    if person.getOccupation() is not None:
        person.getOccupation().removeWorker(person)
        person.setOccupation(None)
        PLEH.lostEmpoyment(person, world)

