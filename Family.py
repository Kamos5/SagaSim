import Utils
from Enums import Sexes, MaritalStatus


class Family:

    def __init__(self, fname):
        self.familyUUID = Utils.createUUID()
        self.familyName = fname
        self.familyBranchedFrom = ''
        self.foundingYear = 0
        self.originRegion = ''
        self.originSettlement = ''
        self.originCulture = ''

        #every member of family
        self.femaleNumber = 0
        self.maleNumber = 0

        self.femalesList = []
        self.malesList = []

        #only adults members
        self.adultFemale = 0
        self.adultMale = 0

        self.adultFemalesList = []
        vadultMalesList = []

        #only childens members
        self.childrenFemaleNumber = 0
        self.childrenMaleNumber = 0

        self.childrenFemalesList = []
        self.childrenMalesList = []

        self.unmarriedFemaleNumber = 0
        self.unmarriedMaleNumber = 0

        self.unmarriedFemalesList = []
        self.unmarriedMalesList = []

        self.marriedFemaleNumber = 0
        self.marriedMaleNumber = 0

        self.marriedFemalesList = []
        self.marriedMalesList = []

        #sum of female and male numbers
        self.aliveMemberNumber = 0
        self.aliveMembersList = []

        self.deadMemberNumber = 0
        self.deadMembersList = []

    def getOriginRegion(self):
        return self.originRegion
    def setOriginRegion(self, newOriginRegion):
        self.originRegion = newOriginRegion
    def getOriginSettlement(self):
        return self.originSettlement
    def setOriginSettlement(self, newOriginSettlement):
        self.originSettlement = newOriginSettlement


    def getFamilyName(self):
        return self.familyName
    def setFamilyName(self, newFamilyName):
        self.familyName = newFamilyName
    def getFamilyBranchedFrom(self):
        return self.familyBranchedFrom
    def setFamilyBranchedFrom(self, newFamilyRoot):
        self.familyBranchedFrom = newFamilyRoot
    def getFoundingYear(self):
        return self.foundingYear
    def setFoundingYear(self, newFoundingYear):
        self.foundingYear = newFoundingYear


    def getFemaleNumber(self):
        return self.femaleNumber
    def increaseFemaleNumber(self):

        self.femaleNumber += 1
    def decreaseFemaleNumber(self):

        self.femaleNumber -= 1
    def setFemaleNumber(self, number):

        self.femaleNumber = number

    def getMaleNumber(self):
        return self.maleNumber
    def increaseMaleNumber(self):

        self.maleNumber += 1
    def decreaseMaleNumber(self):

        self.maleNumber -= 1
    def setMaleNumber(self, number):

        self.maleNumber = number

    def getAllMembersNumber(self):
        return self.getFemaleNumber() + self.getMaleNumber()

    def getFemalesList(self):
        return self.femalesList
    def appendFemalesList(self, person):
        self.femalesList.append(person)
        self.increaseFemaleNumber()
        self.increaseAliveMemberNumber()
        person.familyObjRef.getOriginSettlement().increasePopulation()
    def removeFromFemalesList(self, person):
        self.femalesList.remove(person)
        self.decreaseFemaleNumber()
        self.decreaseAliveMemberNumber()
        person.familyObjRef.getOriginSettlement().decreasePopulation()
    def setFemalesList(self, list):
        self.femalesList = list

    def getMalesList(self):
        return self.malesList
    def appendMalesList(self, person):
        self.malesList.append(person)
        self.increaseMaleNumber()
        self.increaseAliveMemberNumber()
        person.familyObjRef.getOriginSettlement().increasePopulation()
    def removeFromMalesList(self, person):
        self.malesList.remove(person)
        self.decreaseMaleNumber()
        self.decreaseAliveMemberNumber()
        person.familyObjRef.getOriginSettlement().decreasePopulation()
    def setMalesList(self, list):
        self.malesList = list

    def getAllMembersList(self):
        return self.getFemalesList() + self.getMalesList()

    def getFemaleAdultNumber(self):
        return self.adultFemale
    def increaseFemaleAdultNumber(self):

        self.adultFemale += 1
    def decreaseFemaleAdultNumber(self):

        self.adultFemale -= 1
    def setFemaleAdultNumber(self, number):

        self.adultFemale = number

    def getMaleAdultNumber(self):
        return self.adultMale
    def increaseMaleAdultNumber(self):

        self.adultMale += 1
    def decreaseMaleAdultNumber(self):

        self.adultMale -= 1
    def setMaleAdultNumber(self, number):

        self.adultMale = number

    def getAllAdultMembersNumber(self):
        return self.getFemaleAdultNumber() + self.getMaleAdultNumber()

    def getAdultFemalesList(self):
        return self.adultFemalesList
    def appendAdultFemalesList(self, person):
        self.adultFemalesList.append(person)
        self.increaseFemaleAdultNumber()
    def removeFromAdultFemalesList(self, person):
        self.adultFemalesList.remove(person)
        self.decreaseFemaleAdultNumber()
    def setAdultFemalesList(self, list):
        self.adultFemalesList = list

    def getAdultMalesList(self):
        return self.adultMalesList
    def appendAdultMalesList(self, person):
        self.adultMalesList.append(person)
        self.increaseMaleAdultNumber()
    def removeFromAdultMalesList(self, person):
        self.adultMalesList.remove(person)
        self.decreaseMaleAdultNumber()
    def setAdultMalesList(self, list):
        self.adultMalesList = list

    def getAllAdulsMembersList(self):
        return self.getAdultFemalesList() + self.getAdultMalesList()

    def getChildrenFemaleNumber(self):
        return self.childrenFemaleNumber
    def increaseChildrenFemaleNumber(self):

        self.childrenFemaleNumber += 1
    def decreaseChildrenFemaleNumber(self):

        self.childrenFemaleNumber -= 1
    def setChildrenFemaleNumber(self, number):

        self.childrenFemaleNumber = number

    def getChildrenMaleNumber(self):
        return self.childrenMaleNumber
    def increaseChildrenMaleNumber(self):

        self.childrenMaleNumber += 1
    def decreaseChildrenMaleNumber(self):

        self.childrenMaleNumber -= 1
    def setChildrenMaleNumber(self, number):

        self.childrenMaleNumber = number

    def getAllChildrenNumber(self):
        return self.getChildrenFemaleNumber() + self.getChildrenMaleNumber()

    def getChildrenFemalesList(self):
        return self.childrenFemalesList
    def appendChildrenFemalesList(self, person):
        self.childrenFemalesList.append(person)
        self.increaseChildrenFemaleNumber()
        self.appendFemalesList(person)
    def removeFromChildrenFemalesList(self, person):
        self.childrenFemalesList.remove(person)
        self.decreaseChildrenFemaleNumber()
        self.removeFromFemalesList(person)
    def setChildrenFemalesList(self, list):
        self.childrenFemalesList = list

    def getChildrenMalesList(self):
        return self.childrenMalesList
    def appendChildrenMalesList(self, person):
        self.childrenMalesList.append(person)
        self.increaseChildrenMaleNumber()
        self.appendMalesList(person)
    def removeFromChildrenMalesList(self, person):
        self.childrenMalesList.remove(person)
        self.decreaseChildrenMaleNumber()
        self.removeFromMalesList(person)
    def setChildrenMalesList(self, list):
        self.childrenMalesList = list

    def getAllChildrenList(self):
        return self.getChildrenFemalesList() + self.getChildrenMalesList()
    def addChildren(self, person):
        if person.sex == Sexes.FEMALE:
            self.appendChildrenFemalesList(person)

        else:
            self.appendChildrenMalesList(person)

    def removeChildren(self, person):
        if person.sex == Sexes.FEMALE:
            self.removeFromChildrenFemalesList(person)
        else:
            self.removeFromChildrenMalesList(person)
    def getUnmarriedFemaleNumber(self):
        return self.unmarriedFemaleNumber
    def increaseUnmarriedFemaleNumber(self):

        self.unmarriedFemaleNumber += 1
    def decreaseUnmarriedFemaleNumber(self):

        self.unmarriedFemaleNumber -= 1
    def setUnmarriedFemaleNumber(self, number):

        self.unmarriedFemaleNumber = number

    def getUnmarriedMaleNumber(self):
        return self.unmarriedMaleNumber
    def increaseUnmarriedMaleNumber(self):

        self.unmarriedMaleNumber += 1
    def decreaseUnmarriedMaleNumber(self):

        self.unmarriedMaleNumber -= 1
    def setUnmarriedMaleNumber(self, number):

        self.unmarriedMaleNumber = number

    def getAllUnmarriedNumber(self):
        return self.getUnmarriedFemaleNumber() + self.getUnmarriedMaleNumber()

    def getUnmarriedFemalesList(self):
        return self.unmarriedFemalesList
    def appendUnmarriedFemalesList(self, person):
        self.appendFemalesList(person)
        self.unmarriedFemalesList.append(person)
        self.increaseUnmarriedFemaleNumber()
    def removeFromUnmarriedFemalesList(self, person):
        self.removeFromFemalesList(person)
        self.unmarriedFemalesList.remove(person)
        self.decreaseUnmarriedFemaleNumber()
    def setUnmarriedFemalesList(self, list):
        self.unmarriedFemalesList = list

    def getUnmarriedMalesList(self):
        return self.unmarriedMalesList
    def appendUnmarriedMalesList(self, person):
        self.appendMalesList(person)
        self.unmarriedMalesList.append(person)
        self.increaseUnmarriedMaleNumber()
    def removeFromUnmarriedMalesList(self, person):
        self.removeFromMalesList(person)
        self.unmarriedMalesList.remove(person)
        self.decreaseUnmarriedMaleNumber()
    def setUnmarriedMalesList(self, list):
        self.unmarriedMalesList = list

    def getAllUnmarriedList(self):
        return self.getUnmarriedFemalesList() + self.getUnmarriedMalesList()
    def addUnmarriedMember(self, person):
        if person.sex == Sexes.FEMALE:
            self.appendUnmarriedFemalesList(person)
        else:
            self.appendUnmarriedMalesList(person)

    def removeUnmarriedMember(self, person):
        if person.sex == Sexes.FEMALE:
            self.removeFromUnmarriedFemalesList(person)
        else:
            self.removeFromUnmarriedMalesList(person)

    def getMarriedFemaleNumber(self):
        return self.marriedFemaleNumber
    def increaseMarriedFemaleNumber(self):

        self.marriedFemaleNumber += 1
    def decreaseMarriedFemaleNumber(self):

        self.marriedFemaleNumber -= 1
    def setMarriedFemaleNumber(self, number):

        self.marriedFemaleNumber = number

    def getMarriedMaleNumber(self):
        return self.marriedMaleNumber
    def increaseMarriedMaleNumber(self):

        self.marriedMaleNumber += 1
    def decreaseMarriedMaleNumber(self):

        self.marriedMaleNumber -= 1
    def setMarriedMaleNumber(self, number):

        self.marriedMaleNumber = number

    def getAllMarriedNumber(self):
        return self.getMarriedFemaleNumber() + self.getMarriedMaleNumber()

    def getMarriedFemalesList(self):
        return self.marriedFemalesList
    def appendMarriedFemalesList(self, person):
        self.appendFemalesList(person)
        self.marriedFemalesList.append(person)
        self.increaseMarriedFemaleNumber()
    def removeFromMarriedFemalesList(self, person):
        self.removeFromFemalesList(person)
        self.marriedFemalesList.remove(person)
        self.decreaseMarriedFemaleNumber()
    def setMarriedFemalesList(self, list):
        self.marriedFemalesList = list

    def getMarriedMalesList(self):
        return self.marriedMalesList
    def appendMarriedMalesList(self, person):
        self.appendMalesList(person)
        self.marriedMalesList.append(person)
        self.increaseMarriedMaleNumber()
    def removeFromMarriedMalesList(self, person):
        self.removeFromMalesList(person)
        self.marriedMalesList.remove(person)
        self.decreaseMarriedMaleNumber()
    def setMarriedMalesList(self, list):
        self.marriedMalesList = list

    def getAllMarriedList(self):
        return self.getMarriedFemalesList() + self.getMarriedMalesList()
    def addMarriedMember(self, person):
        if person.sex == Sexes.FEMALE:
            self.appendMarriedFemalesList(person)
        else:
            self.appendMarriedMalesList(person)
    def removeMarriedMember(self, person):
        if person.sex == Sexes.FEMALE:
            self.removeFromMarriedFemalesList(person)
        else:
            self.removeFromMarriedMalesList(person)

    def getAliveMemberNumber(self):
        return self.aliveMemberNumber
    def increaseAliveMemberNumber(self):
        self.aliveMemberNumber += 1
    def decreaseAliveMemberNumber(self):
        self.aliveMemberNumber -= 1
    def setAliveMemberNumber(self, newAliveMemberNumber):
        self.aliveMemberNumber = newAliveMemberNumber

    def getAliveMembersList(self):
        return self.aliveMembersList
    def setAliveMembersList(self, list):
        self.aliveMembersList = list

    def getDeadMemberNumber(self):
        return self.deadMemberNumber
    def increaseDeadMemberNumber(self):
        self.deadMemberNumber += 1
    def decreaseDeadMemberNumber(self):
        self.deadMemberNumber -= 1
    def setDeadMemberNumber(self, newDeadMemberNumber):
        self.deadMemberNumber = newDeadMemberNumber

    def getDeadMembersList(self):
        return self.deadMembersList
    def appendDeadMembersList(self, person):

        if person.age >= 15:
            if person.maritalStatus == MaritalStatus.MARRIED:
                self.removeMarriedMember(person)
            else:
                self.removeUnmarriedMember(person)
            self.deadMembersList.append(person)
            self.increaseDeadMemberNumber()
        else:
            self.removeChildren(person)
    def setDeadMembersList(self, list):
        self.deadMembersList = list

    def moveChildToAdultMembers(self, person):

        self.removeChildren(person)
        self.addUnmarriedMember(person)


    def addNewMember(self, person):

        if person.age < 15:
            self.addChildren(person)
        else:
            if person.maritalStatus == MaritalStatus.MARRIED:
                self.addMarriedMember(person)
            else:
                self.addUnmarriedMember(person)




