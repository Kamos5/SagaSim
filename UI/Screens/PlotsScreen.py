import pygame
import matplotlib

import Enums
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

    def addPlots(self, world):

        self.plotsLabel = Label("Plots Menu:", 140, self.lineHeight, self.textFont, False, True, 2)
        self.plotsLabel.setActiveRectColor(50, 50, 50)
        self.plotsLabel.setActiveBorderColor(10, 10, 100)

        self.plotsScreenSurface.blit(self.plotsLabel.localSurface, (self.width * 0.10, self.writeLine*self.lineHeight))

        self.writeLine += 3

        peopleWithBlackEyeColor = []
        peopleWithBrownEyeColor = []
        peopleWithAmberEyeColor = []
        peopleWithHazelEyeColor = []
        peopleWithGreenEyeColor = []
        peopleWithBlueEyeColor = []
        peopleWithGrayEyeColor = []

        for year in world.getPeopleAliveHistory():
            peopleWithBlackEyeColorTemp = 0
            peopleWithBrownEyeColorTemp = 0
            peopleWithAmberEyeColorTemp = 0
            peopleWithHazelEyeColorTemp = 0
            peopleWithGreenEyeColorTemp = 0
            peopleWithBlueEyeColorTemp = 0
            peopleWithGrayEyeColorTemp = 0
            for person in year:
                if person.getEyeColor() == Enums.EyeColor.BLACK:
                    peopleWithBlackEyeColorTemp+=1
                if person.getEyeColor() == Enums.EyeColor.BROWN:
                    peopleWithBrownEyeColorTemp+=1
                if person.getEyeColor() == Enums.EyeColor.AMBER:
                    peopleWithAmberEyeColorTemp+=1
                if person.getEyeColor() == Enums.EyeColor.HAZEL:
                    peopleWithHazelEyeColorTemp+=1
                if person.getEyeColor() == Enums.EyeColor.GREEN:
                    peopleWithGreenEyeColorTemp+=1
                if person.getEyeColor() == Enums.EyeColor.BLUE:
                    peopleWithBlueEyeColorTemp+=1
                if person.getEyeColor() == Enums.EyeColor.GRAY:
                    peopleWithGrayEyeColorTemp+=1

            peopleWithBlackEyeColor.append(peopleWithBlackEyeColorTemp)
            peopleWithBrownEyeColor.append(peopleWithBrownEyeColorTemp)
            peopleWithAmberEyeColor.append(peopleWithAmberEyeColorTemp)
            peopleWithHazelEyeColor.append(peopleWithHazelEyeColorTemp)
            peopleWithGreenEyeColor.append(peopleWithGreenEyeColorTemp)
            peopleWithBlueEyeColor.append(peopleWithBlueEyeColorTemp)
            peopleWithGrayEyeColor.append(peopleWithGrayEyeColorTemp)

        plot = Plots(world.getWorldYearHistory(), peopleWithBrownEyeColor, self.width-self.marginLeftOffSet-self.marginRightOffSet, self.height*.8)

        self.plotsField = plot.getPlotSurface()

        self.plotsScreenSurface.blit(self.plotsField, (self.marginLeftOffSet, self.writeLine * self.lineHeight))

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