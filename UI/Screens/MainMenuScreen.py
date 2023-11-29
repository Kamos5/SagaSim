
import pygame

from UI.Misc.FloatingRune import FloatingRune
from UI.Utils.Button import Button
from UI.Utils.Fonts import Fonts
from UI.Utils.Label2 import Label2


class MainMenuScreen:

    def __init__(self, width, height, widthOffSet, heightOffSet, screenPosX, screenPosY):
    
        #self.screenColor = (50, 10, 50)
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

        self.runes = []
        self.floatingRune1 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune2 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune3 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune4 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune5 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune6 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune7 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune8 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune9 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune10 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune11 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune12 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune13 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune14 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune15 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune16 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune17 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune18 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune19 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune20 = FloatingRune(self.width, self.height, imageUrl='random')

        # self.runes = [self.floatingRune1, self.floatingRune2, self.floatingRune3, self.floatingRune4, self.floatingRune5, self.floatingRune6, self.floatingRune7, self.floatingRune8, self.floatingRune9, self.floatingRune10,
        #               self.floatingRune11, self.floatingRune12, self.floatingRune13, self.floatingRune14, self.floatingRune15, self.floatingRune16, self.floatingRune17, self.floatingRune18, self.floatingRune19, self.floatingRune20]
        self.runes = [self.floatingRune1, self.floatingRune2]

        self.newWorldButton = Button('New World')
        self.saveWorldButton = Button('New World')
        self.loadWorldButton = Button('New World')
        self.continueButton = Button('Continue')
        self.quitButton = Button('Quit')

        self.rotation = 0
    def moveAndAddRunesToScreen(self, runes):

        for rune in runes:
            rune.movement(runes)
            self.mainMenuScreenSurface.blit(rune.getImage(), rune.getPositions())

    def loadBackground(self, windowSizeX, windowsSizeY):

        sagaSimImg = pygame.image.load('inputFiles\sagasim.jpg')
        sagaSimImg = pygame.transform.scale(sagaSimImg, (windowSizeX, windowsSizeY))
        self.mainMenuScreenSurface.blit(sagaSimImg, (self.screenPosX, self.screenPosY))
        #
        # sagaSimImg = pygame.transform.rotate(sagaSimImg, self.rotation)
        # new_rect = sagaSimImg.get_rect(center=sagaSimImg.get_rect(center=(windowSizeX // 2, windowsSizeY // 2)).center)
        #
        # self.rotation += 1
        self.moveAndAddRunesToScreen(self.runes)

    def showMainMenu(self, world):

        self.writeLine += 1

        self.mainMenuLabel = Label2(f'Saga Simulator', self.titleFont, False, borderSize=1)
        self.mainMenuLabel.setActiveRectColor(150, 50, 150)
        self.mainMenuLabel.setActiveBorderColor(10, 10, 100)
        self.mainMenuScreenSurface.blit(self.mainMenuLabel.localSurface, (self.mainMenuLabel.centerElement(self.width), self.getVerticalPositioning()))

        self.writeLine += 5


        text1 = f'N'
        text2 = f'ew World'
        textColor1 = [text1, (50, 150, 50)]
        textColor2 = [text2, None]

        self.mainMenuLabel2 = Label2(f'New World', self.titleButtonFont, True, borderSize=3, multiColor=True, multiColorText=[textColor1, textColor2])
        self.mainMenuLabel2.setActiveRectColor(10, 50, 100)
        self.mainMenuLabel2.setActiveBorderColor(50, 50, 50)
        self.mainMenuLabel2.changeColorOnHover(self.newWorldButton.getOnHover())
        self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.mainMenuLabel2.localSurface, (self.mainMenuLabel2.centerElement(self.width), self.getVerticalPositioning())), self.newWorldButton])

        self.writeLine += 4

        self.mainMenuLabel3 = Label2(f'Load World', self.titleButtonFont, True, borderSize=3)
        self.mainMenuLabel3.setActiveRectColor(100, 100, 10)
        # Grayout
        self.mainMenuLabel3.setActiveRectColor(50, 50, 50)
        self.mainMenuLabel3.setActiveBorderColor(50, 50, 50)
        self.mainMenuLabel3.changeColorOnHover(self.loadWorldButton.getOnHover())
        self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.mainMenuLabel3.localSurface, (self.mainMenuLabel3.centerElement(self.width), self.getVerticalPositioning())), self.loadWorldButton])

        if world.getGameState().getGameState() != 0:

            self.writeLine += 4

            self.mainMenuLabel4 = Label2(f'Save World', self.titleButtonFont, True, borderSize=3)
            self.mainMenuLabel4.setActiveRectColor(30, 100, 30)
            #Grayout
            self.mainMenuLabel4.setActiveRectColor(50, 50, 50)
            self.mainMenuLabel4.setActiveBorderColor(50, 50, 50)
            self.mainMenuLabel4.changeColorOnHover(self.saveWorldButton.getOnHover())
            self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.mainMenuLabel4.localSurface, (self.mainMenuLabel4.centerElement(self.width), self.getVerticalPositioning())), self.saveWorldButton])

        if world.getGameState().getGameState() != 0:

            self.writeLine += 4

            text1 = f'C'
            text2 = f'ontinue'
            textColor1 = [text1, (50, 150, 50)]
            textColor2 = [text2, None]

            self.mainMenuLabel5 = Label2(f'Continue', self.titleButtonFont, True, borderSize=3, multiColor=True, multiColorText=[textColor1, textColor2])
            self.mainMenuLabel5.setActiveRectColor(100, 30, 100)
            self.mainMenuLabel5.setActiveBorderColor(50, 50, 50)
            self.mainMenuLabel5.changeColorOnHover(self.continueButton.getOnHover())
            self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.mainMenuLabel5.localSurface, (self.mainMenuLabel5.centerElement(self.width), self.getVerticalPositioning())), self.continueButton])


        self.writeLine += 4

        text1 = f'Q'
        text2 = f'uit'
        textColor1 = [text1, (50, 150, 50)]
        textColor2 = [text2, None]

        self.mainMenuLabel6 = Label2(f'Quit', self.titleButtonFont, True, borderSize=3, multiColor=True, multiColorText=[textColor1, textColor2])
        self.mainMenuLabel6.setActiveRectColor(100, 10, 10)
        self.mainMenuLabel6.setActiveBorderColor(50, 50, 50)
        self.mainMenuLabel6.changeColorOnHover(self.quitButton.getOnHover())
        self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.mainMenuLabel6.localSurface, (self.mainMenuLabel6.centerElement(self.width), self.getVerticalPositioning())), self.quitButton])

        self.writeLine += 8

        self.mainMenuLabel7 = Label2(f'© 2023 by Zbigniew (Kamos5) Fietkiewicz', self.textFont, True, borderSize=2)
        self.mainMenuLabel7.setActiveRectColor(10, 100, 10)
        self.mainMenuLabel7.setActiveBorderColor(20, 20, 20)
        self.mainMenuScreenSurface.blit(self.mainMenuLabel7.localSurface, (self.width * 6 // 8, self.height * 0.9))


    def getVerticalPositioning(self):
        return self.writeLine * (self.lineHeight + 4 * self.labelBoarderDefault + 4 * self.labelMarginVerticalDefault)

    def getMainMenuScreenSurface(self):
        return self.mainMenuScreenSurface

    def cleanScreen(self):

        #self.mainMenuScreenSurface.fill(self.screenColor, (0, 0, self.width, self.height))
        self.mainMenuScreenSurfaceObjsRect = []
        self.resetWriteLine()

    def resetWriteLine(self):

        self.writeLine = 0