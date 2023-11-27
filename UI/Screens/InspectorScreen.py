import pygame

import Enums
from Family import Family
from House import House
from Person import Person
from Province import Province
from Region import Region
from Settlements import Settlements
from UI.Utils import Colors
from UI.Utils.Button import Button
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
        self.symbolFont = self.font.getSymbolFont()
        self.lineHeight = self.font.getLineHeight()
        self.scroll_y = 0
        self.screenPosX = screenPosX
        self.screenPosY = screenPosY
        self.leftPadding = self.width * 0.05

        self.inspectorScreenSurface = pygame.Surface([self.width, self.height - self.heightOffSet])
        self.inspectorScreenSurfaceObjsRect = []

        self.favoriteButton = None
        self.familyTreeButton = None
        self.provinceInRegionButton = None
        self.settlementInProvinceButton = None
        self.providesToButton = None
        self.unemployedResidentsButton = None
        self.unemployedResidentsPerson = None
        self.adminFeatureButton = None
        self.milFeatureButton = None
        self.prodFeatureButton = None
        self.foodFeatureButton = None
        self.adminFeatureWorkerButton = None
        self.milFeatureWorkerButton = None
        self.prodFeatureWorkerButton = None
        self.foodFeatureWorkerButton = None
        self.houseButton = None
        self.foundedByButton = None
        self.originalRegionButton = None
        self.originalSettlementButton = None
        self.houseResidentButton = None
        self.familyNameButton = None
        self.livingInSettlementButton = None
        self.personHouseButton = None
        self.personFatherButton = None
        self.personMotherButton = None
        self.personSpouseButton = None
        self.personLoverButton = None
        self.personExSpouseButton = None
        self.personDeceasedSpouseButton = None
        self.personFriendButton = None
        self.personRivalButton = None
        self.personAliveChildrenButton = None
        self.personDeceasedChildrenButton = None
        self.inspectorScreenButtons = []

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

            if isinstance(object, Province):
                self.addInspectorForProvince(object)

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
        for province in object.getProvinces():

            self.provinceInRegionButton = self.makeNewMultiButton(self.inspectorScreenButtons, province, 'provinceInRegion')
            self.provinceInRegionLabel = Label(f'{province.getName()}', 500, self.lineHeight, self.textFont, True)

            self.provinceInRegionLabel.changeColorOnHover(self.provinceInRegionButton.getOnHover())

            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.provinceInRegionLabel.localSurface, (self.leftPadding * 3, self.lineHeight * self.writeLine + self.scroll_y)), self.provinceInRegionButton])
            self.writeLine += 1

    def addInspectorForProvince(self, object):

        label = Label("Province name: " + object.getName(), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Last weather: " + object.getWeather().value[0], 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding * 2, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Settlements:", 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        for settlement in object.getSettlements():

            self.settlementInProvinceButton = self.makeNewMultiButton(self.inspectorScreenButtons, settlement, 'settlementInProvince')
            self.settlementInProvinceLabel = Label("Settlements name: " + settlement.getSettlementName(), 500, self.lineHeight, self.textFont, True)

            self.settlementInProvinceLabel.changeColorOnHover(self.settlementInProvinceButton.getOnHover())

            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.settlementInProvinceLabel.localSurface, (self.leftPadding*4, self.lineHeight * self.writeLine + self.scroll_y)), self.settlementInProvinceButton])
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

            self.providesToButton = self.makeNewMultiButton(self.inspectorScreenButtons, object.getProvision(), 'providesTo')
            self.providesToLabel = Label("Provides to: " + str(object.getProvision().getSettlementName()), 500, self.lineHeight, self.textFont, True)

            self.providesToLabel.changeColorOnHover(self.providesToButton.getOnHover())

            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.providesToLabel.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), self.providesToButton])
            self.writeLine += 1
        label = Label("Number of employed residents: " + str(len(object.getEmployedResidentsList())), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Number of unfit to work residents: " + str(len(object.getUnfitResidentsList())), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1

        self.unemployedResidentsButton = self.makeNewMultiButton(self.inspectorScreenButtons, object, 'unemployedResidents')
        self.unemployedResidenstLabel = Label("Number of unemployed residents: " + str(len(object.getUnemployedResidentsList())), 500, self.lineHeight, self.textFont, True)

        self.unemployedResidenstLabel.changeColorOnHover(self.unemployedResidentsButton.getOnHover())

        self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.unemployedResidenstLabel.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), self.unemployedResidentsButton])
        self.writeLine += 1

        if self.unemployedResidentsButton.getIsActive():
            for worker in object.getUnemployedResidentsList():

                self.unemployedResidentsPerson = self.makeNewMultiButton(self.inspectorScreenButtons, worker, 'unemployedPerson')
                self.unemployedPersonLabel = Label(str(worker.getFirstName() + " " + str(worker.getLastName())), 500, self.lineHeight, self.textFont, True)

                self.unemployedPersonLabel.changeColorOnHover(self.unemployedResidentsPerson.getOnHover())

                self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.unemployedPersonLabel.localSurface, (self.leftPadding * 3, self.lineHeight * self.writeLine + self.scroll_y)), self.unemployedResidentsPerson])
                self.writeLine += 1

        label = Label(f'Number of civilian workplaces: {object.getCivilianWorkplaces()}', 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label(f'Number of military personel: {object.getMilitaryNumber()}', 500, self.lineHeight, self.textFont)
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

        label = Label(f'Current technology researched: {object.getRegion().getOriginalCulture().getTechnologiesInProgress()[0].value[1]} ({object.getRegion().getOriginalCulture().getPercentOfTechnologyInProgress()} %)', 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1

        label = Label("Features:", 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1

        for feature in object.getAdminFeatures():

            self.adminFeatureButton = self.makeNewMultiButton(self.inspectorScreenButtons, feature, 'adminFeature')
            self.adminFeatureLabel = Label(f"Admin feature: {feature.getName()} < {feature.getFoundationType()['name']} ({feature.getWorkerListNumber()} / {feature.getMaxWorkersNumber()} )>", 500, self.lineHeight, self.textFont, True)
            self.adminFeatureLabel.changeColorOnHover(self.adminFeatureButton.getOnHover())

            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.adminFeatureLabel.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), self.adminFeatureButton])
            self.writeLine += 1
            if self.adminFeatureButton.getIsActive():
                for worker in feature.getWorkerList():
                    self.adminFeatureWorkerButton = self.makeNewMultiButton(self.inspectorScreenButtons, worker, 'adminWorkerFeature')
                    self.adminWorkerLabel = Label(str(worker.getFirstName() + " " + str(worker.getLastName())), 500, self.lineHeight, self.textFont, True)
                    self.adminWorkerLabel.changeColorOnHover(self.adminFeatureWorkerButton.getOnHover())

                    self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.adminWorkerLabel.localSurface, (self.leftPadding*3, self.lineHeight * self.writeLine + self.scroll_y)), self.adminFeatureWorkerButton])
                    self.writeLine += 1

        for feature in object.getMilitaryFeatures():

            self.milFeatureButton = self.makeNewMultiButton(self.inspectorScreenButtons, feature, 'milfeature')
            self.milFeatureLabel = Label(f"Military feature: {feature.getName()} < ({feature.getWorkerListNumber()} / {feature.getMaxWorkersNumber()} )>", 500, self.lineHeight, self.textFont, True)
            self.milFeatureLabel.changeColorOnHover(self.milFeatureButton.getOnHover())

            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.milFeatureLabel.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), self.milFeatureButton])
            self.writeLine += 1
            if self.milFeatureButton.getIsActive():
                for worker in feature.getWorkerList():
                    self.milFeatureWorkerButton = self.makeNewMultiButton(self.inspectorScreenButtons, worker, 'milWorkerFeature')
                    self.milWorkerLabel = Label(str(worker.getFirstName() + " " + str(worker.getLastName())), 500, self.lineHeight, self.textFont, True)
                    self.milWorkerLabel.changeColorOnHover(self.milFeatureWorkerButton.getOnHover())

                    self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.milWorkerLabel.localSurface, (self.leftPadding*3, self.lineHeight * self.writeLine + self.scroll_y)), self.milFeatureWorkerButton])
                    self.writeLine += 1

        for feature in object.getFoodFeatures():
            self.foodFeatureButton = self.makeNewMultiButton(self.inspectorScreenButtons, feature, 'foodfeature')
            self.foodFeatureLabel = Label(f"Food feature: {feature.getName()} < {feature.getFoundationType()['name']} ({feature.getWorkerListNumber()} / {feature.getMaxWorkersNumber()} )>", 500, self.lineHeight, self.textFont, True)
            self.foodFeatureLabel.changeColorOnHover(self.foodFeatureButton.getOnHover())

            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.foodFeatureLabel.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), self.foodFeatureButton])
            self.writeLine += 1
            if self.foodFeatureButton.getIsActive():
                for worker in feature.getWorkerList():
                    self.foodFeatureWorkerButton = self.makeNewMultiButton(self.inspectorScreenButtons, worker, 'foodWorkerFeature')
                    self.foodWorkerLabel = Label(str(worker.getFirstName() + " " + str(worker.getLastName())), 500, self.lineHeight, self.textFont, True)
                    self.foodWorkerLabel.changeColorOnHover(self.foodFeatureWorkerButton.getOnHover())

                    self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.foodWorkerLabel.localSurface, (self.leftPadding*3, self.lineHeight * self.writeLine + self.scroll_y)), self.foodFeatureWorkerButton])
                    self.writeLine += 1

        for feature in object.getProdFeatures():
            self.prodFeatureButton = self.makeNewMultiButton(self.inspectorScreenButtons, feature, 'prodfeature')
            self.prodFeatureLabel = Label(f"Prod feature: {feature.getName()} < {feature.getFoundationType()['name']} ({feature.getWorkerListNumber()} / {feature.getMaxWorkersNumber()} )>", 500, self.lineHeight, self.textFont, True)
            self.prodFeatureLabel.changeColorOnHover(self.prodFeatureButton.getOnHover())

            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.prodFeatureLabel.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), self.prodFeatureButton])
            self.writeLine += 1
            if self.prodFeatureButton.getIsActive():
                for worker in feature.getWorkerList():
                    self.prodFeatureWorkerButton = self.makeNewMultiButton(self.inspectorScreenButtons, worker, 'prodWorkerFeature')
                    self.prodWorkerLabel = Label(str(worker.getFirstName() + " " + str(worker.getLastName())), 500, self.lineHeight, self.textFont, True)
                    self.prodWorkerLabel.changeColorOnHover(self.prodFeatureWorkerButton.getOnHover())
                    self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.prodWorkerLabel.localSurface, (self.leftPadding*3, self.lineHeight * self.writeLine + self.scroll_y)), self.prodFeatureWorkerButton])
                    self.writeLine += 1

        self.housesLabel = Label("Houses: " + str(len(object.getHousing())), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(self.housesLabel.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        for house in object.getHousing():
            self.houseButton = self.makeNewMultiButton(self.inspectorScreenButtons, house, 'house')
            self.houseLabel = Label(f'{house.getHouseType().value.getHouseTypeName()} ({len(house.getHouseResidents())})', 500, self.lineHeight, self.textFont, True)
            self.houseLabel.changeColorOnHover(self.houseButton.getOnHover())

            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.houseLabel.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), self.houseButton])
            self.writeLine += 1

        self.writeLine = SingleLineSurface("Events:", 500, self.lineHeight, self.textFont, self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y, self.inspectorScreenSurface, self.writeLine)
        for liveEvent in object.getEvent():
            self.writeLine = MultiLineSurface(str(liveEvent), 500, self.lineHeight, self.textFont, self.leftPadding * 2, self.lineHeight * self.writeLine + self.scroll_y, self.inspectorScreenSurface, self.writeLine)

    def addInspectorForFamily(self, object):

        label = Label("Family name: " + object.getFamilyName(), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label("Founding year: " + str(object.getFoundingYear()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1

        self.foundedByButton = self.makeNewMultiButton(self.inspectorScreenButtons, object.getFoundedBy(), 'foundedBy')
        self.foundedByLabel = Label("Founded by: " + str(object.getFoundedBy().getFirstName()) + " " + str(object.getFoundedBy().getLastName()), 500, self.lineHeight, self.textFont, True)
        self.foundedByLabel.changeColorOnHover(self.foundedByButton.getOnHover())
        self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.foundedByLabel.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), self.foundedByButton])
        self.writeLine += 1

        self.originalRegionButton = self.makeNewMultiButton(self.inspectorScreenButtons, object.getOriginRegion(), 'originalRegion')
        self.originalRegionlabel = Label("Original region: " + str(object.getOriginRegion().getRegionName()), 500, self.lineHeight, self.textFont, True)
        self.originalRegionlabel.changeColorOnHover(self.originalRegionButton.getOnHover())
        self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.originalRegionlabel.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), self.originalRegionButton])
        self.writeLine += 1

        self.originalSettlementButton = self.makeNewMultiButton(self.inspectorScreenButtons, object.getOriginSettlement(), 'originalRegion')
        self.originalSettlementLabel = Label("Original settlement: " + str(object.getOriginSettlement().getSettlementName()), 500, self.lineHeight, self.textFont, True)
        self.originalSettlementLabel.changeColorOnHover(self.originalSettlementButton.getOnHover())
        self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.originalSettlementLabel.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), self.originalSettlementButton])
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
                self.houseResidentButton = self.makeNewMultiButton(self.inspectorScreenButtons, resident, 'houseResident')
                self.NameLabel = Label("Name: " + str(resident.getFirstName()), 500, self.lineHeight, self.textFont, True)
                self.NameLabel.changeColorOnHover(self.houseResidentButton.getOnHover())
                self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.NameLabel.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), self.houseResidentButton])
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

        self.favoriteButton = self.makeNewMultiButton(self.inspectorScreenButtons, object)
        self.favoriteLabel = Label("☆☆☆", 50, self.lineHeight, self.symbolFont, True)

        self.favoriteLabel.changeColorBasedOnActive(self.favoriteButton.getIsActive())
        self.favoriteLabel.changeColorOnHover(self.favoriteButton.getOnHover())

        self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.favoriteLabel.localSurface, (self.width-400, self.lineHeight * self.writeLine + self.scroll_y)), self.favoriteButton])
        self.writeLine += 1

        label = Label("Last name: " + str(object.getLastName()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1

        self.familyNameButton = self.makeNewMultiButton(self.inspectorScreenButtons, object.getFamilyObjectRef(), 'familyName')
        self.familyNameLabel = Label("Family name: " + str(object.getFamilyName()), 500, self.lineHeight, self.textFont, True)
        self.familyNameLabel.changeColorOnHover(self.familyNameButton.getOnHover())
        self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.familyNameLabel.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), self.familyNameButton])

        self.familyTreeButton = self.makeNewMultiButton(self.inspectorScreenButtons, object, 'familyTreeButton')
        self.familyTreeLabel = Label("Show family tree", 150, self.lineHeight, self.textFont, True)
        self.familyTreeLabel.changeColorOnHover(self.familyTreeButton.getOnHover())

        self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.familyTreeLabel.localSurface, (self.width - 150, self.lineHeight * self.writeLine + self.scroll_y)), self.familyTreeButton])
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
        label = Label(f'Happiness: {object.getHappiness()}', 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label(f'Happiness level: {object.getHappinessLevel().value[2]}', 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        label = Label(f'Life Status: {object.getLifeStatus().value}', 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        label = Label("♥", 25, self.lineHeight, self.symbolFont, textColor=Colors.getColorBasedOnParam(object.getLifeStatus()))
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding+500, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1

        label = Label(f'General Health Status: {object.getGeneralHealth().value[1]}', 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        label = Label("✚", 25, self.lineHeight, self.symbolFont, textColor=Colors.getColorBasedOnParam(object.getGeneralHealth()))
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding+500, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1

        if len(object.getCurrentInjuries()) > 0:
            label = Label("Suffer from injury:", 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            for injury in object.getCurrentInjuries():
                label = Label(str(injury[0]['name'] + " healed in: " + str(round(injury[2], 2)) + "%"), 500, self.lineHeight, self.textFont)
                self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y))
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
                label = Label(str(disease[0]['name'] + " immunity gained: " + str(round(disease[2], 2)) + "%"), 500, self.lineHeight, self.textFont)
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

        label = Label(f'Sex: {object.getSex().value[1]}', 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        if object.getSex() == Enums.Sexes.FEMALE:
            stringText = '♀'
        else:
            stringText = '♂'
        label = Label(stringText, 25, self.lineHeight, self.symbolFont, textColor=Colors.getColorBasedOnParam(object.getSex()))
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding + 500, self.lineHeight * self.writeLine + self.scroll_y))

        self.writeLine += 1
        if object.getSex() == Enums.Sexes.FEMALE and object.getAge() >= 15:
            label = Label("Is pregnant: " + str(object.getIsPregnant()), 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            if object.getImpregnationMonth() is not None:
                label = Label("Impregnation month: " + str(object.getImpregnationMonth().value[1]), 500, self.lineHeight, self.textFont)
                self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
                self.writeLine += 1

        self.livingInSettlementButton = self.makeNewMultiButton(self.inspectorScreenButtons, object.getSettlement(), 'livingInSettlement')
        self.livingInSettlementLabel = Label("Living in: " + str(object.getSettlement().getSettlementName()), 500, self.lineHeight, self.textFont, True)
        self.livingInSettlementLabel.changeColorOnHover(self.livingInSettlementButton.getOnHover())
        self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.livingInSettlementLabel.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), self.livingInSettlementButton])
        self.writeLine += 1

        if object.getAccommodation() is not None:

            self.personHouseButton = self.makeNewMultiButton(self.inspectorScreenButtons, object.getAccommodation(), 'personHouse')
            self.personHouseLabel = Label("House: " + str(object.getAccommodation().getHouseType().value.getHouseTypeName()), 500, self.lineHeight, self.textFont, True)
            self.personHouseLabel.changeColorOnHover(self.personHouseButton.getOnHover())
            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.personHouseLabel.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), self.personHouseButton])
            self.writeLine += 1
            label = Label("House dur: " + str(object.getAccommodation().getHouseDurability()), 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
        label = Label("Free wealth: " + str(object.getFreeWealth()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        if object.getFather() is not None:
            self.personFatherButton = self.makeNewMultiButton(self.inspectorScreenButtons, object.getFather(), 'personFather')
            self.personFatherLabel = Label("Father: " + str(object.getFather().getFirstName()) + " " + str(object.getFather().getLastName()), 500, self.lineHeight, self.textFont, True)
            self.personFatherLabel.changeColorOnHover(self.personFatherButton.getOnHover())
            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.personFatherLabel.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), self.personFatherButton])
            self.writeLine += 1
        if object.getMother() is not None:
            self.personMotherButton = self.makeNewMultiButton(self.inspectorScreenButtons, object.getMother(), 'personMother')
            self.personMotherLabel = Label("Mother: " + str(object.getMother().getFirstName()) + " " + str(object.getMother().getLastName()), 500, self.lineHeight, self.textFont, True)
            self.personMotherLabel.changeColorOnHover(self.personMotherButton.getOnHover())
            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.personMotherLabel.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), self.personMotherButton])
            self.writeLine += 1
        if object.getSpouse() is not None:
            if object.getSpouse().getSex() == Enums.Sexes.FEMALE:
                familyName = f' ({object.getSpouse().getFamilyName()})'
            else:
                familyName = f''
            self.personSpouseButton = self.makeNewMultiButton(self.inspectorScreenButtons, object.getSpouse(), 'personSpouse')
            self.personSpouseLabel = Label(f'Spouse: {object.getSpouse().getFirstName()} {object.getSpouse().getLastName()}{familyName}', 500, self.lineHeight, self.textFont, True)
            self.personSpouseLabel.changeColorOnHover(self.personSpouseButton.getOnHover())
            self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.personSpouseLabel.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), self.personSpouseButton])
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

        if len(object.getLovers()) > 0:
            label = Label("Lovers: ", 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            for lover in object.getLovers():
                self.personLoverButton = self.makeNewMultiButton(self.inspectorScreenButtons, lover, 'personLover')
                self.personLoverLabel = Label(f'{lover.getFirstName()} {lover.getLastName()}', 500, self.lineHeight, self.textFont, True)
                self.personLoverLabel.changeColorOnHover(self.personLoverButton.getOnHover())
                self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.personLoverLabel.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), self.personLoverButton])
                self.writeLine += 1

        if len(object.getExSpouses()) > 0:
            label = Label("Ex spouses: ", 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            for ex in object.getExSpouses():
                self.personExSpouseButton = self.makeNewMultiButton(self.inspectorScreenButtons, ex, 'personExSpouse')
                self.personExLabel = Label(str(ex.getFirstName()) + " " + str(ex.getLastName()), 500, self.lineHeight, self.textFont, True)
                self.personExLabel.changeColorOnHover(self.personExSpouseButton.getOnHover())
                self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.personExLabel.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), self.personExSpouseButton])
                self.writeLine += 1

        if len(object.getDeadSpouses()) > 0:
            label = Label("Deceased spouses: ", 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            for deceased in object.getDeadSpouses():
                self.personDeceasedSpouseButton = self.makeNewMultiButton(self.inspectorScreenButtons, deceased, 'personDeceasedSpouse')
                self.personDeceasedSpouseLabel = Label(str(deceased.getFirstName()) + " " + str(deceased.getLastName()), 500, self.lineHeight, self.textFont, True)
                self.personDeceasedSpouseLabel.changeColorOnHover(self.personDeceasedSpouseButton.getOnHover())
                self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.personDeceasedSpouseLabel.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), self.personDeceasedSpouseButton])
                self.writeLine += 1

        if len(object.getFriends()) > 0:
            label = Label("Friends: ", 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            for friend in object.getFriends():
                self.personFriendButton = self.makeNewMultiButton(self.inspectorScreenButtons, friend, 'personFriend')
                self.personFriendLabel = Label(f'{friend.getFirstName()} {friend.getLastName()}', 500, self.lineHeight, self.textFont, True)
                self.personFriendLabel.changeColorOnHover(self.personFriendButton.getOnHover())
                self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.personFriendLabel.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), self.personFriendButton])
                self.writeLine += 1

        if len(object.getRivals()) > 0:
            label = Label("Rivals: ", 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            for rival in object.getRivals():
                self.personRivalButton = self.makeNewMultiButton(self.inspectorScreenButtons, rival, 'personRival')
                self.personRivalLabel = Label(f'{rival.getFirstName()} {rival.getLastName()}', 500, self.lineHeight, self.textFont, True)
                self.personRivalLabel.changeColorOnHover(self.personRivalButton.getOnHover())
                self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.personRivalLabel.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), self.personRivalButton])
                self.writeLine += 1

        label = Label("Occupation: " + str(object.getOccupationName()), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        if object.getOccupation() is not None:
            label = Label("Workplace: " + str(object.getOccupation().getName()), 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1

        label = Label("Skills:", 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.writeLine += 1
        for skill in object.getSkills().getSkills():
            label = Label(f'Skill: {skill.getSkillName().value} XP: {skill.getSkillXp()} Level: {skill.getSkillLevel().value[1]}', 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding * 2, self.lineHeight * self.writeLine + self.scroll_y))
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
        label = Label("Skin Color: " + str(object.getSkinColor().value[1]), 500, self.lineHeight, self.textFont)
        self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
        self.drawCircle(self.width * 0.30 + self.lineHeight / 2, self.lineHeight * self.writeLine + self.scroll_y + self.lineHeight / 2, self.lineHeight / 2, (object.getSkinColor().value[2]))
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
                self.personAliveChildrenButton = self.makeNewMultiButton(self.inspectorScreenButtons, children, 'personAliveChildren')
                if children.getSex().value[1] == 'M':
                    self.personAliveChildrenLabel = Label("Son: " + children.getFirstName(), 500, self.lineHeight, self.textFont, True)
                else:
                    self.personAliveChildrenLabel = Label("Daughter: " + children.getFirstName(), 500, self.lineHeight, self.textFont, True)
                self.personAliveChildrenLabel.changeColorOnHover(self.personAliveChildrenButton.getOnHover())
                self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.personAliveChildrenLabel.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), self.personAliveChildrenButton])
                self.writeLine += 1
        if len(object.getDeadChildrens()) > 0:
            label = Label("Deceased childrens:", 500, self.lineHeight, self.textFont)
            self.inspectorScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
            self.writeLine += 1
            for children in object.getDeadChildrens():
                self.personDeceasedChildrenButton = self.makeNewMultiButton(self.inspectorScreenButtons, children, 'personDeceasedChildren')
                if children.getSex().value[1] == 'M':
                    self.personDeceasedChildrenLabel = Label("Son: " + children.getFirstName() + " (" + str(children.getAge()) + ")", 500, self.lineHeight, self.textFont, True)
                else:
                    self.personDeceasedChildrenLabel = Label("Daughter: " + children.getFirstName() + " (" + str(children.getAge()) + ")", 500, self.lineHeight, self.textFont, True)
                self.personDeceasedChildrenLabel.changeColorOnHover(self.personDeceasedChildrenButton.getOnHover())
                self.inspectorScreenSurfaceObjsRect.append([self.inspectorScreenSurface.blit(self.personDeceasedChildrenLabel.localSurface, (self.leftPadding*2, self.lineHeight * self.writeLine + self.scroll_y)), self.personDeceasedChildrenButton])
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


    def makeNewMultiButton(self, buttonsList, newButtonName, newButtonName2= '',shouldBeActive=False):

        for button in buttonsList:
            if button.getButtonName() == newButtonName and button.getButtonName2() == newButtonName2:
                return button
        newButton = Button(newButtonName, newButtonName2)
        buttonsList.append(newButton)
        if shouldBeActive:
            newButton.setActiveStatus()
        return newButton

    def getInspectorScreenButtons(self):
        return self.inspectorScreenButtons