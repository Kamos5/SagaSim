import pygame


class Fonts:

    def __init__(self):

        self.lineHeight = 22
        self.fontSize = 16
        self.titleFontSize = 50
        self.titleButtonFontSize = 40
        self.titleSmallButtonFontSize = 30
        self.titleSmallerButtonFontSize = 22
        self.fontMiniSize = 14
        self.generalFont = "segoeui"
        self.symbolFont = "segoeuisymbol"
        self.helpFontSize = 22
        self.helpLineHeight = 25
        self.plotsFontSize = 22
        self.plotsLineHeight = 25
        self.mainMenuLineHeight = 22
        self.font1 = pygame.font.SysFont(self.generalFont, self.fontSize)
        self.font2 = pygame.font.SysFont(self.generalFont, self.fontSize)
        self.fontTitle = pygame.font.SysFont(self.generalFont, self.titleFontSize)
        self.titleButtonFont = pygame.font.SysFont(self.generalFont, self.titleButtonFontSize)
        self.titleSmallButtonFont = pygame.font.SysFont(self.generalFont, self.titleSmallButtonFontSize)
        self.titleSmallerButtonFont = pygame.font.SysFont(self.generalFont, self.titleSmallerButtonFontSize)
        self.miniFont = pygame.font.SysFont(self.generalFont, self.fontMiniSize)
        self.symbolFont = pygame.font.SysFont(self.symbolFont, self.fontSize)
        self.helpFont = pygame.font.SysFont(self.generalFont, self.helpFontSize)
        self.plotsFont = pygame.font.SysFont(self.generalFont, self.plotsFontSize)

    def getFont1(self):
        return self.font1

    def getFont2(self):
        return self.font2

    def getTitleFont(self):
        return self.fontTitle

    def getTitleButtonFont(self):
        return self.titleButtonFont

    def getTitleSmallButtonFont(self):
        return self.titleSmallButtonFont

    def getTitleSmallerButtonFont(self):
        return self.titleSmallerButtonFont

    def getMiniFont(self):
        return self.miniFont

    def getSymbolFont(self):
        return self.symbolFont

    def getHelpFont(self):
        return self.helpFont

    def getPlotsFont(self):
        return self.plotsFont

    def getGeneralFontType(self):
        return self.generalFont

    def getLineHeight(self):
        return self.lineHeight

    def getHelpLineHeight(self):
        return self.helpLineHeight

    def getPlotsLineHeight(self):
        return self.plotsLineHeight

    def getMainMenuLineHeight(self):
        return self.mainMenuLineHeight
