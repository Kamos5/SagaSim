import pygame
import matplotlib

import Enums
import Parameters
from UI.Utils.Plots import Plots

matplotlib.use("Agg")

import matplotlib.backends.backend_agg as agg


import pylab
from UI.Utils.Fonts import Fonts
from UI.Utils.Label import Label


class PlotsScreen:

    def __init__(self, width, height, widthOffSet, heightOffSet, screenPosX, screenPosY):

        self.screenColor = 20, 60, 20
        self.writeLine = 1
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

        self.plotsScreenSurface = pygame.Surface([self.width, self.height - self.heightOffSet])
        self.plotsScreenSurfaceObjsRect = []

        self.marginLeftWidthMultiplier = 0.05
        self.marginRightWidthMultiplier = 0.05
        self.marginLeftOffSet = self.width*self.marginLeftWidthMultiplier
        self.marginRightOffSet = self.width*self.marginRightWidthMultiplier
        self.selectedPlot = ''

        self.titleLabel = ''
        self.arrayLabel = ['']
        self.arrayLabelColor = ['']
        self.arrayData = []

    def addHeaderPlot(self, lastFocusObj, world):

        self.plotsLabel = Label("Plots Menu:", 130, self.lineHeight, self.textFont, False, 1)
        self.plotsLabel.setActiveRectColor(50, 50, 50)
        self.plotsLabel.setActiveBorderColor(10, 10, 100)
        self.plotsScreenSurface.blit(self.plotsLabel.localSurface, (self.width * 0.10, self.writeLine*self.lineHeight))
        self.writeLine += 2

        if lastFocusObj == 'eyes':
            self.plotsLabel = Label("Eye", 55, self.lineHeight, self.textFont, True, True)
        else:
            self.plotsLabel = Label("Eye", 55, self.lineHeight, self.textFont, True)

        self.plotsScreenSurfaceObjsRect.append([self.plotsScreenSurface.blit(self.plotsLabel.localSurface, (self.width * 0.10, self.writeLine * self.lineHeight)), 'eyes'])

        if lastFocusObj == 'hairs':
            self.plotsLabel = Label("Hair", 60, self.lineHeight, self.textFont, True, True)
        else:
            self.plotsLabel = Label("Hair", 60, self.lineHeight, self.textFont, True)

        self.plotsScreenSurfaceObjsRect.append([self.plotsScreenSurface.blit(self.plotsLabel.localSurface, (self.width * 0.15, self.writeLine * self.lineHeight)), 'hairs'])

        self.writeLine += 2

        self.addGeneralPlotsFields(lastFocusObj, world)

    def addPlots(self, world):

        xLabel = 'Year'
        yLabel = 'Population'

        plot = Plots(self.width-self.marginLeftOffSet-self.marginRightOffSet, self.height*.8, self.titleLabel, xLabel, yLabel, world.getWorldYearHistory(), self.arrayLabel, self.arrayLabelColor, self.arrayData)

        self.plotsField = plot.getPlotSurface()
        self.plotsScreenSurface.blit(self.plotsField, (self.marginLeftOffSet, self.writeLine * self.lineHeight))

        plot.closePlot()

    def addGeneralPlotsFields(self, lastFocusObj, world):

        if lastFocusObj == 'eyes':
            self.titleLabel = 'Eye Colour in Population'
            self.arrayLabel = [Parameters.eyeColorArray[0][0], Parameters.eyeColorArray[1][0], Parameters.eyeColorArray[2][0], Parameters.eyeColorArray[3][0], Parameters.eyeColorArray[4][0], Parameters.eyeColorArray[5][0], Parameters.eyeColorArray[6][0]]
            self.arrayLabelColor = [Parameters.eyeColorArray[0][1], Parameters.eyeColorArray[1][1], Parameters.eyeColorArray[2][1], Parameters.eyeColorArray[3][1], Parameters.eyeColorArray[4][1], Parameters.eyeColorArray[5][1], Parameters.eyeColorArray[6][1]]
            self.arrayData = world.getPeopleEyeColorsComplexArray()

        elif lastFocusObj == 'hairs':
            self.titleLabel = 'Hair Colour in Population'
            self.arrayLabel = [Parameters.hairColorArray[0][0], Parameters.hairColorArray[1][0], Parameters.hairColorArray[2][0], Parameters.hairColorArray[3][0], Parameters.hairColorArray[4][0], Parameters.hairColorArray[5][0]]
            self.arrayLabelColor = [Parameters.hairColorArray[0][1], Parameters.hairColorArray[1][1], Parameters.hairColorArray[2][1], Parameters.hairColorArray[3][1], Parameters.hairColorArray[4][1], Parameters.hairColorArray[5][1]]
            self.arrayData = world.getPeopleHairColorsComplexArray()

        self.addPlots(world)

    def resetWriteLine(self):

        self.writeLine = 1

    def cleanScreen(self):

        self.plotsScreenSurface.fill(self.screenColor, (0, 0, self.width, self.height))
        self.plotsScreenSurfaceObjsRect = []

    def getPlotsScreenSurface(self):
        return self.plotsScreenSurface

    # def addPopulationButton (self):
    #
    #     self.helpLabel = Label("Help", 50, self.lineHeight, self.textFont, True, True, 1)
    #     self.navBarScreenSurfaceObjsRect.append([self.navBarScreenSurface.blit(self.helpLabel.localSurface, (self.width * 0.01, 0)), 'Help'])