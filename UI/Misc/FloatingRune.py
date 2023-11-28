import pygame

import Utils


class FloatingRune:

    def __init__(self, screenWidth, screenHeight, imageUrl = None, startingXCord = -1, startingYCord=-1, startingHorizontalDirection = False, startingVerticalDirection=False, speed=5):

        if imageUrl is not None:
            if imageUrl == 'random':
                self.image = pygame.image.load(self.getRandomRune())
            else:
                self.image = imageUrl
        else:
                self.image = pygame.image.load('inputFiles\sample2.png')

        self.image = pygame.transform.scale(self.image, (50, 75))
        self.imageXSize, self.imageYSize = self.image.get_size()

        if startingXCord > -1:
            self.startingXPos = startingXCord
        else:
            self.startingXPos = Utils.randomRange(0, screenWidth-self.imageXSize)
        if startingXCord > -1:
            self.startingYPos = startingYCord
        else:
            self.startingYPos = Utils.randomRange(0, screenHeight-self.imageYSize)

        self.xPosOffset = 0
        self.yPosOffset = 0
        self.horizontalDirection = startingHorizontalDirection  #false left, true right
        self.verticalDirection = startingVerticalDirection  #false up, true down
        self.speed = speed
        self.maxXWidth = screenWidth-self.imageXSize
        self.maxYWidth = screenHeight-self.imageYSize
        self.xPos = self.startingXPos + self.xPosOffset
        self.yPos = self.startingYPos + self.yPosOffset

    def getPositions(self):
        return (self.xPos, self.yPos)

    def updateXYPos(self):
        self.xPos = self.startingXPos + self.xPosOffset
        self.yPos = self.startingYPos + self.yPosOffset

    def getRandomRune(self):
        runeNumber = Utils.randomRange(1, 24)
        inputFile = f'inputFiles/runes/{runeNumber}.png'
        return inputFile

    def getImage(self):
        return self.image

    def getMaxXWidth(self):
        return self.maxXWidth

    def getMaxYWidth(self):
        return self.maxYWidth

    def getStartingXPos(self):
        return self.startingXPos

    def getStartingYPos(self):
        return self.startingYPos

    def getXPosOffset(self):
        return self.xPosOffset

    def increaseXPosOffset(self, newXPostOffset):
        self.xPosOffset += newXPostOffset

    def getYPosOffset(self):
        return self.yPosOffset

    def increaseYPosOffset(self, newYPostOffset):
        self.yPosOffset += newYPostOffset

    def getHorizontalDirection(self):
        return self.horizontalDirection

    def changeHorizontalDirection(self):
        self.horizontalDirection = not self.horizontalDirection

    def getVerticalDirection(self):
        return self.verticalDirection

    def changeVerticalDirection(self):
        self.verticalDirection = not self.verticalDirection

    def getSpeed(self):
        return self.speed

    def setSpeed(self, newSpeed):
        self.speed = newSpeed

    def movement(self):

        if self.getStartingXPos() + self.getXPosOffset() > 0 and not self.getHorizontalDirection():
            self.increaseXPosOffset(-self.getSpeed())
        if self.getStartingXPos() + self.getXPosOffset() <= 0:
            self.changeHorizontalDirection()
            self.increaseXPosOffset(self.getSpeed())
        if self.getStartingXPos() + self.getXPosOffset() < self.getMaxXWidth() and self.getHorizontalDirection():
            self.increaseXPosOffset(self.getSpeed())
        if self.getStartingXPos() + self.getXPosOffset() >= self.getMaxXWidth():
            self.changeHorizontalDirection()
            self.increaseXPosOffset(-self.getSpeed())

        if self.getStartingYPos() + self.getYPosOffset() > 0 and not self.getVerticalDirection():
            self.increaseYPosOffset(-self.getSpeed())
        if self.getStartingYPos() + self.getYPosOffset() <= 0:
            self.changeVerticalDirection()
            self.increaseYPosOffset(self.getSpeed())
        if self.getStartingYPos() + self.getYPosOffset() < self.getMaxYWidth() and self.getVerticalDirection():
            self.increaseYPosOffset(self.getSpeed())
        if self.getStartingYPos() + self.getYPosOffset() >= self.getMaxYWidth():
            self.changeVerticalDirection()
            self.increaseYPosOffset(-self.getSpeed())
        self.updateXYPos()
