import random
import time

import Province
import Utils


class WorldMap:

    def __init__(self):

        self.x0 = 0
        self.y0 = 0
        self.width = 200
        self.height = 100

        self.numberOfProvinces = 500

        self.worldMapObj = set()
        self.impassibleTerrain = set()

        self.provinces = set()

    def addField(self, borderColor, color=None, x=0, y=0):

        # xCord = len(self.worldMapObj) % self.width
        # yCord = len(self.worldMapObj) // self.width
        if ((x, y), (borderColor, color)) not in self.getWorldMapObj():
            self.worldMapObj.add(((x, y), (borderColor, color)))
        if color == (20, 20, 20) and ((x, y), (borderColor, color)) not in self.getImpassibleTerrain():
            self.impassibleTerrain.add((x, y))

    def resetWorldMapObj(self):
        self.worldMapObj = []

    def getWorldMapObj(self):
        return self.worldMapObj

    def getImpassibleTerrain(self):
        return self.impassibleTerrain

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def generateProvinces(self):

        print("Genereting World Map...")
        provinceMap = set()
        sortedFlag = False
        cordsUsed = set()

        x0 = self.x0
        y0 = self.y0
        maxX = self.width
        maxY = self.height

        shuffledWidth = random.sample(range(maxX+1), maxX+1)
        shuffledHeight = random.sample(range(maxY+1), maxY+1)

        while len(provinceMap) < self.numberOfProvinces:
            randomX = Utils.randomRange(0, maxX-1)
            randomY = Utils.randomRange(0, maxY-1)
            if (randomX, randomY) not in cordsUsed:
                province = Province.Provinve()
                province.addCords(randomX, randomY)
                provinceMap.add(province)
                cordsUsed.add((randomX, randomY))

        while not sortedFlag:
            cordX = shuffledWidth[Utils.randomRange(0, maxX)]
            cordY = shuffledHeight[Utils.randomRange(0, maxY)]
            provinceCandidates = []

            if (cordX, cordY) not in cordsUsed:
                if (cordX, cordY) not in cordsUsed:
                    left = (cordX - 1, cordY)
                    if left in cordsUsed and not cordX == x0:
                        provinceToAdd = self.checkWhereCordsWereUsed(left, provinceMap)
                        if provinceToAdd not in provinceCandidates:
                            provinceCandidates.append(provinceToAdd)
                    # RIGHT
                    right = (cordX + 1, cordY)
                    if right in cordsUsed and not cordX == maxX:
                        provinceToAdd = self.checkWhereCordsWereUsed(right, provinceMap)
                        if provinceToAdd not in provinceCandidates:
                            provinceCandidates.append(provinceToAdd)
                    # UP
                    up = (cordX, cordY - 1)
                    if up in cordsUsed and not cordY == y0:
                        provinceToAdd = self.checkWhereCordsWereUsed(up, provinceMap)
                        if provinceToAdd not in provinceCandidates:
                            provinceCandidates.append(provinceToAdd)
                    # DOWN
                    down = (cordX, cordY + 1)
                    if down in cordsUsed and not cordY == maxY:
                        provinceToAdd = self.checkWhereCordsWereUsed(down, provinceMap)
                        if provinceToAdd not in provinceCandidates:
                            provinceCandidates.append(provinceToAdd)

                    if len(provinceCandidates) > 0:
                        provincesWeight = 100
                        lowestProvince = provinceCandidates[0]
                        for province in provinceCandidates:
                            if len(province.getCords()) < provincesWeight:
                                provincesWeight = len(province.getCords())
                                lowestProvince = province

                        lowestProvince.addCords(cordX, cordY)
                        cordsUsed.add((cordX, cordY))

            if len(cordsUsed) == (maxX + 1) * (maxY + 1):
                sortedFlag = True
            #Utils.printPercentDone(len(cordsUsed), ((maxX + 1) * (maxY + 1)))
        print("Generation Completed!")
        self.provinces = set(provinceMap)
        self.generateProvincesMap()

    def checkWhereCordsWereUsed(self, cords, provinceMap):

        for nProveince in provinceMap:
            if cords in nProveince.getCords():
                return nProveince

    def getProvinces(self):
        return self.provinces

    def generateProvincesMap(self):

        for province in self.getProvinces():
            provinceColor = province.getColor()
            for terrytory in province.getCords():
                provinceX, provinceY = terrytory
                self.addField(provinceColor,  provinceColor, x=provinceX, y=provinceY)