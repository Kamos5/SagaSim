from queue import LifoQueue

import pygame

from UI.InspectorScreen import InspectorScreen
from UI.ListScreen import ListScreen
from UI.NavBarScreen import NavBarScreen


class Canvas:

    def __init__(self):
        self.font1 = pygame.font.SysFont("calibri", 20)
        self.font2 = pygame.font.SysFont("calibri", 20)
        self.windowWidth = 1366
        self.windowHeight = 768

        self.navbarWidth = self.windowWidth
        self.navBarHeight = 20
        self.navBarWidthOffSet = 0
        self.navBarHeightOffSet = 0

        self.inspectorScreenWidth = int(self.windowWidth/2)
        self.inspectorScreenHeight = self.windowHeight
        self.inspectorScreenWidthOffSet = 0
        self.inspectorScreenHeightOffSet = self.navBarHeight

        self.listScreenWidth = int(self.windowWidth/2)
        self.listScreenHeight = self.windowHeight
        self.listScreenWidthOffSet = 0
        self.listScreenHeightOffSet = self.navBarHeight

        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight))

        self.navBarScreen = NavBarScreen(self.navbarWidth, self.navBarHeight, self.navBarWidthOffSet, self.navBarHeightOffSet)
        self.navBarScreenSurface = self.navBarScreen.getNavBarScreenSurface()

        self.listScreen = ListScreen(self.inspectorScreenWidth, self.inspectorScreenHeight, self.inspectorScreenWidthOffSet, self.inspectorScreenHeightOffSet)
        self.listScreenSurface = self.listScreen.getInspectorScreenSurface()

        self.inspectorScreen = InspectorScreen(self.inspectorScreenWidth, self.inspectorScreenHeight, self.inspectorScreenWidthOffSet, self.inspectorScreenHeightOffSet)
        self.inspectorScreenSurface = self.inspectorScreen.getInspectorScreenSurface()

        self.dateTimerObj = None
        self.focusObj = None

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
        if self.focusObj is not None:
            self.inspectorScreen.addGeneralInspectorFields(self.focusObj)

        for region in world.getRegions():
            self.listScreen.addRegion(region, self.focusObj)
            if region.getUIExpand():
                for settlement in region.getSettlements():
                    self.listScreen.addSettlement(settlement, self.focusObj)

        self.listScreen.addFamilies()

        for family in families:
            self.listScreen.addFamily(family, self.focusObj)
            if family.getUIExpand():
                for person in family.getAliveMembersList():
                    self.listScreen.addPerson(person, self.focusObj)

        #Sequence of drawing
        self.navBarScreenObj = self.screen.blit(self.navBarScreenSurface, (0, 0))
        self.listScreenObj = self.screen.blit(self.listScreenSurface, (0, self.navBarHeight))
        self.detailsScreenObj = self.screen.blit(self.inspectorScreenSurface, (int(self.windowWidth / 2), self.navBarHeight))

    def refreshScreen(self, world, families, listScroll_y, detailsScroll_y):

        self.listScreen.setScroll_y(listScroll_y)
        self.inspectorScreen.setScroll_y(detailsScroll_y)
        self.clearCanvas()
        self.navBarScreen.addDateTimer(world)
        self.drawStuff(world, families)
        pygame.display.update()


    def handleClickOnCollection(self, event, itemsObj):

        if itemsObj == 'regionsObjArray':
            itemsObj = self.listScreen.listScreenSurfaceRegionsRect

        if itemsObj == 'familiesObjArray':
            itemsObj = self.listScreen.listScreenSurfaceFamiliesRect

        if itemsObj == 'settlementsObjArray':
            itemsObj = self.listScreen.listScreenSurfaceSettlementsRect

        if itemsObj == 'personObjArray':
            itemsObj = self.listScreen.listScreenSurfacePersonRect

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouseX, mouseY = pygame.mouse.get_pos()
            for itemObj in itemsObj:
                #To offset navBar height
                if itemObj[0].collidepoint([mouseX, mouseY-self.navBarHeight]):
                    if hasattr(itemObj[1], 'getUIExpand'):
                        itemObj[1].setUIExpand(not itemObj[1].getUIExpand())
                    self.focusObj = itemObj[1]
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
