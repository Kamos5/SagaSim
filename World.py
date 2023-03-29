import Enums
import Utils
from Enums import Settlements
from PersonLifeEventsHistory import adulthoodReached
from Region import Region
import RegionNameGenerator as RNG
import Parameters
from RegionLifeEventsHistory import weatherEvent
from WorldMap import WorldMap


class World:

    initYear = Parameters.startingYear
    regions = []
    settlementsInitNumber = Parameters.startingSettlementsPerRegion

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

    def reset(self, startYear=initYear):

        self.initYear = startYear
        self.day = 31
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

    def getWorldMap(self):
        return self.worldMap

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

    def getBirthsPerYearTemp(self):
        return self.birthsPerYearTemp

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

    def changeDivorcesNumber(self, value):
        self.divorcesNumber += value

    def getYear(self):
        return self.year

    def increaseYear(self):
        self.year += 1

    def getDayOfTheYear(self):
        return self.dayOfTheYear

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

    def increaseDayOfWeekFlag(self):
        if self.dayOfWeekFlag < 7:
            self.dayOfWeekFlag += 1
        else:
            self.dayOfWeekFlag = 1

    def getMonth(self):
        return self.month

    def setMonth(self, newMonth):
        self.month = newMonth

    def increaseDay(self):

        if self.getDay() == self.getMonth().value[2]:
            if self.getMonth().value[0] == 1:
                self.month = Enums.Months.FEBRUARY
            elif self.getMonth().value[0] == 2:
                self.month = Enums.Months.MARCH
            elif self.getMonth().value[0] == 3:
                self.month = Enums.Months.APRIL
            elif self.getMonth().value[0] == 4:
                self.month = Enums.Months.MAY
            elif self.getMonth().value[0] == 5:
                self.month = Enums.Months.JUNE
            elif self.getMonth().value[0] == 6:
                self.month = Enums.Months.JULY
            elif self.getMonth().value[0] == 7:
                self.month = Enums.Months.AUGUST
            elif self.getMonth().value[0] == 8:
                self.month = Enums.Months.SEPTEMBER
            elif self.getMonth().value[0] == 9:
                self.month = Enums.Months.OCTOBER
            elif self.getMonth().value[0] == 10:
                self.month = Enums.Months.NOVEMBER
            elif self.getMonth().value[0] == 11:
                self.month = Enums.Months.DECEMBER
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

    def generateRegionsNames(self, regionsNumber = 5):

        startingSet = 1

        if startingSet == 1:
            startingSet1For4 = [(0, 0), (self.getWorldMap().getWidth()-1, 0), (0, self.getWorldMap().getHeight()-1), (self.getWorldMap().getWidth()-1, self.getWorldMap().getHeight()-1)]
        else:
            startingSet1For4 = [(50, 50),(50, 51),(51, 50),(51, 51)]


        if regionsNumber >= 1:
            region = Region(RNG.randomEnglishRegionName())
            region.setRegionColor((220, 20, 20))
            region.addRegionTerritory(startingSet1For4[0])
            self.regions.append(region)
        if regionsNumber >= 2:
            region = Region(RNG.randomNorseRegionName())
            region.setRegionColor((20, 20, 220))
            region.addRegionTerritory(startingSet1For4[1])
            self.regions.append(region)
        if regionsNumber >= 3:
            region = Region(RNG.randomSlavicRegionName())
            region.setRegionColor((20, 220, 20))
            region.addRegionTerritory(startingSet1For4[2])
            self.regions.append(region)
        if regionsNumber >= 4:
            region = Region(RNG.randomEgyptRegionName())
            region.setRegionColor((220, 220, 20))
            region.addRegionTerritory(startingSet1For4[3])
            self.regions.append(region)

        for region in self.getRegions():
            expandToX, expandToY = region.getRegionTerritories()[0]
            self.getWorldMap().addField(region.getRegionColor(), x=expandToX, y=expandToY)

    def generateSettlements(self):

        for region in self.regions:
            townInitList = []
            for i in range(self.settlementsInitNumber):
                newSettlement = region.addInitSettlement(self)
                newSettlement.setRegion(region)
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

    def getBirthsPerYear(self):
        return self.birthsPerYear

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

    def getCrimesPerYearReduced(self):
        return self.crimesPerYearReduced

    def getCrimesHomicidePerYearReduced(self):
        return self.crimeHomicidePerYearReduced

    def getCrimesAssaultPerYearReduced(self):
        return self.crimeAssaultPerYearReduced

    def getCrimesBurglaryPerYearReduced(self):
        return self.crimeBurglaryPerYearReduced

    def getCrimesTheftPerYearReduced(self):
        return self.crimeTheftPerYearReduced

    def getCrimesFailedPerYearReduced(self):
        return self.crimeFailedPerYearReduced

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

    def getBirthsPerYearNumberHistory(self):
        return self.birthsPerYearNumberHistory

    def getAvarageLifeSpam(self):
        return self.avarageLifeSpamHistory

    def getAverageHeightHistory(self):
        return [self.averageHeightHistory, self.averageHeightMHistory, self.averageHeightFHistory]

    def getWorldYearHistory(self):
        return self.worldHistory

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

    def getSexualityPctHistory(self):
        return [self.getSexualityHeteroPct(), self.getSexualityHomoPct()]

    def getPeopleAliveHistory(self):
        return [self.peopleAliveHistory]

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