import pygame

class Canvas():

    def __init__(self):
        self.font1 = pygame.font.SysFont("calibri", 20)
        self.windowWidth = 1366
        self.windowHeight = 768
        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self.scroll_y = 0

    def clearCanvas(self):

        self.screen.fill((0, 0, 0), (0, 0, self.windowWidth, self.windowHeight))

    def addDateTimer(self, world):

        text = self.font1.render("Year: " + str(world.getYear()), True, (255, 255, 255))
        dateTimerObj = self.screen.blit(text, ((self.windowWidth * 0.90), self.scroll_y))

        return dateTimerObj

    def addFamilies(self, iteration):
        text = self.font1.render("Families:", True, (255, 255, 255))
        FamiliesObj = self.screen.blit(text, ((self.windowWidth * 0.05), 20 * iteration + self.scroll_y))

        return FamiliesObj


    def addPerson(self, person, iteration):

        firstName = str(person.firstName)
        lastName = str(person.lastName)
        age = str (person.age)
        spouse = ''
        if person.spouse != None:
            spouse = person.spouse.firstName

        text = self.font1.render(firstName + " " + lastName + " Age: " + age + " Spouse: " + spouse, True, (255, 255, 255))
        self.screen.blit(text, ((self.windowWidth * 0.15), 20 * iteration + self.scroll_y))

    def addFamily(self, family, familiesObjArray, iteration):

        text = self.font1.render(str(family.getFamilyName() + " (" + str(family.getAliveMemberNumber()) + ")" + " Origin: " + str(family.getOriginRegion().getRegionName())), True, (255, 255, 255))
        familiesObjArray.append([self.screen.blit(text, ((self.windowWidth * 0.10), 20 * iteration + self.scroll_y)), family])

        return familiesObjArray

    def addRegions(self, iteration):
        text = self.font1.render("Regions:", True, (255, 255, 255))
        regionsObj = self.screen.blit(text, ((self.windowWidth * 0.05), 20 * iteration + self.scroll_y))

    def addRegion(self, region, regionsObjArray, iteration):

        text = self.font1.render(str(region.getRegionName()), True, (255, 255, 255))
        regionsObjArray.append([self.screen.blit(text, ((self.windowWidth * 0.10), 20 * iteration + self.scroll_y)), region])

        return regionsObjArray

    def addSettlement(self, region, settlement, settlementsObjArray, iteration):
        text = self.font1.render(str(settlement.getSettlementName()) + " (" + str(settlement.getSettlementType().value) + ")" + " - alive population (" + str(settlement.getPopulation()) + ")", True, (255, 255, 255))
        settlementsObjArray.append([self.screen.blit(text, ((self.windowWidth * 0.15), 20 * iteration + self.scroll_y)), region, settlement])

        return settlementsObjArray

    def drawStuff(self, world, families, regionsObjArray, settlementsObjArray, familiesObjArray, iteration):

        self.addRegions(iteration)
        iteration += 1

        for region in world.getRegions():
            regionsObjArray = self.addRegion(region, regionsObjArray, iteration)
            iteration += 1
            if region.getUIExpand():
                for settlement in region.getSettlements():
                    settlementsObjArray = self.addSettlement(region, settlement, settlementsObjArray, iteration)
                    iteration += 1

        self.addFamilies(iteration)
        iteration += 1

        for family in families:
            familiesObjArray = self.addFamily(family, familiesObjArray, iteration)
            iteration += 1
            if family.getUIExpand():
                for person in family.getAliveMembersList():
                    self.addPerson(person, iteration)
                    iteration += 1


        return regionsObjArray, settlementsObjArray, iteration

    def refreshScreen(self, world, families, regionsObjArray, settlementsObjArray, peopleObjArray, scroll_y):


        self.scroll_y = scroll_y
        iteration = 1
        self.clearCanvas()
        self.addDateTimer(world)
        self.drawStuff(world, families, regionsObjArray, settlementsObjArray, peopleObjArray, iteration)
        pygame.display.update()


    def handleClickOnCollection(self, event, itemsObj, scroll_y):

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for itemObj in itemsObj:
                if itemObj[0].collidepoint(pos):
                    itemObj[1].setUIExpand(not itemObj[1].getUIExpand())
                    return True

            return False



    def pauseHandle(self, event, dateTimeObj, pausedPressed):

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if dateTimeObj.collidepoint(pos):
                pausedPressed = not pausedPressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pausedPressed = not pausedPressed

        return pausedPressed
