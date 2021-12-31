import pygame


class Label:


    def __init__(self, text, w, h, font, color=''):

        self.localSurface = pygame.Surface([w, h])
        self.x = 0
        self.y = 0
        self.w = w
        self.h = h
        self.font = font
        self.basicRectColor = 50, 150, 50
        self.activeColor = 100, 0, 100
        self.textColor = 255, 255, 255
        if color != 'active':
            self.rectColor = self.basicRectColor
        else:
            self.rectColor = self.activeColor

        self.set(text)

    def set(self, text):

        self.addRect()
        self.addText(text)

    def addRect(self):
        self.rect = pygame.draw.rect(self.localSurface, self.rectColor, (self.x, self.y, self.w, self.h), 1)

    def addText(self, text):
        textSurface = self.font.render(text, True, self.textColor)
        self.localSurface.blit(textSurface, (self.x, self.y))
