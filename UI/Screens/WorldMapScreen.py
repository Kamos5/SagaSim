import os
import time

import pygame

from UI.Utils.Button import Button
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
        self.map = []
        self.loadedMap = []

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

        self.brushColor = [(20, 220, 20), (20, 20, 220), (220, 20, 20), (220, 220, 20), (20, 220, 220), (220, 20, 220)]
        self.brushColorIndex = 0
        self.changedColorCordsArray = []

        self.brushSize = 1
        self.isLoaded = False

        self.brushFlag = True
        self.eraseFlag = False

    def addMap(self, lastFocusObj):

        self.writeLine += 1

        self.mapLabel = Label2("World Map:", self.textFont, False, True, 2)
        self.mapLabel.setActiveRectColor(20, 20, 20)
        self.mapLabel.setActiveBorderColor(100, 100, 100)

        self.worldMapScreenSurface.blit(self.mapLabel.localSurface, (self.width * 0.10, self.getVerticalPositioning()))

        self.writeLine += 1

        self.brushColorLabel = Label2("Brush Color", self.textFont, True)
        self.brushColorLabel.changeColorBasedOnFlag(self.brushFlag)

        self.worldMapScreenSurfaceObjsRect.append([self.worldMapScreenSurface.blit(self.brushColorLabel.localSurface, (self.width * 0.05, self.getVerticalPositioning())), Button('changeColor')])

        pygame.draw.rect(self.worldMapScreenSurface, self.BORDER_COLOR, [self.width * 0.05 + self.brushColorLabel.w, self.getVerticalPositioning(), self.brushColorLabel.h, self.brushColorLabel.h])
        pygame.draw.rect(self.worldMapScreenSurface, self.brushColor[self.brushColorIndex], [self.width * 0.05 + self.brushColorLabel.w+1, self.getVerticalPositioning()+1, self.brushColorLabel.h-2, self.brushColorLabel.h-2])

        self.eraseLabel = Label2("Erase", self.textFont, True)
        self.eraseLabel.changeColorBasedOnFlag(self.eraseFlag)

        self.worldMapScreenSurfaceObjsRect.append([self.worldMapScreenSurface.blit(self.eraseLabel.localSurface, (self.width * 0.15, self.getVerticalPositioning())), Button('erase')])

        self.saveMapLabel = Label2("Save Map", self.textFont, True)

        self.worldMapScreenSurfaceObjsRect.append([self.worldMapScreenSurface.blit(self.saveMapLabel.localSurface, (self.width * 0.25, self.getVerticalPositioning())), Button('saveMap')])

        self.loadMapLabel = Label2("Load Map", self.textFont, True)

        self.worldMapScreenSurfaceObjsRect.append([self.worldMapScreenSurface.blit(self.loadMapLabel.localSurface, (self.width * 0.35, self.getVerticalPositioning())), Button('loadMap')])

        self.writeLine += 1

        self.brushSizeLabel = Label2("Brush Size", self.textFont, False)
        self.worldMapScreenSurface.blit(self.brushSizeLabel.localSurface, (self.width * 0.05, self.getVerticalPositioning()))

        self.brushSizeDigitLabel = Label2(f'{self.brushSize}', self.textFont, False)
        self.worldMapScreenSurface.blit(self.brushSizeDigitLabel.localSurface, (self.width * 0.05+ self.brushSizeLabel.w, self.getVerticalPositioning()))

        self.writeLine += 3
        if not self.isLoaded:
            self.addDefaultMap()

        else:
            self.addLoadedMap()
        #self.createMap()
        self.modMap()

    def setAllButtonsFalse(self):

        self.brushFlag = False
        self.eraseFlag = False

    def buttonHandling(self, button, eventButton):

        if button.getButtonName() == 'erase':
            self.setAllButtonsFalse()
            self.eraseFlag = True
        if button.getButtonName() == 'changeColor':
            self.setAllButtonsFalse()
            self.brushFlag = True
            self.changeBrushColor(eventButton)
        if button.getButtonName() == 'saveMap':
            self.saveMap()
        if button.getButtonName() == 'loadMap':
            self.loadMap()

    def changeBrushColor(self, eventButton):

        if eventButton == 1:  # left click
            self.brushColorIndex += 1
            if self.brushColorIndex >= len(self.brushColor):
                self.brushColorIndex = 0
        if eventButton == 3:  # right click
            self.brushColorIndex -= 1
            if self.brushColorIndex < 0:
                self.brushColorIndex = len(self.brushColor)-1

    def addLoadedMap(self):

        self.map = []
        for pixel in self.loadedMap:
            color = pixel[2]
            rect = pygame.draw.rect(self.worldMapScreenSurface, self.BORDER_COLOR, [pixel[0][0], pixel[0][1], pixel[0][2], pixel[0][3]])
            rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [pixel[1][0], pixel[1][1], pixel[1][2], pixel[1][3]])
            self.worldMapScreenSurfaceObjsRect.append([rect, rectInner, color])
            self.map.append([rect, rectInner, color])


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
        self.map = []

        for y in range(0, self.mapYSize, chunkSizeXWithBorder):
            for x in range(0, self.mapXSize, chunkSizeYWithBorder):

                rect = pygame.draw.rect(self.worldMapScreenSurface, self.BORDER_COLOR, [x + verticalPadding, y + (self.writeLine * self.lineHeight), chunkSizeXWithBorder, chunkSizeXWithBorder])
                rectInner = pygame.draw.rect(self.worldMapScreenSurface, self.color, [x + verticalPadding+borderChunkSizeX, y + (self.writeLine * self.lineHeight)+borderChunkSizeY, chunkSizeX, chunkSizeY])
                self.worldMapScreenSurfaceObjsRect.append([rect, rectInner, self.color])
                self.map.append([rect, rectInner, self.color])
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
        for changeColorRect, color in self.changedColorCordsArray:
            self.color = color
            x, y, w, h = changeColorRect
            rect = pygame.draw.rect(self.worldMapScreenSurface, self.BORDER_COLOR, [x-1, y-1, w+2, w+2])
            rectInner = pygame.draw.rect(self.worldMapScreenSurface, self.color, [x, y, w, h])
            self.worldMapScreenSurfaceObjsRect.append([rect, rectInner, self.color])
            self.map.append([rect, rectInner, self.color])
        self.color = oldcolor


    def resetWriteLine(self):

        self.writeLine = 0

    def changeColorAfterClick(self, rectBord, rect):

        if self.eraseFlag:
            if self.brushSize % 2 == 1:
                offset = self.brushSize // 2 * 8
            else:
                offset = (self.brushSize // 2 - 1) * 8
            for sizeX in range(self.brushSize):
                for sizeY in range(self.brushSize):
                    for changeColorRect, color in self.changedColorCordsArray:
                        if changeColorRect == (rect.left + sizeX * 8 - offset, rect.top + sizeY * 8 - offset, rect.width, rect.height):
                            self.changedColorCordsArray.remove([(rect.left + sizeX * 8 - offset, rect.top + sizeY * 8 - offset, rect.width, rect.height), color])

        if self.brushFlag:
            color = self.brushColor[self.brushColorIndex]
            if self.brushSize % 2 == 1:
                offset = self.brushSize//2 * 8
            else:
                offset = (self.brushSize//2 - 1) * 8
            for sizeX in range(self.brushSize):
                for sizeY in range(self.brushSize):
                    self.changedColorCordsArray.append([(rect.left+sizeX*8-offset, rect.top+sizeY*8-offset, rect.width, rect.height), color])
                    #self.map.append([(rectBord.left+sizeX*8-offset, rectBord.top++sizeX*8-offset, rectBord.width, rectBord.height), (rect.left+sizeX*8-offset, rect.top+sizeY*8-offset, rect.width, rect.height), color])

    def cleanScreen(self):

        self.worldMapScreenSurface.fill(self.screenColor, (0, 0, self.width, self.height))
        self.worldMapScreenSurfaceObjsRect = []

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

    def getVerticalPositioning(self):
        return self.writeLine * (self.lineHeight + 4 * self.labelBoarderDefault + 4 * self.labelMarginVerticalDefault)

    def saveMap(self):

        f = open("worldMap.txt", "w")
        print(len(self.map))
        for pixelBorder, pixel, color in self.map:
            f.write(f'{color[0]},{color[1]},{color[2]}.{pixelBorder.left},{pixelBorder.top},{pixelBorder.w},{pixelBorder.h}.{pixel.left},{pixel.top},{pixel.w},{pixel.h};')

        f.close()

    def loadMap(self):

        file_exists = os.path.exists('worldMap.txt')

        if file_exists:
            f = open('worldMap.txt', "r")
            pixels = f.readline().split(';')
            self.cleanScreen()
            for dataPack in pixels:
                tempFlag = 0
                splitedDataPack = dataPack.split('.')
                color = self.BORDER_COLOR
                rectData = None
                rectInnerData = None
                for dataInside in splitedDataPack:
                    correctData = dataInside.split(',')
                    if correctData == ['']:
                        break
                    if tempFlag == 0:
                        r, g, b = tuple(correctData)
                        color = (int(r), int(g), int(b))
                    if tempFlag == 1:
                        rectData = [int(correctData[0]), int(correctData[1]), int(correctData[2]), int(correctData[3])]
                    if tempFlag == 2:
                        rectInnerData = [int(correctData[0]), int(correctData[1]), int(correctData[2]), int(correctData[3])]
                    if tempFlag == 2:
                        self.loadedMap.append([rectData, rectInnerData, color])
                    tempFlag += 1

            self.isLoaded = True
            self.changedColorCordsArray = []