from Enums import MaritalStatus
import Utils

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



