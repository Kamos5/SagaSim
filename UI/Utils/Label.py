import pygame
from PIL import ImageFont


class Label:

    def __init__(self, text, w, h, font, clickable=False, focused=False, borderSize=1, textColor = (220, 220, 220)):

        self.localSurface = pygame.Surface([w, h])
        self.x = 0
        self.y = 0
        self.w = w
        self.h = h
        self.font = font
        self.inactiveRectColor = 20, 20, 60
        self.activeRectColor = 100, 0, 0
        self.activeRectColorAlt = 10, 70, 10
        self.rectColor = self.inactiveRectColor
        self.textColor = textColor
        self.inactiveBorderColor = 200, 200, 200
        self.activeBorderColor = 75, 150, 150
        self.borderColor = self.inactiveBorderColor
        self.clickableBorderColor = 0, 200, 0
        self.borderSize = borderSize
        self.focused = focused
        if not self.focused:
            self.rectColor = self.inactiveRectColor
            if clickable:
                self.borderColor = self.clickableBorderColor
            else:
                self.borderColor = self.inactiveBorderColor
        else:
            self.rectColor = self.activeRectColor
            self.borderColor = self.activeBorderColor

        self.text = ''
        self.set(text)

    def set(self, text):
        self.addRect()
        self.addText(text)

    def addRect(self):
        self.border = pygame.draw.rect(self.localSurface, self.borderColor, (self.x, self.y, self.w, self.h))
        self.rect = pygame.draw.rect(self.localSurface, self.rectColor, (self.x+self.borderSize, self.y+self.borderSize, self.w-2*self.borderSize, self.h-2*self.borderSize))

    def addText(self, text):
        textSurface = self.font.render(text, True, self.textColor)
        self.localSurface.blit(textSurface, (self.borderSize*5, self.y))
        self.text = text

    def getText(self):
        return self.text

    def setActiveRectColor(self, r, g, b):
        self.rectColor = (r, g, b)
        self.set(self.text)

    def setInactiveRectColor(self, r, g, b):
        self.rectColor = (r, g, b)
        self.set(self.text)

    def setActiveBorderColor(self, r, g, b):
        self.borderColor = (r, g, b)
        self.set(self.text)

    def setInactiveBorderColor(self, r, g, b):
        self.borderColor = (r, g, b)
        self.set(self.text)

    def getTextSize(self, text, fontSize, fontName):
        font = ImageFont.truetype(fontName, fontSize)
        size = font.getsize(text)
        return size

    def changeColorBasedOnActive(self, flag):
        if flag:
            r, g, b = self.activeRectColorAlt
            self.textColor = 200, 200, 50
        else:
            r, g, b = self.inactiveRectColor
            self.textColor = 220, 220, 220
        self.setActiveRectColor(r, g, b)

    def changeColorOnHover(self, flag):
        r, g, b = self.rectColor
        if flag:
            r, g, b = 200, 200, 200
            self.textColor = 200, 200, 50

        self.setActiveRectColor(r, g, b)