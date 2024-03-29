import pygame
from PIL import ImageFont


class Label2:

    def __init__(self, text, font, clickable=False, focused=False, maxWidth = -1, horizontalMargin = 15, verticalMargin = 2, borderSize=1, onlyText = False, fontColor = (220, 220, 220), multiColor=False, multiColorText=[], roundedEdges=False):

        self.onlyText = onlyText
        fontW, fontH = font.size(text)
        self.horizontalMargin = horizontalMargin
        self.verticalMargin = verticalMargin
        w = fontW + 2 * borderSize + 2 * self.horizontalMargin
        if maxWidth > -1:
            w = maxWidth
        h = fontH + 2 * borderSize + 2 * self.verticalMargin
        if not self.onlyText:
            self.localSurface = pygame.Surface([w, h], pygame.SRCALPHA)
        else:
            self.localSurface = pygame.Surface([w, h], pygame.SRCALPHA)
        self.x = 0
        self.y = 0
        self.w = w
        self.h = h

        self.font = font
        self.inactiveRectColor = 20, 20, 60
        self.activeRectColor = 100, 30, 30
        self.activeRectColorAlt = 10, 70, 10
        self.rectColor = self.inactiveRectColor
        self.textColor = fontColor
        self.inactiveBorderColor = 200, 200, 200
        self.activeBorderColor = 75, 150, 150
        self.borderColor = self.inactiveBorderColor
        self.clickableBorderColor = 0, 200, 0
        self.borderSize = borderSize
        self.focused = focused
        self.roundedEdges = roundedEdges
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
        self.multiColorText = multiColorText
        self.multiColor = multiColor

        if not self.multiColor:
            self.set(text)
        else:
            self.setMultiColor(multiColorText)

    def set(self, text):
        if not self.onlyText:
            self.addRect()
        self.addText(text)

    def setMultiColor(self, multiColorText):
        self.addRect()
        self.addMultiColorText(multiColorText)

    def addRect(self):
        if self.roundedEdges:
            self.border = pygame.draw.rect(self.localSurface, self.borderColor, (self.x, self.y, self.w, self.h), 0, 20, 20, 20, 20)
        else:
            self.border = pygame.draw.rect(self.localSurface, self.borderColor, (self.x, self.y, self.w, self.h))
        if self.roundedEdges:
            self.rect = pygame.draw.rect(self.localSurface, self.rectColor, (self.x + self.borderSize, self.y + self.borderSize, self.w - 2 * self.borderSize, self.h - 2 * self.borderSize), 0, 20, 20, 20, 20)
        else:
            self.rect = pygame.draw.rect(self.localSurface, self.rectColor, (self.x + self.borderSize, self.y + self.borderSize, self.w - 2 * self.borderSize, self.h - 2 * self.borderSize))

    def addText(self, text):
        textSurface = self.font.render(text, True, self.textColor)
        self.localSurface.blit(textSurface, (self.horizontalMargin+self.borderSize, self.verticalMargin+self.borderSize))
        self.text = text

    def addMultiColorText(self, multiColorText):
        offset = 0
        newText = ''

        for text in multiColorText:
            if text[1] == None:
                text[1] = self.textColor
            textSurface = self.font.render(text[0], True, text[1])
            self.localSurface.blit(textSurface, (self.horizontalMargin+self.borderSize+offset, self.verticalMargin+self.borderSize))
            offset += textSurface.get_width()
            newText += text[0] + ''

        self.text = newText.strip()

    def getText(self):
        if not self.multiColor:
            return self.text
        else:
            return self.multiColorText

    def setActiveRectColor(self, r, g, b):
        self.rectColor = (r, g, b)
        if not self.multiColor:
            self.set(self.text)
        else:
            self.setMultiColor(self.multiColorText)

    def setInactiveRectColor(self, r, g, b):
        self.rectColor = (r, g, b)
        if not self.multiColor:
            self.set(self.text)
        else:
            self.setMultiColor(self.multiColorText)

    def setActiveBorderColor(self, r, g, b):
        self.borderColor = (r, g, b)
        if not self.multiColor:
            self.set(self.text)
        else:
            self.setMultiColor(self.multiColorText)

    def setInactiveBorderColor(self, r, g, b):
        self.borderColor = (r, g, b)
        if not self.multiColor:
            self.set(self.text)
        else:
            self.setMultiColor(self.multiColorText)

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

    def centerElement(self, screenWidth):
        return screenWidth * 0.5 - (self.w / 2)

    def changeColorOnHover(self, flag):
        r, g, b = self.rectColor
        if flag:
            r, g, b = r+20, g+20, b+20
            self.textColor = 200, 200, 50

        self.setActiveRectColor(r, g, b)

    def makeTextGivenColor(self, r, g, b):
        self.textColor = r, g, b

        self.set(self.text)