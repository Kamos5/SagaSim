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

        self.brushSize = 1

    def addMap(self):

        self.writeLine += 1

        self.mapLabel = Label2("World Map:", self.textFont, False, True, 2)
        self.mapLabel.setActiveRectColor(20, 20, 20)
        self.mapLabel.setActiveBorderColor(100, 100, 100)

        self.worldMapScreenSurface.blit(self.mapLabel.localSurface, (self.width * 0.10, self.writeLine*self.lineHeight))

        self.writeLine += 5

        self.addDefaultMap()
        self.createMap()
        self.modMap()

    def addDefaultMap(self):


        self.mapXSize = 1600
        self.mapYSize = 800

        chunkSizeXWithBorder = 8
        chunkSizeYWithBorder = 8
        borderChunkSizeX = 1
        borderChunkSizeY = 1
        chunkSizeX = chunkSizeXWithBorder - 2*borderChunkSizeX
        chunkSizeY = chunkSizeYWithBorder - 2*borderChunkSizeY
        verticalPadding = 40

        for y in range(0, self.mapYSize, chunkSizeXWithBorder):
            for x in range(0, self.mapXSize, chunkSizeYWithBorder):

                rect = pygame.draw.rect(self.worldMapScreenSurface, self.BORDER_COLOR, [x + verticalPadding, y + (self.writeLine * self.lineHeight), chunkSizeXWithBorder, chunkSizeXWithBorder])
                rectInner = pygame.draw.rect(self.worldMapScreenSurface, self.color, [x + verticalPadding+borderChunkSizeX, y + (self.writeLine * self.lineHeight)+borderChunkSizeY, chunkSizeX, chunkSizeY])
                self.worldMapScreenSurfaceObjsRect.append([rect, rectInner])
                if self.color == self.GRAY_1:
                    self.color = self.GRAY_2
                else:
                    self.color = self.GRAY_1
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
            self.worldMapScreenSurfaceObjsRect.append([rect, rect])
        self.color = oldcolor

    def resetWriteLine(self):

        self.writeLine = 0

    def changeColorAfterClick(self, rect):

        print(f'AAA {rect}')
        offset = 0
        if self.brushSize % 2 == 1:
            offset = self.brushSize//2 * 5
        else:
            offset = (self.brushSize//2 - 1) * 5
        xCutOff = (rect.left-40)//5
        for sizeX in range(self.brushSize):
            for sizeY in range(self.brushSize):
                # print(xCutOff)
                # print(self.mapXSize//5)
                self.changedColorCordsArray.append((rect.left+sizeX*5-offset, rect.top+sizeY*5-offset, rect.width, rect.height))

    def cleanScreen(self):

        self.worldMapScreenSurface.fill(self.screenColor, (0, 0, self.width, self.height))
        self.plotsScreenSurfaceObjsRect = []

    def getWorldMapScreenSurface(self):
        return self.worldMapScreenSurface

    def makeBrushBigger(self):

        self.brushSize += 1
        if self.brushSize > 20:
            self.brushSize = 20

    def makeBrushSmaller(self):
        self.brushSize -= 1
        if self.brushSize < 1:
            self.brushSize = 1

    def createMap(self):

        w = 6
        h = 6
        dziobakMap = [[100,1],[101,1],[102,1],[103,1],[104,1],[105,1],[104,2],[103,3],[102,4],[101,5],[100,6],[101,6],[102,6],[103,6],[104,6],[105,6]]

        for pair in dziobakMap:
            self.changedColorCordsArray.append((pair[0]*(w+2)+40+1, pair[1]*(h+2) + (self.writeLine * self.lineHeight)+1, w, h))
