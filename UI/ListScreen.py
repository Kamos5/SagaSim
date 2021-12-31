import pygame

from UI.Fonts import Fonts
from UI.Label import Label


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

    def addRegions(self):

        label = Label("Regions: ", 200, self.lineHeight, self.textFont)
        self.listScreenSurface.blit(label.localSurface, (self.width * 0.05, self.lineHeight * self.writeLine + self.scroll_y))

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

        text = str(family.getFamilyName() + " (" + str(family.getAliveMemberNumber()) + ")" + " Origin: " + str(family.getOriginRegion().getRegionName()))

        if focusObj == family:
            label = Label(text, 300, self.lineHeight, self.textFont, True, True)
        else:
            label = Label(text, 300, self.lineHeight, self.textFont, True)

        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, (self.width * 0.10, self.lineHeight * self.writeLine + self.scroll_y)), family])

        self.writeLine += 1


    def addPerson(self, person, focusObj):

        firstName = str(person.getFirstName())
        lastName = str(person.getLastName())
        age = str (person.age)
        spouse = ''
        if person.getSpouse() != None:
            spouse = person.spouse.getFirstName()

        text = firstName + " " + lastName + " Age: " + age + " Spouse: " + spouse

        if focusObj == person:
            label = Label(text, 300, self.lineHeight, self.textFont, True, True)

        else:
            label = Label(text, 300, self.lineHeight, self.textFont, True)

        self.listScreenSurfaceObjsRect.append([self.listScreenSurface.blit(label.localSurface, (self.width * 0.15, self.lineHeight * self.writeLine + self.scroll_y)), person])

        self.writeLine += 1
