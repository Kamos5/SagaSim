import pygame

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


    def getScroll_y(self):

        return self.scroll_y

    def setScroll_y(self, newValue):

        self.scroll_y = newValue

    def resetWriteLine(self):

        self.writeLine = 1

    def cleanScreen(self):

        self.listScreenSurface.fill(self.screenColor, (0, 0, self.width, self.height))
        self.listScreenSurfaceObjsRect = []

    def getInspectorScreenSurface(self):
        return self.listScreenSurface

    def addRegions(self, focusObj):

        label = Label("Regions: ", 200, self.lineHeight, self.textFont)
        self.listScreenSurface.blit(label.localSurface, (self.width * 0.05, self.lineHeight * self.writeLine + self.scroll_y))

        label = Label("Search: ", 80, self.lineHeight, self.textFont)
        self.listScreenSurface.blit(label.localSurface, (self.width * 0.55, self.lineHeight * self.writeLine + self.scroll_y))

        #Search field
        if self.textSearchField is None:
            textField = TextField(180, self.lineHeight, self.textFont)
        else:
            textField = self.textSearchField

        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(textField.localSurface, (self.width * 0.70, self.lineHeight * self.writeLine + self.scroll_y)), textField])

        self.textSearchField = textField
        self.writeLine += 1

    def addRegion(self, region, focusObj):

        if focusObj == region:
            label = Label(str(region.getRegionName()), 200, self.lineHeight, self.textFont, True, True)
        else:
            label = Label(str(region.getRegionName()), 200, self.lineHeight, self.textFont, True)

        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, (self.width * 0.10, self.lineHeight * self.writeLine + self.scroll_y)), region])
        self.writeLine += 1


    def addSettlement(self, settlement, focusObj):

        text = str(settlement.getSettlementName()) + " (" + str(settlement.getSettlementType().value) + ")" + " - alive population (" + str(settlement.getPopulation()) + ")"

        if focusObj == settlement:
                label = Label(text, 400, self.lineHeight, self.textFont, True, True)
        else:
            label = Label(text, 400, self.lineHeight, self.textFont, True)

        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, ((self.width * 0.15), self.lineHeight * self.writeLine + self.scroll_y)), settlement])

        self.writeLine += 1


    def addFamilies(self):

        label = Label("Families: ", 300, self.lineHeight, self.textFont)
        self.listScreenSurface.blit(label.localSurface, (self.width * 0.05, self.lineHeight * self.writeLine + self.scroll_y))

        self.writeLine += 1


    def addFamily(self, family, focusObj):

        text = str(family.getFamilyName() + " (" + str(family.getAliveMemberNumber()) + ")" + " - " + " Origin: " + str(family.getOriginRegion().getRegionName()))

        if focusObj == family:
            label = Label(text, 300, self.lineHeight, self.textFont, True, True)
        else:
            label = Label(text, 300, self.lineHeight, self.textFont, True)

        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, (self.width * 0.10, self.lineHeight * self.writeLine + self.scroll_y)), family])

        self.writeLine += 1

    def addDeadFamilyPeople(self, family, focusObj):

        text = str(family.getFamilyName() + " (" + str(family.getDeadMemberNumber()) + ")")

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
        age = str (person.age)
        maritalStatus = str(person.maritalStatus.value)
        text = firstName + " " + occupationName + " " + lastName + " Age: " + age + " " + maritalStatus

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
        age = str (person.age)
        maritalStatus = str(person.maritalStatus.value)
        text = firstName + " " + lastName + " Age: " + age + " " + maritalStatus

        if focusObj == person:
            label = Label(text, 400, self.lineHeight, self.textFont, True, True)

        else:
            label = Label(text, 400, self.lineHeight, self.textFont, True)

        if self.textSearchField is not None:
            if self.textSearchField.getText().upper() in person.getLastName().upper() or self.textSearchField.getText().lower() in person.getLastName().lower() or self.textSearchField.getText().upper() in person.getFirstName().upper() or self.textSearchField.getText().lower() in person.getFirstName().lower():
                self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, (self.width * 0.15, self.lineHeight * self.writeLine + self.scroll_y)), person])

                self.writeLine += 1
