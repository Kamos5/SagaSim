﻿import Utils


class Province:

    def __init__(self):

        self.name = ''
        self.color = (0, 0, 0)
        self.borderColor = (0, 0, 0)
        self.cords = set()
        self.setRandomColor()
        self.neighbours = set()
        self.provinceType = 'TERRAIN'

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setRandomColor(self):

        r = Utils.randomRange(50, 220)
        g = Utils.randomRange(50, 220)
        b = Utils.randomRange(50, 220)
        self.color = (r, g, b)

    def setColor(self, color):
        self.color = color

    def addCords(self, x, y):
        self.cords.add((x, y))

    def getCords(self):
        return self.cords

    def getColor(self):
        return self.color

    def addNeighbour(self, newNeighbour):

        self.neighbours.add(newNeighbour)

    def getNeighbours(self):
        return self.neighbours

    def getType(self):
        return self.provinceType

    def setType(self, newType):
        self.provinceType = newType