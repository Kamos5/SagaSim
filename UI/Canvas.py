import time

import pygame

from SettlementFeatures import Feature
from UI.Screens.FamilyTreeScreen import FamilyTreeScreen
from UI.Screens.HelpScreen import HelpScreen
from UI.Screens.WorldMapScreen import WorldMapScreen
from UI.Screens.InspectorScreen import InspectorScreen
from UI.Screens.ListScreen import ListScreen
from UI.Screens.NavBarScreen import NavBarScreen
from UI.Screens.PlotsScreen import PlotsScreen
from UI.Utils.Button import Button
from UI.Utils.TextField import TextField


class Canvas:

    windowWidth = 1920 # 1366
    windowHeight = 1080 # 768

    def __init__(self):

        self.redrawScreen()

    def redrawScreen(self):

        self.navbarWidth = self.windowWidth
        self.navBarHeight = 28
        self.navBarWidthOffSet = 0
        self.navBarHeightOffSet = 0
        self.navBarPosX = 0
        self.navBarPosY = 0

        self.helpWidth = int(self.windowWidth*3/4)
        self.helpHeight = int(self.windowHeight*3/4)
        self.helpWidthOffSet = 0
        self.helpHeightOffSet = 0
        self.helpPosX = int(self.windowWidth/8)
        self.helpPosY = int(self.windowHeight/8)

        self.worldMapWidth = int(self.windowWidth*7/8)
        self.worldMapHeight = int(self.windowHeight*15/16)
        self.worldMapWidthOffSet = 0
        self.worldMapHeightOffSet = 0
        self.worldMapPosX = int(self.windowWidth/16)
        self.worldMapPosY = int(self.windowHeight/32)

        self.plotsWidth = int(self.windowWidth*7/8)
        self.plotsHeight = int(self.windowHeight*7/8)
        self.plotsWidthOffSet = 0
        self.plotsHeightOffSet = 0
        self.plotsPosX = int(self.windowWidth/16)
        self.plotsPosY = int(self.windowHeight/16)

        self.listScreenWidth = int(self.windowWidth/2)
        self.listScreenHeight = self.windowHeight
        self.listScreenWidthOffSet = 0
        self.listScreenHeightOffSet = self.navBarHeight
        self.listScreenPosX = 0
        self.listScreenPosY = self.navBarHeight

        self.inspectorScreenWidth = int(self.windowWidth/2)
        self.inspectorScreenHeight = self.windowHeight
        self.inspectorScreenWidthOffSet = 0
        self.inspectorScreenHeightOffSet = self.navBarHeight
        self.inspectorScreenPosX = self.inspectorScreenWidth
        self.inspectorScreenPosY = self.navBarHeight

        self.familyTreeWidth = int(self.windowWidth * 3 / 4)
        self.familyTreeHeight = int(self.windowHeight * 3 / 4)
        self.familyTreeWidthOffSet = 0
        self.familyTreeHeightOffSet = 0
        self.familyTreePosX = int(self.windowWidth / 8)
        self.familyTreePosY = int(self.windowHeight / 8)

        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.RESIZABLE)

        self.helpScreen = HelpScreen(self.helpWidth, self.helpHeight, self.helpWidthOffSet, self.helpHeightOffSet, self.helpPosX, self.helpPosY)
        self.helpScreenSurface = self.helpScreen.getHelpScreenSurface()

        self.worldMapScreen = WorldMapScreen(self.worldMapWidth, self.worldMapHeight, self.worldMapWidthOffSet, self.worldMapHeightOffSet, self.worldMapPosX, self.worldMapPosY)
        self.worldMapScreenSurface = self.worldMapScreen.getWorldMapScreenSurface()

        self.plotsScreen = PlotsScreen(self.plotsWidth, self.plotsHeight, self.plotsWidthOffSet, self.plotsHeightOffSet, self.plotsPosX, self.plotsPosY)
        self.plotsScreenSurface = self.plotsScreen.getPlotsScreenSurface()

        self.navBarScreen = NavBarScreen(self.navbarWidth, self.navBarHeight, self.navBarWidthOffSet, self.navBarHeightOffSet, self.navBarPosX, self.navBarPosY)
        self.navBarScreenSurface = self.navBarScreen.getNavBarScreenSurface()

        self.listScreen = ListScreen(self.inspectorScreenWidth, self.listScreenHeight, 0, self.listScreenHeightOffSet, self.listScreenPosX, self.listScreenPosY)
        self.listScreenSurface = self.listScreen.getInspectorScreenSurface()

        self.inspectorScreen = InspectorScreen(self.inspectorScreenWidth, self.inspectorScreenHeight, 0, self.inspectorScreenHeightOffSet, self.inspectorScreenPosX, self.inspectorScreenPosY)
        self.inspectorScreenSurface = self.inspectorScreen.getInspectorScreenSurface()

        self.familyTreeScreen = FamilyTreeScreen(self.familyTreeWidth, self.familyTreeHeight, self.familyTreeWidthOffSet, self.familyTreeHeightOffSet, self.familyTreePosX, self.familyTreePosY)
        self.familyTreeScreenSurface = self.familyTreeScreen.getFamilyTreeScreenSurface()

        self.dateTimerObj = None
        self.focusObj = []
        self.lastFocusObj = None
        self.favorites = []

        self.showHelp = False
        self.showWorldMap = False
        self.showPlots = False
        self.showFamilyScreen = False
        self.showFamilyObj = None
        self.showUpTree = False
        self.showDownTree = False

        self.showFamilies = False

    def changeCanvasSize(self):

        self.windowHeight = self.windowHeight*2
        self.redrawScreen()


    def clearCanvas(self):

        self.screen.fill((0, 0, 0), (0, 0, self.windowWidth, self.windowHeight))
        HelpScreen.cleanScreen(self.helpScreen)
        WorldMapScreen.cleanScreen(self.worldMapScreen)
        PlotsScreen.cleanScreen(self.plotsScreen)
        NavBarScreen.cleanScreen(self.navBarScreen)
        ListScreen.cleanScreen(self.listScreen)
        InspectorScreen.cleanScreen(self.inspectorScreen)
        FamilyTreeScreen.cleanScreen(self.familyTreeScreen)
        self.dateTimerObj = None
        self.navBarScreenObj = None
        self.listScreenObj = None
        self.detailsScreenObj = None

    def drawStuff(self, world):

        if len(self.focusObj) > 0:
            self.lastFocusObj = self.focusObj[len(self.focusObj)-1]

        self.listScreen.resetWriteLine()
        self.listScreen.addSearch()
        self.listScreen.addRegions(world, self.lastFocusObj)
        self.helpScreen.resetWriteLine()
        self.worldMapScreen.resetWriteLine()
        self.plotsScreen.resetWriteLine()
        self.familyTreeScreen.resetWriteLine()
        self.inspectorScreen.resetWriteLine()
        self.inspectorScreen.addInspectorLabel()

        self.inspectorScreen.addGeneralInspectorFields(self.lastFocusObj)

        for region in world.getRegions():
            self.listScreen.addRegion(region, self.lastFocusObj)
            if region.getUIExpand():
                for settlement in region.getSettlements():
                    self.listScreen.addSettlement(settlement, self.lastFocusObj)
                    if settlement.getUIExpand():
                        self.filterBasedOnParamSettler(settlement.getResidents(), self.listScreen)

        self.listScreen.addFamilies(world.getFamilies())

        if self.showFamilies:
            for family in world.getFamilies():
                self.listScreen.addFamily(family, self.lastFocusObj)
                if family.getUIExpand():
                    self.filterBasedOnParamPerson(family.getAliveMembersList(), self.listScreen)

        self.listScreen.addFavorites()

        for favorite in self.favorites:
            self.listScreen.addFavorite(favorite, self.lastFocusObj)


        #Sequence of drawing
        self.navBarScreenObj = self.screen.blit(self.navBarScreenSurface, (self.navBarPosX, self.navBarPosY))
        self.listScreenObj = self.screen.blit(self.listScreenSurface, (self.listScreenPosX, self.listScreenPosY))
        self.detailsScreenObj = self.screen.blit(self.inspectorScreenSurface, (self.inspectorScreenPosX, self.inspectorScreenPosY))

        if self.showHelp:
            self.helpScreen.addHelp()
            self.helpScreenObj = self.screen.blit(self.helpScreenSurface, (self.helpPosX, self.helpPosY))

        if self.showWorldMap:
            self.worldMapScreen.addMap(self.lastFocusObj)
            self.worldMapScreenObj = self.screen.blit(self.worldMapScreenSurface, (self.worldMapPosX, self.worldMapPosY))

        if self.showPlots:
            self.plotsScreen.addHeaderPlot(self.lastFocusObj, world)
            self.plotsScreenObj = self.screen.blit(self.plotsScreenSurface, (self.plotsPosX, self.plotsPosY))

        if self.showFamilyScreen:
            self.familyTreeScreen.addTree(self.showFamilyObj, self.showUpTree, self.showDownTree)
            self.familyTreeScreenObj = self.screen.blit(self.familyTreeScreenSurface, (self.familyTreePosX, self.familyTreePosY))

    def refreshScreen(self, world, listScroll_y, detailsScroll_y, familyTreeScroll_y):

        self.listScreen.setScroll_y(listScroll_y)
        self.inspectorScreen.setScroll_y(detailsScroll_y)
        self.familyTreeScreen.setScroll_y(familyTreeScroll_y)
        self.clearCanvas()
        self.navBarScreen.addHelpButton()
        self.navBarScreen.addPlotsButton()
        self.navBarScreen.addWorldMapButton()
        self.navBarScreen.addGameSpeedCounter(world)
        self.navBarScreen.addDateTimer(world)
        self.drawStuff(world)
        pygame.display.update()

    def handleClickOnCollection(self, event, pausedPressed):

        #arrays of objects to click
        itemsObjRectArray = [self.listScreen.listScreenSurfaceObjsRect, self.inspectorScreen.inspectorScreenSurfaceObjsRect, self.familyTreeScreen.familyTreeScreenSurfaceObjsRect]
        navBarObjRectArray = [self.navBarScreen.navBarScreenSurfaceObjsRect]

        #arrays of screens with objects to
        itemsObjRectScreensArray = [self.listScreen, self.inspectorScreen, self.familyTreeScreen]
        navBarObjRectScreensArray = [self.navBarScreen]

        if self.showPlots:
            itemsObjRectArray = [self.plotsScreen.plotsScreenSurfaceObjsRect]
            itemsObjRectScreensArray = [self.plotsScreen]

        if self.showWorldMap:
            itemsObjRectArray = [self.worldMapScreen.worldMapScreenSurfaceObjsRect]
            itemsObjRectScreensArray = [self.worldMapScreen]

        for itemObjRect, itemObjRectScreen in zip(itemsObjRectArray, itemsObjRectScreensArray):
            itemsObj = itemObjRect
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.showPlots is False and self.showHelp is False and self.showFamilyScreen is False and self.showWorldMap is False:
                self.showDownTree = False
                self.showUpTree = False
                mouseX, mouseY = pygame.mouse.get_pos()
                for itemObj in itemsObj:
                    if isinstance(itemObj[1], TextField):
                          itemObj[1].deactivate()

                    #To offset position on main screen
                    if itemObj[0].collidepoint([mouseX-itemObjRectScreen.screenPosX, mouseY-itemObjRectScreen.screenPosY]):

                        if isinstance(itemObj[1], Button):
                            self.listScreen.changeFamilyButtons(itemObj[1].getButtonName())

                        if itemObj[1] == 'Favorite' and itemObj[2] not in self.favorites:
                            self.favorites.append(itemObj[2])
                            itemObj[2].isInFavorite = True
                            return True, pausedPressed
                        if itemObj[1] == 'Favorite' and itemObj[2] in self.favorites:
                            self.favorites.remove(itemObj[2])
                            itemObj[2].isInFavorite = False
                            return True, pausedPressed
                        if itemObj[1] == 'showFamilies':
                            self.showFamilies = not self.showFamilies
                        if itemObj[1] == 'FamilyTree':
                            if not pausedPressed:
                                pausedPressed = True
                            self.showFamilyObj = itemObj[2]
                            self.showFamilyScreen = True
                            return True, pausedPressed
                        if hasattr(itemObj[1], 'getUIExpand'):
                            itemObj[1].setUIExpand(not itemObj[1].getUIExpand())
                        self.focusObj.append(itemObj[1])

                        if isinstance(itemObj[1], Feature):
                             self.focusObj.pop()

                        if isinstance(itemObj[1], TextField):
                            itemObj[1].activate()

                        return True, pausedPressed

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.showFamilyScreen is True:
                mouseX, mouseY = pygame.mouse.get_pos()
                for itemObj in itemsObj:
                    if itemObj[0].collidepoint([mouseX - itemObjRectScreen.screenPosX, mouseY - itemObjRectScreen.screenPosY]):
                        if itemObj[1] == 'UpTree':
                            self.showDownTree = False
                            self.showUpTree = True
                        if itemObj[1] == 'DownTree':
                            self.showUpTree = False
                            self.showDownTree = True

        if self.showPlots is True:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for itemObjRect, itemObjRectScreen in zip(itemsObjRectArray, itemsObjRectScreensArray):
                    itemsObj = itemObjRect
                    mouseX, mouseY = pygame.mouse.get_pos()
                    for itemObj in itemsObj:
                        if itemObj[0].collidepoint([mouseX - itemObjRectScreen.screenPosX, mouseY - itemObjRectScreen.screenPosY]):
                            self.focusObj.append(itemObj[1])
                            if isinstance(itemObj[1], Button):
                                itemObj[1].changeActiveStatus()
                                return True, pausedPressed

        if self.showWorldMap is True:
            if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 1 or event.button == 3):
                for itemObjRect, itemObjRectScreen in zip(itemsObjRectArray, itemsObjRectScreensArray):
                    itemsObj = itemObjRect
                    mouseX, mouseY = pygame.mouse.get_pos()
                    for itemObj in itemsObj:
                        if itemObj[0].collidepoint([mouseX - itemObjRectScreen.screenPosX, mouseY - itemObjRectScreen.screenPosY]):
                            if not isinstance(itemObj[1], Button):
                                self.worldMapScreen.changeColorAfterClick(itemObj[0], itemObj[1])
                                return True, pausedPressed
                            else:
                                self.worldMapScreen.buttonHandling(itemObj[1], event.button)
                                return True, pausedPressed
            #burshSize
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.worldMapScreen.makeBrushBigger()
                if event.key == pygame.K_s:
                    self.worldMapScreen.changeBrushColor(1)
                if event.key == pygame.K_z:
                    self.worldMapScreen.makeBrushSmaller()
                if event.key == pygame.K_x:
                    self.worldMapScreen.changeBrushColor(3)
        return False, pausedPressed

    def pauseHandle(self, event, pausedPressed):

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if self.navBarScreen.navBarScreenSurfaceObjsRect[0][0].collidepoint(pos) and not self.showFamilyScreen and not self.showHelp and not self.showWorldMap:
                if not pausedPressed:
                    pausedPressed = True
                self.showHelp = True

            if self.navBarScreen.navBarScreenSurfaceObjsRect[1][0].collidepoint(pos) and not self.showFamilyScreen and not self.showHelp and not self.showWorldMap:
                if not pausedPressed:
                    pausedPressed = True
                self.showPlots = True

            if self.navBarScreen.navBarScreenSurfaceObjsRect[2][0].collidepoint(pos) and not self.showFamilyScreen and not self.showHelp and not self.showWorldMap:
                if not pausedPressed:
                    pausedPressed = True
                self.showWorldMap = True

            if self.navBarScreen.navBarScreenSurfaceObjsRect[3][0].collidepoint(pos) and not self.showFamilyScreen and not self.showHelp and not self.showWorldMap:
                pausedPressed = not pausedPressed
            if pausedPressed == False:
                self.showHelp = False
                self.showPlots = False
                self.showWorldMap = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not self.showFamilyScreen:
                    pausedPressed = not pausedPressed
            if event.key == pygame.K_ESCAPE:
                self.showHelp = False
                self.showPlots = False
                self.showWorldMap = False
                if self.showFamilyScreen:
                    self.showFamilyScreen = False
                    self.familyTreeScreen.setScroll_y(0)
            if pausedPressed == False:
                self.showHelp = False
                self.showPlots = False
                self.showWorldMap = False
            if event.key == pygame.K_q and not self.showHelp and not self.showPlots and not self.showWorldMap and not self.showFamilyScreen:
                exit()


        return pausedPressed

    def filterBasedOnParamSettler(self, collection, screenList):

        for person in collection:
            if screenList.showFamilyAllFlag:
                screenList.addSettler(person, self.lastFocusObj)
                continue
            if person.getAge() >= 15 and screenList.showFamilyAdultsFlag:
                screenList.addSettler(person, self.lastFocusObj)
                continue
            if person.getAge() < 15 and screenList.showFamilyKidsFlag:
                screenList.addSettler(person, self.lastFocusObj)
                continue
            if person.getOccupation() is not None and screenList.showEmployedFlag:
                screenList.addSettler(person, self.lastFocusObj)
                continue
            if person.getOccupation() is None and screenList.showUnemployedFlag:
                screenList.addSettler(person, self.lastFocusObj)
                continue
            if len(person.getCurrentDiseases()) > 0 and screenList.showSickFlag:
                screenList.addSettler(person, self.lastFocusObj)
                continue
            if len(person.getLovers()) > 0 and screenList.showWithLoversFlag:
                screenList.addSettler(person, self.lastFocusObj)
                continue

    def filterBasedOnParamPerson(self, collection, screenList):

        for person in collection:
            if screenList.showFamilyAllFlag:
                screenList.addPerson(person, self.lastFocusObj)
                continue
            if person.getAge() >= 15 and screenList.showFamilyAdultsFlag:
                screenList.addPerson(person, self.lastFocusObj)
                continue
            if person.getAge() < 15 and screenList.showFamilyKidsFlag:
                screenList.addPerson(person, self.lastFocusObj)
                continue
            if person.getOccupation() is not None and screenList.showEmployedFlag:
                screenList.addPerson(person, self.lastFocusObj)
                continue
            if person.getOccupation() is None and screenList.showUnemployedFlag:
                screenList.addPerson(person, self.lastFocusObj)
                continue
            if len(person.getCurrentDiseases()) > 0 and screenList.showSickFlag:
                screenList.addPerson(person, self.lastFocusObj)
                continue
            if len(person.getLovers()) > 0 and screenList.showWithLoversFlag:
                screenList.addPerson(person, self.lastFocusObj)
                continue