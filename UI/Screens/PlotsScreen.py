import pygame
import matplotlib

import Parameters
import Utils
from UI.Utils.Button import Button
from UI.Utils.Label2 import Label2
from UI.Utils.Plots import Plots

matplotlib.use("Agg")

from UI.Utils.Fonts import Fonts


class PlotsScreen:

    def __init__(self, width, height, widthOffSet, heightOffSet, screenPosX, screenPosY):

        self.screenColor = 20, 60, 20
        self.writeLine = 0
        self.width = width
        self.height = height
        self.widthOffSet = widthOffSet
        self.heightOffSet = heightOffSet
        self.font = Fonts()
        self.textFont = self.font.getPlotsFont()
        self.miniTextFont = self.font.getFont2()
        self.lineHeight = self.font.getPlotsLineHeight()
        self.scroll_y = 0
        self.screenPosX = screenPosX
        self.screenPosY = screenPosY
        self.labelBoarderDefault = 1
        self.labelMarginHorizontalDefault = 2
        self.labelMarginVerticalDefault = 2

        self.plotsScreenSurface = pygame.Surface([self.width, self.height - self.heightOffSet])
        self.plotsScreenSurfaceObjsRect = []

        self.marginLeftWidthMultiplier = 0.01
        self.marginRightWidthMultiplier = 0.01
        self.marginLeftOffSet = self.width*self.marginLeftWidthMultiplier
        self.marginRightOffSet = self.width*self.marginRightWidthMultiplier
        self.selectedPlot = ''

        self.titleLabel = ''
        self.arrayLabel = []
        self.arrayLabelColor = ['']
        self.arrayData = []
        self.yLabelTitle = ''

        self.globalPopulationButton = Button('globalPopulation')
        self.birthsDeathsRatioButton = Button('birthsDeathsRatio')
        self.eyesButton = Button('eyes')

        self.hairsButton = Button('hairs')
        self.crimeButton = Button('crime')
        self.sexualityButton = Button('sexuality')
        self.sexualityPercButton = Button('sexuality%')
        self.heightButton = Button('height')

    def addHeaderPlot(self, lastFocusObj, world):

        self.writeLine += 1

        self.plotsLabel = Label2("Plots Menu:", self.textFont, False, borderSize=1)
        self.plotsLabel.setActiveRectColor(50, 50, 50)
        self.plotsLabel.setActiveBorderColor(10, 10, 100)
        self.plotsScreenSurface.blit(self.plotsLabel.localSurface, (self.width * 0.10, self.getVerticalPositioning()))

        self.writeLine += 2

        if self.globalPopulationButton.getIsActive() and lastFocusObj == self.globalPopulationButton:
        # if isinstance(lastFocusObj, Button) and lastFocusObj.getButtonName() == 'globalPopulation':
            self.plotsLabel = Label2("Population", self.textFont, True, lastFocusObj.getButtonFlag())
        else:
            self.plotsLabel = Label2("Population", self.textFont, True)
        self.plotsLabel.changeColorOnHover(self.globalPopulationButton.getOnHover())
        self.plotsScreenSurfaceObjsRect.append([self.plotsScreenSurface.blit(self.plotsLabel.localSurface, (self.width * 0.05, self.getVerticalPositioning())), self.globalPopulationButton])

        if self.birthsDeathsRatioButton.getIsActive() and lastFocusObj == self.birthsDeathsRatioButton:
            self.plotsLabel = Label2("Births to Deaths Ratio", self.textFont, True, lastFocusObj.getButtonFlag())
        else:
            self.plotsLabel = Label2("Births to Deaths Ratio", self.textFont, True)

        self.plotsLabel.changeColorOnHover(self.birthsDeathsRatioButton.getOnHover())
        self.plotsScreenSurfaceObjsRect.append([self.plotsScreenSurface.blit(self.plotsLabel.localSurface, (self.width * 0.15, self.getVerticalPositioning())), self.birthsDeathsRatioButton])

        if self.eyesButton.getIsActive() and lastFocusObj == self.eyesButton:
            self.plotsLabel = Label2("Eye Colour", self.textFont, True, lastFocusObj.getButtonFlag())
        else:
            self.plotsLabel = Label2("Eye Colour", self.textFont, True)

        self.plotsLabel.changeColorOnHover(self.eyesButton.getOnHover())
        self.plotsScreenSurfaceObjsRect.append([self.plotsScreenSurface.blit(self.plotsLabel.localSurface, (self.width * 0.30, self.getVerticalPositioning())), self.eyesButton])

        if self.hairsButton.getIsActive() and lastFocusObj == self.hairsButton:
            self.plotsLabel = Label2("Hair Colour", self.textFont, True, lastFocusObj.getButtonFlag())
        else:
            self.plotsLabel = Label2("Hair Colour", self.textFont, True)

        self.plotsLabel.changeColorOnHover(self.hairsButton.getOnHover())
        self.plotsScreenSurfaceObjsRect.append([self.plotsScreenSurface.blit(self.plotsLabel.localSurface, (self.width * 0.40, self.getVerticalPositioning())), self.hairsButton])

        if self.crimeButton.getIsActive() and lastFocusObj == self.crimeButton:
            self.plotsLabel = Label2("Crime Levels", self.textFont, True, lastFocusObj.getButtonFlag())
        else:
            self.plotsLabel = Label2("Crime Levels", self.textFont, True)

        self.plotsLabel.changeColorOnHover(self.crimeButton.getOnHover())
        self.plotsScreenSurfaceObjsRect.append([self.plotsScreenSurface.blit(self.plotsLabel.localSurface, (self.width * 0.50, self.getVerticalPositioning())), self.crimeButton])

        if self.sexualityButton.getIsActive() and lastFocusObj == self.sexualityButton:
            self.plotsLabel = Label2("Sexuality", self.textFont, True, lastFocusObj.getButtonFlag())
        else:
            self.plotsLabel = Label2("Sexuality", self.textFont, True)

        self.plotsLabel.changeColorOnHover(self.sexualityButton.getOnHover())
        self.plotsScreenSurfaceObjsRect.append([self.plotsScreenSurface.blit(self.plotsLabel.localSurface, (self.width * 0.60, self.getVerticalPositioning())), self.sexualityButton])

        if self.sexualityPercButton.getIsActive() and lastFocusObj == self.sexualityPercButton:
            self.plotsLabel = Label2("%", self.textFont, True, lastFocusObj.getButtonFlag())
        else:
            self.plotsLabel = Label2("%", self.textFont, True)

        self.plotsLabel.changeColorOnHover(self.sexualityPercButton.getOnHover())
        self.plotsScreenSurfaceObjsRect.append([self.plotsScreenSurface.blit(self.plotsLabel.localSurface, (self.width * 0.66, self.getVerticalPositioning())), self.sexualityPercButton])

        if self.heightButton.getIsActive() and lastFocusObj == self.heightButton:
            self.plotsLabel = Label2("Height", self.textFont, True, lastFocusObj.getButtonFlag())
        else:
            self.plotsLabel = Label2("Height", self.textFont, True)

        self.plotsLabel.changeColorOnHover(self.heightButton.getOnHover())
        self.plotsScreenSurfaceObjsRect.append([self.plotsScreenSurface.blit(self.plotsLabel.localSurface, (self.width * 0.70, self.getVerticalPositioning())), self.heightButton])

        # if isinstance(lastFocusObj, Button) and lastFocusObj.getButtonName() == 'weather':
        #     self.plotsLabel = Label2("Weather", self.textFont, True, lastFocusObj.getButtonFlag())
        # else:
        #     self.plotsLabel = Label2("Weather", self.textFont, True)
        #
        # self.plotsScreenSurfaceObjsRect.append([self.plotsScreenSurface.blit(self.plotsLabel.localSurface, (self.width * 0.65, self.getVerticalPositioning())), Button('weather')])

        self.writeLine += 2

        self.addGeneralPlotsFields(lastFocusObj, world)

    def addPlots(self, world):

        xLabel = 'Year'
        yLabel = self.titleLabel
        dummyWeatherFlag = False

        worldYearHistoryParam = world.getWorldYearHistory()

        if yLabel == 'Weather History':
            dummyWeatherFlag = True

        if yLabel == 'Global Population':
            worldYearHistoryParam = world.getWorldYearHistoryReduced()

        if yLabel == 'Dead Alive Ratio':
            # worldYearHistoryParam = world.getWorldYearHistoryReduced()
            worldYearHistoryParam = world.getWorldYearHistoryYearly()

        if yLabel == 'Eye Colour in Population':
            worldYearHistoryParam = world.getWorldYearHistoryReduced()

        if yLabel == 'Hair Colour in Population':
            worldYearHistoryParam = world.getWorldYearHistoryReduced()

        if yLabel == 'Crimes Committed':
            worldYearHistoryParam = world.getWorldYearHistoryReduced()

        plot = Plots(self.width-self.marginLeftOffSet-self.marginRightOffSet, self.height*.8, self.titleLabel, xLabel, yLabel, worldYearHistoryParam, self.arrayLabel, self.arrayLabelColor, self.arrayData, dummyWeatherFlag=dummyWeatherFlag)
        self.plotsField = plot.getPlotSurface()
        self.plotsScreenSurface.blit(self.plotsField, (self.marginLeftOffSet, self.getVerticalPositioning()))

        plot.closePlot()

    def addGeneralPlotsFields(self, lastFocusObj, world):

        if isinstance(lastFocusObj, Button) and lastFocusObj.getButtonName() == 'globalPopulation':
            world.getAlivePeopleNumberHistoryReduced()
            self.titleLabel = 'Global Population'
            self.arrayLabel = [Parameters.globalPopulationArray[0][0]]
            self.arrayLabelColor = [Parameters.globalPopulationArray[0][1]]
            self.arrayData = world.getAlivePeopleNumberHistory()
            self.yLabelTitle = 'Population'

        elif isinstance(lastFocusObj, Button) and lastFocusObj.getButtonName() == 'birthsDeathsRatio':
            # world.getBirthsDeathsPeopleNumberHistoryReduced()
            world.getBirthsDeathsPeopleNumberHistoryYearly()
            self.titleLabel = 'Dead Alive Ratio'
            self.arrayLabel = [Parameters.birthsDeathsColorArray[0][0], Parameters.birthsDeathsColorArray[1][0]]
            self.arrayLabelColor = [Parameters.birthsDeathsColorArray[0][1], Parameters.birthsDeathsColorArray[1][1]]
            # self.arrayData = world.getBirthsDeathsPeopleNumberHistory()
            self.arrayData = world.getDeathsBirthsPeopleNumberHistoryYearly()
            self.yLabelTitle = 'Ammount'

        elif isinstance(lastFocusObj, Button) and lastFocusObj.getButtonName() == 'eyes':
            world.countEyeColor()
            self.titleLabel = 'Eye Colour in Population'
            self.arrayLabel = [Parameters.eyeColorArray[0][0], Parameters.eyeColorArray[1][0], Parameters.eyeColorArray[2][0], Parameters.eyeColorArray[3][0], Parameters.eyeColorArray[4][0], Parameters.eyeColorArray[5][0], Parameters.eyeColorArray[6][0]]
            self.arrayLabelColor = [Parameters.eyeColorArray[0][1], Parameters.eyeColorArray[1][1], Parameters.eyeColorArray[2][1], Parameters.eyeColorArray[3][1], Parameters.eyeColorArray[4][1], Parameters.eyeColorArray[5][1], Parameters.eyeColorArray[6][1]]
            self.arrayData = world.getPeopleEyeColorsComplexArray()
            self.yLabelTitle = 'Population'

        elif isinstance(lastFocusObj, Button) and lastFocusObj.getButtonName() == 'hairs':
            world.countHairColor()
            self.titleLabel = 'Hair Colour in Population'
            self.arrayLabel = [Parameters.hairColorArray[0][0], Parameters.hairColorArray[1][0], Parameters.hairColorArray[2][0], Parameters.hairColorArray[3][0], Parameters.hairColorArray[4][0], Parameters.hairColorArray[5][0]]
            self.arrayLabelColor = [Parameters.hairColorArray[0][1], Parameters.hairColorArray[1][1], Parameters.hairColorArray[2][1], Parameters.hairColorArray[3][1], Parameters.hairColorArray[4][1], Parameters.hairColorArray[5][1]]
            self.arrayData = world.getPeopleHairColorsComplexArray()
            self.yLabelTitle = 'Population'

        elif isinstance(lastFocusObj, Button) and lastFocusObj.getButtonName() == 'crime':
            world.countCrime()
            self.titleLabel = 'Crimes Committed'
            self.arrayLabel = [Parameters.crimeColorArray[0][0], Parameters.crimeColorArray[1][0], Parameters.crimeColorArray[2][0], Parameters.crimeColorArray[3][0], Parameters.crimeColorArray[4][0], Parameters.crimeColorArray[5][0]]
            self.arrayLabelColor = [Parameters.crimeColorArray[0][1], Parameters.crimeColorArray[1][1], Parameters.crimeColorArray[2][1], Parameters.crimeColorArray[3][1], Parameters.crimeColorArray[4][1], Parameters.crimeColorArray[5][1]]
            self.arrayData = world.getCrimeHistoryReduced()
            self.yLabelTitle = 'Crimes number'

        elif isinstance(lastFocusObj, Button) and lastFocusObj.getButtonName() == 'sexuality':
            self.titleLabel = 'Sexuality'
            self.arrayLabel = [Parameters.sexualityColorArray[0][0], Parameters.sexualityColorArray[1][0]]
            self.arrayLabelColor = [Parameters.sexualityColorArray[0][1], Parameters.sexualityColorArray[1][1]]
            self.arrayData = world.getSexualityHistory()
            self.yLabelTitle = 'Sexuality type'

        elif isinstance(lastFocusObj, Button) and lastFocusObj.getButtonName() == 'sexuality%':
            self.titleLabel = 'Sexuality per Capita'
            self.arrayLabel = [Parameters.sexualityColorArray[0][0], Parameters.sexualityColorArray[1][0]]
            self.arrayLabelColor = [Parameters.sexualityColorArray[0][1], Parameters.sexualityColorArray[1][1]]
            self.arrayData = world.getSexualityPctHistory()
            self.yLabelTitle = 'Sexuality type'

        elif isinstance(lastFocusObj, Button) and lastFocusObj.getButtonName() == 'height':
            self.titleLabel = 'Average Height'
            self.arrayLabel = [Parameters.averageHeightColorArray[0][0], Parameters.averageHeightColorArray[1][0], Parameters.averageHeightColorArray[2][0]]
            self.arrayLabelColor = [Parameters.averageHeightColorArray[0][1], Parameters.averageHeightColorArray[1][1], Parameters.averageHeightColorArray[2][1]]
            self.arrayData = world.getAverageHeightHistory()
            self.yLabelTitle = 'Height'

        elif isinstance(lastFocusObj, Button) and lastFocusObj.getButtonName() == 'weather':
            self.titleLabel = 'Weather History'
            self.arrayLabel = self.getRegionsLabelArray(world)
            self.arrayLabelColor = [Parameters.regionColorArray[0][0], Parameters.regionColorArray[1][0]]
            self.arrayData = world.getWeatherHistoryForAllRegions()
            self.yLabelTitle = 'Last season weather pattern'

        else:
            self.titleLabel = ''
            self.arrayLabel = []
            self.arrayLabelColor = []
            self.arrayData = []
            self.yLabelTitle = ''


        plotTime = Utils.timeFunction(True, self.addPlots, world)
        #print("Plot Time: " + str(plotTime))

    def resetWriteLine(self):

        self.writeLine = 0

    def cleanScreen(self):

        self.plotsScreenSurface.fill(self.screenColor, (0, 0, self.width, self.height))
        self.plotsScreenSurfaceObjsRect = []

    def getPlotsScreenSurface(self):
        return self.plotsScreenSurface

    def getVerticalPositioning(self):
        return self.writeLine * (self.lineHeight + 4 * self.labelBoarderDefault + 4 * self.labelMarginVerticalDefault)

    def getRegionsLabelArray(self, world):

        regionsLabelArray = []
        for region in world.getRegions():
            regionsLabelArray.append(region.getRegionName())
        return regionsLabelArray