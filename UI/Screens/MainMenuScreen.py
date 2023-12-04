
import pygame

import Enums
from UI.Misc.FloatingRune import FloatingRune
from UI.Utils.Button import Button
from UI.Utils.DropDownList import DropDownList
from UI.Utils.Fonts import Fonts
from UI.Utils.Label2 import Label2


class MainMenuScreen:

    def __init__(self, width, height, widthOffSet, heightOffSet, screenPosX, screenPosY):
    
        #self.screenColor = (50, 10, 50)
        self.writeLine = 0
        self.width = width
        self.height = height
        self.widthOffSet = widthOffSet
        self.heightOffSet = heightOffSet
        self.font = Fonts()
        self.titleFont = self.font.getTitleFont()
        self.titleButtonFont = self.font.getTitleButtonFont()
        self.titleSmallButtonFont = self.font.getTitleSmallButtonFont()
        self.titleSmallerButtonFont = self.font.getTitleSmallerButtonFont()
        self.textFont = self.font.getFont1()
        self.miniTextFont = self.font.getFont2()
        self.lineHeight = self.font.getMainMenuLineHeight()
        self.scroll_y = 0
        self.screenPosX = screenPosX
        self.screenPosY = screenPosY
        self.labelBoarderDefault = 1
        self.labelMarginHorizontalDefault = 5
        self.labelMarginVerticalDefault = 5

        self.dropDownLabelWidth = 200
        self.mainMenuScreenSurface = pygame.Surface([self.width, self.height - self.heightOffSet])
        self.mainMenuScreenSurfaceObjsRect = []

        self.runes = []
        self.floatingRune1 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune2 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune3 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune4 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune5 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune6 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune7 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune8 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune9 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune10 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune11 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune12 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune13 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune14 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune15 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune16 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune17 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune18 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune19 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune20 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune21 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune22 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune23 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune24 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune25 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune26 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune27 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune28 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune29 = FloatingRune(self.width, self.height, imageUrl='random')
        self.floatingRune30 = FloatingRune(self.width, self.height, imageUrl='random')

        self.runes = [self.floatingRune1, self.floatingRune2, self.floatingRune3, self.floatingRune4, self.floatingRune5, self.floatingRune6, self.floatingRune7, self.floatingRune8, self.floatingRune9, self.floatingRune10,
                      self.floatingRune11, self.floatingRune12, self.floatingRune13, self.floatingRune14, self.floatingRune15, self.floatingRune16, self.floatingRune17, self.floatingRune18, self.floatingRune19, self.floatingRune20,
                      self.floatingRune21, self.floatingRune22, self.floatingRune23, self.floatingRune24, self.floatingRune25, self.floatingRune26, self.floatingRune27, self.floatingRune28, self.floatingRune29, self.floatingRune30]
        # self.runes = [self.floatingRune1, self.floatingRune2]

        self.newWorldButton = Button('New World')
        self.saveWorldButton = Button('Save World')
        self.loadWorldButton = Button('Load World')
        self.continueButton = Button('Continue')
        self.quickStartButton = Button('Quick Start')
        self.createWorldButton = Button('Create World')
        self.dropDownCultureButton = Button('Drop Culture Down')
        self.dropDownRegionButton = Button('Drop Region Down')
        self.dropDownProvinceButton = Button('Drop Province Down')
        self.dropDownSettlementButton = Button('Drop Settlement Down')
        self.dropDownFamilyNameButton = Button('Drop Family Name Down')
        self.dropDownGenderButton = Button('Drop Gender Down')
        self.dropDownFirstNameButton = Button('Drop First Name Down')
        self.dropDownButtonList = [self.dropDownCultureButton, self.dropDownRegionButton, self.dropDownProvinceButton, self.dropDownSettlementButton, self.dropDownFamilyNameButton, self.dropDownGenderButton, self.dropDownFirstNameButton]

        self.quitButton = Button('Quit')
        self.returnButton = Button('Return')
        self.showNamingMenuFlag = False
        self.showMenuFlag = True
        self.dropDownMultiCultureButton = None
        self.dropDownMultiRegionButton = None
        self.dropDownMultiProvinceButton = None
        self.dropDownMultiSettlementButton = None
        self.dropDownMultiFamilyNameButton = None
        self.dropDownMultiGenderButton = None
        self.dropDownMultiFirstNameButton = None

        self.dropDownCultureSelectLabel = DropDownList(self.titleSmallerButtonFont, True, borderSize=2, maxWidth=self.dropDownLabelWidth)
        self.dropDownRegionSelectLabel = DropDownList(self.titleSmallerButtonFont, True, borderSize=2, maxWidth=self.dropDownLabelWidth)
        self.dropDownProvinceSelectLabel = DropDownList(self.titleSmallerButtonFont, True, borderSize=2, maxWidth=self.dropDownLabelWidth)
        self.dropDownSettlementSelectLabel = DropDownList(self.titleSmallerButtonFont, True, borderSize=2, maxWidth=self.dropDownLabelWidth)
        self.dropDownFamilyNameSelectLabel = DropDownList(self.titleSmallerButtonFont, True, borderSize=2, maxWidth=self.dropDownLabelWidth)
        self.dropDownGenderSelectLabel = DropDownList(self.titleSmallerButtonFont, True, borderSize=2, maxWidth=self.dropDownLabelWidth)
        self.dropDownFirstNameSelectLabel = DropDownList(self.titleSmallerButtonFont, True, borderSize=2, maxWidth=self.dropDownLabelWidth)
        self.formSelectedLabels = [self.dropDownCultureSelectLabel, self.dropDownRegionSelectLabel, self.dropDownProvinceSelectLabel, self.dropDownSettlementSelectLabel, self.dropDownFamilyNameSelectLabel, self.dropDownGenderSelectLabel, self.dropDownFirstNameSelectLabel]
        self.defaultTextForDropDown = "-Select-"
        self.regionNames = None
        self.provinceNames = None
        self.familyNames = None
        self.genders = None
        self.firstNames = None
        self.dropDownDynamicCultureList = []
        self.dropDownDynamicRegionList = []
        self.dropDownDynamicProvinceList = []
        self.dropDownDynamicSettlementList = []
        self.dropDownDynamicFamilyNameList = []
        self.dropDownDynamicGenderList = []
        self.dropDownDynamicFirstNameList = []


        self.rotation = 0
    def moveAndAddRunesToScreen(self, runes):

        for rune in runes:
            rune.movement(runes)
            self.mainMenuScreenSurface.blit(rune.getImage(), rune.getPositions())

    def loadBackground(self, windowSizeX, windowsSizeY):

        sagaSimImg = pygame.image.load('inputFiles\sagasim.jpg')
        sagaSimImg = pygame.transform.scale(sagaSimImg, (windowSizeX, windowsSizeY))
        self.mainMenuScreenSurface.blit(sagaSimImg, (self.screenPosX, self.screenPosY))
        #
        # sagaSimImg = pygame.transform.rotate(sagaSimImg, self.rotation)
        # new_rect = sagaSimImg.get_rect(center=sagaSimImg.get_rect(center=(windowSizeX // 2, windowsSizeY // 2)).center)
        #
        # self.rotation += 1
        self.moveAndAddRunesToScreen(self.runes)

    def showNamingMenu(self, world):

        self.writeLine += 1

        self.mainMenuLabel = Label2(f'Saga Simulator', self.titleFont, False, borderSize=1)
        self.mainMenuLabel.setActiveRectColor(150, 50, 150)
        self.mainMenuLabel.setActiveBorderColor(10, 10, 100)
        self.mainMenuScreenSurface.blit(self.mainMenuLabel.localSurface, (self.mainMenuLabel.centerElement(self.width), self.getVerticalPositioning()))

        self.writeLine += 2

        text1 = f'R'
        text2 = f'eturn'
        textColor1 = [text1, (50, 150, 50)]
        textColor2 = [text2, None]
        self.returnLabel = Label2(f'Return', self.titleSmallButtonFont, True, borderSize=3, multiColor=True, multiColorText=[textColor1, textColor2])
        self.returnLabel.setActiveRectColor(100, 40, 40)
        self.returnLabel.setActiveBorderColor(50, 50, 50)
        self.returnLabel.changeColorOnHover(self.returnButton.getOnHover())
        self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.returnLabel.localSurface, (self.returnLabel.centerElement(self.width) - 2 * self.width //6, self.getVerticalPositioning())), self.returnButton])

        text1 = f'Quick '
        text2 = f'S'
        text3 = f'tart'
        textColor1 = [text1, None]
        textColor2 = [text2, (50, 150, 50)]
        textColor3 = [text3, None]

        self.quickStartLabel = Label2(f'Quick Start', self.titleSmallButtonFont, True, borderSize=3, multiColor=True, multiColorText=[textColor1, textColor2, textColor3])
        self.quickStartLabel.setActiveRectColor(40, 100, 40)
        self.quickStartLabel.setActiveBorderColor(50, 50, 50)
        self.quickStartLabel.changeColorOnHover(self.quickStartButton.getOnHover())
        self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.quickStartLabel.localSurface, (self.quickStartLabel.centerElement(self.width), self.getVerticalPositioning())), self.quickStartButton])


        self.createWorldLabel = Label2(f'Create World', self.titleSmallButtonFont, True, borderSize=3)
        self.createWorldLabel.setActiveRectColor(150, 150, 40)
        self.createWorldLabel.setActiveBorderColor(50, 50, 50)
        self.createWorldLabel.changeColorOnHover(self.createWorldButton.getOnHover())
        self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.createWorldLabel.localSurface, (self.createWorldLabel.centerElement(self.width) + 2 * self.width //6, self.getVerticalPositioning())), self.createWorldButton])

        self.writeLine += 2

        self.dropDownCultureLabel = Label2(f'Pick Culture', self.titleSmallerButtonFont, True, borderSize=2, maxWidth=self.dropDownLabelWidth)
        self.dropDownCultureLabel.setActiveRectColor(10, 50, 100)
        self.dropDownCultureLabel.setActiveBorderColor(50, 50, 50)
        self.mainMenuScreenSurface.blit(self.dropDownCultureLabel.localSurface, (self.width // 6, self.getVerticalPositioning()))

        self.dropDownRegionLabel = Label2(f'Pick region', self.titleSmallerButtonFont, True, borderSize=2, maxWidth=self.dropDownLabelWidth)
        self.dropDownRegionLabel.setActiveRectColor(10, 50, 100)
        self.dropDownRegionLabel.setActiveBorderColor(50, 50, 50)
        self.mainMenuScreenSurface.blit(self.dropDownRegionLabel.localSurface, (2 * self.width // 6, self.getVerticalPositioning()))

        self.dropDownProvinceLabel = Label2(f'Pick province', self.titleSmallerButtonFont, True, borderSize=2, maxWidth=self.dropDownLabelWidth)
        self.dropDownProvinceLabel.setActiveRectColor(10, 50, 100)
        self.dropDownProvinceLabel.setActiveBorderColor(50, 50, 50)
        self.mainMenuScreenSurface.blit(self.dropDownProvinceLabel.localSurface, (3 * self.width // 6, self.getVerticalPositioning()))

        self.dropDownSettlementLabel = Label2(f'Pick settlement', self.titleSmallerButtonFont, True, borderSize=2, maxWidth=self.dropDownLabelWidth)
        self.dropDownSettlementLabel.setActiveRectColor(10, 50, 100)
        self.dropDownSettlementLabel.setActiveBorderColor(50, 50, 50)
        self.mainMenuScreenSurface.blit(self.dropDownSettlementLabel.localSurface, (4 * self.width // 6, self.getVerticalPositioning()))

        self.writeLine += 5

        self.dropDownFamilyNameLabel = Label2(f'Pick Family', self.titleSmallerButtonFont, True, borderSize=2, maxWidth=self.dropDownLabelWidth)
        self.dropDownFamilyNameLabel.setActiveRectColor(10, 50, 100)
        self.dropDownFamilyNameLabel.setActiveBorderColor(50, 50, 50)
        self.mainMenuScreenSurface.blit(self.dropDownFamilyNameLabel.localSurface, (2 * self.width // 8, self.getVerticalPositioning()))

        self.dropDownFamilyNameSelectLabel.changeDropDownClicked(self.dropDownFamilyNameButton.getIsActive())
        self.dropDownFamilyNameSelectLabel.setActiveRectColor(10, 50, 100)
        self.dropDownFamilyNameSelectLabel.setActiveBorderColor(150, 150, 150)
        self.dropDownFamilyNameSelectLabel.changeColorOnHover(self.dropDownFamilyNameButton.getOnHover())

        self.dropDownGenderLabel = Label2(f'Pick Gender', self.titleSmallerButtonFont, True, borderSize=2, maxWidth=self.dropDownLabelWidth)
        self.dropDownGenderLabel.setActiveRectColor(10, 50, 100)
        self.dropDownGenderLabel.setActiveBorderColor(50, 50, 50)

        self.mainMenuScreenSurface.blit(self.dropDownGenderLabel.localSurface, (3.5 * self.width // 8, self.getVerticalPositioning()))

        self.dropDownGenderSelectLabel.changeDropDownClicked(self.dropDownGenderButton.getIsActive())
        self.dropDownGenderSelectLabel.setActiveRectColor(10, 50, 100)
        self.dropDownGenderSelectLabel.setActiveBorderColor(150, 150, 150)
        self.dropDownGenderSelectLabel.changeColorOnHover(self.dropDownGenderButton.getOnHover())

        self.dropDownFirstNameLabel = Label2(f'Pick Name', self.titleSmallerButtonFont, True, borderSize=2, maxWidth=self.dropDownLabelWidth)
        self.dropDownFirstNameLabel.setActiveRectColor(10, 50, 100)
        self.dropDownFirstNameLabel.setActiveBorderColor(50, 50, 50)

        self.mainMenuScreenSurface.blit(self.dropDownFirstNameLabel.localSurface, (5 * self.width // 8, self.getVerticalPositioning()))

        self.dropDownFirstNameSelectLabel.changeDropDownClicked(self.dropDownFirstNameButton.getIsActive())
        self.dropDownFirstNameSelectLabel.setActiveRectColor(10, 50, 100)
        self.dropDownFirstNameSelectLabel.setActiveBorderColor(150, 150, 150)
        self.dropDownFirstNameSelectLabel.changeColorOnHover(self.dropDownFirstNameButton.getOnHover())

        self.writeLine += 1

        xPosition = (3.5 * self.width // 8)
        self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.dropDownGenderSelectLabel.localSurface, (xPosition, self.getVerticalPositioning())), self.dropDownGenderButton])

        if self.dropDownGenderSelectLabel.dropDownClicked:
            self.genders = [Enums.Sexes["MALE"].name, Enums.Sexes["FEMALE"].name]
            self.dropDownGenderSelectLabel.addOptions(dataList=self.genders, identifierString='gender', vericalOffset=self.getVerticalPositioning(), horizontalOffset=xPosition, screenSurface=self.mainMenuScreenSurface, screenSurfaceObjRect=self.mainMenuScreenSurfaceObjsRect, dynamicDropDownList=self.dropDownDynamicGenderList)

        xPosition = 2 * self.width // 8
        self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.dropDownFamilyNameSelectLabel.localSurface, (xPosition, self.getVerticalPositioning())), self.dropDownFamilyNameButton])

        if self.dropDownFamilyNameSelectLabel.dropDownClicked:
            if self.dropDownCultureSelectLabel.getText() != '-Select-':

                self.familyNames = world.getAllNames()[self.dropDownCultureSelectLabel.getText()][f'{self.dropDownCultureSelectLabel.getText()}FamilyNames']['familyNames']
                self.dropDownFamilyNameSelectLabel.addOptions(dataList=self.familyNames, identifierString='family', vericalOffset=self.getVerticalPositioning(), horizontalOffset=xPosition, screenSurface=self.mainMenuScreenSurface, screenSurfaceObjRect=self.mainMenuScreenSurfaceObjsRect, dynamicDropDownList=self.dropDownDynamicFamilyNameList)

        xPosition = 5 * self.width // 8
        self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.dropDownFirstNameSelectLabel.localSurface, (xPosition, self.getVerticalPositioning())), self.dropDownFirstNameButton])

        if self.dropDownFirstNameSelectLabel.dropDownClicked:
            if self.dropDownCultureSelectLabel.getText() != '-Select-' and (self.dropDownGenderSelectLabel.getText() == 'MALE' or self.dropDownGenderSelectLabel.getText() == 'FEMALE'):
                self.firstNames = world.getAllNames()[self.dropDownCultureSelectLabel.getText()][f'{self.dropDownGenderSelectLabel.getText().lower()}{self.dropDownCultureSelectLabel.getText().capitalize()}Names']['names']
                self.dropDownFamilyNameSelectLabel.addOptions(dataList=self.firstNames, identifierString='firstNames', vericalOffset=self.getVerticalPositioning(), horizontalOffset=xPosition, screenSurface=self.mainMenuScreenSurface, screenSurfaceObjRect=self.mainMenuScreenSurfaceObjsRect, dynamicDropDownList=self.dropDownDynamicFirstNameList)

        self.writeLine -= 5

        self.dropDownCultureSelectLabel.changeDropDownClicked(self.dropDownCultureButton.getIsActive())
        self.dropDownCultureSelectLabel.setActiveRectColor(10, 50, 100)
        self.dropDownCultureSelectLabel.setActiveBorderColor(150, 150, 150)
        self.dropDownCultureSelectLabel.changeColorOnHover(self.dropDownCultureButton.getOnHover())

        self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.dropDownCultureSelectLabel.localSurface, (self.width // 6, self.getVerticalPositioning())), self.dropDownCultureButton])

        if self.dropDownCultureSelectLabel.dropDownClicked:
            counter = 1
            for data in world.getCultures():
                if counter == len(world.getCultures()):
                    continue

                self.dropDownMultiCultureButton = self.makeNewMultiButton(self.dropDownDynamicCultureList, data, 'culture')
                self.dropDownCultureChoiceLabel = Label2(f'{data.getCultureName()}', self.titleSmallerButtonFont, True, borderSize=2, maxWidth=self.dropDownLabelWidth)
                self.dropDownCultureChoiceLabel.setActiveRectColor(20, 20, 20)
                self.dropDownCultureChoiceLabel.setActiveBorderColor(200, 200, 200)
                self.dropDownCultureChoiceLabel.changeColorOnHover(self.dropDownMultiCultureButton.getOnHover())
                self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.dropDownCultureChoiceLabel.localSurface, (self.width // 6, self.getVerticalPositioning() + self.dropDownCultureLabel.h * counter)), self.dropDownMultiCultureButton])

                counter += 1

        self.dropDownRegionSelectLabel.changeDropDownClicked(self.dropDownRegionButton.getIsActive())
        self.dropDownRegionSelectLabel.setActiveRectColor(10, 50, 100)
        self.dropDownRegionSelectLabel.setActiveBorderColor(150, 150, 150)
        self.dropDownRegionSelectLabel.changeColorOnHover(self.dropDownRegionButton.getOnHover())

        xPosition = 2 * self.width // 6
        self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.dropDownRegionSelectLabel.localSurface, (xPosition, self.getVerticalPositioning())), self.dropDownRegionButton])

        if self.dropDownRegionSelectLabel.dropDownClicked:

            if self.dropDownCultureSelectLabel.getText() != '-Select-':
                self.regionNames = world.getAllNames()[self.dropDownCultureSelectLabel.getText()][f'{self.dropDownCultureSelectLabel.getText()}RegionNames']['regionNames']
                self.dropDownRegionSelectLabel.addOptions(dataList=self.regionNames, identifierString='region', vericalOffset=self.getVerticalPositioning(), horizontalOffset=xPosition, screenSurface=self.mainMenuScreenSurface, screenSurfaceObjRect=self.mainMenuScreenSurfaceObjsRect, dynamicDropDownList=self.dropDownDynamicRegionList)

        self.dropDownProvinceSelectLabel.changeDropDownClicked(self.dropDownProvinceButton.getIsActive())
        self.dropDownProvinceSelectLabel.setActiveRectColor(10, 50, 100)
        self.dropDownProvinceSelectLabel.setActiveBorderColor(150, 150, 150)
        self.dropDownProvinceSelectLabel.changeColorOnHover(self.dropDownProvinceButton.getOnHover())

        xPosition = 3 * self.width // 6
        self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.dropDownProvinceSelectLabel.localSurface, (xPosition, self.getVerticalPositioning())), self.dropDownProvinceButton])

        if self.dropDownProvinceSelectLabel.dropDownClicked:
            if self.dropDownCultureSelectLabel.getText() != '-Select-':
                self.provinceNames = world.getAllNames()[self.dropDownCultureSelectLabel.getText()][f'{self.dropDownCultureSelectLabel.getText()}ProvinceNames']['provinceNames']
                self.dropDownRegionSelectLabel.addOptions(dataList=self.provinceNames, identifierString='province', vericalOffset=self.getVerticalPositioning(), horizontalOffset=xPosition, screenSurface=self.mainMenuScreenSurface, screenSurfaceObjRect=self.mainMenuScreenSurfaceObjsRect, dynamicDropDownList=self.dropDownDynamicProvinceList)


        self.dropDownSettlementSelectLabel.changeDropDownClicked(self.dropDownSettlementButton.getIsActive())
        self.dropDownSettlementSelectLabel.setActiveRectColor(10, 50, 100)
        self.dropDownSettlementSelectLabel.setActiveBorderColor(150, 150, 150)
        self.dropDownSettlementSelectLabel.changeColorOnHover(self.dropDownSettlementButton.getOnHover())

        xPosition = 4 * self.width // 6
        self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.dropDownSettlementSelectLabel.localSurface, (xPosition, self.getVerticalPositioning())), self.dropDownSettlementButton])

        if self.dropDownSettlementSelectLabel.dropDownClicked:

            if self.dropDownCultureSelectLabel.getText() != '-Select-':
                self.settlementsNames = world.getAllNames()[self.dropDownCultureSelectLabel.getText()][f'{self.dropDownCultureSelectLabel.getText()}SettlementsNames']['settlementsNames']
                self.dropDownRegionSelectLabel.addOptions(dataList=self.settlementsNames, identifierString='settlement', vericalOffset=self.getVerticalPositioning(), horizontalOffset=xPosition, screenSurface=self.mainMenuScreenSurface, screenSurfaceObjRect=self.mainMenuScreenSurfaceObjsRect, dynamicDropDownList=self.dropDownDynamicSettlementList)
        self.writeLine += 10

        return

    def setMenuFlag(self):
        self.showMenuFlag = True
        self.showNamingMenuFlag = False

    def setNamingMenuFlag(self):
        self.showMenuFlag = False
        self.showNamingMenuFlag = True

    def showMainMenu(self, world):

        self.writeLine += 1

        self.mainMenuLabel = Label2(f'Saga Simulator', self.titleFont, False, borderSize=1)
        self.mainMenuLabel.setActiveRectColor(150, 50, 150)
        self.mainMenuLabel.setActiveBorderColor(10, 10, 100)
        self.mainMenuScreenSurface.blit(self.mainMenuLabel.localSurface, (self.mainMenuLabel.centerElement(self.width), self.getVerticalPositioning()))

        self.writeLine += 5


        text1 = f'N'
        text2 = f'ew World'
        textColor1 = [text1, (50, 150, 50)]
        textColor2 = [text2, None]

        self.mainMenuLabel2 = Label2(f'New World', self.titleButtonFont, True, borderSize=3, multiColor=True, multiColorText=[textColor1, textColor2])
        self.mainMenuLabel2.setActiveRectColor(10, 50, 100)
        self.mainMenuLabel2.setActiveBorderColor(50, 50, 50)
        self.mainMenuLabel2.changeColorOnHover(self.newWorldButton.getOnHover())
        self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.mainMenuLabel2.localSurface, (self.mainMenuLabel2.centerElement(self.width), self.getVerticalPositioning())), self.newWorldButton])

        self.writeLine += 4

        self.mainMenuLabel3 = Label2(f'Load World', self.titleButtonFont, True, borderSize=3)
        self.mainMenuLabel3.setActiveRectColor(100, 100, 10)
        # Grayout
        self.mainMenuLabel3.setActiveRectColor(50, 50, 50)
        self.mainMenuLabel3.setActiveBorderColor(50, 50, 50)
        self.mainMenuLabel3.changeColorOnHover(self.loadWorldButton.getOnHover())
        self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.mainMenuLabel3.localSurface, (self.mainMenuLabel3.centerElement(self.width), self.getVerticalPositioning())), self.loadWorldButton])

        if world.getGameState().getGameState() != 0:

            self.writeLine += 4

            self.mainMenuLabel4 = Label2(f'Save World', self.titleButtonFont, True, borderSize=3)
            self.mainMenuLabel4.setActiveRectColor(30, 100, 30)
            #Grayout
            self.mainMenuLabel4.setActiveRectColor(50, 50, 50)
            self.mainMenuLabel4.setActiveBorderColor(50, 50, 50)
            self.mainMenuLabel4.changeColorOnHover(self.saveWorldButton.getOnHover())
            self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.mainMenuLabel4.localSurface, (self.mainMenuLabel4.centerElement(self.width), self.getVerticalPositioning())), self.saveWorldButton])

        if world.getGameState().getGameState() != 0:

            self.writeLine += 4

            text1 = f'C'
            text2 = f'ontinue'
            textColor1 = [text1, (50, 150, 50)]
            textColor2 = [text2, None]

            self.mainMenuLabel5 = Label2(f'Continue', self.titleButtonFont, True, borderSize=3, multiColor=True, multiColorText=[textColor1, textColor2])
            self.mainMenuLabel5.setActiveRectColor(100, 30, 100)
            self.mainMenuLabel5.setActiveBorderColor(50, 50, 50)
            self.mainMenuLabel5.changeColorOnHover(self.continueButton.getOnHover())
            self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.mainMenuLabel5.localSurface, (self.mainMenuLabel5.centerElement(self.width), self.getVerticalPositioning())), self.continueButton])


        self.writeLine += 4

        text1 = f'Q'
        text2 = f'uit'
        textColor1 = [text1, (50, 150, 50)]
        textColor2 = [text2, None]

        self.mainMenuLabel6 = Label2(f'Quit', self.titleButtonFont, True, borderSize=3, multiColor=True, multiColorText=[textColor1, textColor2])
        self.mainMenuLabel6.setActiveRectColor(100, 10, 10)
        self.mainMenuLabel6.setActiveBorderColor(50, 50, 50)
        self.mainMenuLabel6.changeColorOnHover(self.quitButton.getOnHover())
        self.mainMenuScreenSurfaceObjsRect.append([self.mainMenuScreenSurface.blit(self.mainMenuLabel6.localSurface, (self.mainMenuLabel6.centerElement(self.width), self.getVerticalPositioning())), self.quitButton])

        self.writeLine += 8

        self.mainMenuLabel7 = Label2(f'© 2023 by Zbigniew (Kamos5) Fietkiewicz', self.textFont, True, borderSize=2)
        self.mainMenuLabel7.setActiveRectColor(10, 100, 10)
        self.mainMenuLabel7.setActiveBorderColor(20, 20, 20)
        self.mainMenuScreenSurface.blit(self.mainMenuLabel7.localSurface, (self.width * 6 // 8, self.height * 0.9))

    def getVerticalPositioning(self):
        return self.writeLine * (self.lineHeight + 4 * self.labelBoarderDefault + 4 * self.labelMarginVerticalDefault)

    def getMainMenuScreenSurface(self):
        return self.mainMenuScreenSurface

    def cleanScreen(self):

        #self.mainMenuScreenSurface.fill(self.screenColor, (0, 0, self.width, self.height))
        self.mainMenuScreenSurfaceObjsRect = []
        self.resetWriteLine()

    def resetWriteLine(self):

        self.writeLine = 0

    def makeNewMultiButton(self, buttonsList, newButtonName, newButtonName2= '',shouldBeActive=False):

        for button in buttonsList:
            if button.getButtonName() == newButtonName and button.getButtonName2() == newButtonName2:
                return button
        newButton = Button(newButtonName, newButtonName2)
        buttonsList.append(newButton)
        if shouldBeActive:
            newButton.setActiveStatus()
        return newButton

    def getDropDownDynamicCultureButtons(self):
        return self.dropDownDynamicCultureList

    def getDropDownDynamicRegionButtons(self):
        return self.dropDownDynamicRegionList

    def getDropDownDynamicProvinceButtons(self):
        return self.dropDownDynamicProvinceList

    def getDropDownDynamicSettlementButtons(self):
        return self.dropDownDynamicSettlementList

    def getDropDownDynamicFamilyNameButtons(self):
        return self.dropDownDynamicFamilyNameList

    def getDropDownDynamicGenderButtons(self):
        return self.dropDownDynamicGenderList

    def getDropDownDynamicFirstNameButtons(self):
        return self.dropDownDynamicFirstNameList

    def getChosenNames(self):
        returnedList = []
        for label in self.formSelectedLabels:
            chosenText = label.getText()
            if chosenText == '-Select-':
                chosenText = ''
            returnedList.append(chosenText)
        return returnedList

