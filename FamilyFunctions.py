import HouseFunctions
from Enums import MaritalStatus, Sexes
import Enums
import Utils
import PersonLifeEventsHistory as PLEH

def FindAvailableSpouses (families, person):

    availableSpouses = []
    for family in families:
        if family.familyName != person.familyName and (family.getOriginRegion() == person.familyObjRef.getOriginRegion() or False): #temp flag
            if person.sex == Sexes.MALE:
                for eachFreeMember in family.getUnmarriedFemalesList():
                    availableSpouses.append(eachFreeMember)
            if person.sex == Sexes.FEMALE:
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
            randomChance = Utils.randomRange(1, 100)
            if randomChance < abs(person.getSpouseRelation()):
                person.changeMaritalStatus(Enums.MaritalStatus.DIVORCED)
                person.spouse.changeMaritalStatus(Enums.MaritalStatus.DIVORCED)
                PLEH.divorced(person, world)
                PLEH.divorced(person.getSpouse(), world)
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


def spouseMatchmaking (world):

    #CANT USE PERSON IN UNMARIED LIST BECAUSE OF STRANGE ERRORS CONNECTED WITH PREVIOUS SPOUS DYING IN THE SAME YEAR AND LOOP family.getUnmarried list NOT RECOGNIZING IT!!!

    for person in world.getAlivePeople():

         if person.lifeStatus == Enums.LifeStatus.ALIVE and person.age >= 15 and person.spouse is None and (person.maritalStatus == Enums.MaritalStatus.SINGLE or person.maritalStatus == Enums.MaritalStatus.WIDOW or person.maritalStatus == Enums.MaritalStatus.WIDOWER or person.maritalStatus == Enums.MaritalStatus.DIVORCED):

            availableSpouesesList = FindAvailableSpouses(world.getFamilies(), person)
            if len(availableSpouesesList) > 0:
                randomSpouse = Utils.randomFromCollection(availableSpouesesList)
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

                #TODO FIX ISSUE WHEN ONLY 1 FEMALE IS IN FAMILY
                RemoveFromUnmarriedList(person, spouseObj)
                AddToMarriedList(person, spouseObj)
                ChangeFamilyName(person, spouseObj, world)

                newHouse = HouseFunctions.getNewHouse()
                person.getSettlement().buildNewHouse(newHouse)
                HouseFunctions.setHouseDurability(newHouse, Utils.randomRange(60, 90))
                person.getAccommodation().removeHouseResident(person)
                person.getSpouse().getAccommodation().removeHouseResident(spouseObj)
                HouseFunctions.setNewHouseToPerson(person, newHouse)
                HouseFunctions.setNewHouseToPerson(spouseObj, newHouse)
                newHouse.addHouseResident(person)
                newHouse.addHouseResident(person.getSpouse())


def checkLDTraitsNumber(person):

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