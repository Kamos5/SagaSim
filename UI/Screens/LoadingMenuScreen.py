import pygame

from UI.Utils.Fonts import Fonts
from UI.Utils.Label2 import Label2


class LoadingScreen:

    def __init__(self, width, height, widthOffSet, heightOffSet, screenPosX, screenPosY):
    
        self.screenColor = (0, 0, 0)
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

        self.provinces = False

        self.loadingScreenSurface = pygame.Surface([self.width, self.height - self.heightOffSet])
        self.loadingScreenSurfaceObjsRect = []

        self.temp = 0

    def showLoading(self, neighbours=False, seas=False, shuffling=False, worldMap=False):

        self.writeLine += 1

        self.loadingLabel = Label2(f'Loading', self.titleFont, False, borderSize=1)
        self.loadingLabel.setActiveRectColor(50, 50, 50)
        self.loadingLabel.setActiveBorderColor(10, 10, 100)
        self.loadingScreenSurface.blit(self.loadingLabel.localSurface, (self.loadingLabel.centerElement(self.width), self.getVerticalPositioning()))

        self.writeLine += 5

        provincesLoadingLabelText = 'Generating Provinves...'
        if self.provinces:
            provincesLoadingLabelText += 'Done!'

        self.loadingProvincesLabel = Label2(f'{provincesLoadingLabelText}', self.textFont, False, borderSize=1)
        # self.loadingProvincesLabel.setActiveRectColor(50, 50, 50)
        # self.loadingProvincesLabel.setActiveBorderColor(10, 10, 100)
        self.loadingScreenSurface.blit(self.loadingLabel.localSurface, (self.loadingLabel.centerElement(self.width), self.getVerticalPositioning()))
        self.writeLine += 3



    def getVerticalPositioning(self):
        return self.writeLine * (self.lineHeight + 4 * self.labelBoarderDefault + 4 * self.labelMarginVerticalDefault)

    def getLoadingScreenSurface(self):
        return self.loadingScreenSurface

    def cleanScreen(self):

        self.loadingScreenSurface.fill(self.screenColor, (0, 0, self.width, self.height))
        self.loadingScreenSurfaceObjsRect = []
        self.resetWriteLine()

    def resetWriteLine(self):

        self.writeLine = 0