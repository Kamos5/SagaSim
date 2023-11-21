import math

import numpy

import Enums
import SettlementNameGenerator
import Utils
from Culture import Culture
from Enums import Settlements
from PersonLifeEventsHistory import adulthoodReached
from Region import Region
import RegionNameGenerator as RNG
import Parameters
from RegionLifeEventsHistory import weatherEvent
from WorldMap import WorldMap
from WorldMapObjClass import WorldMapObjClass


class World:

    initYear = Parameters.startingYear
    regions = []
    settlementsInitNumber = Parameters.startingSettlementsPerProvince

    def __init__(self, startYear=initYear):

        self.initYear = startYear
        self.day = 31
        self.dayOfWeekFlag = Utils.randomRange(1, 7)
        self.dayOfTheYear = 0
        self.month = Enums.Months.DECEMBER
        self.year = self.initYear
        self.regions = []
        self.gameSpeed = 3000    #50
        self.gameSpeedCounter = 8  #5
        self.divorcesNumber = 0
        self.families = []
        self.people = []
        self.alivePeople = []
        self.birthsPerYear = []
        self.birthsPerYearTemp = 0
        self.crimesPerYear = []
        self.crimesPerYearReduced = []
        self.avarageLifeSpamHistory = []
        self.averageHeightHistory = []
        self.averageHeightMHistory = []
        self.averageHeightFHistory = []

        self.crimeHomicidePerYear = []
        self.crimeAssaultPerYear = []
        self.crimeBurglaryPerYear = []
        self.crimeTheftPerYear = []
        self.crimeFailedPerYear = []

        self.crimeHomicidePerYearReduced = []
        self.crimeAssaultPerYearReduced = []
        self.crimeBurglaryPerYearReduced = []
        self.crimeTheftPerYearReduced = []
        self.crimeFailedPerYearReduced = []

        self.sexualityHomoHistory = []
        self.sexualityHeteroHistory = []

        self.sexualityHomoPctHistory = []
        self.sexualityHeteroPctHistory = []

        self.worldHistory = []
        self.worldHistoryReduced = []
        self.peopleNumberHistory = []
        self.alivePeopleNumberHistory = []
        self.alivePeopleNumberHistoryReduced = []
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

        self.worldMap = WorldMap()

        self.allNames = None
        self.cultures = []

        self.gameState = 0

        self.diseases = []
        self.injures = []
        self.fleshWounds = 0
        self.deepWounds = 0
        self.brokenBones = 0
        self.concussion = 0
        self.organFailure = 0

    def loadWorld(self, world):

        self.setInitYear(world.getInitYear())
        self.setDay(world.getDay())
        self.setDayOfTheYear(world.getDayOfTheYear())
        self.setDayOfWeekFlag(world.getDayOfWeekFlag())
        self.setMonth(world.getMonth())
        self.setYear(world.getYear())
        self.setRegions(world.getRegions())
        self.setGameSpeed(world.getGameSpeed())
        self.setGameSpeedCounter(world.getGameSpeedCounter())
        self.setDivorcesNumber(world.getDivorcesNumber())
        self.setFamilies(world.getFamilies())
        self.setPeople(world.getPeople())
        self.setAlivePeople(world.getAlivePeople())
        self.setBirthsPerYear(world.getBirthsPerYear())
        self.setBirthsPerYearTemp(world.getBirthsPerYearTemp())
        self.setCrimesPerYear(world.getCrimesPerYear())
        self.setCrimesPerYearReduced(world.getCrimesPerYearReduced())
        self.setAvarageLifeSpamHistory(world.getAvarageLifeSpam())
        self.setAverageHeightHistory(world.getAverageHeightHistory()[0])
        self.setAverageHeightMHistory(world.getAverageHeightHistory()[1])
        self.setAverageHeightFHistory(world.getAverageHeightHistory()[2])
        self.setCrimesHomicidePerYear(world.getCrimesHomicidePerYear())
        self.setCrimesAssaultPerYear(world.getCrimesAssaultPerYear())
        self.setCrimesBurglaryPerYear(world.getCrimesBurglaryPerYear())
        self.setCrimesTheftPerYear(world.getCrimesTheftPerYear())
        self.setCrimesFailedPerYear(world.getCrimesFailedPerYear())
        self.setCrimesHomicidePerYearReduced(world.getCrimesHomicidePerYearReduced())
        self.setCrimesAssaultPerYearReduced(world.getCrimesAssaultPerYearReduced())
        self.setCrimesBurglaryPerYearReduced(world.getCrimesBurglaryPerYearReduced())
        self.setCrimesTheftPerYearReduced(world.getCrimesTheftPerYearReduced())
        self.setCrimesFailedPerYearReduced(world.getCrimesFailedPerYearReduced())
        self.setSexualityHomoHistory(world.getSexualityHistory()[1])
        self.setSexualityHeteroHistory(world.getSexualityHistory()[0])
        self.setSexualityHomoPctHistory(world.getSexualityPctHistory()[1])
        self.setSexualityHeteroPctHistory(world.getSexualityPctHistory()[0])
        self.setWorldYearHistory(world.getWorldYearHistory())
        self.setWorldYearHistoryReduced(world.getWorldYearHistoryReduced())
        # self.setPeopleNumberHistory(world.getPeopleNumberHistory())
        # self.setAlivePeopleNumberHistory(world.getAlivePeopleNumberHistory())
        # self.setAlivePeopleNumberHistoryReduced(world.getAlivePeopleNumberHistoryReduced())
        # self.setBirthsPerYearNumberHistory(world.getBirthsPerYearNumberHistory())
        # self.setCrimesPerYearNumberHistory(world.getCrimesPerYearNumberHistory())
        # self.setFamiliesMembersNumberHistory(world.getFamiliesMembersNumberHistory())
        # self.setPeopleAliveHistory(world.getPeopleAliveHistory())
        self.updateAlive()
        self.countEyeColor()
        self.countHairColor()
        self.makeHistory()
        self.setWorldMap(world.getWorldMap())
        self.setAllNames(world.getAllNames())
        self.setCultures(world.getCultures())
        self.setGameState(world.getGameState())


    def reset(self, startYear=initYear):

        self.initYear = startYear
        self.day = 31
        self.dayOfTheYear = 0
        self.dayOfWeekFlag = Utils.randomRange(1, 7)
        self.month = Enums.Months.DECEMBER
        self.year = self.initYear
        self.regions = []
        self.gameSpeed = 3000    #50
        self.gameSpeedCounter = 8  #5
        self.divorcesNumber = 0
        self.families = []
        self.people = []
        self.alivePeople = []
        self.birthsPerYear = []
        self.birthsPerYearTemp = 0
        self.crimesPerYear = []
        self.crimesPerYearReduced = []
        self.avarageLifeSpamHistory = []
        self.averageHeightHistory = []
        self.averageHeightMHistory = []
        self.averageHeightFHistory = []

        self.crimeHomicidePerYear = []
        self.crimeAssaultPerYear = []
        self.crimeBurglaryPerYear = []
        self.crimeTheftPerYear = []
        self.crimeFailedPerYear = []

        self.crimeHomicidePerYearReduced = []
        self.crimeAssaultPerYearReduced = []
        self.crimeBurglaryPerYearReduced = []
        self.crimeTheftPerYearReduced = []
        self.crimeFailedPerYearReduced = []

        self.sexualityHomoHistory = []
        self.sexualityHeteroHistory = []

        self.sexualityHomoPctHistory = []
        self.sexualityHeteroPctHistory = []

        self.worldHistory = []
        self.worldHistoryReduced = []
        self.peopleNumberHistory = []
        self.alivePeopleNumberHistory = []
        self.alivePeopleNumberHistoryReduced = []
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

        self.worldMap = WorldMap()
        self.worldMap.reset()

        self.allNames = None
        self.cultures = []

        self.gameState = 0

        self.deathAgeAdults = []

        self.season = Enums.Seasons.WINTER

    def getInitYear(self):
        return self.initYear

    def setInitYear(self, newYear):
        self.initYear = newYear

    def getAverageDeathAge(self):
        if len(self.deathAgeAdults) > 0:
            return numpy.average(self.deathAgeAdults)
        else:
            return 0

    def getWorldMap(self):
        return self.worldMap

    def setWorldMap(self, newWorldMap):
        self.worldMap = newWorldMap

    def setAllNames(self, names):
        self.allNames = names

    def getAllNames(self):
        return self.allNames

    def setCultures(self, cultures):
        for culture in cultures:
            self.cultures.append(Culture(culture))

    def getCultures(self):
        return self.cultures

    def getPeople(self):
        return self.people

    def setPeople(self, people):
        self.people = people

    def addPerson(self, person):
        self.people.append(person)

    def removePeople(self, person):
        self.people.remove(person)

    def getInjuries(self):
        return self.injures

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

    def getBirthsPerYearTemp(self):
        return self.birthsPerYearTemp

    def setBirthsPerYearTemp(self, newBirths):
        self.birthsPerYearTemp = newBirths

    def increaseBirthsPerYearTemp(self):
        self.birthsPerYearTemp += 1

    def resetBirthsPerYearTemp(self):
        self.birthsPerYearTemp = 0

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

    def getGameSpeedCounter(self):
        return self.gameSpeedCounter

    def setGameSpeedCounter(self, newCounter):
        self.gameSpeedCounter = newCounter

    def getDivorcesNumber(self):
        return self.divorcesNumber

    def setDivorcesNumber(self, newNumber):
        self.divorcesNumber = newNumber

    def changeDivorcesNumber(self, value):
        self.divorcesNumber += value

    def getYear(self):
        return self.year

    def setYear(self, newYear):
        self.year = newYear

    def increaseYear(self):
        self.year += 1

    def getDayOfTheYear(self):
        return self.dayOfTheYear

    def setDayOfTheYear(self, newDayOfTheYear):
        self.dayOfTheYear = newDayOfTheYear

    def resetDayOfTheYear(self):
        self.dayOfTheYear = 0

    def increaseDayOfTheYear(self):
        self.dayOfTheYear += 1

    def getDay(self):
        return self.day

    def setDay(self, newDay):
        self.day = newDay

    def setNextDay(self):
        self.day += 1

    def resetDay(self):
        self.day = 1

    def getDayOfWeekFlag(self):
        return self.dayOfWeekFlag

    def setDayOfWeekFlag(self, newDayOfWeekFlag):
        self.dayOfWeekFlag = newDayOfWeekFlag

    def increaseDayOfWeekFlag(self):
        if self.dayOfWeekFlag < 7:
            self.dayOfWeekFlag += 1
        else:
            self.dayOfWeekFlag = 1

    def getMonth(self):
        return self.month

    def setMonth(self, newMonth):
        self.month = newMonth

    def setSeason(self, newSeason):
        self.season = newSeason

    def getSeason(self):
        return self.season

    def increaseDay(self):

        if self.getDay() == self.getMonth().value[2]:
            if self.getMonth().value[0] == 1:
                self.month = Enums.Months.FEBRUARY
            elif self.getMonth().value[0] == 2:
                self.month = Enums.Months.MARCH
                self.setSeason(Enums.Seasons.SPRING)
            elif self.getMonth().value[0] == 3:
                self.month = Enums.Months.APRIL
            elif self.getMonth().value[0] == 4:
                self.month = Enums.Months.MAY
            elif self.getMonth().value[0] == 5:
                self.month = Enums.Months.JUNE
                self.setSeason(Enums.Seasons.SUMMER)
            elif self.getMonth().value[0] == 6:
                self.month = Enums.Months.JULY
            elif self.getMonth().value[0] == 7:
                self.month = Enums.Months.AUGUST
            elif self.getMonth().value[0] == 8:
                self.month = Enums.Months.SEPTEMBER
                self.setSeason(Enums.Seasons.FALL)
            elif self.getMonth().value[0] == 9:
                self.month = Enums.Months.OCTOBER
            elif self.getMonth().value[0] == 10:
                self.month = Enums.Months.NOVEMBER
            elif self.getMonth().value[0] == 11:
                self.month = Enums.Months.DECEMBER
                self.setSeason(Enums.Seasons.WINTER)
            else:
                self.month = Enums.Months.JANUARY
                self.increaseYear()
                self.appendBirthsPerYear(self.birthsPerYearTemp)
                self.birthsPerYearTemp = 0
                self.resetDayOfTheYear()

            self.resetDay()
        else:
            self.setNextDay()
        self.increaseDayOfTheYear()

        self.increaseDayOfWeekFlag()

    def getCiTySize(self):
        return Parameters.baseCitySize

    def getVillageSize(self):
        return Parameters.baseVillageSize

    def getGameState(self):
        return self.gameState

    def setGameState(self, newGameState):
        self.gameState = newGameState

    def generateRegionsNames(self, regionsNumber = 5):

        startingSet = 0

        if startingSet == 0:
            startingSet1For4 = [[], [], [], []]
        elif startingSet == 1:
            startingSet1For4 = [(0, 0), (self.getWorldMap().getWidth()-1, 0), (0, self.getWorldMap().getHeight()-1), (self.getWorldMap().getWidth()-1, self.getWorldMap().getHeight()-1)]
        else:
            startingSet1For4 = [(50, 50), (50, 51), (51, 50), (51, 51)]

        regionNamesStr = 'RegionNames'
        regionNamesStrLowerFirst = regionNamesStr[0].lower() + regionNamesStr[1:]
        colorsStr = 'Colors'

        for number in range(regionsNumber):
            cultureName = self.cultures[number].getCultureName()
            cultureRegionNames = f'{cultureName}{regionNamesStr}'
            regionNames = f'{regionNamesStrLowerFirst}'
            cultureColors = f'{cultureName}{colorsStr}'
            region = Region(RNG.randomRegionName(self.allNames[cultureName][cultureRegionNames][regionNames], regionsNumber))
            region.setRegionNumber(number)
            region.setRegionCulture(cultureName)
            region.setRegionColor(eval(self.allNames[cultureName][cultureColors]))
            self.regions.append(region)

    def generateProvinceNames(self, region):

        provinceNamesStr = 'ProvinceNames'
        provinceNamesStrLowerFirst = provinceNamesStr[0].lower() + provinceNamesStr[1:]
        provinceCultureStr = region.getRegionCulture()

        for province in region.getProvinces():
            print()


    def generateSettlements(self):
        SettlementNameGenerator.makeListsForSettlementsNames(self)
        for region in self.regions:
            townInitList = []
            cordsUsed = []
            for i in range(self.settlementsInitNumber):
                newSettlement = region.getProvinces()[0].addInitSettlement(self, region)
                newSettlement.setRegion(region)
                newSettlement.setProvince(region.getProvinces()[0])
                notClear = True
                settlementCord = (0, 0, 0)
                while notClear:
                    settlementCord = Utils.randomFromCollection(list(newSettlement.getProvince().getInnerCords()))
                    if settlementCord not in newSettlement.getProvince().getCordsUsed():
                        notClear = False
                newSettlement.getProvince().addCordsUsed(settlementCord)
                newSettlement.getProvince().addCordsUsed((settlementCord[0]-1, settlementCord[1], settlementCord[2]))
                newSettlement.getProvince().addCordsUsed((settlementCord[0]+1, settlementCord[1], settlementCord[2]))
                newSettlement.getProvince().addCordsUsed((settlementCord[0], settlementCord[1]-1, settlementCord[2]))
                newSettlement.getProvince().addCordsUsed((settlementCord[0], settlementCord[1]+1, settlementCord[2]))
                newSettlement.setProvinceCords(settlementCord)
                worldMapObjClass = WorldMapObjClass(colors=(newSettlement.getRegion().getRegionColor(), newSettlement.getProvince().getColor()), cords=(settlementCord[0],settlementCord[1]), objectVar=newSettlement, isInner=False)
                self.getWorldMap().addField(worldMapObjClass, weight=2)
                # First settlement is always TOWN
                if i == 0:
                    newSettlement.changeSettlementType(Settlements.TOWN)
                    townInitList.append(newSettlement)
                else:
                    newSettlement.changeSettlementType(Settlements.VILLAGE)
                    newSettlement.setProvision(Utils.randomFromCollection(townInitList))


    def getRegionFromIndex(self, index):
        return self.regions[index]

    def getRegions(self):
        return self.regions

    def setRegions(self, newRegions):
        self.regions = newRegions

    def getBirthsPerYear(self):
        return self.birthsPerYear

    def setBirthsPerYear(self, newBirths):
        self.birthsPerYear = newBirths

    def appendBirthsPerYear(self, value):
        self.birthsPerYear.append(int(value))

    def getSexualityHetero(self):
        return self.sexualityHeteroHistory

    def getSexualityHomo(self):
        return self.sexualityHomoHistory

    def getSexualityHeteroPct(self):
        return self.sexualityHeteroPctHistory

    def getSexualityHomoPct(self):
        return self.sexualityHomoPctHistory

    def getCrimesPerYear(self):
        return self.crimesPerYear

    def setCrimesPerYear(self, newCrimePerYear):
        self.crimesPerYear = newCrimePerYear

    def getCrimesHomicidePerYear(self):
        return self.crimeHomicidePerYear

    def setCrimesHomicidePerYear(self, newCrimeHomicidePerYear):
        self.crimeHomicidePerYear = newCrimeHomicidePerYear

    def getCrimesAssaultPerYear(self):
        return self.crimeAssaultPerYear

    def setCrimesAssaultPerYear(self, newCrimesAssaultPerYear):
        self.crimeAssaultPerYear = newCrimesAssaultPerYear

    def getCrimesBurglaryPerYear(self):
        return self.crimeBurglaryPerYear

    def setCrimesBurglaryPerYear(self, newCrimeBurglaryPerYear):
        self.crimeBurglaryPerYear = newCrimeBurglaryPerYear

    def getCrimesTheftPerYear(self):
        return self.crimeTheftPerYear

    def setCrimesTheftPerYear(self, newCrimeTheftPerYear):
        self.crimeTheftPerYear = newCrimeTheftPerYear

    def getCrimesFailedPerYear(self):
        return self.crimeFailedPerYear

    def setCrimesFailedPerYear(self, newCrimeFailedPerYear):
        self.crimeFailedPerYear = newCrimeFailedPerYear

    def getCrimesPerYearReduced(self):
        return self.crimesPerYearReduced

    def setCrimesPerYearReduced(self, newCrimesPerYearReduced):
        self.crimesPerYearReduced = newCrimesPerYearReduced

    def getCrimesHomicidePerYearReduced(self):
        return self.crimeHomicidePerYearReduced

    def setCrimesHomicidePerYearReduced(self, newCrimeHomicidePerYearReduced):
        self.crimeHomicidePerYearReduced = newCrimeHomicidePerYearReduced

    def getCrimesAssaultPerYearReduced(self):
        return self.crimeAssaultPerYearReduced

    def setCrimesAssaultPerYearReduced(self, newCrimeAssaultPerYearReduced):
        self.crimeAssaultPerYearReduced = newCrimeAssaultPerYearReduced

    def getCrimesBurglaryPerYearReduced(self):
        return self.crimeBurglaryPerYearReduced

    def setCrimesBurglaryPerYearReduced(self, newCrimeBurglaryPerYearReduced):
        self.crimeBurglaryPerYearReduced = newCrimeBurglaryPerYearReduced

    def getCrimesTheftPerYearReduced(self):
        return self.crimeTheftPerYearReduced

    def setCrimesTheftPerYearReduced(self, newCrimeTheftPerYearReduced):
        self.crimeTheftPerYearReduced = newCrimeTheftPerYearReduced

    def getCrimesFailedPerYearReduced(self):
        return self.crimeFailedPerYearReduced

    def setCrimesFailedPerYearReduced(self, newCrimeFailedPerYearReduced):
        self.crimeFailedPerYearReduced = newCrimeFailedPerYearReduced

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

    def weatherChange(self):

        seasonWeathers = Enums.weatherStatus.NORMAL
        for region in self.getRegions():

            region.increaseDaysSinceWeatherChangeCounter()

            if (self.getMonth() == Enums.Months.DECEMBER) | (self.getMonth() == Enums.Months.JANUARY) | (self.getMonth() == Enums.Months.FEBRUARY):
                seasonWeathers = Enums.weatherBlizzard
            if (self.getMonth() == Enums.Months.MARCH) | (self.getMonth() == Enums.Months.APRIL) | (self.getMonth() == Enums.Months.MAY):
                seasonWeathers = Enums.weatherFloods
            if (self.getMonth() == Enums.Months.JUNE) | (self.getMonth() == Enums.Months.JULY) | (self.getMonth() == Enums.Months.AUGUST):
                seasonWeathers = Enums.weatherDroughts
            if (self.getMonth() == Enums.Months.SEPTEMBER) | (self.getMonth() == Enums.Months.OCTOBER) | (self.getMonth() == Enums.Months.NOVEMBER):
                seasonWeathers = Enums.weatherWildFire

            if region.getDaysSinceWeatherChange() >= region.getWeather().value[3]:
                weatherPattern = Utils.randomRange(0, 10000)
                if weatherPattern <= 9950:
                    region.setWeather(Enums.weatherStatus.NORMAL)
                elif 9980 >= weatherPattern > 9950:
                    region.setWeather(seasonWeathers.MILD)
                    region.resetDaysSinceWeatherChange()
                    weatherEvent(region, self)
                elif 9995 >= weatherPattern > 9980:
                    region.setWeather(seasonWeathers.MEDIUM)
                    region.resetDaysSinceWeatherChange()
                    weatherEvent(region, self)
                elif 9998 >= weatherPattern > 9995:
                    region.setWeather(seasonWeathers.STRONG)
                    region.resetDaysSinceWeatherChange()
                    weatherEvent(region, self)
                else:
                    region.setWeather(seasonWeathers.EXTREME)
                    region.resetDaysSinceWeatherChange()
                    weatherEvent(region, self)

            region.setCurrentTemperature(Utils.getTemperatureBasedOnDay(self.getDayOfTheYear()) + region.getWeather().value[4])

    def makeHistory(self):


        self.worldHistory.append(str(self.day) + '/' + str(self.getMonth().value[0]) + '/' + str(self.year))
        # self.peopleNumberHistory.append(len(self.getPeople())) TODO NOT USED?
        #self.birthsPerYearNumberHistory = self.getBirthsPerYear() TODO NOT USED?
        #self.crimesPerYearNumberHistory = self.getCrimesPerYear() TODO NOT USED?
        self.peopleAliveHistory.append(self.getAlivePeople())

        self.countPersonStatistics()



    def countPersonStatistics(self):

        heteroCountTemp = 0
        homoCountTemp = 0
        heightTemp = 0
        heightMTemp = 0
        heightFTemp = 0
        liveAdultsTemp = 0
        liveAdultsMTemp = 0
        liveAdultsFTemp = 0
        SICKTEMP = 0
        SICKTEMP2 = 0

        for person in self.getAlivePeople():

            if person.getSexGen1()[1] == 1:
                SICKTEMP += 1
            if person.getSexGen2()[1] == 1:
                SICKTEMP2 += 1
            if person.getSexuality() == 'hetero':
                heteroCountTemp += 1
            else:
                homoCountTemp += 1
            if person.getAge() >= 15:
                heightTemp += person.getHeight()
                liveAdultsTemp += 1
                if person.getSex() == Enums.Sexes.MALE:
                    heightMTemp += person.getHeight()
                    liveAdultsMTemp += 1
                else:
                    heightFTemp += person.getHeight()
                    liveAdultsFTemp += 1

            if person.eyeColorGen1[1] == 1 and person.eyeColorGen2[1] == 1:
                print("Ślepy")
            if person.hairColorGen1[1] == 1 and person.hairColorGen2[1] == 1:
                print("Łysy")

        if liveAdultsTemp > 0:
            self.averageHeightHistory.append((heightTemp / liveAdultsTemp))
        else:
            self.averageHeightHistory.append(len(self.averageHeightHistory)-1)
        if liveAdultsMTemp > 0:
            self.averageHeightMHistory.append((heightMTemp / liveAdultsMTemp))
        else:
            self.averageHeightMHistory.append(len(self.averageHeightMHistory)-1)
        if liveAdultsFTemp > 0:
            self.averageHeightFHistory.append((heightFTemp / liveAdultsFTemp))
        else:
            self.averageHeightFHistory.append(len(self.averageHeightFHistory)-1)

        self.sexualityHeteroHistory.append(heteroCountTemp)
        self.sexualityHeteroPctHistory.append(heteroCountTemp/len(self.getAlivePeople())*100)
        self.sexualityHomoHistory.append(homoCountTemp)
        self.sexualityHomoPctHistory.append(homoCountTemp / len(self.getAlivePeople())*100)
        # print('Sick')
        # print(SICKTEMP)
        # print(SICKTEMP2)


    def getAlivePeopleNumberHistoryReduced(self):

        self.alivePeopleNumberHistory = []

        modVariable = self.getModVariableForReducesHistory()

        yearIndex = 1

        for AlivePeopleInYear in self.getPeopleAliveHistory():
            for year in AlivePeopleInYear:
                if modVariable < 2 or yearIndex % modVariable == 0:
                    self.alivePeopleNumberHistory.append(len(year))
                    yearIndex += 1
                else:
                    yearIndex += 1
                    continue

        return

    def countEyeColor(self):

        self.eyeColorHistoryArrayTemp = []
        self.eyeColorBlackHistory = []
        self.eyeColorBrownHistory = []
        self.eyeColorAmberHistory = []
        self.eyeColorHazelHistory = []
        self.eyeColorGreenHistory = []
        self.eyeColorBlueHistory = []
        self.eyeColorGrayHistory = []

        modVariable = self.getModVariableForReducesHistory()

        yearIndex = 1


        for AlivePeopleInYear in self.getPeopleAliveHistory():
            for year in AlivePeopleInYear:

                if modVariable < 2 or yearIndex % modVariable == 0:
                    self.eyeColorHistoryArrayTemp = []
                    for color in Parameters.eyeColorArray:
                        self.eyeColorHistoryArrayTemp.append(0)
                    for person in year:
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

                    yearIndex += 1
                else:
                    yearIndex += 1
                    continue
        return

    def countHairColor(self):

        self.hairColorHistoryArrayTemp = []
        self.hairColorBlackHistory = []
        self.hairColorBrownHistory = []
        self.hairColorYellowHistory = []
        self.hairColorRedHistory = []
        self.hairColorWhiteHistory = []
        self.hairColorGrayHistory = []

        modVariable = self.getModVariableForReducesHistory()

        yearIndex = 1

        for AlivePeopleInYear in self.getPeopleAliveHistory():
            for year in AlivePeopleInYear:

                if modVariable < 2 or yearIndex % modVariable == 0:
                    self.hairColorHistoryArrayTemp = []
                    for color in Parameters.hairColorArray:
                        self.hairColorHistoryArrayTemp.append(0)
                    for person in year:
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

                    yearIndex += 1
                else:
                    yearIndex += 1
                    continue
        return

    def countCrime(self):

        self.crimeHistoryReduced = []
        self.crimesPerYearReduced = []
        self.crimeHomicidePerYearReduced = []
        self.crimeAssaultPerYearReduced = []
        self.crimeBurglaryPerYearReduced = []
        self.crimeTheftPerYearReduced = []
        self.crimeFailedPerYearReduced = []

        modVariable = self.getModVariableForReducesHistory()

        yearIndex = 1


        for i in range(len(self.crimeHomicidePerYear)):

            if modVariable < 2 or yearIndex % modVariable == 0:

                self.crimesPerYearReduced.append(self.crimesPerYear[i])
                self.crimeHomicidePerYearReduced.append(self.crimeHomicidePerYear[i])
                self.crimeAssaultPerYearReduced.append(self.crimeAssaultPerYear[i])
                self.crimeBurglaryPerYearReduced.append(self.crimeBurglaryPerYear[i])
                self.crimeTheftPerYearReduced.append(self.crimeTheftPerYear[i])
                self.crimeFailedPerYearReduced.append(self.crimeFailedPerYear[i])

                self.crimeHistoryReduced.append([self.crimesPerYearReduced, self.crimeHomicidePerYearReduced, self.crimeAssaultPerYearReduced, self.crimeBurglaryPerYearReduced, self.crimeTheftPerYearReduced, self.crimeFailedPerYearReduced])
                yearIndex += 1

            else:
                yearIndex += 1
                continue

        return

    def getAlivePeopleNumberHistory(self):
        return [self.alivePeopleNumberHistory]

    def setAlivePeopleNumberHistory(self, newAlivePeopleNumberHistory):
        self.alivePeopleNumberHistory = newAlivePeopleNumberHistory

    def getBirthsPerYearNumberHistory(self):
        return self.birthsPerYearNumberHistory

    def getAvarageLifeSpam(self):
        return self.avarageLifeSpamHistory

    def setAvarageLifeSpamHistory(self, newAvarageLifeSpamHistory):
        self.avarageLifeSpamHistory = newAvarageLifeSpamHistory

    def getAverageHeightHistory(self):
        return [self.averageHeightHistory, self.averageHeightMHistory, self.averageHeightFHistory]

    def setAverageHeightHistory(self, newAverageHeightHistory):
        self.averageHeightHistory = newAverageHeightHistory

    def setAverageHeightMHistory(self, newAverageHeightMHistory):
        self.averageHeightMHistory = newAverageHeightMHistory

    def setAverageHeightFHistory(self, newAverageHeightFHistory):
        self.averageHeightFHistory = newAverageHeightFHistory

    def getWorldYearHistory(self):
        return self.worldHistory

    def setWorldYearHistory(self, newWorldHistory):
        self.worldHistory = newWorldHistory

    def getWorldYearHistoryReduced(self):

        modVariable = self.getModVariableForReducesHistory()

        yearIndex = 1
        self.worldHistoryReduced = []
        for year in self.worldHistory:
            if modVariable < 2 or yearIndex % modVariable == 0:
                self.worldHistoryReduced.append(year)
                yearIndex +=1
            else:
                yearIndex += 1
                continue
        return self.worldHistoryReduced

    def setWorldYearHistoryReduced(self, newWorldHistoryReduced):
        self.worldHistoryReduced = newWorldHistoryReduced

    def getWeatherHistoryForAllRegions(self):

        weatherHistoryForAllRegions = []
        for region in self.getRegions():
            weatherHistoryForAllRegions.append(region.weatherHistory)

        return weatherHistoryForAllRegions

    # def getFamiliesMembersNumberHistory(self):
    #     return self.familiesMembersNumberHistory

    def getCrimeHistory(self):
        return [self.getCrimesPerYear(), self.getCrimesHomicidePerYear(), self.getCrimesAssaultPerYear(), self.getCrimesBurglaryPerYear(), self.getCrimesTheftPerYear(), self.getCrimesFailedPerYear()]

    def getCrimeHistoryReduced(self):
        return [self.getCrimesPerYearReduced(), self.getCrimesHomicidePerYearReduced(), self.getCrimesAssaultPerYearReduced(), self.getCrimesBurglaryPerYearReduced(), self.getCrimesTheftPerYearReduced(), self.getCrimesFailedPerYearReduced()]

    def getSexualityHistory(self):
        return [self.getSexualityHetero(), self.getSexualityHomo()]

    def setSexualityHeteroHistory(self, newSexualityHeteroHistory):
        self.sexualityHeteroHistory = newSexualityHeteroHistory

    def setSexualityHomoHistory(self, newSexualityHomoHistory):
        self.sexualityHomoHistory = newSexualityHomoHistory

    def getSexualityPctHistory(self):
        return [self.getSexualityHeteroPct(), self.getSexualityHomoPct()]

    def setSexualityHeteroPctHistory(self, newSexualityHeteroPctHistory):
        self.sexualityHeteroPctHistory = newSexualityHeteroPctHistory

    def setSexualityHomoPctHistory(self, newSexualityHomoPctHistory):
        self.sexualityHomoPctHistory = newSexualityHomoPctHistory

    def getPeopleAliveHistory(self):
        return [self.peopleAliveHistory]

    def setPeopleAliveHistory(self, newPeopleAliveHistory):
        self.peopleAliveHistory = newPeopleAliveHistory

    def getPeopleEyeColorsComplexArray(self):
        return [self.eyeColorBlackHistory, self.eyeColorBrownHistory, self.eyeColorAmberHistory, self.eyeColorHazelHistory, self.eyeColorGreenHistory, self.eyeColorBlueHistory, self.eyeColorGrayHistory]

    def getPeopleHairColorsComplexArray(self):
        return [self.hairColorBlackHistory, self.hairColorBrownHistory, self.hairColorYellowHistory, self.hairColorRedHistory, self.hairColorWhiteHistory, self.hairColorGrayHistory]


    def getModVariableForReducesHistory(self):

        getPeopleAliveHistoryLen = len(self.worldHistory)
        maxDataToDisplay = 150
        modVariable = 0

        if getPeopleAliveHistoryLen > maxDataToDisplay:
            modVariable = getPeopleAliveHistoryLen // maxDataToDisplay


        return modVariable

    def pickRandomProvincesForRegions(self):

        provincesUsed = set()
        provincesNotUsed = set()

        for i in range(5):
            for region in self.regions:
                findFirst = True
                provincesNotFound = True
                secBreak = 0
                while provincesNotFound:
                    provinceToAdd = None
                    if len(region.getProvinces()) == 0:
                        while findFirst:
                            secVariable = 0
                            provinceToAdd = Utils.randomFromCollection(list(self.getWorldMap().getProvinces()))
                            if provinceToAdd.getType() == 'SEA' or provinceToAdd.getRegion() is not None:
                                continue
                            else:
                                isNeighbourTaken = False
                                for neighbour in provinceToAdd.getNeighbours():
                                    if neighbour in provincesUsed:
                                        isNeighbourTaken = True
                                if isNeighbourTaken:
                                    continue
                                else:
                                    findFirst = False
                                    provincesUsed.add(provinceToAdd)

                            secVariable += 1
                            if secVariable > 100:
                                break
                    else:
                        possibleExpansions = set()
                        for province in region.getProvinces():
                            for neighbour in province.getNeighbours():
                                if (not neighbour.getType() == 'SEA' or neighbour.getRegion() is not None) and neighbour not in region.getProvinces() and neighbour not in provincesUsed:
                                    possibleExpansions.add(neighbour)

                        if len(possibleExpansions) > 0:
                            provinceToAdd = Utils.randomFromCollection(list(possibleExpansions))

                    if provinceToAdd is not None:
                        region.addProvince(provinceToAdd)
                        provincesUsed.add(provinceToAdd)
                        provinceToAdd.setRegion(region)
                        provincesNotFound = False

                    secBreak += 1
                    if secBreak == 1000:
                        break

        for region in self.regions:
            centerCords = []
            for province in region.getProvinces():
                centerCords.append(list(province.getMiddleCords()))
            region.caltulateMiddleCords(centerCords)

        for province in self.getWorldMap().getProvinces():
            if province.getRegion() is None and not province.getType() == 'SEA':
                provincesNotUsed.add(province)

        if len(provincesNotUsed) > 0:
            self.reshuffleProvincesInRegions(self.getRegions(), provincesUsed, provincesNotUsed)

        for region in self.regions:
            region.generateNamesForProvinces()

        for region in self.regions:
            region.generateRegionalProvincesMap(self)


    def reshuffleProvincesInRegions(self, regions, provincesUsed, provincesNotUsed):

        print("NOT USED")
        print(len(provincesNotUsed))
        for provinceNotUsed in provincesNotUsed:
            closestRegion = None
            closestRegionDistance = 0
            provinceNotUsedX, provinceNotUsedY = provinceNotUsed.getMiddleCords()
            for region in regions:
                if closestRegion == None:
                    closestRegion = region
                    regionX, regionY = region.getMiddleCords()
                    closestRegionDistance = math.sqrt((regionX-provinceNotUsedX)**2+(regionY-provinceNotUsedY)**2)

                else:
                    regionX, regionY = region.getMiddleCords()
                    regionDistanceToProvince = math.sqrt((regionX - provinceNotUsedX) ** 2 + (regionY - provinceNotUsedY) ** 2)
                    if regionDistanceToProvince < closestRegionDistance:
                        closestRegionDistance = regionDistanceToProvince
                        closestRegion = region

            closestRegion.addProvince(provinceNotUsed)
            provincesUsed.add(provinceNotUsed)
            provinceNotUsed.setRegion(closestRegion)

        for province in provincesUsed:
            closestRegion = None
            provinceNotUsedX, provinceNotUsedY = province.getMiddleCords()
            region0X, region0Y = province.getRegion().getMiddleCords()
            closestRegionDistance = math.sqrt((region0X - provinceNotUsedX) ** 2 + (region0Y - provinceNotUsedY) ** 2)
            for region in regions:
                    regionX, regionY = region.getMiddleCords()
                    regionDistanceToProvince = math.sqrt((regionX - provinceNotUsedX) ** 2 + (regionY - provinceNotUsedY) ** 2)
                    if regionDistanceToProvince < closestRegionDistance:
                        closestRegionDistance = regionDistanceToProvince
                        closestRegion = region


            if closestRegion is not None:
                print("RESHUFFLED")
                print(province.getName())
                print("FROM")
                print(province.getRegion().getRegionColor())
                print("TO")
                province.getRegion().removeProvince(province)
                closestRegion.addProvince(province)
                province.setRegion(closestRegion)
                print(province.getRegion().getRegionColor())
        return


