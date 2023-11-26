import pygame

import Enums
from UI.Utils.Button import Button
from UI.Utils.Fonts import Fonts
from UI.Utils.Label import Label
from UI.Utils.TextField import TextField


class ListScreen:

    def __init__(self, width, height, widthOffSet, heightOffSet, screenPosX, screenPosY):

        self.screenColor = 20, 20, 20
        self.font = Fonts()
        self.textFont = self.font.getFont1()
        self.lineHeight = self.font.getLineHeight()
        self.writeLine = 1
        self.width = width
        self.height = height
        self.widthOffSet = widthOffSet
        self.heightOffSet = heightOffSet
        self.scroll_y = 0
        self.screenPosX = screenPosX
        self.screenPosY = screenPosY

        self.textSearchField = None
        self.listScreenSurface = pygame.Surface([self.width, self.height - self.heightOffSet])
        self.listScreenSurfaceObjsRect = []

        self.showFamilyAllFlag = True
        self.showFamilyAdultsFlag = False
        self.showFamilyKidsFlag = False
        self.showEmployedFlag = False
        self.showUnemployedFlag = False
        self.showSickFlag = False
        self.showWithLoversFlag = False

        self.allButton = Button('allFamilySettlers')
        self.familyAdultsButton = Button('familyAdults')
        self.familyKidsButton = Button('familyKids')
        self.employedButton = Button('employed')
        self.unemployedButton = Button('unemployed')
        self.sickButton = Button('sick')
        self.withLoversButton = Button('withLovers')

        self.showFamiliesButton = Button('showFamilies')

        self.regionButton = None
        self.settlementButton = None
        self.familyButton = None
        self.listScreenButtons = [self.showFamiliesButton]

    def getScroll_y(self):

        return self.scroll_y

    def setScroll_y(self, newValue):

        self.scroll_y = newValue

    def resetWriteLine(self):

        self.writeLine = 1

    def cleanScreen(self):

        self.listScreenSurface.fill(self.screenColor, (0, 0, self.width, self.height))
        self.listScreenSurfaceObjsRect = []

    def setAllButtonsFalse(self):

        self.showFamilyAllFlag = False
        self.showFamilyAdultsFlag = False
        self.showFamilyKidsFlag = False
        self.showEmployedFlag = False
        self.showSickFlag = False
        self.showUnemployedFlag = False
        self.showWithLoversFlag = False

    def changeFamilyButtons(self, buttonClicked, event):

        if buttonClicked == self.allButton:
            buttonClicked.setOnHover()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.setAllButtonsFalse()
                self.showFamilyAllFlag = True
            return
        elif buttonClicked == self.familyAdultsButton:
            buttonClicked.setOnHover()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.showFamilyAllFlag = False
                self.showFamilyAdultsFlag = not self.showFamilyAdultsFlag
            return
        elif buttonClicked == self.familyKidsButton:
            buttonClicked.setOnHover()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.showFamilyAllFlag = False
                self.showFamilyKidsFlag = not self.showFamilyKidsFlag
            return
        elif buttonClicked == self.employedButton:
            buttonClicked.setOnHover()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.showFamilyAllFlag = False
                self.showEmployedFlag = not self.showEmployedFlag
            return
        elif buttonClicked == self.unemployedButton:
            buttonClicked.setOnHover()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.showFamilyAllFlag = False
                self.showUnemployedFlag = not self.showUnemployedFlag
            return
        elif buttonClicked == self.sickButton:
            buttonClicked.setOnHover()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.showFamilyAllFlag = False
                self.showSickFlag = not self.showSickFlag
            return
        elif buttonClicked == self.withLoversButton:
            buttonClicked.setOnHover()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.showFamilyAllFlag = False
                self.showWithLoversFlag = not self.showWithLoversFlag
            return

    def getInspectorScreenSurface(self):
        return self.listScreenSurface

    def addSearch(self):

        label = Label("Search: ", 80, self.lineHeight, self.textFont)
        self.listScreenSurface.blit(label.localSurface, (self.width * 0.55, self.lineHeight * self.writeLine + self.scroll_y))

        # Search field
        if self.textSearchField is None:
            textField = TextField(180, self.lineHeight, self.textFont)
        else:
            textField = self.textSearchField

        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(textField.localSurface, (self.width * 0.70, self.lineHeight * self.writeLine + self.scroll_y)), textField])

        self.textSearchField = textField
        self.writeLine += 1

    def addRegions(self, world, focusObj):

        label = Label(f'Regions: ({(len(world.getAlivePeople()))})', 200, self.lineHeight, self.textFont)
        self.listScreenSurface.blit(label.localSurface, (self.width * 0.05, self.lineHeight * self.writeLine + self.scroll_y))
        self.showButtonAllSettlers()
        self.showButtonOnlyAdults()
        self.showButtonOnlyKids()
        self.showButtonEmployedPeople()
        self.showButtonUnemployedPeople()
        self.showButtonSickPeople()
        self.showButtonWithLovers()

        self.writeLine += 1

    def addRegion(self, region, focusObj):

        self.regionButton = self.makeNewMultiButton(self.getListScreenButtons(), region.getRegionName())

        self.label = Label(f'{region.getRegionName()}', 200, self.lineHeight, self.textFont, True, False, textColor=region.getRegionColor())

        self.label.changeColorOnHover(self.regionButton.getOnHover())

        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(self.label.localSurface, (self.width * 0.10, self.lineHeight * self.writeLine + self.scroll_y)), self.regionButton])

        self.writeLine += 1

    def addProvinces(self, region, focusObj):

        label = Label(f'Provinces:', 200, self.lineHeight, self.textFont)

        self.listScreenSurface.blit(label.localSurface, (self.width * 0.15, self.lineHeight * self.writeLine + self.scroll_y))

        self.writeLine += 1

    def addProvince(self, province, focusObj):

        label = Label(f'{province.getName()} ({(province.getCurrentTemperature())} °C)', 200, self.lineHeight, self.textFont)

        self.listScreenSurface.blit(label.localSurface, (self.width * 0.20, self.lineHeight * self.writeLine + self.scroll_y))

        self.writeLine += 1

    def addSettlement(self, settlement, focusObj):

        self.settlementButton = self.makeNewMultiButton(self.getListScreenButtons(), settlement.getSettlementName())

        text = ''.join([str(settlement.getSettlementName()), " (", str(settlement.getSettlementType().value), ")", " - alive population (", str(settlement.getPopulation()), ")"])

        if focusObj == settlement:
            self.settlementLabel = Label(text, 400, self.lineHeight, self.textFont, True, True)
        else:
            self.settlementLabel = Label(text, 400, self.lineHeight, self.textFont, True)

        self.settlementLabel.changeColorOnHover(self.settlementButton.getOnHover())

        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(self.settlementLabel.localSurface, ((self.width * 0.25), self.lineHeight * self.writeLine + self.scroll_y)), self.settlementButton])

        self.writeLine += 1

    def showButtonAllSettlers(self):

        self.allLabel = Label(f'All', 25, self.lineHeight, self.textFont, True)
        self.allLabel.changeColorBasedOnActive(self.showFamilyAllFlag)
        self.allLabel.changeColorOnHover(self.allButton.getOnHover())
        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(self.allLabel.localSurface, ((self.width * 0.10)+400, self.lineHeight * self.writeLine + self.scroll_y)), self.allButton])

    def showButtonOnlyAdults(self):

        self.adultsLabel = Label(f'Adults', 50, self.lineHeight, self.textFont, True)
        self.adultsLabel.changeColorBasedOnActive(self.showFamilyAdultsFlag)
        self.adultsLabel.changeColorOnHover(self.familyAdultsButton.getOnHover())
        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(self.adultsLabel.localSurface, ((self.width * 0.10)+425, self.lineHeight * self.writeLine + self.scroll_y)), self.familyAdultsButton])

    def showButtonOnlyKids(self):

        self.kidsLabel = Label(f'Kids', 35, self.lineHeight, self.textFont, True)
        self.kidsLabel.changeColorBasedOnActive(self.showFamilyKidsFlag)
        self.kidsLabel.changeColorOnHover(self.familyKidsButton.getOnHover())
        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(self.kidsLabel.localSurface, ((self.width * 0.10)+475, self.lineHeight * self.writeLine + self.scroll_y)), self.familyKidsButton])

    def showButtonEmployedPeople(self):

        self.employedLabel = Label(f'Employed', 75, self.lineHeight, self.textFont, True)
        self.employedLabel.changeColorBasedOnActive(self.showEmployedFlag)
        self.employedLabel.changeColorOnHover(self.employedButton.getOnHover())
        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(self.employedLabel.localSurface, ((self.width * 0.10)+510, self.lineHeight * self.writeLine + self.scroll_y)), self.employedButton])

    def showButtonUnemployedPeople(self):

        self.unemployedLabel = Label(f'Unemployed', 95, self.lineHeight, self.textFont, True)
        self.unemployedLabel.changeColorBasedOnActive(self.showUnemployedFlag)
        self.unemployedLabel.changeColorOnHover(self.unemployedButton.getOnHover())
        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(self.unemployedLabel.localSurface, ((self.width * 0.10)+585, self.lineHeight * self.writeLine + self.scroll_y)), self.unemployedButton])

    def showButtonSickPeople(self):

        self.sickLabel = Label(f'Sick', 35, self.lineHeight, self.textFont, True)
        self.sickLabel.changeColorBasedOnActive(self.showSickFlag)
        self.sickLabel.changeColorOnHover(self.sickButton.getOnHover())
        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(self.sickLabel.localSurface, ((self.width * 0.10)+680, self.lineHeight * self.writeLine + self.scroll_y)), self.sickButton])

    def showButtonWithLovers(self):

        self.withLoversLabel = Label(f'With lovers', 85, self.lineHeight, self.textFont, True)
        self.withLoversLabel.changeColorBasedOnActive(self.showWithLoversFlag)
        self.withLoversLabel.changeColorOnHover(self.withLoversButton.getOnHover())
        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(self.withLoversLabel.localSurface, ((self.width * 0.10)+715, self.lineHeight * self.writeLine + self.scroll_y)), self.withLoversButton])

    def addFamilies(self, families):

        self.label = Label(f'Families: ({len(families)})', 300, self.lineHeight, self.textFont, True)
        self.label.changeColorOnHover(self.showFamiliesButton.getOnHover())
        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(self.label.localSurface, (self.width * 0.05, self.lineHeight * self.writeLine + self.scroll_y)), self.showFamiliesButton])

        self.writeLine += 1

    def addFamily(self, family, focusObj):

        screenYPosition = self.lineHeight * self.writeLine + self.scroll_y

        text1 = f'{family.getFamilyName()} ({family.getAliveMemberNumber()}) - Origin: '
        text2 = f'{family.getOriginRegion().getRegionName()}'
        textColor1 = [text1, None]
        textColor2 = [text2, family.getOriginRegion().getRegionColor()]

        self.familyButton = self.makeNewMultiButton(self.getListScreenButtons(), family.getFamilyName())

        if focusObj == family:
            self.familyLabel = Label(text1, 300, self.lineHeight, self.textFont, True, True, multiColor=True, multiColorText=[textColor1, textColor2])
        else:
            self.familyLabel = Label(text1, 300, self.lineHeight, self.textFont, True, multiColor=True, multiColorText=[textColor1, textColor2])


        self.familyLabel.changeColorOnHover(self.familyButton.getOnHover())

        if self.height >= screenYPosition:
            self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(self.familyLabel.localSurface, (self.width * 0.10, self.lineHeight * self.writeLine + self.scroll_y)), self.familyButton])
            self.writeLine += 1


    def addDeadFamilyPeople(self, family, focusObj):

        text = ''.join([str(family.getFamilyName()), " (", str(family.getDeadMemberNumber()), ")"])

        if focusObj == family:
            label = Label(text, 300, self.lineHeight, self.textFont, True, True)
        else:
            label = Label(text, 300, self.lineHeight, self.textFont, True)

        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, (self.width * 0.05, self.lineHeight * self.writeLine + self.scroll_y)), family])

        self.writeLine += 1


    def addSettler(self, person, focusObj):

        firstName = str(person.getFirstName())
        lastName = str(person.getLastName())
        occupationName = str(person.getOccupationName())
        if occupationName != '':
            occupationName = "<"+occupationName+">"
        age = str(person.age)
        maritalStatus = str(person.maritalStatus.value)
        text = ''.join([firstName, " ",  occupationName, " ", lastName, " Age: ", age, " ", maritalStatus])

        self.settlerButton = self.makeNewMultiButton(self.getListScreenButtons(), person)

        if focusObj == person:
            self.settlerLabel = Label(text, 400, self.lineHeight, self.textFont, True, True)

        else:
            self.settlerLabel = Label(text, 400, self.lineHeight, self.textFont, True)

        # if person.getSex() == Enums.Sexes.MALE:
        #     label.makeTextGivenColor(50, 150, 150)
        # if person.getSex() == Enums.Sexes.FEMALE:
        #     label.makeTextGivenColor(150, 50, 150)

        self.settlerLabel.changeColorOnHover(self.settlerButton.getOnHover())

        if self.textSearchField is not None:
            if self.textSearchField.getText().upper() in person.getLastName().upper() or self.textSearchField.getText().lower() in person.getLastName().lower() or self.textSearchField.getText().upper() in person.getFirstName().upper() or self.textSearchField.getText().lower() in person.getFirstName().lower():
                self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(self.settlerLabel.localSurface, (self.width * 0.30, self.lineHeight * self.writeLine + self.scroll_y)), person])

                self.writeLine += 1

    def addPerson(self, person, focusObj):

        firstName = str(person.getFirstName())
        lastName = str(person.getLastName())
        age = str(person.age)
        maritalStatus = str(person.maritalStatus.value)
        text = ''.join([firstName, " ", lastName, " Age: ", age, " ", maritalStatus])

        if focusObj == person:
            label = Label(text, 400, self.lineHeight, self.textFont, True, True)

        else:
            label = Label(text, 400, self.lineHeight, self.textFont, True)

        if self.textSearchField is not None:
            if self.textSearchField.getText().upper() in person.getLastName().upper() or self.textSearchField.getText().lower() in person.getLastName().lower() or self.textSearchField.getText().upper() in person.getFirstName().upper() or self.textSearchField.getText().lower() in person.getFirstName().lower():
                self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, (self.width * 0.15, self.lineHeight * self.writeLine + self.scroll_y)), person])

                self.writeLine += 1

    def addFavorites(self):
        label = Label("Favorites: ", 300, self.lineHeight, self.textFont)
        self.listScreenSurface.blit(label.localSurface, (self.width * 0.05, self.lineHeight * self.writeLine + self.scroll_y))

        self.writeLine += 1

    def addFavorite(self, object, lastFocusedObj):

        firstName = str(object.getFirstName())
        lastName = str(object.getLastName())
        text = ''.join([firstName, " ", lastName])

        if lastFocusedObj == object:
            label = Label(text, 400, self.lineHeight, self.textFont, True, True)

        else:
            label = Label(text, 400, self.lineHeight, self.textFont, True)

        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, (self.width * 0.10, self.lineHeight * self.writeLine + self.scroll_y)), object])

        self.writeLine += 1

    def makeNewMultiButton(self, buttonsList, newButtonName, shouldBeActive=False):

        for button in buttonsList:
            if button.getButtonName() == newButtonName:
                return button
        newButton = Button(newButtonName)
        buttonsList.append(newButton)
        if shouldBeActive:
            newButton.setActiveStatus()
        return newButton

    def getListScreenButtons(self):
        return self.listScreenButtons
