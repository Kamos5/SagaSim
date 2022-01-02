import pygame

from UI.Utils.Fonts import Fonts
from UI.Utils.Label import Label


class HelpScreen:

    def __init__(self, width, height, widthOffSet, heightOffSet, screenPosX, screenPosY):

        self.screenColor = 50, 20, 20
        self.writeLine = 1
        self.width = width
        self.height = height
        self.widthOffSet = widthOffSet
        self.heightOffSet = heightOffSet
        self.font = Fonts()
        self.textFont = self.font.getFont1()
        self.lineHeight = self.font.getLineHeight()
        self.scroll_y = 0
        self.screenPosX = screenPosX
        self.screenPosY = screenPosY

        self.helpScreenSurface = pygame.Surface([self.width, self.height - self.heightOffSet])
        self.helpScreenSurfaceObjsRect = []

    def addHelp(self):

        self.helpLabel = Label("Help", 50, self.lineHeight, self.textFont, True, True, 1)
        self.helpScreenSurfaceObjsRect.append([self.helpScreenSurface.blit(self.helpLabel.localSurface, (self.width * 0.01, 0)), 'Help'])
        self.writeLine = 1

    def cleanScreen(self):

        self.helpScreenSurface.fill(self.screenColor, (0, 0, self.width, self.height))
        self.helpScreenSurfaceObjsRect = []

    def getHelpScreenSurface(self):
        return self.helpScreenSurface