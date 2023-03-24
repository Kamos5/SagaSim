import pygame


class Fonts:

    def __init__(self):

        self.lineHeight = 22
        self.fontSize = 16
        self.generalFont = "segoeui"
        self.symbolFont = "segoeuisymbol"
        self.helpLineHeight = 25
        self.plotsLineHeight = 25
        self.font1 = pygame.font.SysFont(self.generalFont, self.fontSize)
        self.font2 = pygame.font.SysFont(self.generalFont, self.fontSize)
        self.symbolFont = pygame.font.SysFont(self.symbolFont, self.fontSize)
        self.helpFont = pygame.font.SysFont(self.generalFont, 25)
        self.plotsFont = pygame.font.SysFont(self.generalFont, 25)

    def getFont1(self):
        return self.font1

    def getFont2(self):
        return self.font2

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