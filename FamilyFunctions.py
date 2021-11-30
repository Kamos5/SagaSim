from Enums import MaritalStatus, Sexes
import Enums
import Utils
import PeopleInterface as PIF

def FindAvailableSpouses (families, person):

    availableSpouses = []
    for family in families:
        if family.familyName != person.familyName and (family.getOriginSettlement() == person.familyObjRef.getOriginSettlement() or True): #temp flag
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

    #move wife to husband's family
    if person.sex == Enums.Sexes.MALE:
        person.familyObjRef.addMarriedMember(person)
        person.familyObjRef.addMarriedMember(spouse)
    else:
        spouse.familyObjRef.addMarriedMember(person)
        spouse.familyObjRef.addMarriedMember(spouse)

def ChangeFamilyName (person, spouse):

    spouseObj = spouse

    if person.sex == Sexes.FEMALE:
        person.lastName = spouseObj.lastName
        person.familyObjRef = spouse.familyObjRef
    else:
        spouseObj.lastName = person.lastName
        spouse.familyObjRef = person.familyObjRef

def SpouseMatchmaking (families, people):

    for person in people:
        if person.lifeStatus == Enums.LifeStatus.ALIVE and person.age >= 15 and person.spouse is None and (person.maritalStatus == Enums.MaritalStatus.SINGLE or person.maritalStatus == Enums.MaritalStatus.WIDOW or person.maritalStatus == Enums.MaritalStatus.WIDOWER or person.maritalStatus == Enums.MaritalStatus.DIVORCED):

            availableSpouesesList = FindAvailableSpouses(families, person)
            if len(availableSpouesesList) > 0:
                person.spouse = Utils.randomFromCollection(availableSpouesesList)

                spouseObj = person.spouse

                person.maritalStatus = Enums.MaritalStatus.MARRIED
                spouseObj.spouse = person
                spouseObj.maritalStatus = Enums.MaritalStatus.MARRIED
                RemoveFromUnmarriedList(person, spouseObj)
                ChangeFamilyName(person, spouseObj)


def FindNextHeir (families, people):

    return