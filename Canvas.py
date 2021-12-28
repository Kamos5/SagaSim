import pygame

from UI.Label import Label


class Canvas():

    def __init__(self):
        self.font1 = pygame.font.SysFont("calibri", 20)
        self.windowWidth = 1366
        self.windowHeight = 768
        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self.listScreen = pygame.Surface([int(self.windowWidth/2), self.windowHeight])
        self.listScroll_y = 0
        self.dateTimerObj = None
        self.regionsObjArray = []
        self.familiesObjArray = []
        self.personObjArray = []
        self.settlementsObjArray = []

    def clearCanvas(self):

        self.screen.fill((0, 0, 0), (0, 0, self.windowWidth, self.windowHeight))
        self.listScreen.fill((20, 20, 20), (0, 0, int(self.windowWidth/2), self.windowHeight))
        self.dateTimerObj = None
        self.regionsObjArray = []
        self.familiesObjArray = []

    def addDateTimer(self, world):

        label = Label("Year: " + str(world.getYear()), 100, 20, self.font1)
        self.dateTimerObj = self.screen.blit(label.localSurface, (self.windowWidth * 0.92, 0))

    def addFamilies(self, iteration):

        label = Label("Families: ", 300, 20, self.font1)
        self.FamiliesObj = self.listScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * iteration + self.listScroll_y))

    def addPerson(self, person, iteration):

        firstName = str(person.firstName)
        lastName = str(person.lastName)
        age = str (person.age)
        spouse = ''
        if person.spouse != None:
            spouse = person.spouse.firstName

        text = firstName + " " + lastName + " Age: " + age + " Spouse: " + spouse

        label = Label(text, 300, 20, self.font1)
        self.personObjArray.append([self.listScreen.blit(label.localSurface, (self.windowWidth * 0.15, 20 * iteration + self.listScroll_y)), person])

    def addFamily(self, family, iteration):

        text = str(family.getFamilyName() + " (" + str(family.getAliveMemberNumber()) + ")" + " Origin: " + str(family.getOriginRegion().getRegionName()))

        label = Label(text, 300, 20, self.font1)
        self.familiesObjArray.append([self.listScreen.blit(label.localSurface, (self.windowWidth * 0.10, 20 * iteration + self.listScroll_y)), family])

    def addRegions(self, iteration):

        label = Label("Regions: ", 200, 20, self.font1)
        self.listScreen.blit(label.localSurface, (self.windowWidth * 0.05, 20 * iteration + self.listScroll_y))


    def addRegion(self, region, iteration):

        label = Label(str(region.getRegionName()), 200, 20, self.font1)
        self.regionsObjArray.append([self.listScreen.blit(label.localSurface, (self.windowWidth * 0.10, 20 * iteration + self.listScroll_y)), region])

    def addSettlement(self, region, settlement, iteration):

        text = str(settlement.getSettlementName()) + " (" + str(settlement.getSettlementType().value) + ")" + " - alive population (" + str(settlement.getPopulation()) + ")"
        label = Label(text, 400, 20, self.font1)
        self.settlementsObjArray.append([self.listScreen.blit(label.localSurface, ((self.windowWidth * 0.15), 20 * iteration + self.listScroll_y)), region, settlement])

    def drawStuff(self, world, families, iteration):

        self.addRegions(iteration)
        iteration += 1

        for region in world.getRegions():
            self.addRegion(region, iteration)
            iteration += 1
            if region.getUIExpand():
                for settlement in region.getSettlements():
                    self.addSettlement(region, settlement, iteration)
                    iteration += 1

        self.addFamilies(iteration)
        iteration += 1

        for family in families:
            self.addFamily(family, iteration)
            iteration += 1
            if family.getUIExpand():
                for person in family.getAliveMembersList():
                    self.addPerson(person, iteration)
                    iteration += 1

        self.screen.blit(self.listScreen, (0, 0))
        return iteration

    def refreshScreen(self, world, families, scroll_y):


        self.listScroll_y = scroll_y
        iteration = 1
        self.clearCanvas()
        self.addDateTimer(world)
        iteration = self.drawStuff(world, families, iteration)
        pygame.display.update()


    def handleClickOnCollection(self, event, itemsObj):

        if itemsObj == 'regionsObjArray':
            itemsObj = self.regionsObjArray

        if itemsObj == 'familiesObjArray':
            itemsObj = self.familiesObjArray

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for itemObj in itemsObj:
                if itemObj[0].collidepoint(pos):
                    itemObj[1].setUIExpand(not itemObj[1].getUIExpand())
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
