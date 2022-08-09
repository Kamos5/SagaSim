from Enums import MaritalStatus, Sexes
import Enums
import Utils
import time
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



def ChangeFamilyName (person, spouse):

    spouseObj = spouse
    #if female change lastName => could be modified by culture
    #exception when it is only member of family, don't change
    #CULTURE MIX WHAT IF 2 DIFF CULTURES MEET? => random who is first as person
    if person.familyObjRef.getOriginCulture().getInheritanceBy() != person.sex:
        person.lastName = spouseObj.lastName
        person.familyObjRef = spouse.familyObjRef
    else:
        spouseObj.lastName = person.lastName
        spouse.familyObjRef = person.familyObjRef



def SpouseMatchmaking (world):

    timeTable1 = []
    timeTable2 = []
    timeTable3 = []
    tempVar=0

    #CANT USE PERSON IN UNMARIED LIST BECAUSE OF STRANGE ERRORS CONNECTED WITH PREVIOUS SPOUS DYING IN THE SAME YEAR AND LOOP family.getUnmarried list NOT RECOGNIZING IT!!!
    for person in world.getPeople():
         if person.lifeStatus == Enums.LifeStatus.ALIVE and person.age >= 15 and person.spouse is None and (person.maritalStatus == Enums.MaritalStatus.SINGLE or person.maritalStatus == Enums.MaritalStatus.WIDOW or person.maritalStatus == Enums.MaritalStatus.WIDOWER or person.maritalStatus == Enums.MaritalStatus.DIVORCED):

            availableSpouesesList = FindAvailableSpouses(world.getFamilies(), person)
            #1 because there can be 2 people alone in the families and changning last name of 1 would make other family empty - which is not cool :(
            if len(availableSpouesesList) > 1:
                person.spouse = Utils.randomFromCollection(availableSpouesesList)

                spouseObj = person.spouse

                person.maritalStatus = Enums.MaritalStatus.MARRIED
                spouseObj.spouse = person
                spouseObj.maritalStatus = Enums.MaritalStatus.MARRIED
                PLEH.married(person, world)
                PLEH.married(spouseObj, world)

                RemoveFromUnmarriedList(person, spouseObj)

                AddToMarriedList(person, spouseObj)
                ChangeFamilyName(person, spouseObj)



def FindNextHeir (families, people):

    return