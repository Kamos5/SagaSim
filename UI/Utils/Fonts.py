import pygame


class Fonts:

    def __init__(self):

        self.lineHeight = 20
        self.font1 = pygame.font.SysFont("calibri", self.lineHeight)
        self.font2 = pygame.font.SysFont("calibri", self.lineHeight)

    def getFont1(self):
        return self.font1

    def getFont2(self):
        return self.font2

    def getLineHeight(self):
        return self.lineHeight