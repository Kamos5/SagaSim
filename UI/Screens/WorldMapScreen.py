import os
import time

import pygame

from Province import Province
from Region import Region
from Settlements import Settlements
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
        self.miniTextFont = self.font.getMiniFont()
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

        self.ERASE_COLOR = self.DEFAULT_GRAY_1

        self.GRAY_1 = self.DEFAULT_GRAY_1
        self.GRAY_2 = self.DEFAULT_GRAY_2
        self.BORDER_COLOR = self.DEFAULT_BORDER_COLOR

        self.color = self.GRAY_1

        self.brushColor = [(20, 220, 20), (20, 20, 220), (220, 20, 20), (220, 220, 20), (20, 220, 220), (220, 20, 220), (20, 20, 20)]
        self.brushColorIndex = 0
        self.changedColorCordsArray = []

        self.brushSize = 1
        self.isLoaded = False

        self.brushFlag = True
        self.eraseFlag = False

        self.mapXSize = 1600
        self.mapYSize = 800

        self.chunkSizeXWithBorder = 8
        self.chunkSizeYWithBorder = 8
        self.borderChunkSizeX = 1
        self.borderChunkSizeY = 1
        self.chunkSizeX = self.chunkSizeXWithBorder - 2*self.borderChunkSizeX
        self.chunkSizeY = self.chunkSizeYWithBorder - 2*self.borderChunkSizeY
        self.verticalPadding = 40

    def switchBackgroundColors(self):

        if self.color == self.DEFAULT_GRAY_1:
            self.color = self.DEFAULT_GRAY_2
        elif self.color == self.DEFAULT_GRAY_2:
            self.color = self.DEFAULT_GRAY_1

    def addMap(self, lastFocusObj, world):

        self.writeLine += 1

        self.mapLabel = Label2("World Map:", self.textFont, False, True, 2)
        self.mapLabel.setActiveRectColor(20, 20, 20)
        self.mapLabel.setActiveBorderColor(100, 100, 100)

        self.worldMapScreenSurface.blit(self.mapLabel.localSurface, (self.width * 0.10, self.getVerticalPositioning()))

        # self.writeLine += 1
        #
        # self.brushColorLabel = Label2("Brush Color", self.textFont, True)
        # self.brushColorLabel.changeColorBasedOnFlag(self.brushFlag)
        #
        # self.worldMapScreenSurfaceObjsRect.append([self.worldMapScreenSurface.blit(self.brushColorLabel.localSurface, (self.width * 0.05, self.getVerticalPositioning())), Button('changeColor')])
        #
        # pygame.draw.rect(self.worldMapScreenSurface, self.BORDER_COLOR, [self.width * 0.05 + self.brushColorLabel.w, self.getVerticalPositioning(), self.brushColorLabel.h, self.brushColorLabel.h])
        # pygame.draw.rect(self.worldMapScreenSurface, self.brushColor[self.brushColorIndex], [self.width * 0.05 + self.brushColorLabel.w+1, self.getVerticalPositioning()+1, self.brushColorLabel.h-2, self.brushColorLabel.h-2])
        #
        # self.eraseLabel = Label2("Erase", self.textFont, True)
        # self.eraseLabel.changeColorBasedOnFlag(self.eraseFlag)
        #
        # self.worldMapScreenSurfaceObjsRect.append([self.worldMapScreenSurface.blit(self.eraseLabel.localSurface, (self.width * 0.15, self.getVerticalPositioning())), Button('erase')])
        #
        # self.saveMapLabel = Label2("Save Map", self.textFont, True)
        #
        # self.worldMapScreenSurfaceObjsRect.append([self.worldMapScreenSurface.blit(self.saveMapLabel.localSurface, (self.width * 0.25, self.getVerticalPositioning())), Button('saveMap')])
        #
        # self.loadMapLabel = Label2("Load Map", self.textFont, True)
        #
        # self.worldMapScreenSurfaceObjsRect.append([self.worldMapScreenSurface.blit(self.loadMapLabel.localSurface, (self.width * 0.35, self.getVerticalPositioning())), Button('loadMap')])
        #
        # self.cleanBoardLabel = Label2("Clean Board", self.textFont, True)
        #
        # self.worldMapScreenSurfaceObjsRect.append([self.worldMapScreenSurface.blit(self.cleanBoardLabel.localSurface, (self.width * 0.75, self.getVerticalPositioning())), Button('cleanBoard')])
        #
        # self.writeLine += 1
        #
        # self.brushSizeLabel = Label2("Brush Size", self.textFont, False)
        # self.worldMapScreenSurface.blit(self.brushSizeLabel.localSurface, (self.width * 0.05, self.getVerticalPositioning()))
        #
        # self.brushSizeDigitLabel = Label2(f'{self.brushSize}', self.textFont, False)
        # self.worldMapScreenSurface.blit(self.brushSizeDigitLabel.localSurface, (self.width * 0.05+ self.brushSizeLabel.w, self.getVerticalPositioning()))

        self.writeLine += 5
        # if not self.isLoaded:
        #     # self.addDefaultMap()
        #
        # else:
        #     self.addLoadedMap()
        #self.createMap()
        self.modMap(world)

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
        if button.getButtonName() == 'cleanBoard':
            self.isLoaded = False
            self.changedColorCordsArray = []
            self.cleanScreen()

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
        print(self.loadedMap)
        for pixel in self.loadedMap:
            color = pixel[2]
            borderColor = pixel[3]
            rect = pygame.draw.rect(self.worldMapScreenSurface, borderColor, [pixel[0][0], pixel[0][1], pixel[0][2], pixel[0][3]])
            rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [pixel[1][0], pixel[1][1], pixel[1][2], pixel[1][3]])
            self.worldMapScreenSurfaceObjsRect.append([rect, rectInner, color, borderColor])
            self.map.append([rect, rectInner, color, borderColor])


    def addDefaultMap(self):

        self.map = []

        for y in range(0, self.mapYSize, self.chunkSizeXWithBorder):
            for x in range(0, self.mapXSize, self.chunkSizeYWithBorder):

                rect = pygame.draw.rect(self.worldMapScreenSurface, self.BORDER_COLOR, [x + self.verticalPadding, y + (self.writeLine * self.lineHeight), self.chunkSizeXWithBorder, self.chunkSizeXWithBorder])
                rectInner = pygame.draw.rect(self.worldMapScreenSurface, self.color, [x + self.verticalPadding+self.borderChunkSizeX, y + (self.writeLine * self.lineHeight)+self.borderChunkSizeY, self.chunkSizeX, self.chunkSizeY])
                self.worldMapScreenSurfaceObjsRect.append([rect, rectInner, self.color, self.BORDER_COLOR])
                self.map.append([rect, rectInner, self.color, self.BORDER_COLOR])
                self.switchBackgroundColors()
            self.switchBackgroundColors()


    def modMap(self, world):

        # oldcolor = self.color
        # for changeColorRectBorder, changeColorRect, color, borderColor in self.changedColorCordsArray:
        #     self.color = color
        #     borderColor = borderColor
        #     x, y, w, h = changeColorRect
        #     xB, yB, wB, hB = changeColorRectBorder
        #     rect = pygame.draw.rect(self.worldMapScreenSurface, borderColor, [xB, yB, wB, hB])
        #     rectInner = pygame.draw.rect(self.worldMapScreenSurface, self.color, [x, y, w, h])
        #     self.worldMapScreenSurfaceObjsRect.append([rect, rectInner, self.color, borderColor])
        #     self.map.append([rect, rectInner, self.color, borderColor])
        #
        #     normX, normY = self.convertCordsToNormalized(xB, yB)
        #     for region in world.getRegions():
        #         if borderColor == region.getRegionColor():
        #             region.addRegionTerritory((normX, normY))
        #
        #     world.getWorldMap().addField(borderColor, color, normX, normY)
        #
        # self.color = oldcolor

        forLater = set()
        sortedSet = self.sort(world.getWorldMap().getWorldMapObj())
        regions = set()
        for worldMapObjClass, weight in sortedSet:

            xNorm, yNorm, = worldMapObjClass.getCords()
            borderColor = worldMapObjClass.getBorderColor()

            if worldMapObjClass.getColor() is not None:
                color = worldMapObjClass.getColor()
            else:
                if (xNorm + yNorm) % 2 == 0:
                    color = self.DEFAULT_GRAY_1
                else:
                    color = self.DEFAULT_GRAY_2

            x, y = self.convertCordsFromNormalized(xNorm, yNorm)
            w, h = (self.chunkSizeXWithBorder, self.chunkSizeYWithBorder)
            if worldMapObjClass.isInner:
                rect = pygame.draw.rect(self.worldMapScreenSurface, color, [x, y, w, h])
                rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [x + 1, y + 1, w - 2, h - 2])
            else:
                rect = pygame.draw.rect(self.worldMapScreenSurface, borderColor, [x, y, w, h])
                rectInner = self.returnRectInner(worldMapObjClass, color, x, y, w, h)
            self.worldMapScreenSurfaceObjsRect.append([rect, rectInner, color, borderColor])
            self.map.append([rect, rectInner, color, borderColor])

            if isinstance(worldMapObjClass.getObject(), Province):
                self.showProvinceNamesOnMap(worldMapObjClass)
                if worldMapObjClass.getObject().getRegion() not in regions and worldMapObjClass.getObject().getType() != 'SEA':
                   regions.add(worldMapObjClass.getObject().getRegion())

            if isinstance(worldMapObjClass.getObject(), Settlements):
                self.showCitiesOnMap(worldMapObjClass)

        for region in regions:
            self.showRegionNamesOnMap(region)

    def sort(self, sub_li):

        listSorted = list(sub_li)
        listSorted.sort(key=lambda x: x[1])
        return listSorted

    def showCitiesOnMap(self, object):

        xNorm, yNorm, tNorm = object.getObject().getProvinceCords()
        x, y = self.convertCordsFromNormalized(xNorm, yNorm)
        w, h = (self.chunkSizeXWithBorder, self.chunkSizeYWithBorder)
        color = (20, 20, 20)
        borderColor = (20, 20, 20)
        rect = pygame.draw.rect(self.worldMapScreenSurface, color, [x, y, w, h])
        rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [x + 1, y + 1, w - 2, h - 2])
        self.worldMapScreenSurfaceObjsRect.append([rect, rectInner, color, borderColor])
        self.map.append([rect, rectInner, color, borderColor])
        self.settlementLabel = Label2(f'{object.getObject().getSettlementName()}', self.miniTextFont, onlyText=True, fontColor=color)
        self.worldMapScreenSurface.blit(self.settlementLabel.localSurface, (x-(self.settlementLabel.w//2), y-(self.settlementLabel.h//2)+self.lineHeight))

    def showProvinceNamesOnMap(self, object, isInRegion = False):

        xNorm, yNorm = object.getObject().getMiddleCords()
        x, y = self.convertCordsFromNormalized(xNorm, yNorm)

        # if object.getObject().getRegion() is not None:
        #     regionXNorm, regionYNorm = object.getObject().getRegion().getMiddleCords()
        #     rX, rY = self.convertCordsFromNormalized(regionXNorm, regionYNorm)
        #     pygame.draw.line(self.worldMapScreenSurface, (220, 220, 220), (x, y), (rX, rY), 1)
        color = (20, 20, 20)
        if object.getObject().getType() == 'SEA':
            color = (220, 200, 200)
        else:
            color = object.getObject().getRegion().getRegionColor()
        self.provinceLabel = Label2(f'{object.getObject().getName()}', self.miniTextFont, isInRegion, onlyText=True, fontColor=color)
        self.worldMapScreenSurface.blit(self.provinceLabel.localSurface, (x-(self.provinceLabel.w//2), y-(self.provinceLabel.h//2)))

    def showRegionNamesOnMap(self, object):

        xNorm, yNorm = object.getMiddleCords()
        x, y = self.convertCordsFromNormalized(xNorm, yNorm)

        # if object.getObject().getRegion() is not None:
        #     regionXNorm, regionYNorm = object.getObject().getRegion().getMiddleCords()
        #     rX, rY = self.convertCordsFromNormalized(regionXNorm, regionYNorm)
        #     pygame.draw.line(self.worldMapScreenSurface, (220, 220, 220), (x, y), (rX, rY), 1)

        color = object.getRegionColor()
        self.provinceLabel = Label2(f'{object.getRegionName()}', self.textFont, onlyText=True, fontColor=color)
        self.worldMapScreenSurface.blit(self.provinceLabel.localSurface, (x-(self.provinceLabel.w//2), y-(self.provinceLabel.h//2)))



    def resetWriteLine(self):

        self.writeLine = 0

    def returnRectInner(self, worldMapObjClass, color, x, y, w, h):

        if worldMapObjClass.getOuterType() == 0:  # NO BORDERS  0000 dec 0
            rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [x, y, w, h])
        elif worldMapObjClass.getOuterType() == 8:  # LEFT   1000 dec 8
            rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [x + 1, y, w - 1, h])
        elif worldMapObjClass.getOuterType() == 4:  # RIGHT 0100 dec 4
            rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [x, y, w - 1, h])
        elif worldMapObjClass.getOuterType() == 2:  # UP 0010 dec 2
            rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [x, y + 1, w, h - 1])
        elif worldMapObjClass.getOuterType() == 1:  # DOWN 0001 dec 1
            rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [x, y, w, h - 1])
        elif worldMapObjClass.getOuterType() == 12:  # LEFT+RIGHT 1100 dec 12
            rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [x + 1, y, w - 2, h])
        elif worldMapObjClass.getOuterType() == 3:  # UP+DOWN 0011 dec 3
            rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [x, y + 1, w, h - 2])
        elif worldMapObjClass.getOuterType() == 10:  # LEFT+UP 1010 dec 10
            rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [x + 1, y + 1, w - 1, h - 1])
        elif worldMapObjClass.getOuterType() == 6:  # RIGHT+UP 0110 dec 6
            rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [x, y + 1, w - 1, h - 1])
        elif worldMapObjClass.getOuterType() == 9:  # LEFT+DOWN 1001 dec 9
            rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [x + 1, y, w - 1, h - 1])
        elif worldMapObjClass.getOuterType() == 5:  # RIGHT+DOWN 0101 dec 5
            rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [x, y, w - 1, h - 1])
        elif worldMapObjClass.getOuterType() == 14:  # LEFT+RIGHT+UP 1110 dec 14
            rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [x + 1, y + 1, w - 2, h - 1])
        elif worldMapObjClass.getOuterType() == 13:  # LEFT+RIGHT+DOWN 1101 dec 13
            rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [x + 1, y, w - 2, h - 1])
        elif worldMapObjClass.getOuterType() == 7:  # RIGHT+UP+DOWN 0111 dec 7
            rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [x, y + 1, w - 1, h - 2])
        elif worldMapObjClass.getOuterType() == 11:  # LEFT+UP+DOWN 1011 dec 11
            rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [x + 1, y + 1, w - 1, h - 2])
        elif worldMapObjClass.getOuterType() == 15:  # RIGHT+LEFT+UP+DOWN 1111 dec 15
            rectInner = pygame.draw.rect(self.worldMapScreenSurface, color, [x + 1, y + 1, w - 2, h - 2])

        return rectInner

    def changeColorAfterClick(self, rectBord, rect):

        if self.eraseFlag:
            if self.brushSize % 2 == 1:
                offset = self.brushSize // 2 * 8
            else:
                offset = (self.brushSize // 2 - 1) * 8
            for sizeX in range(self.brushSize):
                for sizeY in range(self.brushSize):
                    for changeColorRectBorder, changeColorRect, color, borderColor in self.map:
                        if (changeColorRect.left, changeColorRect.top, changeColorRect.width, changeColorRect.height) == (rect.left + sizeX * 8 - offset, rect.top + sizeY * 8 - offset, rect.width, rect.height):
                            if color != self.DEFAULT_GRAY_1 and color != self.DEFAULT_GRAY_2:
                                if [(rectBord.left + sizeX * 8 - offset, rectBord.top + sizeY * 8 - offset, rectBord.width, rectBord.height), (rect.left + sizeX * 8 - offset, rect.top + sizeY * 8 - offset, rect.width, rect.height), color, borderColor] in self.changedColorCordsArray:
                                    self.changedColorCordsArray.remove([(rectBord.left + sizeX * 8 - offset, rectBord.top + sizeY * 8 - offset, rectBord.width, rectBord.height),(rect.left + sizeX * 8 - offset, rect.top + sizeY * 8 - offset, rect.width, rect.height), color, borderColor ])

                                if [[changeColorRectBorder.left, changeColorRectBorder.top, changeColorRectBorder.width, changeColorRectBorder.height], [changeColorRect.left, changeColorRect.top, changeColorRect.width, changeColorRect.height], color, borderColor] in self.loadedMap:
                                    self.loadedMap.remove([[changeColorRectBorder.left, changeColorRectBorder.top, changeColorRectBorder.width, changeColorRectBorder.height], [changeColorRect.left, changeColorRect.top, changeColorRect.width, changeColorRect.height], color, borderColor])

        if self.brushFlag:
            color = self.brushColor[self.brushColorIndex]
            #borderColor = (255-color[0],255-color[1],255-color[2])
            borderColor = color
            if self.brushSize % 2 == 1:
                offset = self.brushSize//2 * 8
            else:
                offset = (self.brushSize//2 - 1) * 8
            for sizeX in range(self.brushSize):
                for sizeY in range(self.brushSize):
                    x, y, w, h = rectBord
                    # LIMIT TO BORDER X
                    if sizeX - offset//self.chunkSizeXWithBorder + (x-self.verticalPadding)//self.chunkSizeXWithBorder < 0 or sizeX - offset//self.chunkSizeXWithBorder + (x-self.verticalPadding)//self.chunkSizeXWithBorder > self.mapXSize//self.chunkSizeXWithBorder - 1:
                        continue
                    # LIMIT TO BORDER Y
                    if sizeY - offset//self.chunkSizeYWithBorder + (y-self.writeLine * self.lineHeight)//self.chunkSizeYWithBorder < 0 or sizeY - offset//self.chunkSizeYWithBorder + (y-self.writeLine * self.lineHeight)//self.chunkSizeYWithBorder > self.mapYSize//self.chunkSizeYWithBorder - 1:
                        continue

                    self.changedColorCordsArray.append([(rectBord.left+sizeX*8-offset, rectBord.top+sizeY*8-offset, rectBord.width, rectBord.height),(rect.left+sizeX*8-offset, rect.top+sizeY*8-offset, rect.width, rect.height), color,borderColor])

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

    def convertCordsFromNormalized(self, xNorm, yNorm):

        x = xNorm * self.chunkSizeXWithBorder + self.verticalPadding
        y = yNorm * self.chunkSizeYWithBorder + (self.writeLine * self.lineHeight)

        return x, y

    def convertCordsToNormalized(self, x, y):

        xNorm = (x - self.verticalPadding) // self.chunkSizeYWithBorder
        yNorm = (y - (self.writeLine * self.lineHeight)) // self.chunkSizeYWithBorder

        return xNorm, yNorm

    def saveMap(self):

        f = open("worldMap.txt", "w")
        print(len(self.map))
        for pixelBorder, pixel, color, borderColor in self.map:
            f.write(f'{color[0]},{color[1]},{color[2]}.{borderColor[0]},{borderColor[1]},{borderColor[2]}.{pixelBorder.left},{pixelBorder.top},{pixelBorder.w},{pixelBorder.h}.{pixel.left},{pixel.top},{pixel.w},{pixel.h};')

        f.close()

    def loadMap(self):

        file_exists = os.path.exists('worldMap.txt')

        if file_exists:
            f = open('worldMap.txt', "r")
            pixels = f.readline().split(';')
            self.cleanScreen()
            self.loadedMap = []
            for dataPack in pixels:
                tempFlag = 0
                splitedDataPack = dataPack.split('.')
                color = self.BORDER_COLOR
                colorBorder = color
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
                        rb, gb, bb = tuple(correctData)
                        colorBorder = (int(rb), int(gb), int(bb))
                    if tempFlag == 2:
                        rectData = [int(correctData[0]), int(correctData[1]), int(correctData[2]), int(correctData[3])]
                    if tempFlag == 3:
                        rectInnerData = [int(correctData[0]), int(correctData[1]), int(correctData[2]), int(correctData[3])]
                    if tempFlag == 3:
                        self.loadedMap.append([rectData, rectInnerData, color, colorBorder])
                    tempFlag += 1

            self.isLoaded = True
            self.changedColorCordsArray = []