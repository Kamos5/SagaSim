import pygame

class Canvas():

    def __init__(self):
        self.font1 = pygame.font.SysFont("calibri", 20)
        self.windowWidth = 1024
        self.windowHeight = 768
        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight))

    def clearCanvas(self):

        self.screen.fill((0, 0, 0), (0, 0, self.windowWidth, self.windowHeight))

    def addDateTimer(self, world):

        text = self.font1.render("Year: " + str(world.getYear()), True, (255, 255, 255))
        dateTimerObj = self.screen.blit(text, ((self.windowWidth * 0.90), 0))

        return dateTimerObj

    def addRegion(self, region, regionsObjArray, iteration):

        text = self.font1.render(str(region.getRegionName()), True, (255, 255, 255))
        regionsObjArray.append([self.screen.blit(text, ((self.windowWidth * 0.05), 20 * iteration)), region])

        return regionsObjArray

    def addSettlement(self, region, settlement, settlementsObjArray, iteration):
        text = self.font1.render(str(settlement.getSettlementName()) + " (" + str(settlement.getSettlementType().value) + ")" + " - alive population (" + str(settlement.getPopulation()) + ")", True, (255, 255, 255))
        settlementsObjArray.append([self.screen.blit(text, ((self.windowWidth * 0.10), 20 * iteration)), region, settlement])

        return settlementsObjArray

    def drawStuff(self, world, regionsObjArray, settlementsObjArray, iteration):

        for region in world.getRegions():
            regionsObjArray = self.addRegion(region, regionsObjArray, iteration)
            iteration += 1
            if region.getUIExpand():
                for settlement in region.getSettlements():
                    settlementsObjArray = self.addSettlement(region, settlement, settlementsObjArray, iteration)
                    iteration += 1

        return regionsObjArray, settlementsObjArray, iteration

    def refreshScreen(self, world, regionsObjArray, settlementsObjArray):

        iteration = 1
        self.screen.fill((0, 0, 0), (0, 0, self.windowWidth, self.windowHeight))
        self.addDateTimer(world)
        self.drawStuff(world, regionsObjArray, settlementsObjArray, iteration)
        pygame.display.update()


    def handleClickOnRegion(self, event, itemsObj):

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
