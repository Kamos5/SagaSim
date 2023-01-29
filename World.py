import Enums
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

        self.crimeHomicidePerYear = []
        self.crimeAssaultPerYear = []
        self.crimeBurglaryPerYear = []
        self.crimeTheftPerYear = []
        self.crimeFailedPerYear = []


        self.worldHistory = []
        self.peopleNumberHistory = []
        self.alivePeopleNumberHistory = []
        self.birthsPerYearNumberHistory = []
        self.crimesPerYearNumberHistory = []
        self.familiesMembersNumberHistory = []
        self.peopleAliveHistory = []

        self.eyeColorBlackHistory = []
        self.eyeColorBrownHistory = []
        self.eyeColorAmberHistory = []
        self.eyeColorHazelHistory = []
        self.eyeColorGreenHistory = []
        self.eyeColorBlueHistory = []
        self.eyeColorGrayHistory = []

        self.hairColorBlackHistory = []
        self.hairColorBrownHistory = []
        self.hairColorYellowHistory = []
        self.hairColorRedHistory = []
        self.hairColorWhiteHistory = []
        self.hairColorGrayHistory = []


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

    def getCrimesHomicidePerYear(self):
        return self.crimeHomicidePerYear

    def getCrimesAssaultPerYear(self):
        return self.crimeAssaultPerYear

    def getCrimesBurglaryPerYear(self):
        return self.crimeBurglaryPerYear

    def getCrimesTheftPerYear(self):
        return self.crimeTheftPerYear

    def getCrimesFailedPerYear(self):
        return self.crimeFailedPerYear

    def appendCrimesPerYear(self, value, crimes):
        self.crimesPerYear.append(int(value))
        self.crimeHomicidePerYear.append(crimes[0])
        self.crimeAssaultPerYear.append(crimes[1])
        self.crimeBurglaryPerYear.append(crimes[2])
        self.crimeTheftPerYear.append(crimes[3])
        self.crimeFailedPerYear.append(crimes[4])

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
        self.countEyeColor()
        self.countHairColor()


    def countEyeColor(self):

        self.eyeColorHistoryArrayTemp =[]
        for color in Parameters.eyeColorArray:
            self.eyeColorHistoryArrayTemp.append(0)
        for person in self.getAlivePeople():
            if person.getEyeColor() == Enums.EyeColor.BLACK:
                self.eyeColorHistoryArrayTemp[0] += 1
            if person.getEyeColor() == Enums.EyeColor.BROWN:
                self.eyeColorHistoryArrayTemp[1] += 1
            if person.getEyeColor() == Enums.EyeColor.AMBER:
                self.eyeColorHistoryArrayTemp[2] += 1
            if person.getEyeColor() == Enums.EyeColor.HAZEL:
                self.eyeColorHistoryArrayTemp[3] += 1
            if person.getEyeColor() == Enums.EyeColor.GREEN:
                self.eyeColorHistoryArrayTemp[4] += 1
            if person.getEyeColor() == Enums.EyeColor.BLUE:
                self.eyeColorHistoryArrayTemp[5] += 1
            if person.getEyeColor() == Enums.EyeColor.GRAY:
                self.eyeColorHistoryArrayTemp[6] += 1

        self.eyeColorBlackHistory.append(self.eyeColorHistoryArrayTemp[0])
        self.eyeColorBrownHistory.append(self.eyeColorHistoryArrayTemp[1])
        self.eyeColorAmberHistory.append(self.eyeColorHistoryArrayTemp[2])
        self.eyeColorHazelHistory.append(self.eyeColorHistoryArrayTemp[3])
        self.eyeColorGreenHistory.append(self.eyeColorHistoryArrayTemp[4])
        self.eyeColorBlueHistory.append(self.eyeColorHistoryArrayTemp[5])
        self.eyeColorGrayHistory.append(self.eyeColorHistoryArrayTemp[6])

    def countHairColor(self):

        self.hairColorHistoryArrayTemp = []
        for color in Parameters.hairColorArray:
            self.hairColorHistoryArrayTemp.append(0)
        for person in self.getAlivePeople():
            if person.getHairColor() == Enums.HairColor.BLACK:
                self.hairColorHistoryArrayTemp[0] += 1
            if person.getHairColor() == Enums.HairColor.BROWN:
                self.hairColorHistoryArrayTemp[1] += 1
            if person.getHairColor() == Enums.HairColor.YELLOW:
                self.hairColorHistoryArrayTemp[2] += 1
            if person.getHairColor() == Enums.HairColor.RED:
                self.hairColorHistoryArrayTemp[3] += 1
            if person.getHairColor() == Enums.HairColor.WHITE:
                self.hairColorHistoryArrayTemp[4] += 1
            if person.getHairColor() == Enums.HairColor.GRAY:
                self.hairColorHistoryArrayTemp[5] += 1

        self.hairColorBlackHistory.append(self.hairColorHistoryArrayTemp[0])
        self.hairColorBrownHistory.append(self.hairColorHistoryArrayTemp[1])
        self.hairColorYellowHistory.append(self.hairColorHistoryArrayTemp[2])
        self.hairColorRedHistory.append(self.hairColorHistoryArrayTemp[3])
        self.hairColorWhiteHistory.append(self.hairColorHistoryArrayTemp[4])
        self.hairColorGrayHistory.append(self.hairColorHistoryArrayTemp[5])


    def getAlivePeopleNumberHistory(self):
        return [self.alivePeopleNumberHistory]

    def getBirthsPerYearNumberHistory(self):
        return self.birthsPerYearNumberHistory

    def getWorldYearHistory(self):
        return self.worldHistory

    # def getFamiliesMembersNumberHistory(self):
    #     return self.familiesMembersNumberHistory

    def getCrimeHistory(self):
        return [self.getCrimesPerYear(), self.getCrimesHomicidePerYear(), self.getCrimesAssaultPerYear(), self.getCrimesBurglaryPerYear(), self.getCrimesTheftPerYear(), self.getCrimesFailedPerYear()]

    def getPeopleAliveHistory(self):
        return [self.peopleAliveHistory]

    def getPeopleEyeColorsComplexArray(self):
        return [self.eyeColorBlackHistory, self.eyeColorBrownHistory, self.eyeColorAmberHistory, self.eyeColorHazelHistory, self.eyeColorGreenHistory, self.eyeColorBlueHistory, self.eyeColorGrayHistory]

    def getPeopleHairColorsComplexArray(self):
        return [self.hairColorBlackHistory, self.hairColorBrownHistory, self.hairColorYellowHistory, self.hairColorRedHistory, self.hairColorWhiteHistory, self.eyeColorGrayHistory]
