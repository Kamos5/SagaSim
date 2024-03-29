﻿import random

import Parameters
import Province
import ProvinceNameGenerator as PNG
import Utils
from WorldMapObjClass import WorldMapObjClass


class WorldMap:

    def __init__(self):

        self.x0 = 0
        self.y0 = 0
        self.width = 200
        self.height = 100

        self.numberOfProvinces = Parameters.startingNumberOfRegions * Parameters.provincesPerRegion * 3 // 2
        self.numberOfSeaProvinces = self.numberOfProvinces // 3
        self.seaNeighboursForSeaProvincesParam = 2

        self.worldMapObj = set()
        self.impassibleTerrain = set()

        self.provinces = set()
        self.seaProvinces = set()
        self.landProvinces = set()

    def reset(self):

        self.x0 = 0
        self.y0 = 0
        self.width = 200
        self.height = 100

        self.numberOfProvinces = Parameters.startingNumberOfRegions * Parameters.provincesPerRegion * 3 // 2
        self.numberOfSeaProvinces = self.numberOfProvinces // 3
        self.seaNeighboursForSeaProvincesParam = 2

        self.worldMapObj = set()
        self.impassibleTerrain = set()

        self.provinces = set()
        self.seaProvinces = set()
        self.landProvinces = set()

    def addField(self, worldMapObjClass, weight=0):

        if worldMapObjClass not in self.getWorldMapObj():
            self.worldMapObj.add((worldMapObjClass, weight))
        if worldMapObjClass.getColor() and worldMapObjClass not in self.getImpassibleTerrain():
            self.impassibleTerrain.add(worldMapObjClass.getCords())

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

    def generateProvinces(self, canvas):

        print("Genereting World Map...")
        print("Genereting Provinces...")
        provinceMap = set()
        sortedFlag = False
        cordsUsed = set()
        tempName = 0

        maxX = self.width
        maxY = self.height

        shuffledWidth = random.sample(range(maxX), maxX)
        shuffledHeight = random.sample(range(maxY), maxY)

        while len(provinceMap) < self.numberOfProvinces:
            randomX = Utils.randomRange(0, maxX-1)
            randomY = Utils.randomRange(0, maxY-1)
            if (randomX, randomY) not in cordsUsed:
                province = Province.Province(self)
                province.addCords(randomX, randomY)
                province.setName(tempName)
                tempName += 1
                provinceMap.add(province)
                cordsUsed.add((randomX, randomY))
            if len(provinceMap) == maxX * maxY:
                break

        while not sortedFlag:
            cordX = shuffledWidth[Utils.randomRange(0, maxX-1)]
            cordY = shuffledHeight[Utils.randomRange(0, maxY-1)]
            provinceCandidates = []

            if (cordX, cordY) not in cordsUsed:
                if (cordX, cordY) not in cordsUsed:
                    left = (cordX - 1, cordY)
                    if left in cordsUsed and not cordX == self.x0:
                        pixelToAdd = self.checkWhereCordsWereUsed(left, provinceMap)
                        if pixelToAdd not in provinceCandidates:
                            provinceCandidates.append(pixelToAdd)
                    # RIGHT
                    right = (cordX + 1, cordY)
                    if right in cordsUsed and not cordX == maxX-1:
                        pixelToAdd = self.checkWhereCordsWereUsed(right, provinceMap)
                        if pixelToAdd not in provinceCandidates:
                            provinceCandidates.append(pixelToAdd)
                    # UP
                    up = (cordX, cordY - 1)
                    if up in cordsUsed and not cordY == self.y0:
                        pixelToAdd = self.checkWhereCordsWereUsed(up, provinceMap)
                        if pixelToAdd not in provinceCandidates:
                            provinceCandidates.append(pixelToAdd)
                    # DOWN
                    down = (cordX, cordY + 1)
                    if down in cordsUsed and not cordY == maxY-1:
                        pixelToAdd = self.checkWhereCordsWereUsed(down, provinceMap)
                        if pixelToAdd not in provinceCandidates:
                            provinceCandidates.append(pixelToAdd)

                    if len(provinceCandidates) > 0:
                        provincesWeight = 100
                        lowestProvince = provinceCandidates[0]
                        for province in provinceCandidates:
                            if len(province.getCords()) < provincesWeight:
                                provincesWeight = len(province.getCords())
                                lowestProvince = province

                        lowestProvince.addCords(cordX, cordY)
                        cordsUsed.add((cordX, cordY))

            if len(cordsUsed) == (maxX) * (maxY):
                sortedFlag = True
            #Utils.printPercentDone(len(cordsUsed), ((maxX) * (maxY)))
        self.provinces = set(provinceMap)
        for province in self.provinces:
            province.setMiddleCord()
            province.markInnerCords()
        self.landProvinces = self.provinces - self.seaProvinces
        print("Genereting Provinces Completed!")
        canvas.loadingScreen.provinces = True
        print("Generation Neighbours...")
        self.generateProvinceNeighbours()
        print("Generation Neighbours Completed!")
        print("Generation Seas...")
        self.genereteSeas()
        self.nameSeaProvinces()
        print("Generation Seas Completed!")
        self.generateProvincesMap()
        print("Generation Completed!")

    def checkWhereCordsWereUsed(self, cords, provinceMap):

        for nProveince in provinceMap:
            if cords in nProveince.getCords():
                return nProveince

    def getProvinces(self):
        return self.provinces

    def generateProvincesMap(self):

        for province in self.getProvinces():
            provinceColor = province.getColor()
            provinceBorderColor = provinceColor
            province.checkIfIsland()
            weight = 0
            if province.getType() == 'SEA':
                provinceBorderColor = (10, 60, 90)
                provinceColor = (00, 70, 95)
                province.markInnerCords()
                weight = 1
            for innerTerrytories in province.getInnerCords():
                terrytoryX, terrytoryY, terrytoryType = innerTerrytories
                self.addField(WorldMapObjClass(colors=(provinceBorderColor, provinceColor), cords=(terrytoryX, terrytoryY), objectVar=province, isInner=True, outerType=terrytoryType), weight)

            for outerTerrytories in province.getOuterCords():
                terrytoryX, terrytoryY, terrytoryType = outerTerrytories
                self.addField(WorldMapObjClass(colors=(provinceBorderColor, provinceColor), cords=(terrytoryX, terrytoryY), objectVar=province, isInner=False, outerType=terrytoryType), weight)


    def generateProvinceNeighbours(self):

        maxX = self.width
        maxY = self.height

        for province in self.getProvinces():
            for cordX, cordY in province.getCords():
                left = (cordX - 1, cordY)
                if left not in province.getCords() and not cordX == self.x0:
                    neighbour = self.checkOtherProvincesForCords(left)
                    if neighbour not in province.getNeighbours():
                        province.addNeighbour(neighbour)
                # RIGHT
                right = (cordX + 1, cordY)
                if right not in province.getCords() and not cordX == maxX-1:
                    neighbour = self.checkOtherProvincesForCords(right)
                    if neighbour not in province.getNeighbours():
                        province.addNeighbour(neighbour)
                # UP
                up = (cordX, cordY - 1)
                if up not in province.getCords() and not cordY == self.y0:
                    neighbour = self.checkOtherProvincesForCords(up)
                    if neighbour not in province.getNeighbours():
                        province.addNeighbour(neighbour)
                # DOWN
                down = (cordX, cordY + 1)
                if down not in province.getCords() and not cordY == maxY-1:
                    neighbour = self.checkOtherProvincesForCords(down)
                    if neighbour not in province.getNeighbours():
                        province.addNeighbour(neighbour)

    def checkOtherProvincesForCords(self, cords):

        for province in self.getProvinces():
            if cords in province.getCords():
                return province

    def genereteSeas(self, province=None, numberOfSeaProvinces = None):

        try:
            if numberOfSeaProvinces is None:
                numberOfSeaProvinces = self.numberOfSeaProvinces
            if province is None:
                province = Utils.randomFromCollection(list(self.getProvinces()))
            randomProvince = Utils.randomFromCollection(list(province.getNeighbours()))
            seaNeighbours = 0
            for provinceNeighbour in province.getNeighbours():
                if provinceNeighbour.getType() == 'SEA':
                    seaNeighbours += 1

            if randomProvince not in self.seaProvinces and seaNeighbours <= self.seaNeighboursForSeaProvincesParam:
                self.seaProvinces.add(randomProvince)
                randomProvince.setType('SEA')
                numberOfSeaProvinces -= 1
                if numberOfSeaProvinces > 0:
                    self.genereteSeas(randomProvince, numberOfSeaProvinces)
            else:
                self.genereteSeas(None, numberOfSeaProvinces)
        except RecursionError:
            print("RECURSION ERROR FAILED")
            return

    def nameSeaProvinces(self):

        for sea in self.seaProvinces:
            sea.setName(PNG.randomProvinceSeaName())

