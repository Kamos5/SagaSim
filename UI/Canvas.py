import pygame

from UI.Screens.HelpScreen import HelpScreen
from UI.Screens.InspectorScreen import InspectorScreen
from UI.Screens.ListScreen import ListScreen
from UI.Screens.NavBarScreen import NavBarScreen
from UI.Utils.TextField import TextField


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

        self.helpWidth = int(self.windowWidth*3/4)
        self.helpHeight = int(self.windowHeight*3/4)
        self.helpWidthOffSet = 0
        self.helpHeightOffSet = 0
        self.helpPosX = int(self.windowWidth/8)
        self.helpPosY = int(self.windowHeight/8)

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

        self.helpScreen = HelpScreen(self.helpWidth, self.helpHeight, self.helpWidthOffSet, self.helpHeightOffSet, self.helpPosX, self.helpPosY)
        self.helpScreenSurface = self.helpScreen.getHelpScreenSurface()

        self.navBarScreen = NavBarScreen(self.navbarWidth, self.navBarHeight, self.navBarWidthOffSet, self.navBarHeightOffSet, self.navBarPosX, self.navBarPosY)
        self.navBarScreenSurface = self.navBarScreen.getNavBarScreenSurface()

        self.listScreen = ListScreen(self.inspectorScreenWidth, self.listScreenHeight, 0, self.listScreenHeightOffSet, self.listScreenPosX, self.listScreenPosY)
        self.listScreenSurface = self.listScreen.getInspectorScreenSurface()

        self.inspectorScreen = InspectorScreen(self.inspectorScreenWidth, self.inspectorScreenHeight, 0, self.inspectorScreenHeightOffSet, self.inspectorScreenPosX, self.inspectorScreenPosY)
        self.inspectorScreenSurface = self.inspectorScreen.getInspectorScreenSurface()

        self.dateTimerObj = None
        self.focusObj = []
        self.lastFocusObj = None

        self.showHelp = False

    def clearCanvas(self):

        self.screen.fill((0, 0, 0), (0, 0, self.windowWidth, self.windowHeight))
        HelpScreen.cleanScreen(self.helpScreen)
        NavBarScreen.cleanScreen(self.navBarScreen)
        ListScreen.cleanScreen(self.listScreen)
        InspectorScreen.cleanScreen(self.inspectorScreen)
        self.dateTimerObj = None
        self.navBarScreenObj = None
        self.listScreenObj = None
        self.detailsScreenObj = None


    def drawStuff(self, world, families):

        if len(self.focusObj) > 0:
            self.lastFocusObj = self.focusObj[len(self.focusObj)-1]

        self.listScreen.resetWriteLine()
        self.listScreen.addRegions(self.lastFocusObj)
        self.helpScreen.resetWriteLine()
        self.inspectorScreen.resetWriteLine()
        self.inspectorScreen.addInspectorLabel()

        self.inspectorScreen.addGeneralInspectorFields(self.lastFocusObj)

        for region in world.getRegions():
            self.listScreen.addRegion(region, self.lastFocusObj)
            if region.getUIExpand():
                for settlement in region.getSettlements():
                    self.listScreen.addSettlement(settlement, self.lastFocusObj)
                    if settlement.getUIExpand():
                        for person in settlement.getResidents():
                            self.listScreen.addSettler(person, self.lastFocusObj)

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

        if self.showHelp:
            self.helpScreen.addHelp()
            self.helpScreenObj = self.screen.blit(self.helpScreenSurface, (self.helpPosX, self.helpPosY))

    def refreshScreen(self, world, families, listScroll_y, detailsScroll_y):

        self.listScreen.setScroll_y(listScroll_y)
        self.inspectorScreen.setScroll_y(detailsScroll_y)
        self.clearCanvas()
        self.navBarScreen.addHelp()
        self.navBarScreen.addDateTimer(world)
        self.drawStuff(world, families)
        pygame.display.update()


    def handleClickOnCollection(self, event):

        #arrays of objects to click
        itemsObjRectArray = [self.listScreen.listScreenSurfaceObjsRect, self.inspectorScreen.inspectorScreenSurfaceObjsRect]
        navBarObjRectArray = [self.navBarScreen.navBarScreenSurfaceObjsRect]

        #arrays of screens with objects to
        itemsObjRectScreensArray = [self.listScreen, self.inspectorScreen]
        navBarObjRectScreensArray = [self.navBarScreen]

        for itemObjRect, itemObjRectScreen in zip(itemsObjRectArray, itemsObjRectScreensArray):
            itemsObj = itemObjRect
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.showHelp is False:
                mouseX, mouseY = pygame.mouse.get_pos()
                for itemObj in itemsObj:
                    if isinstance(itemObj[1], TextField):
                        itemObj[1].deactivate()
                    #To offset position on main screen
                    if itemObj[0].collidepoint([mouseX-itemObjRectScreen.screenPosX, mouseY-itemObjRectScreen.screenPosY]):
                        if hasattr(itemObj[1], 'getUIExpand'):
                            itemObj[1].setUIExpand(not itemObj[1].getUIExpand())
                        self.focusObj.append(itemObj[1])
                        if isinstance(itemObj[1], TextField):
                            itemObj[1].activate()
                        return True

        return False

    def pauseHandle(self, event, pausedPressed):

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if self.navBarScreen.navBarScreenSurfaceObjsRect[0][0].collidepoint(pos):
                if not pausedPressed:
                    pausedPressed = True
                self.showHelp = True

            if self.navBarScreen.navBarScreenSurfaceObjsRect[1][0].collidepoint(pos):
                pausedPressed = not pausedPressed
            if pausedPressed == False:
                self.showHelp = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pausedPressed = not pausedPressed
            if event.key == pygame.K_ESCAPE:
                self.showHelp = False
            if pausedPressed == False:
                self.showHelp = False
            if event.key == pygame.K_q:
                exit()

        return pausedPressed
