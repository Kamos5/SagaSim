import pygame

from UI.Fonts import Fonts
from UI.Label import Label


class ListScreen:

    def __init__(self, width, height, widthOffSet, heightOffSet):

        self.font1 = Fonts().getFont1()
        self.writeLine = 1
        self.width = width
        self.height = height
        self.widthOffSet = widthOffSet
        self.heightOffSet = heightOffSet
        self.scroll_y = 0

        self.listScreenSurface = pygame.Surface([self.width, self.height - self.heightOffSet])
        self.listScreenSurfaceRegionsRect = []
        self.listScreenSurfaceSettlementsRect = []
        self.listScreenSurfaceFamiliesRect = []
        self.listScreenSurfacePersonRect = []


    def getScroll_y(self):

        return self.scroll_y

    def setScroll_y(self, newValue):

        self.scroll_y = newValue

    def resetWriteLine(self):

        self.writeLine = 1

    def cleanScreen(self):

        self.listScreenSurface.fill((20, 20, 20), (0, 0, self.width, self.height))
        self.listScreenSurfaceRegionsRect = []
        self.listScreenSurfaceSettlementsRect = []
        self.listScreenSurfaceFamiliesRect = []
        self.listScreenSurfacePersonRect = []

    def getInspectorScreenSurface(self):
        return self.listScreenSurface

    def addRegions(self):

        label = Label("Regions: ", 200, 20, self.font1)
        self.listScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))

        self.writeLine += 1

    def addRegion(self, region, focusObj):

        if focusObj != region:
            label = Label(str(region.getRegionName()), 200, 20, self.font1)

        if focusObj == region:
            label = Label(str(region.getRegionName()), 200, 20, self.font1, 'active')

        self.listScreenSurfaceRegionsRect.append([self.listScreenSurface.blit(label.localSurface, (self.width * 0.10, 20 * self.writeLine + self.scroll_y)), region])
        self.writeLine += 1


    def addSettlement(self, settlement, focusObj):

        text = str(settlement.getSettlementName()) + " (" + str(settlement.getSettlementType().value) + ")" + " - alive population (" + str(settlement.getPopulation()) + ")"

        if focusObj != settlement:
            label = Label(text, 400, 20, self.font1)

        if focusObj == settlement:
            label = Label(text, 400, 20, self.font1, 'active')

        self.listScreenSurfaceSettlementsRect.append([self.listScreenSurface.blit(label.localSurface, ((self.width * 0.15), 20 * self.writeLine + self.scroll_y)), settlement])

        self.writeLine += 1


    def addFamilies(self):

        label = Label("Families: ", 300, 20, self.font1)
        self.listScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))

        self.writeLine += 1


    def addFamily(self, family, focusObj):

        text = str(family.getFamilyName() + " (" + str(family.getAliveMemberNumber()) + ")" + " Origin: " + str(family.getOriginRegion().getRegionName()))

        if focusObj != family:
            label = Label(text, 300, 20, self.font1)

        if focusObj == family:
            label = Label(text, 300, 20, self.font1, 'active')

        self.listScreenSurfaceFamiliesRect.append([self.listScreenSurface.blit(label.localSurface, (self.width * 0.10, 20 * self.writeLine + self.scroll_y)), family])

        self.writeLine += 1


    def addPerson(self, person, focusObj):

        firstName = str(person.getFirstName())
        lastName = str(person.getLastName())
        age = str (person.age)
        spouse = ''
        if person.getSpouse() != None:
            spouse = person.spouse.getFirstName()

        text = firstName + " " + lastName + " Age: " + age + " Spouse: " + spouse

        if focusObj != person:
            label = Label(text, 300, 20, self.font1)

        if focusObj == person:
            label = Label(text, 300, 20, self.font1, 'active')

        self.listScreenSurfacePersonRect.append([self.listScreenSurface.blit(label.localSurface, (self.width * 0.15, 20 * self.writeLine + self.scroll_y)), person])

        self.writeLine += 1
