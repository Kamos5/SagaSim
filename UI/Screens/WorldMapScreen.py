import time

import pygame

from UI.Utils.Label2 import Label2


from UI.Utils.Fonts import Fonts


class WorldMapScreen:

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

        self.worldMapScreenSurface = pygame.Surface([self.width, self.height - self.heightOffSet])
        self.worldMapScreenSurfaceObjsRect = []

        self.marginLeftWidthMultiplier = 0.01
        self.marginRightWidthMultiplier = 0.01
        self.marginLeftOffSet = self.width*self.marginLeftWidthMultiplier
        self.marginRightOffSet = self.width*self.marginRightWidthMultiplier

        self.DEFAULT_GRAY_1 = (128, 128, 128)
        self.DEFAULT_GRAY_2 = (192, 192, 192)
        self.DEFAULT_BORDER_COLOR = (20, 20, 20)

        self.GRAY_1 = self.DEFAULT_GRAY_1
        self.GRAY_2 = self.DEFAULT_GRAY_2
        self.BORDER_COLOR = self.DEFAULT_BORDER_COLOR

        self.color = self.GRAY_1

        self.changedColorCordsArray = []


    def addMap(self):

        self.writeLine += 1

        self.mapLabel = Label2("World Map:", self.textFont, False, True, 2)
        self.mapLabel.setActiveRectColor(20, 20, 20)
        self.mapLabel.setActiveBorderColor(100, 100, 100)

        self.worldMapScreenSurface.blit(self.mapLabel.localSurface, (self.width * 0.10, self.writeLine*self.lineHeight))

        self.writeLine += 5

        self.addDefaultMap()

        self.modMap()

    def addDefaultMap(self):


        mapXSize = 1600
        mapYSize = 800

        chunkSizeXWithBorder = 5
        chunkSizeYWithBorder = 5
        borderChunkSizeX = 1
        borderChunkSizeY = 1
        chunkSizeX = chunkSizeXWithBorder - borderChunkSizeX
        chunkSizeY = chunkSizeYWithBorder - borderChunkSizeY
        verticalPadding = 40

        for y in range(0, mapYSize, chunkSizeXWithBorder):
            for x in range(0, mapXSize, chunkSizeYWithBorder):

                rect = pygame.draw.rect(self.worldMapScreenSurface, self.color, [x + verticalPadding, y + (self.writeLine * self.lineHeight), chunkSizeX, chunkSizeY])
                self.worldMapScreenSurfaceObjsRect.append([rect, self])
                if self.color == self.GRAY_1:
                    self.color = self.GRAY_2
                else:
                    self.color = self.GRAY_1
                if x < mapXSize-chunkSizeXWithBorder:
                    pygame.draw.rect(self.worldMapScreenSurface, self.BORDER_COLOR, [x + verticalPadding+chunkSizeX, y + (self.writeLine * self.lineHeight), borderChunkSizeX, chunkSizeX])
                if y < mapYSize-chunkSizeYWithBorder:
                    pygame.draw.rect(self.worldMapScreenSurface, self.BORDER_COLOR, [x + verticalPadding, y + (self.writeLine * self.lineHeight)+chunkSizeY, chunkSizeY, borderChunkSizeY])
            if self.color == self.GRAY_1:
                self.color = self.GRAY_2
            else:
                self.color = self.GRAY_1

    def modMap(self):
        oldcolor = self.color
        for changeColor in self.changedColorCordsArray:
            self.color = (20, 220, 20)
            x, y, w, h = changeColor
            rect = pygame.draw.rect(self.worldMapScreenSurface, self.color, [x, y, w, h])
            self.worldMapScreenSurfaceObjsRect.append([rect, self])
        self.color = oldcolor

    def resetWriteLine(self):

        self.writeLine = 0

    def changeColorAfterClick(self, rect):

        self.changedColorCordsArray.append((rect.left, rect.top, rect.width, rect.height))

    def cleanScreen(self):

        self.worldMapScreenSurface.fill(self.screenColor, (0, 0, self.width, self.height))
        self.plotsScreenSurfaceObjsRect = []

    def getWorldMapScreenSurface(self):
        return self.worldMapScreenSurface

