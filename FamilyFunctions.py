from Enums import MaritalStatus
import Enums
import Utils
import PeopleInterface as PIF

def UpdateLists (families, people):

    for family in families:
        deadMembersList = []
        childrenNumber = 0
        unmarriedAdultMaleList = []
        unmarriedAdultFemaleList = []
        adultMalesNumer = 0
        adultFemalesNumber = 0
        for person in people:
            if (family.familyName == person.familyName):
                if person.maritalStatus == MaritalStatus.DEAD:
                    deadMembersList.append(person.personUUID)
                if person.age < 15 and person.maritalStatus != MaritalStatus.DEAD:
                    childrenNumber += 1
                if person.maritalStatus != MaritalStatus.DEAD and person.sex == "M":
                    adultMalesNumer += 1
                if person.maritalStatus != MaritalStatus.DEAD and person.sex == "F":
                    adultFemalesNumber +=1
                if person.age > 15 and person.maritalStatus != MaritalStatus.DEAD and person.sex == "M" and person.maritalStatus != MaritalStatus.MARRIED:
                    unmarriedAdultMaleList.append(person.personUUID)
                if person.age > 15 and person.maritalStatus != MaritalStatus.DEAD and person.sex == "F" and person.maritalStatus != MaritalStatus.MARRIED:
                    unmarriedAdultFemaleList.append(person.personUUID)
        family.deadMemberList = deadMembersList
        family.childrenNumber = childrenNumber
        family.unmarriedAdultMaleList = unmarriedAdultMaleList
        family.unmarriedAdultFemaleList = unmarriedAdultFemaleList
        family.setMaleNumber(adultMalesNumer)
        family.setFemaleNumber(adultFemalesNumber)


def FindAvailableSpouses (families, person):

    availableSpouses = []
    if person.lifeStatus == Enums.LifeStatus.ALIVE and person.spouse == '' and person.age > 15:
        for family in families:
            if family.familyName != person.familyName:
                if person.sex == 'M':
                    for eachFreeMember in family.unmarriedAdultFemaleList:
                        availableSpouses.append(eachFreeMember)
                if person.sex == 'F':
                    for eachFreeMember in family.unmarriedAdultMaleList:
                        availableSpouses.append(eachFreeMember)

    return availableSpouses


def RemoveFromUnmarriedList (families, people, person):

    for family in families:
        if family.familyName == person.familyName:
            if person.sex == "M":
                family.removeFromUnmarriedAdultMalesUUIDsList(person.personUUID)
            if person.sex == "F":
                family.removeFromUnmarriedAdultFemalesUUIDsList(person.personUUID)


def ChangeFamilyName (people, person):

    if person.sex == "F":
        person.lastName = PIF.findOnePersonObj(people, person.spouse).lastName
    else:
        if PIF.findOnePersonObj(people, person.spouse).sex == "F":
            PIF.findOnePersonObj(people, person.spouse).lastName = person.lastName


def SpouseMatchmaking (families, people):

    for person in people:
        if person.lifeStatus == Enums.LifeStatus.ALIVE and person.spouse == '' and (person.maritalStatus == Enums.MaritalStatus.SINGLE or person.maritalStatus == Enums.MaritalStatus.WIDOW or person.maritalStatus == Enums.MaritalStatus.WIDOWER or person.maritalStatus == Enums.MaritalStatus.DIVORCED):

            availableSpouesesList = FindAvailableSpouses(families, person)
            if (len(availableSpouesesList) > 0):
                person.spouse = Utils.randomFromCollection(FindAvailableSpouses(families, person))
                person.maritalStatus = Enums.MaritalStatus.MARRIED
                PIF.findOnePersonObj(people, person.spouse).spouse = person.personUUID
                PIF.findOnePersonObj(people, person.spouse).maritalStatus = Enums.MaritalStatus.MARRIED
                RemoveFromUnmarriedList(families, people, PIF.findOnePersonObj(people, person.spouse))
                ChangeFamilyName(people, person)