﻿

class WorldMapObjClass:

    def __init__(self, cords=(), colors=((0, 0, 0), (0, 0, 0)), objectVar=None, isInner = False, outerType = 0):

        self.cordX, self.cordY = cords
        self.borderColor, self.color = colors
        self.objectVar = objectVar
        self.isInner = isInner
        self.outerType = outerType

    def getCordX(self):
        return self.cordX

    def getCordY(self):
        return self.cordY

    def getCords(self):
        return (self.cordX, self.cordY)

    def getBorderColor(self):
        return self.borderColor

    def getColor(self):
        return self.color

    def getColors(self):
        return (self.borderColor, self.color)

    def getObject(self):
        return self.objectVar

    def setIsInner(self, newValue):
        self.isInner = newValue

    def setOuterType(self, type):
        self.outerType = type

    def getOuterType(self):
        return self.outerType
