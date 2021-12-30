import pygame

from Family import Family
from Person import Person
from Region import Region
from Settlements import Settlements
from UI.Fonts import Fonts
from UI.Label import Label


class InspectorScreen:

    def __init__(self, width, height, widthOffSet, heightOffSet):

        self.writeLine = 1
        self.width = width
        self.height = height
        self.widthOffSet = widthOffSet
        self.heightOffSet = heightOffSet
        self.font2 = Fonts().getFont2()
        self.scroll_y = 0

        self.inspectorScreenSurface = pygame.Surface([self.width, self.height - self.heightOffSet])


    def resetWriteLine(self):

        self.writeLine = 1

    def cleanScreen(self):

        self.inspectorScreenSurface.fill((50, 50, 50), (0, 0, self.width, self.height))

    def getInspectorScreenSurface(self):
        return self.inspectorScreenSurface

    def addInspectorLabel(self):

        label = Label("Inspector: ", 100, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (0, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1

    def addGeneralInspectorFields(self, object):

        if isinstance(object, Region):
            self.addInspectorForRegion(object)

        elif isinstance(object, Settlements):
            self.addInspectorForSettlements(object)

        elif isinstance(object, Family):
            self.addInspectorForFamily(object)

        elif isinstance(object, Person):
            self.addInspectorForPerson(object)


    def addInspectorForRegion(self, object):

        label = Label("Region name: " + object.getRegionName(), 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Settlements:", 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        for settlement in object.getSettlements():
            label = Label("Settlements name: " + settlement.getSettlementName(), 500, 20, self.font2)
            self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.10, 20 * self.writeLine + self.scroll_y))
            self.writeLine += 1


    def addInspectorForSettlements(self, object):

        label = Label("Settlement name: " + object.getSettlementName(), 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Population: " + str(object.getPopulation()), 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Founded in: " + str(object.getFounedIn()), 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        # label = Label("Residents:", 500, 20, self.font2)
        # self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine))
        # inspectorLine += 1
        # for resident in object.getResidents():
        #     label = Label(str(resident.getFirstName() + " " + str(resident.getLastName())), 500, 20, self.font2)
        #     self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.10, 20 * inspectorLine))
        #     inspectorLine += 1
        label = Label("Features:", 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        for feature in object.getFeatures():
            label = Label("Feature: " + str(feature.value[1]), 500, 20, self.font2)
            self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.10, 20 * self.writeLine + self.scroll_y))
            self.writeLine += 1


    def addInspectorForFamily(self, object):

        label = Label("Family name: " + object.getFamilyName(), 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Founding year: " + str(object.getFoundingYear()), 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Founded by: " + str(object.getFoundedBy().getFirstName()) + " " + str(object.getFoundedBy().getLastName()), 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Original region: " + str(object.getOriginRegion().getRegionName()), 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Original settlement: " + str(object.getOriginSettlement().getSettlementName()), 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1

    def addInspectorForPerson(self, object):

        label = Label("Name: " + str(object.getFirstName()), 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Last name: " + str(object.getLastName()), 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Family name: " + str(object.getFamilyName()), 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Year of birth: " + str(object.getYearOfBirth()), 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Age: " + str(object.getAge()), 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Sex: " + str(object.getSex().value[1]), 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        if object.getFather() != '':
            label = Label("Father: " + str(object.getFather().getFirstName()) + " " + str(object.getFather().getLastName()), 500, 20, self.font2)
            self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
            self.writeLine += 1
        if object.getMother() != '':
            label = Label("Mother: " + str(object.getMother().getFirstName()) + " " + str(object.getMother().getLastName()), 500, 20, self.font2)
            self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
            self.writeLine += 1
        if object.getSpouse() != None:
            label = Label("Spouse: " + str(object.getSpouse().getFirstName()) + " " + str(object.getSpouse().getLastName()), 500, 20, self.font2)
            self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
            self.writeLine += 1
        label = Label("Height: " + str(object.getHeight()), 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Hair Color: " + str(object.getHairColor().value[1]), 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Eye Color: " + str(object.getEyeColor().value[1]), 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Life events:", 500, 20, self.font2)
        self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.05, 20 * self.writeLine + self.scroll_y))
        self.writeLine += 1
        for liveEvent in object.getLifeEvent():
            label = Label(str(liveEvent), 700, 20, self.font2)
            self.inspectorScreenSurface.blit(label.localSurface, (self.width * 0.10, 20 * self.writeLine + self.scroll_y))
            self.writeLine += 1
