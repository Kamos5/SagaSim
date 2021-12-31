from queue import LifoQueue

import pygame

from UI.InspectorScreen import InspectorScreen
from UI.ListScreen import ListScreen
from UI.NavBarScreen import NavBarScreen


class Canvas:

    def __init__(self):
        self.windowWidth = 1366
        self.windowHeight = 768

        self.navbarWidth = self.windowWidth
        self.navBarHeight = 20
        self.navBarWidthOffSet = 0
        self.navBarHeightOffSet = 0
        self.navBarPosX = 0
        self.navBarPosY = 0

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

        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight))

        self.navBarScreen = NavBarScreen(self.navbarWidth, self.navBarHeight, self.navBarWidthOffSet, self.navBarHeightOffSet, self.navBarPosX, self.navBarPosY)
        self.navBarScreenSurface = self.navBarScreen.getNavBarScreenSurface()

        self.listScreen = ListScreen(self.inspectorScreenWidth, self.listScreenHeight, 0, self.listScreenHeightOffSet, self.listScreenPosX, self.listScreenPosY)
        self.listScreenSurface = self.listScreen.getInspectorScreenSurface()

        self.inspectorScreen = InspectorScreen(self.inspectorScreenWidth, self.inspectorScreenHeight, 0, self.inspectorScreenHeightOffSet, self.inspectorScreenPosX, self.inspectorScreenPosY)
        self.inspectorScreenSurface = self.inspectorScreen.getInspectorScreenSurface()

        self.dateTimerObj = None
        self.focusObj = []
        self.lastFocusObj = None

    def clearCanvas(self):

        self.screen.fill((0, 0, 0), (0, 0, self.windowWidth, self.windowHeight))
        NavBarScreen.cleanScreen(self.navBarScreen)
        ListScreen.cleanScreen(self.listScreen)
        InspectorScreen.cleanScreen(self.inspectorScreen)
        self.dateTimerObj = None
        self.navBarScreenObj = None
        self.listScreenObj = None
        self.detailsScreenObj = None


    def drawStuff(self, world, families):

        self.listScreen.resetWriteLine()
        self.listScreen.addRegions()
        self.inspectorScreen.resetWriteLine()
        self.inspectorScreen.addInspectorLabel()
        if len(self.focusObj) > 0:
            self.lastFocusObj = self.focusObj[len(self.focusObj)-1]
            self.inspectorScreen.addGeneralInspectorFields(self.lastFocusObj)

        for region in world.getRegions():
            self.listScreen.addRegion(region, self.lastFocusObj)
            if region.getUIExpand():
                for settlement in region.getSettlements():
                    self.listScreen.addSettlement(settlement, self.lastFocusObj)

        self.listScreen.addFamilies()

        for family in families:
            self.listScreen.addFamily(family, self.lastFocusObj)
            if family.getUIExpand():
                for person in family.getAliveMembersList():
                    self.listScreen.addPerson(person, self.lastFocusObj)

        #Sequence of drawing
        self.navBarScreenObj = self.screen.blit(self.navBarScreenSurface, (self.navBarPosX, self.navBarPosY))
        self.listScreenObj = self.screen.blit(self.listScreenSurface, (self.listScreenPosX, self.listScreenPosY))
        self.detailsScreenObj = self.screen.blit(self.inspectorScreenSurface, (self.inspectorScreenPosX, self.inspectorScreenPosY))

    def refreshScreen(self, world, families, listScroll_y, detailsScroll_y):

        self.listScreen.setScroll_y(listScroll_y)
        self.inspectorScreen.setScroll_y(detailsScroll_y)
        self.clearCanvas()
        self.navBarScreen.addDateTimer(world)
        self.drawStuff(world, families)
        pygame.display.update()


    def handleClickOnCollection(self, event):

        #arrays of objects to click
        itemsObjRectArray = [self.listScreen.listScreenSurfaceObjsRect, self.inspectorScreen.inspectorScreenSurfaceObjsRect]
        #arrays of screens with objects to click
        itemsObjRectScreensArray = [self.listScreen, self.inspectorScreen]

        for itemObjRect, itemObjRectScreen in zip(itemsObjRectArray, itemsObjRectScreensArray):
            itemsObj = itemObjRect
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouseX, mouseY = pygame.mouse.get_pos()
                for itemObj in itemsObj:
                    #To offset position on main screen
                    if itemObj[0].collidepoint([mouseX-itemObjRectScreen.screenPosX, mouseY-itemObjRectScreen.screenPosY]):
                        if hasattr(itemObj[1], 'getUIExpand'):
                            itemObj[1].setUIExpand(not itemObj[1].getUIExpand())
                        self.focusObj.append(itemObj[1])
                        return True

        return False

    def pauseHandle(self, event, pausedPressed):

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if self.navBarScreen.listScreenSurfaceTimeRect[0].collidepoint(pos):
                pausedPressed = not pausedPressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pausedPressed = not pausedPressed

        return pausedPressed
