import pygame

from UI.Utils.Fonts import Fonts
from UI.Utils.Label import Label


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
        self.screenPosX = screenPosX
        self.screenPosY = screenPosY

        self.navBarScreenSurface = pygame.Surface([self.width, self.height - self.heightOffSet])
        self.navBarScreenSurfaceObjsRect = []


    def resetWriteLine(self):

        self.writeLine = 1

    def cleanScreen(self):

        self.navBarScreenSurface.fill(self.screenColor, (0, 0, self.width, self.height))

    def getNavBarScreenSurface(self):
        return self.navBarScreenSurface

    def addDateTimer(self, world):

        self.dateTimeLabel = Label("Year: " + str(world.getYear()), 100, self.lineHeight, self.textFont, True, False, 1)
        self.navBarScreenSurfaceObjsRect.append([self.navBarScreenSurface.blit(self.dateTimeLabel.localSurface, (self.width * 0.92, 0)), 'Clock'])

