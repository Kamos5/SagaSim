import pygame


class TextField:

    def __init__(self, w, h, font, focused=False, borderSize=2):

        self.localSurface = pygame.Surface([w, h])
        self.x = 0
        self.y = 0
        self.w = w
        self.h = h
        self.font = font
        self.inactiveRectColor = 200, 200, 200
        self.activeRectColor = 240, 240, 240
        self.rectColor = self.inactiveRectColor
        self.textColor = 20, 20, 20
        self.inactiveBorderColor = 150, 150, 0
        self.activeBorderColor = 100, 100, 0
        self.borderColor = self.inactiveBorderColor
        self.borderSize = borderSize
        self.focused = focused

        if not self.focused:
            self.rectColor = self.inactiveRectColor
        else:
            self.rectColor = self.activeRectColor
            self.borderColor = self.activeBorderColor
        self.text = ''
        self.set()

    def set(self):

        self.addRect()
        self.setInitText()

    def addRect(self):
        self.border = pygame.draw.rect(self.localSurface, self.borderColor, (self.x, self.y, self.w, self.h))
        self.rect = pygame.draw.rect(self.localSurface, self.rectColor, (self.x+self.borderSize, self.y+self.borderSize, self.w-2*self.borderSize, self.h-2*self.borderSize))

    def setInitText(self):

        textSurface = self.font.render(self.text, True, self.textColor)
        self.localSurface.blit(textSurface, (self.x+self.borderSize*2, self.y))

    def getText(self):
        return self.text

    def setText(self, text):
        self.text = text
        self.addRect()
        textSurface = self.font.render(self.text, True, self.textColor)
        self.localSurface.blit(textSurface, (self.x+self.borderSize*2, self.y))

    def addText(self, text):
        self.text = self.text + text
        self.addRect()
        textSurface = self.font.render(self.text, True, self.textColor)
        self.localSurface.blit(textSurface, (self.x+self.borderSize*2, self.y))

    def activate(self):
        self.focused = True
        self.rectColor = self.activeRectColor
        self.borderColor = self.activeBorderColor
        self.addRect()
        textSurface = self.font.render(self.text, True, self.textColor)
        self.localSurface.blit(textSurface, (self.x+self.borderSize*2, self.y))

    def deactivate(self):
        self.focused = False
        self.rectColor = self.inactiveRectColor
        self.borderColor = self.inactiveBorderColor
        self.addRect()
        textSurface = self.font.render(self.text, True, self.textColor)
        self.localSurface.blit(textSurface, (self.x+self.borderSize*2, self.y))