import pygame


class Fonts:

    def __init__(self):
        self.font1 = pygame.font.SysFont("calibri", 20)
        self.font2 = pygame.font.SysFont("calibri", 20)

    def getFont1(self):
        return self.font1

    def getFont2(self):
        return self.font2