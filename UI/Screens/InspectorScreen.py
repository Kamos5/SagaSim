import pygame

import Enums
from Family import Family
from House import House
from Person import Person
from Region import Region
from Settlements import Settlements
from UI.Utils.Fonts import Fonts
from UI.Utils.Label import Label
from UI.Utils.MultiLineSurface import MultiLineSurface
from UI.Utils.SingleLineSurface import SingleLineSurface


class InspectorScreen:

    def __init__(self, width, height, widthOffSet, heightOffSet, screenPosX, screenPosY):

        self.screenColor = 25, 25, 25
        self.writeLine = 1
        self.width = width
        self.height = height
        self.widthOffSet = widthOffSet
        self.heightOffSet = heightOffSet
        self.font = Fonts()
        self.textFont = self.font.getFont2()
        self.lineHeight = self.font.getLineHeight()
        self.scroll_y = 0
        self.screenPosX = screenPosX
        self.screenPosY = screenPosY
        self.leftPadding = self.width * 0.05

        self.inspectorScreenSurface = pygame.Surface([self.width, self.height - self.heightOffSet])
        self.inspectorScreenSurfaceObjsRect = []

    def getScroll_y(self):

        return self.scroll_y

    def setScroll_y(self, newValue):

        self.scroll_y = newValue

    def resetWriteLine(self):

        self.writeLine = 1

    def cleanScreen(self):

        self.inspectorScreenSurface.fill(self.screenColor, (0, 0, self.width, self.height))
        self.inspectorScreenSurfaceObjsRect = []

    def getInspectorScreenSurface(self):
        return self.inspectorScreenSurface

    def addInspectorLabel(self):

        label = Label("Inspector: ", 100, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1

    def drawCircle (self, x, y, radius, color):

        r, g, b = color
        borderColor = (255-r, 255-g, 255-b)
        cirleColor = color
        borderPadding = 1
        borderWidth = 2
        radius = radius

        pygame.draw.circle(self.inspectorScreenSurface, borderColor, (x, y), radius- borderPadding)
        pygame.draw.circle(self.inspectorScreenSurface, cirleColor, (x, y), radius - borderWidth)

    def addGeneralInspectorFields(self, object):

        if isinstance(object, Region):
            self.addInspectorForRegion(object)

        elif isinstance(object, Settlements):
            self.addInspectorForSettlements(object)

        elif isinstance(object, Family):
            self.addInspectorForFamily(object)

        elif isinstance(object, Person):
            self.addInspectorForPerson(object)

        elif isinstance(object, House):
            self.addInspectorForHouses(object)


    def addInspectorForRegion(self, object):

        label = Label("Region name: " + object.getRegionName(), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Last weather: " + object.getWeather().value[0], 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding * 2, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Settlements:", 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        for settlement in object.getSettlements():
            label = Label("Settlements name: " + settlement.getSettlementName(), 500, self.lineHeight, self.textFont, True)
            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*3, self.lineHeight * self.writeLine + self.scroll_y)), settlement])
            self.writeLine += 1

        self.writeLine = SingleLineSurface("Events:", 500, self.lineHeight, self.textFont, self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y, self.inspectorScreenSurface, self.writeLine)
        for liveEvent in object.getEvent():

            self.writeLine = MultiLineSurface(str(liveEvent), 500, self.lineHeight, self.textFont, self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y, self.inspectorScreenSurface, self.writeLine)

    def addInspectorForSettlements(self, object):

        label = Label("Settlement name: " + object.getSettlementName(), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Population: " + str(object.getPopulation()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Founded in: " + str(object.getFounedIn()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        if object.getProvision() is not None:
            label = Label("Provides to: " + str(object.getProvision().getSettlementName()), 500, self.lineHeight, self.textFont, True)
            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), object.getProvision()])
            self.writeLine += 1
        label = Label("Number of employed residents: " + str(len(object.getEmployedResidentsList())), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Number of unemployed residents: " + str(len(object.getUnemployedResidentsList())), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label(f'Number of civilian workplaces: {object.getCivilianWorkplaces()}', 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        if (len(object.getEmployedResidentsList())+len(object.getUnemployedResidentsList())*100) > 0:
            label = Label("Percentage unemployed: " + str(round(len(object.getUnemployedResidentsList())/(len(object.getEmployedResidentsList())+len(object.getUnemployedResidentsList()))*100)) + "%", 500, self.lineHeight, self.textFont)
        else:
            label = Label("Percentage unemployed: " + "0%", 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Food produced last week: " + str(object.getSettlementFoodProducedLastYear()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Food consumed last week: " + str(object.getSettlementFoodConsumedLastYear()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Food net last week: " + str(object.getNetFoodLastYear()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Free food: " + str(object.getFreeFood()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Production produced last week: " + str(object.getSettlementProdProducedLastYear()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("All-time food prod: " + str(object.getSettlementFoodProduced()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Free production: " + str(object.getFreeProd()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Free wealth: " + str(object.getFreeWealth()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Income Tax Rate: " + str(round(object.getLocalIncomeTax(), 2)) + "%", 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1

        label = Label("Features:", 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1

        for feature in object.getAdminFeatures():
            label = Label("Admin feature: " + str(feature.getName()) + " <" + str(feature.getFoundationType().value.name) + " (" + str(feature.getWorkerListNumber()) + "/" + str(feature.getMaxWorkersNumber()) + ")> ", 500, self.lineHeight, self.textFont, True)
            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), feature])
            self.writeLine += 1
            if feature.getUIExpand():
                for worker in feature.getWorkerList():
                    label = Label(str(worker.getFirstName() + " " + str(worker.getLastName())), 500, self.lineHeight, self.textFont, True)
                    self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*3, self.lineHeight * self.writeLine + self.scroll_y)), worker])
                    self.writeLine += 1

        for feature in object.getFoodFeatures():
            label = Label("Food feature: " + str(feature.getName()) + " <" + str(feature.getFoundationType().value.name) + " (" + str(feature.getWorkerListNumber()) + "/" + str(feature.getMaxWorkersNumber()) + ")>", 500, self.lineHeight, self.textFont, True)
            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), feature])
            self.writeLine += 1
            if feature.getUIExpand():
                for worker in feature.getWorkerList():
                    label = Label(str(worker.getFirstName() + " " + str(worker.getLastName())), 500, self.lineHeight, self.textFont, True)
                    self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*3, self.lineHeight * self.writeLine + self.scroll_y)), worker])
                    self.writeLine += 1

        for feature in object.getProdFeatures():
            label = Label("Prod feature: " + str(feature.getName()) + " <" + str(feature.getFoundationType().value.name) + " (" + str(feature.getWorkerListNumber()) + "/" + str(feature.getMaxWorkersNumber()) + ")>", 500, self.lineHeight, self.textFont, True)
            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), feature])
            self.writeLine += 1
            if feature.getUIExpand():
                for worker in feature.getWorkerList():
                    label = Label(str(worker.getFirstName() + " " + str(worker.getLastName())), 500, self.lineHeight, self.textFont, True)
                    self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*3, self.lineHeight * self.writeLine + self.scroll_y)), worker])
                    self.writeLine += 1

        label = Label("Houses: " + str(len(object.getHousing())), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        for house in object.getHousing():
            label = Label(house.getHouseType().value.getHouseTypeName() + " (" + str(len(house.getHouseResidents())) + ")", 500, self.lineHeight, self.textFont, True)
            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), house])
            self.writeLine += 1

    def addInspectorForFamily(self, object):

        label = Label("Family name: " + object.getFamilyName(), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Founding year: " + str(object.getFoundingYear()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Founded by: " + str(object.getFoundedBy().getFirstName()) + " " + str(object.getFoundedBy().getLastName()), 500, self.lineHeight, self.textFont, True)
        self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), object.getFoundedBy()])
        self.writeLine += 1
        label = Label("Original region: " + str(object.getOriginRegion().getRegionName()), 500, self.lineHeight, self.textFont, True)
        self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), object.getOriginRegion()])
        self.writeLine += 1
        label = Label("Original settlement: " + str(object.getOriginSettlement().getSettlementName()), 500, self.lineHeight, self.textFont, True)
        self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), object.getOriginSettlement()])
        self.writeLine += 1

    def addInspectorForHouses(self, object):

        label = Label("House: " + str(object.getHouseType().value.getHouseTypeName()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("House dur: " + str(object.getHouseDurability()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Residents:", 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        if len(object.getHouseResidents()) > 0:
            for resident in object.getHouseResidents():
                label = Label("Name: " + str(resident.getFirstName()), 500, self.lineHeight, self.textFont, True)
                self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), resident])
                self.writeLine += 1
                label = Label("Age: " + str(resident.getAge()), 500, self.lineHeight, self.textFont)
                self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding * 2, self.lineHeight * self.writeLine + self.scroll_y))
                self.writeLine += 1
                label = Label("Free wealth: " + str(resident.getFreeWealth()), 500, self.lineHeight, self.textFont)
                self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*3, self.lineHeight * self.writeLine + self.scroll_y))
                self.writeLine += 1


    def addInspectorForPerson(self, object):

        label = Label("Name: " + str(object.getFirstName()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        label = Label("FAVORITE?", 95, self.lineHeight, self.textFont, True)
        self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.width-400, self.lineHeight * self.writeLine + self.scroll_y)), 'Favorite', object])
        self.writeLine += 1
        label = Label("Last name: " + str(object.getLastName()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Family name: " + str(object.getFamilyName()), 500, self.lineHeight, self.textFont, True)
        self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), object.getFamilyObjectRef()])
        label = Label("Show family tree", 150, self.lineHeight, self.textFont, True)
        self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.width - 150, self.lineHeight * self.writeLine + self.scroll_y)), 'FamilyTree', object])
        self.writeLine += 1
        label = Label("Day of birth: " + str(object.getDayOfBirth()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Month of birth: " + str(object.getMonthOfBirth().value[1]), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Year of birth: " + str(object.getYearOfBirth()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Age: " + str(object.getAge()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Life Status: " + str(object.getLifeStatus().value), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("General Health Status: " + str(object.getGeneralHealth().value[1]), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        if len(object.getInfections()) > 0:
            label = Label("Get infected by:", 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            for infection in object.getInfections():
                label = Label(str(infection[0]['name']), 500, self.lineHeight, self.textFont)
                self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y))
                self.writeLine += 1
        if len(object.getCurrentDiseases()) > 0:
            label = Label("Suffer from diseases:", 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            for disease in object.getCurrentDiseases():
                label = Label(str(disease[0]['name'] + " immunity gained: " + str(disease[2]) + "%"), 500, self.lineHeight, self.textFont)
                self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y))
                self.writeLine += 1
        if len(object.getImmunityTo()) > 0:
            label = Label("Immunities to diseases:", 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            for immunityTo in object.getImmunityTo():
                label = Label(str(immunityTo[0][0]['name']), 500, self.lineHeight, self.textFont)
                self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y))
                self.writeLine += 1
        label = Label("Sex: " + str(object.getSex().value[1]), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        if object.getSex() == Enums.Sexes.FEMALE and object.getAge() >= 15:
            label = Label("Is pregnant: " + str(object.getIsPregnant()), 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            if object.getImpregnationMonth() is not None:
                label = Label("Impregnation month: " + str(object.getImpregnationMonth().value[1]), 500, self.lineHeight, self.textFont)
                self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
                self.writeLine += 1
        label = Label("Living in: " + str(object.getSettlement().getSettlementName()), 500, self.lineHeight, self.textFont, True)
        self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), object.getSettlement()])
        self.writeLine += 1
        if object.getAccommodation() is not None:
            label = Label("House: " + str(object.getAccommodation().getHouseType().value.getHouseTypeName()), 500, self.lineHeight, self.textFont, True)
            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), object.getAccommodation()])
            self.writeLine += 1
            label = Label("House dur: " + str(object.getAccommodation().getHouseDurability()), 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
        label = Label("Free wealth: " + str(object.getFreeWealth()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        if object.getFather() is not None:
            label = Label("Father: " + str(object.getFather().getFirstName()) + " " + str(object.getFather().getLastName()), 500, self.lineHeight, self.textFont, True)
            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), object.getFather()])
            self.writeLine += 1
        if object.getMother() is not None:
            label = Label("Mother: " + str(object.getMother().getFirstName()) + " " + str(object.getMother().getLastName()), 500, self.lineHeight, self.textFont, True)
            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), object.getMother()])
            self.writeLine += 1
        if object.getSpouse() is not None:
            label = Label("Spouse: " + str(object.getSpouse().getFirstName()) + " " + str(object.getSpouse().getLastName()), 500, self.lineHeight, self.textFont, True)
            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), object.getSpouse()])
            self.writeLine += 1
            label = Label("Spouse relation: " + str(object.getSpouseRelation()), 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            label = Label("Spouse liked traits number: " + str(object.getSpouseNumberOfLikedTraits()), 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            label = Label("Spouse disliked traits number: " + str(object.getSpouseNumberOfDislikedTraits()), 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1

        if len(object.getExSpouses()) > 0:
            label = Label("Ex spouses: ", 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            for ex in object.getExSpouses():
                label = Label(str(ex.getFirstName()) + " " + str(ex.getLastName()), 500, self.lineHeight, self.textFont, True)
                self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), ex])
                self.writeLine += 1

        if len(object.getDeadSpouses()) > 0:
            label = Label("Deceased spouses: ", 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            for deceased in object.getDeadSpouses():
                label = Label(str(deceased.getFirstName()) + " " + str(deceased.getLastName()), 500, self.lineHeight, self.textFont, True)
                self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), deceased])
                self.writeLine += 1

        if len(object.getFriends()) > 0:
            label = Label("Friends: ", 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            for friend in object.getFriends():
                label = Label(f'{friend.getFirstName()} {friend.getLastName()}', 500, self.lineHeight, self.textFont, True)
                self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), friend])
                self.writeLine += 1

        if len(object.getRivals()) > 0:
            label = Label("Rivals: ", 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            for rival in object.getRivals():
                label = Label(f'{rival.getFirstName()} {rival.getLastName()}', 500, self.lineHeight, self.textFont, True)
                self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), rival])
                self.writeLine += 1

        label = Label("Occupation: " + str(object.getOccupationName()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        if object.getOccupation() is not None:
            label = Label("Workplace: " + str(object.getOccupation().getName()), 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
        label = Label("Height: " + str(object.getHeight()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Hair Color: " + str(object.getHairColor().value[1]), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.drawCircle(self.width * 0.30 + self.lineHeight/2, self.lineHeight * self.writeLine + self.scroll_y + self.lineHeight/2, self.lineHeight/2, (object.getHairColor().value[2]))
        #self.inspectorScreenSurface.fill(object.getHairColor().value[2], (self.width * 0.30 + 5, self.lineHeight * self.writeLine + self.scroll_y + 2, self.lineHeight - 4, self.lineHeight - 4))
        self.writeLine += 1
        label = Label("Eye Color: " + str(object.getEyeColor().value[1]), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.drawCircle(self.width * 0.30 + self.lineHeight / 2, self.lineHeight * self.writeLine + self.scroll_y + self.lineHeight / 2, self.lineHeight / 2, (object.getEyeColor().value[2]))
        #self.inspectorScreenSurface.fill(object.getEyeColor().value[2], (self.width * 0.30 + 5, self.lineHeight * self.writeLine + self.scroll_y + 2, self.lineHeight - 4, self.lineHeight - 4))
        self.writeLine += 1
        if len(object.getTraits()) > 0:
            traits = ""
            for trait in object.getTraits():
                traits += trait.value[1] + " "
            label = Label("Traits: " + str(traits).strip(), 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
        if len(object.getLikedTraits()) > 0:
            traits = ""
            for trait in object.getLikedTraits():
                traits += trait.value[1] + " "
            label = Label("Likes: " + str(traits).strip(), 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
        if len(object.getDislikedTraits()) > 0:
            traits = ""
            for trait in object.getDislikedTraits():
                traits += trait.value[1] + " "
            label = Label("Dislikes: " + str(traits).strip(), 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
        if len(object.getAliveChildrenList()) > 0:
            label = Label("Alive childrens:", 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            for children in object.getAliveChildrenList():
                if children.getSex().value[1] == 'M':
                    label = Label("Son: " + children.getFirstName(), 500, self.lineHeight, self.textFont, True)
                else:
                    label = Label("Daughter: " + children.getFirstName(), 500, self.lineHeight, self.textFont, True)
                self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), children])
                self.writeLine += 1
        if len(object.getDeadChildrens()) > 0:
            label = Label("Deceased childrens:", 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            for children in object.getDeadChildrens():
                if children.getSex().value[1] == 'M':
                    label = Label("Son: " + children.getFirstName() + " (" + str(children.getAge()) + ")", 500, self.lineHeight, self.textFont, True)
                else:
                    label = Label("Daughter: " + children.getFirstName() + " (" + str(children.getAge()) + ")", 500, self.lineHeight, self.textFont, True)
                self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), children])
                self.writeLine += 1

        self.writeLine = SingleLineSurface("Life events:", 500, self.lineHeight, self.textFont, self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y, self.inspectorScreenSurface, self.writeLine)

        # label = Label("Life events:", 500, self.lineHeight, self.textFont)
        # self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        # self.writeLine += 1
        for liveEvent in object.getLifeEvent():

            self.writeLine = MultiLineSurface(str(liveEvent), 750, self.lineHeight, self.textFont, self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y, self.inspectorScreenSurface, self.writeLine)
            # label = Label(str(liveEvent), 700, self.lineHeight, self.textFont)
            # self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y))
            # self.writeLine += 1
