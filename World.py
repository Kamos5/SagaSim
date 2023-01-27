from Enums import Settlements
from Region import Region
import RegionNameGenerator as RNG
import Parameters

class World:

    initYear = Parameters.startingYear
    regions = []
    settlementsInitNumber = Parameters.startingSettlementsPerRegion


    def __init__(self, startYear=initYear):

        self.initYear = startYear
        self.year = self.initYear
        self.regions = []
        self.gameSpeed = 50
        self.divorcesNumber = 0
        self.families = []
        self.people = []
        self.alivePeople = []
        self.birthsPerYear = []
        self.crimesPerYear = []

        self.worldHistory = []
        self.peopleNumberHistory = []
        self.alivePeopleNumberHistory = []
        self.birthsPerYearNumberHistory = []
        self.crimesPerYearNumberHistory = []
        self.familiesMembersNumberHistory = []
        self.peopleAliveHistory = []

    def getPeople(self):
        return self.people

    def setPeople(self, people):
        self.people = people

    def addPerson(self, person):
        self.people.append(person)

    def removePeople(self, person):
        self.people.remove(person)

    def getAlivePeople(self):

        return self.alivePeople

    def getAlivePeopleFunction(self):

        for family in self.getFamilies():
            self.alivePeople += family.getAliveMembersList()

        return self.alivePeople

    def setAlivePeople(self, people):
        self.alivePeople = people

    def addAlivePerson(self, person):
        self.alivePeople.append(person)

    def removeAlivePeople(self, person):
        self.alivePeople.remove(person)

    def getFamilies(self):
        return self.families

    def setFamilies(self, families):
        self.families = families

    def addFamily(self, newFamily):
        self.families.append(newFamily)

    def removeFamily(self, family):
        self.families.remove(family)

    def getGameSpeed(self):
        return self.gameSpeed

    def setGameSpeed(self, newSpeed):
        self.gameSpeed = newSpeed

    def getDivorcesNumber(self):
        return self.divorcesNumber

    def changeDivorcesNumber(self, value):
        self.divorcesNumber += value

    def getYear(self):
        return self.year

    def increaseYear(self):
        self.year += 1

    def getCiTySize(self):
        return Parameters.baseCitySize

    def getVillageSize(self):
        return Parameters.baseVillageSize

    def generateRegions(self, regionsNumber = 5):

        self.regions.append(Region(RNG.randomEnglishRegionName()))
        self.regions.append(Region(RNG.randomNorseRegionName()))

    def generateSettlements(self):

        for region in self.regions:
            for i in range(self.settlementsInitNumber):
                newSettlement = region.addSettlement(self)
                newSettlement.setRegion(region)
                # First settlement is always TOWN
                if i == 0:
                    newSettlement.changeSettlementType(Settlements.TOWN)
                else:
                    newSettlement.changeSettlementType(Settlements.VILLAGE)

    def getRegionFromIndex(self, index):
        return self.regions[index]

    def getRegions(self):
        return self.regions

    def getBirthsPerYear(self):
        return self.birthsPerYear

    def appendBirthsPerYear(self, value):
        self.birthsPerYear.append(int(value))

    def getCrimesPerYear(self):
        return self.crimesPerYear

    def appendCrimesPerYear(self, value):
        self.crimesPerYear.append(int(value))

    def updateAlive(self):
        self.alivePeople = []
        self.alivePeople = self.getAlivePeopleFunction()

    def makeHistory(self):
        self.worldHistory.append(self.year)
        self.peopleNumberHistory.append(len(self.getPeople()))
        self.alivePeopleNumberHistory.append(len(self.getAlivePeople()))
        self.birthsPerYearNumberHistory = self.getBirthsPerYear()
        self.crimesPerYearNumberHistory = self.getCrimesPerYear()
        self.peopleAliveHistory.append(self.getAlivePeople())


    def getAlivePeopleNumberHistory(self):
        return self.alivePeopleNumberHistory

    def getBirthsPerYearNumberHistory(self):
        return self.birthsPerYearNumberHistory

    def getWorldYearHistory(self):
        return self.worldHistory

    # def getFamiliesMembersNumberHistory(self):
    #     return self.familiesMembersNumberHistory

    def getPeopleAliveHistory(self):
        return self.peopleAliveHistory
