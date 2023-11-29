﻿import pygame

import Utils


class FloatingRune:

    def __init__(self, screenWidth, screenHeight, imageUrl = None, startingXCord = -1, startingYCord=-1, startingHorizontalDirection = False, startingVerticalDirection=False, speed=5, randomDirections = True):

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
        if randomDirections:
            self.horizontalDirection = Utils.randomBool()
            self.verticalDirection = Utils.randomBool()
        else:
            self.horizontalDirection = startingHorizontalDirection  #false left, true right
            self.verticalDirection = startingVerticalDirection  #false up, true down
        self.speed = speed
        self.maxXWidth = screenWidth-self.imageXSize
        self.maxYWidth = screenHeight-self.imageYSize
        self.xPos = self.startingXPos + self.xPosOffset
        self.yPos = self.startingYPos + self.yPosOffset

    def getImageXSize(self):
        return self.imageXSize

    def getImageYSize(self):
        return self.imageYSize

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

    def movement(self, runes):

        switchtedHor = False
        switchtedVer = False

        # left
        isAllowed, conflictWith = self.checkLeft(runes)
        if isAllowed and not self.getHorizontalDirection():
            self.increaseXPosOffset(-self.getSpeed())
            self.updateXYPos()
        else:
            if not self.getHorizontalDirection() and not switchtedHor and not switchtedVer:
                self.changeHorizontalDirection()
                for rune in conflictWith:
                    rune.changeHorizontalDirection()
                    switchtedHor = True
        # right
        isAllowed, conflictWith = self.checkRight(runes)
        if isAllowed and self.getHorizontalDirection():
            self.increaseXPosOffset(self.getSpeed())
            self.updateXYPos()
        else:
            if self.getHorizontalDirection() and not switchtedHor and not switchtedVer:
                self.changeHorizontalDirection()
                for rune in conflictWith:
                    rune.changeHorizontalDirection()
                    switchtedHor = True

        # up
        isAllowed, conflictWith = self.checkUp(runes)
        if isAllowed and not self.getVerticalDirection():
            self.increaseYPosOffset(-self.getSpeed())
            self.updateXYPos()
        else:
            if not self.getVerticalDirection() and not switchtedVer and not switchtedHor:
                self.changeVerticalDirection()
                for rune in conflictWith:
                    rune.changeVerticalDirection()
                    switchtedVer = True

        # down
        isAllowed, conflictWith = self.checkDown(runes)
        if isAllowed and self.getVerticalDirection():
            self.increaseYPosOffset(self.getSpeed())
            self.updateXYPos()
        else:
            if self.getVerticalDirection() and not switchtedVer and not switchtedHor:
                self.changeVerticalDirection()
                for rune in conflictWith:
                    rune.changeVerticalDirection()
                    switchtedVer = True

        # if self.getStartingXPos() + self.getXPosOffset() > 0 and not self.getHorizontalDirection():
        #     self.increaseXPosOffset(-self.getSpeed())
        # if self.getStartingXPos() + self.getXPosOffset() <= 0:
        #     self.changeHorizontalDirection()
        #     self.increaseXPosOffset(self.getSpeed())
        # if self.getStartingXPos() + self.getXPosOffset() < self.getMaxXWidth() and self.getHorizontalDirection():
        #     self.increaseXPosOffset(self.getSpeed())
        # if self.getStartingXPos() + self.getXPosOffset() >= self.getMaxXWidth():
        #     self.changeHorizontalDirection()
        #     self.increaseXPosOffset(-self.getSpeed())

        # if self.getStartingYPos() + self.getYPosOffset() > 0 and not self.getVerticalDirection():
        #     self.increaseYPosOffset(-self.getSpeed())
        # if self.getStartingYPos() + self.getYPosOffset() <= 0:
        #     self.changeVerticalDirection()
        #     self.increaseYPosOffset(self.getSpeed())
        # if self.getStartingYPos() + self.getYPosOffset() < self.getMaxYWidth() and self.getVerticalDirection():
        #     self.increaseYPosOffset(self.getSpeed())
        # if self.getStartingYPos() + self.getYPosOffset() >= self.getMaxYWidth():
        #     self.changeVerticalDirection()
        #     self.increaseYPosOffset(-self.getSpeed())


    def checkLeft(self, runes):
        isAllowed = True
        conflictWith = []
        selfXPos, selfYPos = self.getPositions()
        for rune in runes:
            if selfXPos - self.getSpeed() <= 0:
                isAllowed &= False
                continue
            if rune == self:
                continue
            else:
                runeXPos, runeYPos = rune.getPositions()
                #moving left
                if not self.getHorizontalDirection():
                    if selfXPos - self.getSpeed() >= runeXPos + rune.getImageXSize() or (selfYPos > runeYPos + rune.getImageYSize() or selfYPos + self.getImageYSize() < runeYPos) or selfXPos + self.imageXSize < runeXPos:
                        isAllowed &= True
                    elif (selfXPos <= runeXPos + rune.getImageXSize() and selfXPos >= runeXPos) or (selfXPos + self.getImageXSize() >= runeXPos and selfXPos + self.getImageXSize() <= runeXPos + rune.getImageXSize()):
                        isAllowed &= True
                    else:
                        isAllowed &= False
                        conflictWith.append(rune)
        return isAllowed, conflictWith

    def checkRight(self, runes):
        isAllowed = True
        conflictWith = []
        selfXPos, selfYPos = self.getPositions()
        for rune in runes:
            if selfXPos + self.getSpeed() >= self.getMaxXWidth():
                isAllowed &= False
                continue
            if rune == self:
                continue
            else:
                runeXPos, runeYPos = rune.getPositions()
                #moving right
                if self.getHorizontalDirection():
                    if selfXPos + self.getImageXSize() + self.getSpeed() < runeXPos or (selfYPos > runeYPos + rune.getImageYSize() or selfYPos + self.getImageYSize() < runeYPos) or selfXPos > runeXPos + rune.imageXSize:
                        isAllowed &= True
                    elif (selfXPos <= runeXPos + rune.getImageXSize() and selfXPos >= runeXPos) or (selfXPos + self.getImageXSize() >= runeXPos and selfXPos + self.getImageXSize() <= runeXPos + rune.getImageXSize()):
                        isAllowed &= True
                    else:
                        isAllowed &= False
                        conflictWith.append(rune)
        return isAllowed, conflictWith

    def checkUp(self, runes):
        isAllowed = True
        conflictWith = []
        selfXPos, selfYPos = self.getPositions()
        for rune in runes:
            if selfYPos - self.getSpeed() <= 0:
                isAllowed &= False
                continue
            if rune == self:
                continue
            else:
                runeXPos, runeYPos = rune.getPositions()
                # moving Up
                if not self.getVerticalDirection():
                    if selfYPos - self.getSpeed() >= runeYPos + rune.getImageYSize() or (selfXPos > runeXPos + rune.getImageXSize() or selfXPos + self.getImageXSize() < runeXPos) or selfYPos + self.imageYSize < runeYPos:
                        isAllowed &= True
                    elif (selfYPos <= runeYPos + rune.getImageYSize() and selfYPos >= runeYPos) or (selfYPos + self.getImageYSize() >= runeYPos and selfYPos + self.getImageYSize() <= runeYPos + rune.getImageYSize()):
                        isAllowed &= True
                    else:
                        isAllowed &= False
                        conflictWith.append(rune)
        return isAllowed, conflictWith

    def checkDown(self, runes):
        isAllowed = True
        conflictWith = []
        selfXPos, selfYPos = self.getPositions()
        for rune in runes:
            if selfYPos + self.getSpeed() >= self.getMaxYWidth():
                isAllowed &= False
                continue
            if rune == self:
                continue
            else:
                runeXPos, runeYPos = rune.getPositions()
                #moving down
                if self.getVerticalDirection():
                    if selfYPos + self.getImageYSize() + self.getSpeed() < runeYPos or (selfXPos > runeXPos + rune.getImageXSize() or selfXPos + self.getImageXSize() < runeXPos) or selfYPos > runeYPos + rune.imageYSize:
                        isAllowed &= True
                    elif (selfYPos <= runeYPos + rune.getImageYSize() and selfYPos >= runeYPos) or (selfYPos + self.getImageYSize() >= runeYPos and selfYPos + self.getImageYSize() <= runeYPos + rune.getImageYSize()):
                        isAllowed &= True
                    else:
                        isAllowed &= False
                        conflictWith.append(rune)
        return isAllowed, conflictWith