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
        self.textFont = self.font.getHelpFont()
        self.miniTextFont = self.font.getFont2()
        self.lineHeight = self.font.getHelpLineHeight()
        self.scroll_y = 0
        self.screenPosX = screenPosX
        self.screenPosY = screenPosY

        self.helpScreenSurface = pygame.Surface([self.width, self.height - self.heightOffSet])
        self.helpScreenSurfaceObjsRect = []

    def addHelp(self):

        self.helpLabel = Label("Help Menu:", 120, self.lineHeight, self.textFont, False, True, 2)
        self.helpLabel.setActiveRectColor(20, 20, 20)
        self.helpLabel.setActiveBorderColor(100, 10, 10)

        self.helpScreenSurface.blit(self.helpLabel.localSurface, (self.width * 0.10, self.writeLine*self.lineHeight))

        self.writeLine += 3

        self.helpLabel = Label("\"q\" - Quits application", 500, self.lineHeight, self.miniTextFont, False, True, 1)
        self.helpLabel.setActiveRectColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])
        self.helpLabel.setActiveBorderColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])

        self.helpScreenSurface.blit(self.helpLabel.localSurface, (self.width * 0.05, self.writeLine*self.lineHeight))
        self.writeLine += 1

        self.helpLabel = Label("\"space bar\" - pauses/resumes simulation", 500, self.lineHeight, self.miniTextFont, False, True, 1)
        self.helpLabel.setActiveRectColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])
        self.helpLabel.setActiveBorderColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])

        self.helpScreenSurface.blit(self.helpLabel.localSurface, (self.width * 0.05, self.writeLine*self.lineHeight))
        self.writeLine += 1

        self.helpLabel = Label("Year: ", 50, self.lineHeight, self.miniTextFont, False, True, 1)
        self.helpLabel.setActiveRectColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])
        self.helpLabel.setActiveBorderColor(0, 200, 0)
        self.helpLabel.setActiveRectColor(20, 20, 60)

        self.helpScreenSurface.blit(self.helpLabel.localSurface, (self.width * 0.05, self.writeLine * self.lineHeight))

        self.helpLabel = Label(" - clicking pauses/resumes simulation", 500, self.lineHeight, self.miniTextFont, False, True, 1)
        self.helpLabel.setActiveRectColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])
        self.helpLabel.setActiveBorderColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])

        self.helpScreenSurface.blit(self.helpLabel.localSurface, (self.width * 0.10, self.writeLine*self.lineHeight))
        self.writeLine += 1

        self.helpLabel = Label("\"esc\" - closes this window", 500, self.lineHeight, self.miniTextFont, False, True, 1)
        self.helpLabel.setActiveRectColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])
        self.helpLabel.setActiveBorderColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])

        self.helpScreenSurface.blit(self.helpLabel.localSurface, (self.width * 0.05, self.writeLine*self.lineHeight))
        self.writeLine += 1

        self.helpLabel = Label("\"end key\" - goes back to previous focused object", 500, self.lineHeight, self.miniTextFont, False, True, 1)
        self.helpLabel.setActiveRectColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])
        self.helpLabel.setActiveBorderColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])

        self.helpScreenSurface.blit(self.helpLabel.localSurface, (self.width * 0.05, self.writeLine*self.lineHeight))
        self.writeLine += 1

        self.helpLabel = Label("\"backspace\" - removes one letter from search window", 500, self.lineHeight, self.miniTextFont, False, True, 1)
        self.helpLabel.setActiveRectColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])
        self.helpLabel.setActiveBorderColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])

        self.helpScreenSurface.blit(self.helpLabel.localSurface, (self.width * 0.05, self.writeLine * self.lineHeight))
        self.writeLine += 1

        self.helpLabel = Label("\"-\" - slows down simulation", 500, self.lineHeight, self.miniTextFont, False, True, 1)
        self.helpLabel.setActiveRectColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])
        self.helpLabel.setActiveBorderColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])

        self.helpScreenSurface.blit(self.helpLabel.localSurface, (self.width * 0.05, self.writeLine * self.lineHeight))
        self.writeLine += 1

        self.helpLabel = Label("\"+\" - speeds up simulation", 500, self.lineHeight, self.miniTextFont, False, True, 1)
        self.helpLabel.setActiveRectColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])
        self.helpLabel.setActiveBorderColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])

        self.helpScreenSurface.blit(self.helpLabel.localSurface, (self.width * 0.05, self.writeLine * self.lineHeight))
        self.writeLine += 1

        self.helpLabel = Label("  ", 50, self.lineHeight, self.miniTextFont, False, True, 1)
        self.helpLabel.setActiveRectColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])
        self.helpLabel.setActiveBorderColor(0, 200, 0)

        self.helpScreenSurface.blit(self.helpLabel.localSurface, (self.width * 0.05, self.writeLine * self.lineHeight))

        self.helpLabel = Label(" - clickable clickable", 500, self.lineHeight, self.miniTextFont, False, True, 1)
        self.helpLabel.setActiveRectColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])
        self.helpLabel.setActiveBorderColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])

        self.helpScreenSurface.blit(self.helpLabel.localSurface, (self.width * 0.10, self.writeLine * self.lineHeight))
        self.writeLine += 1

        self.helpLabel = Label("  ", 50, self.lineHeight, self.miniTextFont, False, True, 1)
        self.helpLabel.setActiveRectColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])
        self.helpLabel.setActiveBorderColor(200, 200, 200)

        self.helpScreenSurface.blit(self.helpLabel.localSurface, (self.width * 0.05, self.writeLine * self.lineHeight))

        self.helpLabel = Label(" - not clickable object", 500, self.lineHeight, self.miniTextFont, False, True, 1)
        self.helpLabel.setActiveRectColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])
        self.helpLabel.setActiveBorderColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])

        self.helpScreenSurface.blit(self.helpLabel.localSurface, (self.width * 0.10, self.writeLine * self.lineHeight))
        self.writeLine += 1

        self.helpLabel = Label("  ", 50, self.lineHeight, self.miniTextFont, False, True, 1)
        self.helpLabel.setActiveRectColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])
        self.helpLabel.setActiveRectColor(100, 0, 0)
        self.helpLabel.setActiveBorderColor(50, 50, 50)

        self.helpScreenSurface.blit(self.helpLabel.localSurface, (self.width * 0.05, self.writeLine * self.lineHeight))

        self.helpLabel = Label(" - focused object", 500, self.lineHeight, self.miniTextFont, False, True, 1)
        self.helpLabel.setActiveRectColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])
        self.helpLabel.setActiveBorderColor(self.screenColor[0], self.screenColor[1], self.screenColor[2])

        self.helpScreenSurface.blit(self.helpLabel.localSurface, (self.width * 0.10, self.writeLine * self.lineHeight))
        self.writeLine += 1


    def resetWriteLine(self):

        self.writeLine = 1

    def cleanScreen(self):

        self.helpScreenSurface.fill(self.screenColor, (0, 0, self.width, self.height))
        self.helpScreenSurfaceObjsRect = []

    def getHelpScreenSurface(self):
        return self.helpScreenSurface