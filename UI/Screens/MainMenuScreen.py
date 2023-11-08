﻿import pygame

from UI.Utils.Fonts import Fonts
from UI.Utils.Label2 import Label2


class MainMenuScreen:

    def __init__(self, width, height, widthOffSet, heightOffSet, screenPosX, screenPosY):
    
        self.screenColor = (50, 10, 50)
        self.writeLine = 0
        self.width = width
        self.height = height
        self.widthOffSet = widthOffSet
        self.heightOffSet = heightOffSet
        self.font = Fonts()
        self.titleFont = self.font.getTitleFont()
        self.titleButtonFont = self.font.getTitleButtonFont()
        self.textFont = self.font.getFont1()
        self.miniTextFont = self.font.getFont2()
        self.lineHeight = self.font.getMainMenuLineHeight()
        self.scroll_y = 0
        self.screenPosX = screenPosX
        self.screenPosY = screenPosY
        self.labelBoarderDefault = 1
        self.labelMarginHorizontalDefault = 2
        self.labelMarginVerticalDefault = 2

        self.mainMenuScreenSurface = pygame.Surface([self.width, self.height - self.heightOffSet])
        self.mainMenuScreenSurfaceObjsRect = []

        self.temp = 0

    def showMainMenu(self, world):

        self.writeLine += 1

        self.mainMenuLabel = Label2(f'Saga Simulator', self.titleFont, False, borderSize=1)
        self.mainMenuLabel.setActiveRectColor(50, 50, 50)
        self.mainMenuLabel.setActiveBorderColor(10, 10, 100)
        self.mainMenuScreenSurface.blit(self.mainMenuLabel.localSurface, (self.mainMenuLabel.centerElement(self.width), self.getVerticalPositioning()))

        self.writeLine += 5

        self.mainMenuLabel2 = Label2(f'New World', self.titleButtonFont, True, borderSize=3)
        self.mainMenuLabel2.setActiveRectColor(10, 100, 10)
        self.mainMenuLabel2.setActiveBorderColor(50, 50, 50)
        self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.mainMenuLabel2.localSurface, (self.mainMenuLabel2.centerElement(self.width), self.getVerticalPositioning())), 'New World'])

        self.writeLine += 4

        self.mainMenuLabel3 = Label2(f'Load World', self.titleButtonFont, True, borderSize=3)
        self.mainMenuLabel3.setActiveRectColor(100, 100, 10)
        self.mainMenuLabel3.setActiveBorderColor(50, 50, 50)
        self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.mainMenuLabel3.localSurface, (self.mainMenuLabel3.centerElement(self.width), self.getVerticalPositioning())), 'Load World'])

        self.writeLine += 8

        self.mainMenuLabel4 = Label2(f'Quit', self.titleButtonFont, True, borderSize=3)
        self.mainMenuLabel4.setActiveRectColor(100, 10, 10)
        self.mainMenuLabel4.setActiveBorderColor(50, 50, 50)
        self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.mainMenuLabel4.localSurface, (self.mainMenuLabel4.centerElement(self.width), self.getVerticalPositioning())), 'Quit'])


    def getVerticalPositioning(self):
        return self.writeLine * (self.lineHeight + 4 * self.labelBoarderDefault + 4 * self.labelMarginVerticalDefault)

    def getMainMenuScreenSurface(self):
        return self.mainMenuScreenSurface

    def cleanScreen(self):

        self.mainMenuScreenSurface.fill(self.screenColor, (0, 0, self.width, self.height))
        self.mainMenuScreenSurfaceObjsRect = []
        self.resetWriteLine()

    def resetWriteLine(self):

        self.writeLine = 0