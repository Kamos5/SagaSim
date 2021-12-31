import pygame

from Family import Family
from Person import Person
from Region import Region
from Settlements import Settlements
from UI.Fonts import Fonts
from UI.Label import Label


class NavBarScreen:

    def __init__(self, width, height, widthOffSet, heightOffSet):

        self.screenColor = 0, 0, 0
        self.writeLine = 1
        self.width = width
        self.height = height
        self.widthOffSet = widthOffSet
        self.heightOffSet = heightOffSet
        self.font1 = Fonts().getFont1()
        self.scroll_y = 0

        self.navBarScreenSurface = pygame.Surface([self.width, self.height - self.heightOffSet])
        self.listScreenSurfaceTimeRect = []


    def resetWriteLine(self):

        self.writeLine = 1

    def cleanScreen(self):

        self.navBarScreenSurface.fill(self.screenColor, (0, 0, self.width, self.height))

    def getNavBarScreenSurface(self):
        return self.navBarScreenSurface

    def addDateTimer(self, world):

        label = Label("Year: " + str(world.getYear()), 100, 20, self.font1)
        self.listScreenSurfaceTimeRect.append(self.navBarScreenSurface.blit(label.localSurface, (self.width * 0.92, 0)))

