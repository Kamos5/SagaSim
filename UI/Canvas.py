import time

import pygame

import SettlementFeatures
from SettlementFeatures import Feature
from Settlements import Settlements
from UI.Screens.FamilyTreeScreen import FamilyTreeScreen
from UI.Screens.HelpScreen import HelpScreen
from UI.Screens.LoadingMenuScreen import LoadingScreen
from UI.Screens.MainMenuScreen import MainMenuScreen
from UI.Screens.WorldMapScreen import WorldMapScreen
from UI.Screens.InspectorScreen import InspectorScreen
from UI.Screens.ListScreen import ListScreen
from UI.Screens.NavBarScreen import NavBarScreen
from UI.Screens.PlotsScreen import PlotsScreen
from UI.Utils.Button import Button
from UI.Utils.DropDownList import DropDownList
from UI.Utils.TextField import TextField


class Canvas:

    windowWidth = 1920 # 1366
    windowHeight = 1080 # 768

    drawObject = None

    def __init__(self):

        self.redrawScreen()

    def redrawScreen(self):

        self.navbarWidth = self.windowWidth
        self.navBarHeight = 38
        self.navBarWidthOffSet = 0
        self.navBarHeightOffSet = 5
        self.navBarPosX = 0
        self.navBarPosY = 0

        self.mainMenuWidth = int(self.windowWidth)
        self.mainMenuHeight = int(self.windowHeight)
        self.mainMenuWidthOffSet = 0
        self.mainMenuHeightOffSet = 0
        self.mainMenuPosX = 0
        self.mainMenuPosY = 0

        self.loadingWidth = int(self.windowWidth)
        self.loadingHeight = int(self.windowHeight)
        self.loadingWidthOffSet = 0
        self.loadingHeightOffSet = 0
        self.loadingPosX = 0
        self.loadingPosY = 0

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

        self.mainMenuScreen = MainMenuScreen(self.mainMenuWidth, self.mainMenuHeight, self.mainMenuWidthOffSet, self.mainMenuHeightOffSet, self.mainMenuPosX, self.mainMenuPosY)
        self.mainMenuScreenSurface = self.mainMenuScreen.getMainMenuScreenSurface()

        self.loadingScreen = LoadingScreen(self.loadingWidth, self.loadingHeight, self.loadingWidthOffSet, self.loadingHeightOffSet, self.loadingPosX, self.loadingPosY)
        self.loadingScreenSurface = self.loadingScreen.getLoadingScreenSurface()

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
        self.showMenu = True

        self.showFamilies = False

    def changeCanvasSize(self):

        self.windowHeight = self.windowHeight*2
        self.redrawScreen()


    def cleanCanvas(self):
        self.screen.fill((0, 0, 0), (0, 0, self.windowWidth, self.windowHeight))

    def refreshCanvas(self):
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

    def drawMainMenu(self, world):

        self.mainMenuScreen.cleanScreen()
        self.mainMenuScreen.loadBackground(self.windowWidth, self.windowHeight)
        if self.mainMenuScreen.showMenuFlag:
            self.mainMenuScreen.showMainMenu(world)
        if self.mainMenuScreen.showNamingMenuFlag:
            self.mainMenuScreen.showNamingMenu(world)
        self.mainMenuScreenObj = self.screen.blit(self.mainMenuScreenSurface, (self.mainMenuPosX, self.mainMenuPosY))
        pygame.display.update()

    def drawStuff(self, world, isPausedPressed=False):

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
            for listScreenButton in self.listScreen.getListScreenButtons():
                if region == listScreenButton.getButtonName() and listScreenButton.getIsActive():
                    self.listScreen.addProvinces(region, self.lastFocusObj)
                    for province in region.getProvinces():
                        self.listScreen.addProvince(province, self.lastFocusObj)
                        for listScreenButton2 in self.listScreen.getListScreenButtons():
                            if province == listScreenButton2.getButtonName() and listScreenButton2.getIsActive():
                                for settlement in province.getSettlements():
                                    self.listScreen.addSettlement(settlement, self.lastFocusObj)
                                    for listScreenButton3 in self.listScreen.getListScreenButtons():
                                        if settlement == listScreenButton3.getButtonName() and listScreenButton3.getIsActive():
                                            self.filterBasedOnParamSettler(settlement.getResidents(), self.listScreen)

        self.listScreen.addFamilies(world.getFamilies())
        if self.listScreen.showFamiliesButton.getIsActive():
            for family in world.getFamilies():
                self.listScreen.addFamily(family, self.lastFocusObj)
                for listScreenButton in self.listScreen.getListScreenButtons():
                    if family == listScreenButton.getButtonName() and listScreenButton.getIsActive():
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
            self.worldMapScreen.addMap(self.lastFocusObj, world)
            self.worldMapScreenObj = self.screen.blit(self.worldMapScreenSurface, (self.worldMapPosX, self.worldMapPosY))

        if self.showPlots:
            self.plotsScreen.addHeaderPlot(self.lastFocusObj, world)
            self.plotsScreenObj = self.screen.blit(self.plotsScreenSurface, (self.plotsPosX, self.plotsPosY))

        if self.showFamilyScreen:
            self.familyTreeScreen.addTree(self.showFamilyObj, self.showUpTree, self.showDownTree)
            self.familyTreeScreenObj = self.screen.blit(self.familyTreeScreenSurface, (self.familyTreePosX, self.familyTreePosY))

        if isPausedPressed:
            pauseBorderColor = (100, 0, 0)
            self.screen.fill(pauseBorderColor, (0, 0, self.windowWidth, 3))
            self.screen.fill(pauseBorderColor, (0, 0, 3, self.windowHeight))
            self.screen.fill(pauseBorderColor, (self.windowWidth-3, 0, self.windowWidth, self.windowHeight))
            self.screen.fill(pauseBorderColor, (0, self.windowHeight-3, self.windowWidth, self.windowHeight))

    def refreshScreen(self, world, listScroll_y, detailsScroll_y, familyTreeScroll_y, isPausedPressed=False):

        if self.showMenu:
            self.mainMenuScreen.cleanScreen()
            if self.mainMenuScreen.showMenuFlag:
                self.mainMenuScreen.showMainMenu(world)
            if self.mainMenuScreen.showNamingMenuFlag:
                self.mainMenuScreen.showNamingMenu(world)

        if not self.showMenu:
            self.listScreen.setScroll_y(listScroll_y)
            self.inspectorScreen.setScroll_y(detailsScroll_y)
            self.familyTreeScreen.setScroll_y(familyTreeScroll_y)
            self.refreshCanvas()
            self.navBarScreen.addMenuButton()
            self.navBarScreen.addHelpButton()
            self.navBarScreen.addPlotsButton()
            self.navBarScreen.addWorldMapButton()
            self.navBarScreen.addGameSpeedCounter(world)
            self.navBarScreen.addDateTimer(world)
            if isPausedPressed:
                self.navBarScreen.addPausedIndicator()
            self.drawStuff(world, isPausedPressed)
        pygame.display.update()

    def handleClickOnCollection(self, event, pausedPressed, gameState, worldObj):

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

        if self.showMenu:
            itemsObjRectArray = [self.mainMenuScreen.mainMenuScreenSurfaceObjsRect]
            itemsObjRectScreensArray = [self.mainMenuScreen]

        for itemObjRect, itemObjRectScreen in zip(itemsObjRectArray, itemsObjRectScreensArray):
            itemsObj = itemObjRect
            if self.showPlots is False and self.showHelp is False and self.showFamilyScreen is False and self.showWorldMap is False:
                self.showDownTree = False
                self.showUpTree = False
                mouseX, mouseY = pygame.mouse.get_pos()
                for itemObj in itemsObj:

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.mainMenuScreen.dropDownCultureButton.resetActiveStatus()
                        self.mainMenuScreen.dropDownRegionButton.resetActiveStatus()
                        self.mainMenuScreen.dropDownProvinceButton.resetActiveStatus()
                        self.mainMenuScreen.dropDownSettlementButton.resetActiveStatus()
                        self.mainMenuScreen.dropDownFamilyNameButton.resetActiveStatus()
                        self.mainMenuScreen.dropDownGenderButton.resetActiveStatus()
                        self.mainMenuScreen.dropDownFirstNameButton.resetActiveStatus()

                    if isinstance(itemObj[1], Button):
                        itemObj[1].resetOnHover()

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if isinstance(itemObj[1], TextField):
                              itemObj[1].deactivate()

                    #To offset position on main screen
                    if itemObj[0].collidepoint([mouseX-itemObjRectScreen.screenPosX, mouseY-itemObjRectScreen.screenPosY]):

                        if itemObj[1] == self.inspectorScreen.previousButton:
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                if len(self.focusObj) > 1:
                                    self.focusObj.pop(len(self.focusObj) - 1)
                                    return True, pausedPressed, None
                        if itemObj[1] == self.inspectorScreen.familyTreeButton:
                            itemObj[1].setOnHover()
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                if not pausedPressed:
                                    pausedPressed = True
                                self.showFamilyObj = itemObj[1].getButtonObject()
                                self.showFamilyScreen = True
                                return True, pausedPressed, None

                        if itemObj[1] == self.inspectorScreen.favoriteButton:
                            itemObj[1].setOnHover()
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                if itemObj[1].getButtonName() not in self.favorites:
                                    self.favorites.append(itemObj[1].getButtonName())
                                    itemObj[1].changeActiveStatus()
                                    return True, pausedPressed, None
                                if itemObj[1].getButtonName() in self.favorites:
                                    self.favorites.remove(itemObj[1].getButtonName())
                                    itemObj[1].changeActiveStatus()
                                    return True, pausedPressed, None

                        if itemObj[1] == self.mainMenuScreen.dropDownCultureButton or itemObj[1] == self.mainMenuScreen.dropDownRegionButton or itemObj[1] == self.mainMenuScreen.dropDownProvinceButton or itemObj[1] == self.mainMenuScreen.dropDownSettlementButton or itemObj[1] == self.mainMenuScreen.dropDownFamilyNameButton or itemObj[1] == self.mainMenuScreen.dropDownGenderButton or itemObj[1] == self.mainMenuScreen.dropDownFirstNameButton:
                            itemObj[1].setOnHover()
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                itemObj[1].changeActiveStatus()
                                return True, pausedPressed, None

                        if isinstance(itemObj[1], Button) and itemObj[1] in [self.listScreen.allButton, self.listScreen.familyAdultsButton, self.listScreen.familyKidsButton, self.listScreen.employedButton, self.listScreen.unemployedButton, self.listScreen.sickButton, self.listScreen.withLoversButton]:
                            self.listScreen.changeFamilyButtons(itemObj[1], event)

                        buttonClicked = False
                        for button in self.mainMenuScreen.dropDownButtonList:
                            if button.getIsActive():
                                buttonClicked = True
                        if not buttonClicked:  ##TODO FIX NIE DZIALA NAJLEPIEJ

                            if isinstance(itemObj[1], Button) and itemObj[1] == self.mainMenuScreen.newWorldButton:

                                itemObj[1].setOnHover()
                                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                    self.mainMenuScreen.setNamingMenuFlag()

                            if isinstance(itemObj[1], Button) and itemObj[1] == self.mainMenuScreen.quickStartButton:
                                itemObj[1].setOnHover()
                                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                    self.showMenu = False
                                    gameState.changeToInit()
                                    self.mainMenuScreen.setMenuFlag()
                                    return False, True, None

                            if isinstance(itemObj[1], Button) and itemObj[1] == self.mainMenuScreen.createWorldButton:
                                itemObj[1].setOnHover()
                                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                    self.showMenu = False
                                    gameState.changeToInit(self.mainMenuScreen.getChosenNames())
                                    self.mainMenuScreen.setMenuFlag()
                                    return False, True, None

                            if isinstance(itemObj[1], Button) and itemObj[1] == self.mainMenuScreen.returnButton:
                                itemObj[1].setOnHover()
                                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                    self.mainMenuScreen.setMenuFlag()
                                    return False, True, None

                            if isinstance(itemObj[1], Button) and itemObj[1] == self.mainMenuScreen.continueButton:
                                itemObj[1].setOnHover()
                                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                    self.showMenu = False
                                    gameState.changeToSimulation()
                                    return False, True, None

                            if isinstance(itemObj[1], Button) and itemObj[1] == self.mainMenuScreen.quitButton:
                                itemObj[1].setOnHover()
                                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                    pygame.quit()
                                    exit()

                        if isinstance(itemObj[1], Button) and itemObj[1] in self.listScreen.getListScreenButtons():
                            itemObj[1].setOnHover()
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                itemObj[1].changeActiveStatus()
                                if itemObj[1] == self.listScreen.showFamiliesButton:
                                    return True, pausedPressed, None

                        if isinstance(itemObj[1], Button) and itemObj[1] in self.mainMenuScreen.getDropDownDynamicCultureButtons():
                            itemObj[1].setOnHover()
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                self.mainMenuScreen.dropDownCultureSelectLabel.set(itemObj[1].getButtonName().getCultureName())
                                self.mainMenuScreen.dropDownRegionSelectLabel.resetChoice()
                                self.mainMenuScreen.dropDownProvinceSelectLabel.resetChoice()
                                self.mainMenuScreen.dropDownSettlementSelectLabel.resetChoice()
                                self.mainMenuScreen.dropDownFamilyNameSelectLabel.resetChoice()
                                self.mainMenuScreen.dropDownFirstNameSelectLabel.resetChoice()

                        if isinstance(itemObj[1], Button) and itemObj[1] in self.mainMenuScreen.getDropDownDynamicRegionButtons():
                            itemObj[1].setOnHover()
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                self.mainMenuScreen.dropDownRegionSelectLabel.set(itemObj[1].getButtonName())

                        if isinstance(itemObj[1], Button) and itemObj[1] in self.mainMenuScreen.getDropDownDynamicProvinceButtons():
                            itemObj[1].setOnHover()
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                self.mainMenuScreen.dropDownProvinceSelectLabel.set(itemObj[1].getButtonName())

                        if isinstance(itemObj[1], Button) and itemObj[1] in self.mainMenuScreen.getDropDownDynamicSettlementButtons():
                            itemObj[1].setOnHover()
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                self.mainMenuScreen.dropDownSettlementSelectLabel.set(itemObj[1].getButtonName())

                        if isinstance(itemObj[1], Button) and itemObj[1] in self.mainMenuScreen.getDropDownDynamicFamilyNameButtons():
                            itemObj[1].setOnHover()
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                self.mainMenuScreen.dropDownFamilyNameSelectLabel.set(itemObj[1].getButtonName())

                        if isinstance(itemObj[1], Button) and itemObj[1] in self.mainMenuScreen.getDropDownDynamicGenderButtons():
                            itemObj[1].setOnHover()
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                self.mainMenuScreen.dropDownGenderSelectLabel.set(itemObj[1].getButtonName())

                        if isinstance(itemObj[1], Button) and itemObj[1] in self.mainMenuScreen.getDropDownDynamicFirstNameButtons():
                            itemObj[1].setOnHover()
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                self.mainMenuScreen.dropDownFirstNameSelectLabel.set(itemObj[1].getButtonName())

                        if isinstance(itemObj[1], Button) and itemObj[1] in self.inspectorScreen.getInspectorScreenButtons():
                            itemObj[1].setOnHover()
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                itemObj[1].changeActiveStatus()
                                if itemObj[1] == self.inspectorScreen.unemployedResidentsButton:
                                    return True, pausedPressed, None
                                if isinstance(itemObj[1].getButtonName(), SettlementFeatures.Feature):
                                    return True, pausedPressed, None

                        if hasattr(itemObj[1], 'getUIExpand'):
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                itemObj[1].setUIExpand(not itemObj[1].getUIExpand())

                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            if isinstance(itemObj[1], Button):
                                self.focusObj.append(itemObj[1].getButtonName())
                            else:
                                self.focusObj.append(itemObj[1])

                            if isinstance(itemObj[1], Feature):
                                 self.focusObj.pop()

                            if isinstance(itemObj[1], TextField):
                                itemObj[1].activate()

                            return True, pausedPressed, None
            if self.showMenu:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        if self.mainMenuScreen.showMenuFlag:
                            # self.showMenu = False
                            self.mainMenuScreen.setNamingMenuFlag()
                            # gameState.changeToInit()
                            return False, True, None
                        else:
                            continue


                    if gameState.isMenuState() and event.key == pygame.K_c:
                        self.showMenu = False
                        gameState.changeToSimulation()
                        return False, True, None

                    if event.key == pygame.K_s:
                        if self.mainMenuScreen.showNamingMenuFlag:
                            self.showMenu = False
                            gameState.changeToInit()
                            return False, True, None
                        else:
                            continue

                    if event.key == pygame.K_q:
                            pygame.quit()
                            exit()

            if self.showFamilyScreen is True:
                mouseX, mouseY = pygame.mouse.get_pos()
                for itemObj in itemsObj:
                    if isinstance(itemObj[1], Button):
                        itemObj[1].resetOnHover()

                        if itemObj[0].collidepoint([mouseX - itemObjRectScreen.screenPosX, mouseY - itemObjRectScreen.screenPosY]):
                            itemObj[1].setOnHover()
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and itemObj[1] == self.familyTreeScreen.upTreeButton:
                                self.showDownTree = False
                                self.showUpTree = True
                                itemObj[1].changeActiveStatus()

                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and itemObj[1] == self.familyTreeScreen.downTreeButton:
                                self.showUpTree = False
                                self.showDownTree = True
                                itemObj[1].changeActiveStatus()

        if self.showPlots is True:
            for itemObjRect, itemObjRectScreen in zip(itemsObjRectArray, itemsObjRectScreensArray):
                itemsObj = itemObjRect
                mouseX, mouseY = pygame.mouse.get_pos()
                for itemObj in itemsObj:

                    if isinstance(itemObj[1], Button):
                        itemObj[1].resetOnHover()

                    if itemObj[0].collidepoint([mouseX - itemObjRectScreen.screenPosX, mouseY - itemObjRectScreen.screenPosY]):
                        if isinstance(itemObj[1], Button):
                            itemObj[1].setOnHover()
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                self.focusObj.append(itemObj[1])
                                itemObj[1].setActiveStatus()
                                return True, pausedPressed, None

        if self.showWorldMap is True:
            if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 1 or event.button == 3):
                for itemObjRect, itemObjRectScreen in zip(itemsObjRectArray, itemsObjRectScreensArray):
                    itemsObj = itemObjRect
                    mouseX, mouseY = pygame.mouse.get_pos()
                    for itemObj in itemsObj:
                        if itemObj[0].collidepoint([mouseX - itemObjRectScreen.screenPosX, mouseY - itemObjRectScreen.screenPosY]):
                            if isinstance(itemObj[1], Settlements):
                                print("AAA")

            # #burshSize
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_a:
            #         self.worldMapScreen.makeBrushBigger()
            #     if event.key == pygame.K_s:
            #         self.worldMapScreen.changeBrushColor(1)
            #     if event.key == pygame.K_z:
            #         self.worldMapScreen.makeBrushSmaller()
            #     if event.key == pygame.K_x:
            #         self.worldMapScreen.changeBrushColor(3)
        return False, pausedPressed, None

    def pauseHandle(self, event, pausedPressed):

        for navBarObj in self.navBarScreen.navBarScreenSurfaceObjsRect:
            navBarObj[1].resetOnHover()
        pos = pygame.mouse.get_pos()
        if len(self.navBarScreen.navBarScreenSurfaceObjsRect):
            if self.navBarScreen.navBarScreenSurfaceObjsRect[0][0].collidepoint(pos) and not self.showPlots and not self.showFamilyScreen and not self.showHelp and not self.showWorldMap:
                self.navBarScreen.navBarScreenSurfaceObjsRect[0][1].setOnHover()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if not pausedPressed:
                        pausedPressed = True
                    self.showMenu = True

            if self.navBarScreen.navBarScreenSurfaceObjsRect[1][0].collidepoint(pos) and not self.showPlots and not self.showFamilyScreen and not self.showHelp and not self.showWorldMap:
                self.navBarScreen.navBarScreenSurfaceObjsRect[1][1].setOnHover()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if not pausedPressed:
                        pausedPressed = True
                    self.showHelp = True

            if self.navBarScreen.navBarScreenSurfaceObjsRect[2][0].collidepoint(pos) and not self.showPlots and not self.showFamilyScreen and not self.showHelp and not self.showWorldMap:
                self.navBarScreen.navBarScreenSurfaceObjsRect[2][1].setOnHover()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if not pausedPressed:
                        pausedPressed = True
                    self.showPlots = True

            if self.navBarScreen.navBarScreenSurfaceObjsRect[3][0].collidepoint(pos) and not self.showPlots and not self.showFamilyScreen and not self.showHelp and not self.showWorldMap:
                self.navBarScreen.navBarScreenSurfaceObjsRect[3][1].setOnHover()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if not pausedPressed:
                        pausedPressed = True
                    self.showWorldMap = True

            if self.navBarScreen.navBarScreenSurfaceObjsRect[4][0].collidepoint(pos) and not self.showPlots and not self.showFamilyScreen and not self.showHelp and not self.showWorldMap:
                self.navBarScreen.navBarScreenSurfaceObjsRect[4][1].setOnHover()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
                self.showMenu = False
                self.showPlots = False
                self.showWorldMap = False
                if self.showFamilyScreen:
                    self.showFamilyScreen = False
                    self.familyTreeScreen.setScroll_y(0)
            if pausedPressed == False:
                self.showMenu = False
                self.showHelp = False
                self.showPlots = False
                #self.showWorldMap = False
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
            if (len(person.getCurrentDiseases()) > 0 or len(person.getCurrentInjuries()) > 0) and screenList.showSickFlag:
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
            if (len(person.getCurrentDiseases()) > 0 or len(person.getCurrentInjuries()) > 0) and screenList.showSickFlag:
                screenList.addPerson(person, self.lastFocusObj)
                continue
            if len(person.getLovers()) > 0 and screenList.showWithLoversFlag:
                screenList.addPerson(person, self.lastFocusObj)
                continue