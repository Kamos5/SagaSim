import pygame

from UI.Utils.Button import Button
from UI.Utils.Fonts import Fonts
from UI.Utils.Label import Label
from UI.Utils.Label2 import Label2


class NavBarScreen:

    def __init__(self, width, height, widthOffSet, heightOffSet, screenPosX, screenPosY):

        self.screenColor = 0, 0, 0
        self.writeLine = 1
        self.width = width
        self.height = height
        self.widthOffSet = widthOffSet
        self.heightOffSet = heightOffSet
        self.font = Fonts()
        self.textFont = self.font.getFont1()
        self.lineHeight = self.font.getLineHeight()
        self.scroll_y = 0
        self.labelBoarderDefault = 1
        self.labelMarginHorizontalDefault = 2
        self.labelMarginVerticalDefault = 2
        self.screenPosX = screenPosX
        self.screenPosY = screenPosY
        self.leftPadding = self.width * 0.05

        self.navBarScreenSurface = pygame.Surface([self.width, self.height - self.heightOffSet])
        self.navBarScreenSurfaceObjsRect = []

        self.menuButton = Button('menu')
        self.helpButton = Button('help')
        self.plotsButton = Button('plots')
        self.worldMapButton = Button("worldMap")
        self.clockButton = Button("clock")

    def resetWriteLine(self):

        self.writeLine = 0

    def cleanScreen(self):

        self.navBarScreenSurface.fill(self.screenColor, (0, 0, self.width, self.height))
        self.navBarScreenSurfaceObjsRect = []

    def getNavBarScreenSurface(self):
        return self.navBarScreenSurface

    def addMenuButton (self):

        self.menuLabel = Label2("Menu", self.textFont, True, borderSize=1)
        self.menuLabel.setActiveRectColor(100, 100, 10)
        self.menuLabel.setActiveBorderColor(10, 100, 100)
        self.menuLabel.changeColorOnHover(self.menuButton.getOnHover())
        self.navBarScreenSurfaceObjsRect.append([self.navBarScreenSurface.blit(self.menuLabel.localSurface, (50, self.heightOffSet)), self.menuButton])

    def addHelpButton (self):

        self.helpLabel = Label2("Help", self.textFont, True, True, borderSize=1)
        self.helpLabel.changeColorOnHover(self.helpButton.getOnHover())
        self.navBarScreenSurfaceObjsRect.append([self.navBarScreenSurface.blit(self.helpLabel.localSurface, (150, self.heightOffSet)), self.helpButton])


    def addPlotsButton (self):

        self.plotsLabel = Label2("Graphs", self.textFont, True, borderSize=1)
        self.plotsLabel.setActiveRectColor(20, 60, 20)
        self.plotsLabel.setActiveBorderColor(100, 10, 10)
        self.plotsLabel.changeColorOnHover(self.plotsButton.getOnHover())
        self.navBarScreenSurfaceObjsRect.append([self.navBarScreenSurface.blit(self.plotsLabel.localSurface, (250, self.heightOffSet)), self.plotsButton])

    def addWorldMapButton (self):

        self.worldMapLabel = Label2("World Map", self.textFont, True, borderSize=1)
        self.worldMapLabel.setActiveRectColor(10, 10, 70)
        self.worldMapLabel.setActiveBorderColor(100, 100, 100)
        self.worldMapLabel.changeColorOnHover(self.worldMapButton.getOnHover())
        self.navBarScreenSurfaceObjsRect.append([self.navBarScreenSurface.blit(self.worldMapLabel.localSurface, (350, self.heightOffSet)), self.worldMapButton])


    def addGameSpeedCounter(self, world):

        self.gameSpeedCounter = Label2(f'Speed:', self.textFont, False, borderSize=1)
        self.navBarScreenSurface.blit(self.gameSpeedCounter.localSurface, (self.width * 0.70, self.heightOffSet))

        gameSpeedString = ""
        for gameSpeedCounter in range(world.getGameSpeedCounter()):
            gameSpeedString += "|"

        self.gameSpeedCounter = Label2(gameSpeedString, self.textFont, False, borderSize=1)
        self.navBarScreenSurface.blit(self.gameSpeedCounter.localSurface, (self.width * 0.70 + 70, self.heightOffSet))

    def addDateTimer(self, world):

        self.dateTimeLabel = Label2(f'{str(world.getDay())} / {str(world.getMonth().value[1])} / {str(world.getYear())}', self.textFont, True, borderSize=1, horizontalMargin=10)
        self.dateTimeLabel.changeColorOnHover(self.clockButton.getOnHover())
        self.navBarScreenSurfaceObjsRect.append([self.navBarScreenSurface.blit(self.dateTimeLabel.localSurface, (self.width * 0.80, self.heightOffSet)), self.clockButton])

    def addPausedIndicator(self):

        self.pausedLabel = Label2("PAUSED", self.textFont, False, True)
        self.navBarScreenSurface.blit(self.pausedLabel.localSurface, (self.width * 0.95, self.heightOffSet))

    def getVerticalPositioning(self):
        return self.writeLine * (self.lineHeight + 4 * self.labelBoarderDefault + 4 * self.labelMarginVerticalDefault)