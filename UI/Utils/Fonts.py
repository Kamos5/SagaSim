import pygame


class Fonts:

    def __init__(self):

        self.lineHeight = 20
        self.helpLineHeight = 25
        self.font1 = pygame.font.SysFont("calibri", self.lineHeight)
        self.font2 = pygame.font.SysFont("calibri", self.lineHeight)
        self.helpFont = pygame.font.SysFont("calibri", 25)

    def getFont1(self):
        return self.font1

    def getFont2(self):
        return self.font2

    def getHelpFont(self):
        return self.helpFont

    def getLineHeight(self):
        return self.lineHeight

    def getHelpLineHeight(self):
        return self.helpLineHeight
