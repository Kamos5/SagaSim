import Utils
import NameGenerator
from Enums import Sexes

class Family:

    def __init__(self, fname):
        self.familyUUID = Utils.createUUID()
        self.familyName = fname
        self.femaleNumber = 0
        self.femaleList = []
        self.maleList = []
        self.maleNumber = 0
        self.childrenNumber = 0
        self.adultMaleList = []
        self.adultFemaleList = []
        self.unmarriedAdultMaleList = []
        self.unmarriedAdultFemaleList = []
        self.deadMemberList = []
        self.foundingYear = 0
        self.aliveMembers = []

    def increaseFemaleNumber(self):

        self.femaleNumber += 1

    def increaseMaleNumber(self):

        self.maleNumber += 1

    def increaseChildrenNumber(self):
        self.childrenNumber += 1

    def decreaseChildrenNumber(self):
        self.childrenNumber -= 1

    def getFemaleNumber(self):
        return self.femaleNumber

    def setFemaleNumber(self, number):
        self.femaleNumber = number

    def getMaleNumber(self):
        return self.maleNumber

    def setMaleNumber(self, number):
        self.maleNumber = number

    def getChildrenNumber(self):
        return self.childrenNumber

    def addNewMember(self, person):
        self.membersObj = {}
        self.membersObj['UUID'] = person.personUUID
        self.aliveMembers.append(self.membersObj)

        if person.sex == Sexes.MALE:
            self.increaseMaleNumber()
        else:
            self.increaseFemaleNumber()

    def addNewUnmarriedMember(self, person):

        if person.sex == Sexes.MALE:
            self.unmarriedAdultMaleList.append(person)
        else:
            self.unmarriedAdultFemaleList.append(person)

    def setChildToAdultMember(self, person):

        if person.sex == Sexes.MALE:
            self.unmarriedAdultMaleList.append(person)
        else:
            self.unmarriedAdultFemaleList.append(person)
        self.decreaseChildrenNumber()

    def getAllAliveMembersUUIDs(self):
        return self.aliveMembers

    def getAllUnmarriedAdultMales(self):
        return self.unmarriedAdultMaleList

    def setAllUnmarriedAdultMales(self, list):
        self.unmarriedAdultMaleList = list

    def getAllUnmarriedAdultFemales(self):
        return self.unmarriedAdultFemaleList

    def setAllUnmarriedAdultFemales(self, list):
        self.unmarriedAdultFemaleList = list

    def getFamilyMembersNumber(self):
        return self.femaleNumber + self.maleNumber

    def removeFromUnmarriedAdultMalesList(self, person):
        self.unmarriedAdultMaleList.remove(person)

    def removeFromUnmarriedAdultFemalesList(self, person):
        self.unmarriedAdultFemaleList.remove(person)

    def addToAdultMalesList(self, person):
        self.adultMaleList.append(person)

    def addToAdultFemalesList(self, person):
        self.adultFemaleList.append(person)

    # def removeFromAdultMalesUUIDsList(self, uuid):
    #     self.adultMaleList.remove(uuid)
    #
    # def removeFromAdultFemalesUUIDsList(self, uuid):
    #     self.adultFemaleList.remove(uuid)
    #