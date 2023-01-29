import pygame
import matplotlib
from PIL import ImageFont

import Enums
import Parameters
from UI.Utils.Button import Button
from UI.Utils.Label2 import Label2
from UI.Utils.Plots import Plots

matplotlib.use("Agg")

import matplotlib.backends.backend_agg as agg


import pylab
from UI.Utils.Fonts import Fonts
from UI.Utils.Label import Label


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

        self.marginLeftWidthMultiplier = 0.05
        self.marginRightWidthMultiplier = 0.05
        self.marginLeftOffSet = self.width*self.marginLeftWidthMultiplier
        self.marginRightOffSet = self.width*self.marginRightWidthMultiplier
        self.selectedPlot = ''

        self.titleLabel = ''
        self.arrayLabel = []
        self.arrayLabelColor = ['']
        self.arrayData = []

    def addHeaderPlot(self, lastFocusObj, world):

        self.writeLine += 1

        self.plotsLabel = Label2("Plots Menu:", self.textFont, False, 1)
        self.plotsLabel.setActiveRectColor(50, 50, 50)
        self.plotsLabel.setActiveBorderColor(10, 10, 100)
        self.plotsScreenSurface.blit(self.plotsLabel.localSurface, (self.width * 0.10, self.getVerticalPositioning()))

        self.writeLine += 2

        if isinstance(lastFocusObj, Button) and lastFocusObj.getButtonName() == 'globalPopulation':
            self.plotsLabel = Label2("Population", self.textFont, True, lastFocusObj.getButtonFlag())
        else:
            self.plotsLabel = Label2("Population", self.textFont, True)

        self.plotsScreenSurfaceObjsRect.append([self.plotsScreenSurface.blit(self.plotsLabel.localSurface, (self.width * 0.05, self.getVerticalPositioning())), Button('globalPopulation'),])

        if isinstance(lastFocusObj, Button) and lastFocusObj.getButtonName() == 'eyes':
            self.plotsLabel = Label2("Eye Colour", self.textFont, True, lastFocusObj.getButtonFlag())
        else:
            self.plotsLabel = Label2("Eye Colour", self.textFont, True)

        self.plotsScreenSurfaceObjsRect.append([self.plotsScreenSurface.blit(self.plotsLabel.localSurface, (self.width * 0.15, self.getVerticalPositioning())), Button('eyes')])

        if isinstance(lastFocusObj, Button) and lastFocusObj.getButtonName() == 'hairs':
            self.plotsLabel = Label2("Hair Colour", self.textFont, True, lastFocusObj.getButtonFlag())
        else:
            self.plotsLabel = Label2("Hair Colour", self.textFont, True)

        self.plotsScreenSurfaceObjsRect.append([self.plotsScreenSurface.blit(self.plotsLabel.localSurface, (self.width * 0.25, self.getVerticalPositioning())), Button('hairs')])

        if isinstance(lastFocusObj, Button) and lastFocusObj.getButtonName() == 'crime':
            self.plotsLabel = Label2("Crime Levels", self.textFont, True, lastFocusObj.getButtonFlag())
        else:
            self.plotsLabel = Label2("Crime Levels", self.textFont, True)

        self.plotsScreenSurfaceObjsRect.append([self.plotsScreenSurface.blit(self.plotsLabel.localSurface, (self.width * 0.35, self.getVerticalPositioning())), Button('crime')])

        self.writeLine += 2

        self.addGeneralPlotsFields(lastFocusObj, world)

    def addPlots(self, world):

        xLabel = 'Year'
        yLabel = 'Population'

        plot = Plots(self.width-self.marginLeftOffSet-self.marginRightOffSet, self.height*.8, self.titleLabel, xLabel, yLabel, world.getWorldYearHistory(), self.arrayLabel, self.arrayLabelColor, self.arrayData)

        self.plotsField = plot.getPlotSurface()
        self.plotsScreenSurface.blit(self.plotsField, (self.marginLeftOffSet, self.getVerticalPositioning()))

        plot.closePlot()

    def addGeneralPlotsFields(self, lastFocusObj, world):

        if isinstance(lastFocusObj, Button) and lastFocusObj.getButtonName() == 'globalPopulation':
            self.titleLabel = 'Global Population'
            self.arrayLabel = [Parameters.globalPopulationArray[0][0]]
            self.arrayLabelColor = [Parameters.globalPopulationArray[0][1]]
            self.arrayData = world.getAlivePeopleNumberHistory()

        elif isinstance(lastFocusObj, Button) and lastFocusObj.getButtonName() == 'eyes':
            self.titleLabel = 'Eye Colour in Population'
            self.arrayLabel = [Parameters.eyeColorArray[0][0], Parameters.eyeColorArray[1][0], Parameters.eyeColorArray[2][0], Parameters.eyeColorArray[3][0], Parameters.eyeColorArray[4][0], Parameters.eyeColorArray[5][0], Parameters.eyeColorArray[6][0]]
            self.arrayLabelColor = [Parameters.eyeColorArray[0][1], Parameters.eyeColorArray[1][1], Parameters.eyeColorArray[2][1], Parameters.eyeColorArray[3][1], Parameters.eyeColorArray[4][1], Parameters.eyeColorArray[5][1], Parameters.eyeColorArray[6][1]]
            self.arrayData = world.getPeopleEyeColorsComplexArray()

        elif isinstance(lastFocusObj, Button) and lastFocusObj.getButtonName() == 'hairs':
            self.titleLabel = 'Hair Colour in Population'
            self.arrayLabel = [Parameters.hairColorArray[0][0], Parameters.hairColorArray[1][0], Parameters.hairColorArray[2][0], Parameters.hairColorArray[3][0], Parameters.hairColorArray[4][0], Parameters.hairColorArray[5][0]]
            self.arrayLabelColor = [Parameters.hairColorArray[0][1], Parameters.hairColorArray[1][1], Parameters.hairColorArray[2][1], Parameters.hairColorArray[3][1], Parameters.hairColorArray[4][1], Parameters.hairColorArray[5][1]]
            self.arrayData = world.getPeopleHairColorsComplexArray()

        elif isinstance(lastFocusObj, Button) and lastFocusObj.getButtonName() == 'crime':
            self.titleLabel = 'Crimes Committed'
            self.arrayLabel = [Parameters.crimeArray[0][0], Parameters.crimeArray[1][0], Parameters.crimeArray[2][0], Parameters.crimeArray[3][0], Parameters.crimeArray[4][0], Parameters.crimeArray[5][0]]
            self.arrayLabelColor = [Parameters.crimeArray[0][1], Parameters.crimeArray[1][1], Parameters.crimeArray[2][1], Parameters.crimeArray[3][1], Parameters.crimeArray[4][1], Parameters.crimeArray[5][1]]
            self.arrayData = world.getCrimeHistory()


        else:
            self.titleLabel = ''
            self.arrayLabel = []
            self.arrayLabelColor = []
            self.arrayData = []

        self.addPlots(world)

    def resetWriteLine(self):

        self.writeLine = 0

    def cleanScreen(self):

        self.plotsScreenSurface.fill(self.screenColor, (0, 0, self.width, self.height))
        self.plotsScreenSurfaceObjsRect = []

    def getPlotsScreenSurface(self):
        return self.plotsScreenSurface

    def getVerticalPositioning(self):
        return self.writeLine * (self.lineHeight + 2 * self.labelBoarderDefault + 2 * self.labelMarginVerticalDefault)