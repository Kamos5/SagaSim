import pygame

from Family import Family
from Person import Person
from Region import Region
from Settlements import Settlements
from UI.Label import Label


class Canvas():

    def __init__(self):
        self.font1 = pygame.font.SysFont("calibri", 20)
        self.font2 = pygame.font.SysFont("calibri", 20)
        self.windowWidth = 1366
        self.windowHeight = 768
        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self.listScreen = pygame.Surface([int(self.windowWidth/2), self.windowHeight])
        self.detailsScreen = pygame.Surface([int(self.windowWidth/2), self.windowHeight])
        self.listScroll_y = 0
        self.detailsScroll_y = 0
        self.dateTimerObj = None
        self.regionsObjArray = []
        self.familiesObjArray = []
        self.personObjArray = []
        self.settlementsObjArray = []
        self.focusObj = None

    def clearCanvas(self):

        self.screen.fill((0, 0, 0), (0, 0, self.windowWidth, self.windowHeight))
        self.listScreen.fill((20, 20, 20), (0, 0, int(self.windowWidth/2), self.windowHeight))
        self.detailsScreen.fill((50, 50, 50), (0, 0, int(self.windowWidth/2), self.windowHeight))
        self.dateTimerObj = None
        self.listScreenObj = None
        self.detailsScreenObj = None
        self.regionsObjArray = []
        self.familiesObjArray = []
        self.settlementsObjArray = []
        self.personObjArray = []

    def addDateTimer(self, world):

        label = Label("Year: " + str(world.getYear()), 100, 20, self.font1)
        self.dateTimerObj = self.screen.blit(label.localSurface, (self.windowWidth * 0.92, 0))

    def addInspectorLabel(self):

        label = Label("Inspector: ", 100, 20, self.font1)
        self.detailsScreen.blit(label.localSurface, (0, 0))

    def addGeneralInspectorFields(self, inspectorLine, object):

        if isinstance(object, Region):
            inspectorLine = self.addInspectorForRegion(inspectorLine, object)
            return inspectorLine
        elif isinstance(object, Settlements):
            inspectorLine = self.addInspectorForSettlements(inspectorLine, object)
            return inspectorLine
        elif isinstance(object, Family):
            inspectorLine = self.addInspectorForFamily(inspectorLine, object)
            return inspectorLine
        elif isinstance(object, Person):
            inspectorLine = self.addInspectorForPerson(inspectorLine, object)
            return inspectorLine

    def addInspectorForRegion(self, inspectorLine, object):

        label = Label("Region name: " + object.getRegionName(), 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        label = Label("Settlements:", 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        for settlement in object.getSettlements():
            label = Label("Settlements name: " + settlement.getSettlementName(), 500, 20, self.font2)
            self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.10, 20 * inspectorLine + self.detailsScroll_y))
            inspectorLine += 1

        return inspectorLine

    def addInspectorForSettlements(self, inspectorLine, object):

        label = Label("Settlement name: " + object.getSettlementName(), 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        label = Label("Population: " + str(object.getPopulation()), 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        print(object.getFounedIn())
        label = Label("Founded in: " + str(object.getFounedIn()), 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        # label = Label("Residents:", 500, 20, self.font2)
        # self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine))
        # inspectorLine += 1
        # for resident in object.getResidents():
        #     label = Label(str(resident.getFirstName() + " " + str(resident.getLastName())), 500, 20, self.font2)
        #     self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.10, 20 * inspectorLine))
        #     inspectorLine += 1
        label = Label("Features:", 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        for feature in object.getFeatures():
            label = Label("Feature: " + str(feature.value[1]), 500, 20, self.font2)
            self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.10, 20 * inspectorLine + self.detailsScroll_y))
            inspectorLine += 1

        return inspectorLine

    def addInspectorForFamily(self, inspectorLine, object):

        label = Label("Family name: " + object.getFamilyName(), 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        label = Label("Founding year: " + str(object.getFoundingYear()), 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        label = Label("Founded by: " + str(object.getFoundedBy().getFirstName()) + " " + str(object.getFoundedBy().getLastName()), 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        label = Label("Original region: " + str(object.getOriginRegion().getRegionName()), 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        label = Label("Original settlement: " + str(object.getOriginSettlement().getSettlementName()), 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1

        return inspectorLine

    def addInspectorForPerson(self, inspectorLine, object):

        label = Label("Name: " + str(object.getFirstName()), 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        label = Label("Last name: " + str(object.getLastName()), 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        label = Label("Family name: " + str(object.getFamilyName()), 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        label = Label("Year of birth: " + str(object.getYearOfBirth()), 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        label = Label("Age: " + str(object.getAge()), 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        label = Label("Sex: " + str(object.getSex().value[1]), 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        if object.getFather() != '':
            label = Label("Father: " + str(object.getFather().getFirstName()) + " " + str(object.getFather().getLastName()), 500, 20, self.font2)
            self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
            inspectorLine += 1
        if object.getMother() != '':
            label = Label("Mother: " + str(object.getMother().getFirstName()) + " " + str(object.getMother().getLastName()), 500, 20, self.font2)
            self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
            inspectorLine += 1
        if object.getSpouse() != None:
            label = Label("Spouse: " + str(object.getSpouse().getFirstName()) + " " + str(object.getSpouse().getLastName()), 500, 20, self.font2)
            self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
            inspectorLine += 1
        label = Label("Height: " + str(object.getHeight()), 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        label = Label("Hair Color: " + str(object.getHairColor().value[1]), 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        label = Label("Eye Color: " + str(object.getEyeColor().value[1]), 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        label = Label("Life events:", 500, 20, self.font2)
        self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * inspectorLine + self.detailsScroll_y))
        inspectorLine += 1
        for liveEvent in object.getLifeEvent():
            label = Label(str(liveEvent), 700, 20, self.font2)
            self.detailsScreen.blit(label.localSurface, (self.windowWidth * 0.10, 20 * inspectorLine + self.detailsScroll_y))
            inspectorLine += 1

        return inspectorLine

    def addFamilies(self, listScreenLine):

        label = Label("Families: ", 300, 20, self.font1)
        self.FamiliesObj = self.listScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * listScreenLine + self.listScroll_y))

    def addPerson(self, person, listScreenLine):

        firstName = str(person.getFirstName())
        lastName = str(person.getLastName())
        age = str (person.age)
        spouse = ''
        if person.getSpouse() != None:
            spouse = person.spouse.getFirstName()

        text = firstName + " " + lastName + " Age: " + age + " Spouse: " + spouse

        if self.focusObj != person:
            label = Label(text, 300, 20, self.font1)

        if self.focusObj == person:
            label = Label(text, 300, 20, self.font1, 'active')

        self.personObjArray.append([self.listScreen.blit(label.localSurface, (self.windowWidth * 0.15, 20 * listScreenLine + self.listScroll_y)), person])

    def addFamily(self, family, listScreenLine):

        text = str(family.getFamilyName() + " (" + str(family.getAliveMemberNumber()) + ")" + " Origin: " + str(family.getOriginRegion().getRegionName()))

        if self.focusObj != family:
            label = Label(text, 300, 20, self.font1)

        if self.focusObj == family:
            label = Label(text, 300, 20, self.font1, 'active')

        self.familiesObjArray.append([self.listScreen.blit(label.localSurface, (self.windowWidth * 0.10, 20 * listScreenLine + self.listScroll_y)), family])

    def addRegions(self, listScreenLine):

        label = Label("Regions: ", 200, 20, self.font1)
        self.listScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * listScreenLine + self.listScroll_y))


    def addRegion(self, region, listScreenLine):

        if self.focusObj != region:
            label = Label(str(region.getRegionName()), 200, 20, self.font1)

        if self.focusObj == region:
            label = Label(str(region.getRegionName()), 200, 20, self.font1, 'active')

        self.regionsObjArray.append([self.listScreen.blit(label.localSurface, (self.windowWidth * 0.10, 20 * listScreenLine + self.listScroll_y)), region])

    def addSettlement(self, settlement, listScreenLine):

        text = str(settlement.getSettlementName()) + " (" + str(settlement.getSettlementType().value) + ")" + " - alive population (" + str(settlement.getPopulation()) + ")"

        if self.focusObj != settlement:
            label = Label(text, 400, 20, self.font1)

        if self.focusObj == settlement:
            label = Label(text, 400, 20, self.font1, 'active')

        self.settlementsObjArray.append([self.listScreen.blit(label.localSurface, ((self.windowWidth * 0.15), 20 * listScreenLine + self.listScroll_y)), settlement])

    def drawStuff(self, world, families):

        listScreenLine = 1
        inspectorLine = 1
        self.addRegions(listScreenLine)
        self.addInspectorLabel()
        if self.focusObj != None:
            self.addGeneralInspectorFields(inspectorLine, self.focusObj)
        listScreenLine += 1

        for region in world.getRegions():
            self.addRegion(region, listScreenLine)
            listScreenLine += 1
            if region.getUIExpand():
                for settlement in region.getSettlements():
                    self.addSettlement(settlement, listScreenLine)
                    listScreenLine += 1

        self.addFamilies(listScreenLine)
        listScreenLine += 1

        for family in families:
            self.addFamily(family, listScreenLine)
            listScreenLine += 1
            if family.getUIExpand():
                for person in family.getAliveMembersList():
                    self.addPerson(person, listScreenLine)
                    listScreenLine += 1

        self.listScreenObj = self.screen.blit(self.listScreen, (0, 0))
        self.detailsScreenObj = self.screen.blit(self.detailsScreen, (int(self.windowWidth/2), 20))
        return listScreenLine

    def refreshScreen(self, world, families, listScroll_y, detailsScroll_y):


        self.listScroll_y = listScroll_y
        self.detailsScroll_y = detailsScroll_y
        self.clearCanvas()
        self.addDateTimer(world)
        self.drawStuff(world, families)
        pygame.display.update()


    def handleClickOnCollection(self, event, itemsObj):

        if itemsObj == 'regionsObjArray':
            itemsObj = self.regionsObjArray

        if itemsObj == 'familiesObjArray':
            itemsObj = self.familiesObjArray

        if itemsObj == 'settlementsObjArray':
            itemsObj = self.settlementsObjArray

        if itemsObj == 'personObjArray':
            itemsObj = self.personObjArray

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for itemObj in itemsObj:
                if itemObj[0].collidepoint(pos):
                    if hasattr(itemObj[1], 'getUIExpand'):
                        itemObj[1].setUIExpand(not itemObj[1].getUIExpand())
                    self.focusObj = itemObj[1]
                    return True

            return False



    def pauseHandle(self, event, pausedPressed):

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if self.dateTimerObj.collidepoint(pos):
                pausedPressed = not pausedPressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pausedPressed = not pausedPressed

        return pausedPressed
