import pygame

from UI.Utils.Button import Button
from UI.Utils.Fonts import Fonts
from UI.Utils.Label import Label
from UI.Utils.Label2 import Label2
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

        self.showFamilyAll = True
        self.showFamilyAdults = False
        self.showFamilyKids = False
        self.showEmployed = False
        self.showUnemployed = False
        self.showSick = False

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

        self.showFamilyAll = False
        self.showFamilyAdults = False
        self.showFamilyKids = False
        self.showEmployed = False
        self.showSick = False
        self.showUnemployed = False

    def changeFamilyButtons(self, buttonClicked):

        if buttonClicked == 'allFamilySettlers':
            self.setAllButtonsFalse()
            self.showFamilyAll = True
        elif buttonClicked == 'familyAdults':
            self.showFamilyAll = False
            self.showFamilyAdults = not self.showFamilyAdults
        elif buttonClicked == 'familyKids':
            self.showFamilyAll = False
            self.showFamilyKids = not self.showFamilyKids
        elif buttonClicked == 'employed':
            self.showFamilyAll = False
            self.showEmployed = not self.showEmployed
        elif buttonClicked == 'unemployed':
            self.showFamilyAll = False
            self.showUnemployed = not self.showUnemployed
        elif buttonClicked == 'sick':
            self.showFamilyAll = False
            self.showSick = not self.showSick

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
        self.showAllSettlers()
        self.showOnlyAdults()
        self.showOnlyKids()
        self.showEmployedPeople()
        self.showUnemployedPeople()
        self.showSickPeople()

        self.writeLine += 1

    def addRegion(self, region, focusObj):

        if focusObj == region:
            label = Label(f'{region.getRegionName()} ({(region.getCurrentTemperature())} °C)', 200, self.lineHeight, self.textFont, True, True)
        else:
            label = Label(f'{region.getRegionName()} ({(region.getCurrentTemperature())} °C)', 200, self.lineHeight, self.textFont, True)

        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, (self.width * 0.10, self.lineHeight * self.writeLine + self.scroll_y)), region])

        self.writeLine += 1


    def addSettlement(self, settlement, focusObj):

        text = ''.join([str(settlement.getSettlementName()), " (", str(settlement.getSettlementType().value), ")", " - alive population (", str(settlement.getPopulation()), ")"])

        if focusObj == settlement:
                label = Label(text, 400, self.lineHeight, self.textFont, True, True)
        else:
            label = Label(text, 400, self.lineHeight, self.textFont, True)

        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, ((self.width * 0.15), self.lineHeight * self.writeLine + self.scroll_y)), settlement])

        self.writeLine += 1

    def showAllSettlers(self):

        label = Label(f'All', 25, self.lineHeight, self.textFont, True)
        label.changeColorBasedOnFlag(self.showFamilyAll)
        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, ((self.width * 0.15)+400, self.lineHeight * self.writeLine + self.scroll_y)), Button('allFamilySettlers')])

    def showOnlyAdults(self):

        label = Label(f'Adults', 50, self.lineHeight, self.textFont, True)
        label.changeColorBasedOnFlag(self.showFamilyAdults)
        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, ((self.width * 0.15)+425, self.lineHeight * self.writeLine + self.scroll_y)), Button('familyAdults')])

    def showOnlyKids(self):

        label = Label(f'Kids', 35, self.lineHeight, self.textFont, True)
        label.changeColorBasedOnFlag(self.showFamilyKids)
        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, ((self.width * 0.15)+475, self.lineHeight * self.writeLine + self.scroll_y)), Button('familyKids')])

    def showEmployedPeople(self):

        label = Label(f'Employed', 75, self.lineHeight, self.textFont, True)
        label.changeColorBasedOnFlag(self.showEmployed)
        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, ((self.width * 0.15)+510, self.lineHeight * self.writeLine + self.scroll_y)), Button('employed')])

    def showUnemployedPeople(self):

        label = Label(f'Unemployed', 95, self.lineHeight, self.textFont, True)
        label.changeColorBasedOnFlag(self.showUnemployed)
        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, ((self.width * 0.15)+585, self.lineHeight * self.writeLine + self.scroll_y)), Button('unemployed')])

    def showSickPeople(self):

        label = Label(f'Sick', 35, self.lineHeight, self.textFont, True)
        label.changeColorBasedOnFlag(self.showSick)
        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, ((self.width * 0.15)+680, self.lineHeight * self.writeLine + self.scroll_y)), Button('sick')])

    def addFamilies(self, families):

        label = Label(f'Families: ({len(families)})', 300, self.lineHeight, self.textFont, True)
        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, (self.width * 0.05, self.lineHeight * self.writeLine + self.scroll_y)), 'showFamilies'])

        self.writeLine += 1


    def addFamily(self, family, focusObj):

        screenYPosition = self.lineHeight * self.writeLine + self.scroll_y

        text = ''.join([str(family.getFamilyName()), " (", str(family.getAliveMemberNumber()), ")", " - ", " Origin: ", str(family.getOriginRegion().getRegionName())])

        if focusObj == family:
            label = Label(text, 300, self.lineHeight, self.textFont, True, True)
        else:
            label = Label(text, 300, self.lineHeight, self.textFont, True)

        if self.height >= screenYPosition:

            self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, (self.width * 0.10, self.lineHeight * self.writeLine + self.scroll_y)), family])
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

        if focusObj == person:
            label = Label(text, 400, self.lineHeight, self.textFont, True, True)

        else:
            label = Label(text, 400, self.lineHeight, self.textFont, True)

        if self.textSearchField is not None:
            if self.textSearchField.getText().upper() in person.getLastName().upper() or self.textSearchField.getText().lower() in person.getLastName().lower() or self.textSearchField.getText().upper() in person.getFirstName().upper() or self.textSearchField.getText().lower() in person.getFirstName().lower():
                self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, (self.width * 0.20, self.lineHeight * self.writeLine + self.scroll_y)), person])

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

