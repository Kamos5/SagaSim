
import time

import CultureNames
import Events
import FamilyFunctions as FF
import FamilyInitGenerator as FIG
import FoundationTypes
import IOtools
import MembersInitGenerator as MIG
import Parameters
import pygame

import ProvinceNameGenerator
import Utils
from Family import Family
from Region import Region
from Settlements import Settlements
from UI import Canvas
from UI.Utils.TextField import TextField
from Person import Person
from World import World as World

world = World()
timeTesterFlag = False

def initFamilies():

    families = FIG.Init(world)

    return families


def initPeople(families):

    people = MIG.Init(families, world)

    for family in families:
        MIG.initInitMarrieges(family)

    return people


def running(world, manualOverride):

    timeTable = []

    dayOfWeekFlag = 1
    start = time.perf_counter()
    timers = True

    isAlive = 0
    isDead = 0
    malePop = 0
    femalePop = 0

    if manualOverride:
        input()

    worldtime = Utils.timeFunction(timers, world.increaseDay)

    print(str(world.getDay()) + "/" + str(world.getMonth()) + "/" + str(world.getYear()))

    terrytoryTime = Utils.timeFunction(False, Events.terrytoryManagement, world)
    weatherChangeTime = Utils.timeFunction(timers, world.weatherChange)
    incAgeTime = Utils.timeFunction(timers, Events.increaseAge, world)
    infectionsTime = Utils.timeFunction(timers, Events.infectionsSpread, world)
    diseasesTime = Utils.timeFunction(timers, Events.diseasesProgress, world)
    loveMakingTime = Utils.timeFunction(timers, Events.loveMaking, world)
    birthtime = Utils.timeFunction(timers, Events.birthPeopleNew, world)
    spouseMMTime = Utils.timeFunction(timers, FF.spouseMatchmaking, [world, timeTable])
    divorcesTime = Utils.timeFunction(timers, FF.divorces, world)
    breakSettlementsPopTime = Utils.timeFunction(timers, Events.settlementsPopulationManagement, world)     #ONCE PER YEAR (CHANCE 100% - PARAM)
    workersManagementTime = Utils.timeFunction(timers, Events.settlementWorkersManagement, world)           #DONE ! MAYBE OPTIMIZE IT SOMEHOW LATER ON
    crimeTime = Utils.timeFunction(timers, Events.crime, world)
    settlementGoodsProdTime = Utils.timeFunction(timers, Events.settlementGoodsProduction, world)           #ONCE PER WEEK (ALWAYS ON MONDAYS)
    accommodationManagmentTime = Utils.timeFunction(timers, Events.accommodationManagment, world)           #ONCE PER WEEK (ALWAYS ON MONDAYS)
    updateAliveTime = Utils.timeFunction(timers, world.updateAlive)
    associateManagementTime = Utils.timeFunction(timers, Events.assosiatesFriendsAndFoes, world)
    makeHistoryTime = Utils.timeFunction(timers, world.makeHistory)

    end = time.perf_counter()
    fullTime = end-start
    if fullTime > 0.0:
        print("WorldTime: " + str(worldtime) + " %: " + str(round(worldtime/fullTime, 2)))
        print("TerritoryTime: " + str(terrytoryTime) + " %: " + str(round(terrytoryTime/fullTime, 2)))
        print("WeaterTime: " + str(weatherChangeTime) + " %: " + str(round(weatherChangeTime / fullTime, 2)))
        print("IncAgeTime: " + str(incAgeTime) + " %: " + str(round(incAgeTime/fullTime, 2)))

        print("InfectionsTime: " + str(infectionsTime) + " %: " + str(round(infectionsTime/fullTime, 2)))
        print("DiseasesTime: " + str(diseasesTime) + " %: " + str(round(diseasesTime/fullTime, 2)))
        print("LovemakingTime: " + str(loveMakingTime) + " %: " + str(round(loveMakingTime / fullTime, 2)))
        print("BirthTime: " + str(birthtime) + " %: " + str(round(birthtime/fullTime, 2)))
        print("SpouseMMTime: " + str(spouseMMTime) + " %: " + str(round(spouseMMTime/fullTime, 2)))
        print("DivorcesTime: " + str(divorcesTime) + " %: " + str(round(divorcesTime / fullTime, 2)))
        print("BreakSettlementsPopTime: " + str(breakSettlementsPopTime) + " %: " + str(round(breakSettlementsPopTime/fullTime, 2)))
        print("WorkersManagementTime: " + str(workersManagementTime) + " %: " + str(round(workersManagementTime / fullTime, 2)))
        print("Crime: " + str(crimeTime) + " %: " + str(round(crimeTime / fullTime, 2)))
        print("SettlementGoodsProdTime: " + str(settlementGoodsProdTime) + " %: " + str(round(settlementGoodsProdTime / fullTime, 2)))
        print("AccomodationTime: " + str(accommodationManagmentTime) + " %: " + str(round(accommodationManagmentTime / fullTime, 2)))
        print("UpdateAliveTime: " + str(updateAliveTime) + " %: " + str(round(updateAliveTime / fullTime, 2)))
        print("AssociateMngTime: " + str(associateManagementTime) + " %: " + str(round(associateManagementTime / fullTime, 2)))
        print("MakeHistoryTime: " + str(makeHistoryTime) + " %: " + str(round(makeHistoryTime / fullTime, 2)))
        print(fullTime)

    timeTable.extend(["WorldTime", worldtime, "TerritoryTime", terrytoryTime, "WeaterTime", weatherChangeTime, "IncAgeTime", incAgeTime, "InfectionsTime", infectionsTime, "DiseasesTime", diseasesTime, "LovemakingTime", loveMakingTime, "BirthTime", birthtime, "SpouseMMTime", spouseMMTime, "DivorcesTime", divorcesTime, "BreakSettlementsPopTime", breakSettlementsPopTime, "WorkersManagementTime", workersManagementTime, "Crime", crimeTime, "SettlementGoodsProdTime", settlementGoodsProdTime, "AccomodationTime", accommodationManagmentTime, "UpdateAliveTime", updateAliveTime, "AssociateMngTime", associateManagementTime, "MakeHistoryTime", makeHistoryTime, "FullTime", fullTime])

    for family in world.getFamilies():
        isAlive += family.getAliveMemberNumber()
        isDead += family.getDeadMemberNumber()
        malePop += family.getMaleNumber()
        femalePop += family.getFemaleNumber()

    print("PeopleOBJNUMBER: " + str(len(world.getPeople())))
    print("Population alive: " + str(isAlive))
    print("Population dead: " + str(isDead))
    print("Population sum: " + str(isAlive+isDead))
    print("Male population: " + str(malePop))
    print("Female population: " + str(femalePop))
    print("Births: " + str(world.getBirthsPerYearTemp()))

    return (timeTable)

def main(popBreakLimit=None):

    world.reset()
    names = CultureNames.foundations
    world.setAllNames(names)
    world.setCultures(list(names.keys()))
    world.generateRegionsNames(Parameters.startingNumberOfRegions)
    ProvinceNameGenerator.makeListsForProvinceNames(world)
    world.getWorldMap().generateProvinces()
    world.pickRandomProvincesForRegions()
    world.generateSettlements()
    world.setFamilies(initFamilies())
    world.setPeople(initPeople(world.getFamilies()))
    world.diseases = IOtools.loadFiles('diseases')
    #print(names)

    windowWidth = 1024
    windowHeight = 768
    #pygame init stuff
    pygame.init()
    fps = 60
    clock = pygame.time.Clock()

    manualOverride = False

    sun = True

    pausedPressed = False
    regionPressed = ''

    tickStartTime = time.time() * 1000.0

    canvas = Canvas.Canvas()

    world.updateAlive()

    while sun:

        pCount = world.getGameSpeed()

        pTime = 1000 / pCount

        start = time.perf_counter()
        # VisualLogic
        canvas.clearCanvas()
        canvas.navBarScreen.addHelpButton()
        canvas.navBarScreen.addPlotsButton()
        canvas.navBarScreen.addWorldMapButton()
        canvas.navBarScreen.addGameSpeedCounter(world)
        canvas.navBarScreen.addDateTimer(world)
        canvas.drawStuff(world)

        end = time.perf_counter()
        timeUI = end - start
        print("UITime: " + str(timeUI))

        #GameLogic
        tickCurrentTime = time.time() * 1000.0
        if tickCurrentTime - tickStartTime >= pTime:
            timeTable = running(world, manualOverride)
            tickStartTime = time.time() * 1000.0


        pygame.display.update()
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        for event in pygame.event.get():

            pausedPressed = pygameEvents(event, canvas, pausedPressed)
            while pausedPressed:  #For Pausing and resuming
                for event in pygame.event.get():
                    pausedPressed = pygameEvents(event, canvas, pausedPressed)

                # print(time.perf_counter()) #TODO OGARNAC



        pygame.display.update()  # Call this only once per loop
        clock.tick(fps)

        if popBreakLimit is not None and len(world.getAlivePeople()) > popBreakLimit:
            return timeTable

        if world.getYear() == 1200:

            return


def pygameEvents(event, canvas, pausedPressed):

    #scrolling logic
    if event.type == pygame.MOUSEBUTTONDOWN:
        #scroll up
        if event.button == 4:
            pos = pygame.mouse.get_pos()
            if canvas.listScreenObj.collidepoint(pos) and not canvas.showHelp and not canvas.showPlots and not canvas.showFamilyScreen:
                scroll_y = min(canvas.listScreen.getScroll_y() + 50, 0)
                canvas.refreshScreen(world, scroll_y, canvas.inspectorScreen.getScroll_y(), canvas.familyTreeScreen.getScroll_y())
            if canvas.detailsScreenObj.collidepoint(pos) and not canvas.showHelp and not canvas.showPlots and not canvas.showFamilyScreen:
                scroll_y = min(canvas.inspectorScreen.getScroll_y() + 50, 0)
                canvas.refreshScreen(world, canvas.listScreen.getScroll_y(), scroll_y, canvas.familyTreeScreen.getScroll_y())

            if canvas.showFamilyScreen:
                if canvas.familyTreeScreenObj.collidepoint(pos):
                    scroll_y = min(canvas.familyTreeScreen.getScroll_y() + 50, 0)
                    canvas.refreshScreen(world, canvas.listScreen.getScroll_y(), canvas.inspectorScreen.getScroll_y(), scroll_y)
        # scroll down
        if event.button == 5:
            pos = pygame.mouse.get_pos()
            if canvas.listScreenObj.collidepoint(pos) and not canvas.showHelp and not canvas.showPlots and not canvas.showFamilyScreen:
                if canvas.listScreen.lineHeight*canvas.listScreen.writeLine > canvas.listScreen.height/2:
                    scroll_y = max(canvas.listScreen.getScroll_y() - 50, -int(canvas.listScreen.lineHeight*canvas.listScreen.writeLine) + canvas.listScreen.height/2)
                else:
                    scroll_y = 0
                canvas.refreshScreen(world, scroll_y, canvas.inspectorScreen.getScroll_y(), canvas.familyTreeScreen.getScroll_y())
            if canvas.detailsScreenObj.collidepoint(pos) and not canvas.showHelp and not canvas.showPlots and not canvas.showFamilyScreen:
                if canvas.inspectorScreen.lineHeight*canvas.inspectorScreen.writeLine > canvas.inspectorScreen.height/2:
                    scroll_y = max(canvas.inspectorScreen.getScroll_y() - 50, -int(canvas.inspectorScreen.lineHeight*canvas.inspectorScreen.writeLine) + canvas.inspectorScreen.height/2)
                else:
                    scroll_y = 0
                canvas.refreshScreen(world, canvas.listScreen.getScroll_y(), scroll_y, canvas.familyTreeScreen.getScroll_y())
            if canvas.showFamilyScreen:
                if canvas.familyTreeScreenObj.collidepoint(pos):
                    if canvas.familyTreeScreen.lineHeight*canvas.familyTreeScreen.writeLine > canvas.familyTreeScreen.height/2:
                        scroll_y = max(canvas.familyTreeScreen.getScroll_y() - 50, -int(canvas.familyTreeScreen.lineHeight*canvas.familyTreeScreen.writeLine) + canvas.familyTreeScreen.height/2)
                    else:
                        scroll_y = 0
                    canvas.refreshScreen(world, canvas.listScreen.getScroll_y(), canvas.inspectorScreen.getScroll_y(), scroll_y)

    if event.type == pygame.KEYDOWN:

        pCount = world.getGameSpeed()
        if event.key == pygame.K_KP_PLUS or event.key == pygame.K_PERIOD:
            if pCount == 1:
                pCount = 5
                world.setGameSpeedCounter(2)
            elif pCount == 5:
                pCount = 10
                world.setGameSpeedCounter(3)
            elif pCount == 10:
                pCount = 50
                world.setGameSpeedCounter(4)
            elif pCount == 50:
                pCount = 100
                world.setGameSpeedCounter(5)
            elif pCount == 100:
                pCount = 500
                world.setGameSpeedCounter(6)
            elif pCount == 500:
                pCount = 1000
                world.setGameSpeedCounter(7)
            elif pCount == 1000:
                pCount = 3000
                world.setGameSpeedCounter(8)
            world.setGameSpeed(pCount)

        if event.key == pygame.K_KP_MINUS or event.key == pygame.K_COMMA:
            if pCount == 3000:
                pCount = 1000
                world.setGameSpeedCounter(7)
            elif pCount == 1000:
                pCount = 500
                world.setGameSpeedCounter(6)
            elif pCount == 500:
                pCount = 100
                world.setGameSpeedCounter(5)
            elif pCount == 100:
                pCount = 50
                world.setGameSpeedCounter(4)
            elif pCount == 50:
                pCount = 10
                world.setGameSpeedCounter(3)
            elif pCount == 10:
                pCount = 5
                world.setGameSpeedCounter(2)
            elif pCount == 5:
                pCount = 1
                world.setGameSpeedCounter(1)
            world.setGameSpeed(pCount)

        # going to previous focusObj
        if event.key == pygame.K_END:
            if len(canvas.focusObj) > 0:
                canvas.focusObj.pop(len(canvas.focusObj)-1)
                canvas.refreshScreen(world, canvas.listScreen.getScroll_y(), canvas.inspectorScreen.getScroll_y(), canvas.familyTreeScreen.getScroll_y())

        if event.key == pygame.K_LEFT:

            if len(canvas.focusObj) > 0:
                lastFocusedObj = canvas.focusObj[len(canvas.focusObj) - 1]
                if hasattr(lastFocusedObj, 'getUIExpand'):
                    lastFocusedObj.setUIExpand(False)

        if event.key == pygame.K_RIGHT:

            if len(canvas.focusObj) > 0:
                lastFocusedObj = canvas.focusObj[len(canvas.focusObj) - 1]
                if hasattr(lastFocusedObj, 'getUIExpand'):
                    lastFocusedObj.setUIExpand(True)

        if event.key == pygame.K_UP:
            if len(canvas.focusObj) > 0:
                lastFocusedObj = canvas.focusObj[len(canvas.focusObj) - 1]

                if isinstance(canvas.focusObj[len(canvas.focusObj)-1], Person):
                    if lastFocusedObj.getFamilyObjectRef().getAliveMembersList().index(lastFocusedObj) > 0:
                        canvas.focusObj.append(lastFocusedObj.getFamilyObjectRef().getAliveMembersList()[lastFocusedObj.getFamilyObjectRef().getAliveMembersList().index(lastFocusedObj)-1])
                        return pausedPressed

                    if lastFocusedObj.getFamilyObjectRef().getAliveMembersList().index(lastFocusedObj) == 0:
                        canvas.focusObj.append(lastFocusedObj.getFamilyObjectRef())
                        return pausedPressed

                if isinstance(canvas.focusObj[len(canvas.focusObj) - 1], Family):
                    if world.getFamilies().index(lastFocusedObj) > 0:
                        lastFocusedObj.setUIExpand(False)
                        canvas.focusObj.append(world.getFamilies()[world.getFamilies().index(lastFocusedObj)-1])
                        return pausedPressed

                if isinstance(canvas.focusObj[len(canvas.focusObj) - 1], Settlements):
                    for region in world.getRegions():
                        for province in region.getProvinces():
                            for settlement in province.getSettlements():
                                if settlement == lastFocusedObj and province.getSettlements().index(lastFocusedObj) > 0:
                                    lastFocusedObj.setUIExpand(False)
                                    canvas.focusObj.append(province.getSettlements()[province.getSettlements().index(lastFocusedObj)-1])
                                    return pausedPressed

                                if settlement == lastFocusedObj and province.getSettlements().index(lastFocusedObj) == 0:
                                    lastFocusedObj.setUIExpand(False)
                                    canvas.focusObj.append(province)
                                    return pausedPressed

                if isinstance(canvas.focusObj[len(canvas.focusObj) - 1], Region):
                    if world.getRegions().index(lastFocusedObj) > 0:
                        lastFocusedObj.setUIExpand(False)
                        canvas.focusObj.append(world.getRegions()[world.getRegions().index(lastFocusedObj)-1])
                        return pausedPressed

        if event.key == pygame.K_DOWN:
            if len(canvas.focusObj) > 0:
                lastFocusedObj = canvas.focusObj[len(canvas.focusObj) - 1]

                if isinstance(canvas.focusObj[len(canvas.focusObj)-1], Person):
                    if lastFocusedObj.getFamilyObjectRef().getAliveMembersList().index(lastFocusedObj) < len(lastFocusedObj.getFamilyObjectRef().getAliveMembersList())-1:
                        canvas.focusObj.append(lastFocusedObj.getFamilyObjectRef().getAliveMembersList()[lastFocusedObj.getFamilyObjectRef().getAliveMembersList().index(lastFocusedObj)+1])
                        return pausedPressed

                if isinstance(canvas.focusObj[len(canvas.focusObj) - 1], Family):
                    if world.getFamilies().index(lastFocusedObj) < len(world.getFamilies()) - 1:
                        if not lastFocusedObj.getUIExpand():
                            canvas.focusObj.append(world.getFamilies()[world.getFamilies().index(lastFocusedObj)+1])
                            return pausedPressed
                        else:
                            if len(lastFocusedObj.getAliveMembersList()) > 0:
                                canvas.focusObj.append(lastFocusedObj.getAliveMembersList()[0])
                                return pausedPressed
                            else:
                                canvas.focusObj.append(world.getFamilies()[world.getFamilies().index(lastFocusedObj) + 1])
                                return pausedPressed

                if isinstance(canvas.focusObj[len(canvas.focusObj) - 1], Settlements):
                    for region in world.getRegions():
                        for province in region.getProvinces():
                            for settlement in province.getSettlements():
                                if settlement == lastFocusedObj and province.getSettlements().index(lastFocusedObj) < len(region.getSettlements())-1:
                                    if not lastFocusedObj.getUIExpand():
                                        canvas.focusObj.append(province.getSettlements()[province.getSettlements().index(lastFocusedObj)+1])
                                        return pausedPressed
                                    else:
                                        if len(settlement.getResidents()) > 0:
                                            canvas.focusObj.append(settlement.getResidents()[0])
                                            return pausedPressed
                                        else:
                                            canvas.focusObj.append(province.getSettlements[province.getSettlements().index(lastFocusedObj) + 1])
                                            return pausedPressed

                # if isinstance(canvas.focusObj[len(canvas.focusObj) - 1], Region):
                #     for region in world.getRegions():
                #         # if region == lastFocusedObj and world.getRegions().index(lastFocusedObj) < len(world.getRegions())-1:
                        #     if not lastFocusedObj.getUIExpand():
                        #         canvas.focusObj.append(world.getRegions()[world.getRegions().index(lastFocusedObj)+1])
                        #         return pausedPressed
                        #     else:
                        #         if len(lastFocusedObj.getSettlements()) > 0:
                        #             canvas.focusObj.append(lastFocusedObj.getSettlements()[0])
                        #             return pausedPressed
                        #         else:
                        #             canvas.focusObj.append(world.getRegions()[world.getRegions().index(lastFocusedObj)+1])
                        #             return pausedPressed

        if isinstance(canvas.lastFocusObj, TextField):

            # Check for backspace
            if event.key == pygame.K_BACKSPACE:

                # get text input from 0 to -1 i.e. end.
                canvas.lastFocusObj.setText(canvas.lastFocusObj.getText()[:-1])

            # Unicode standard is used for string
            # formation
            else:
                canvas.lastFocusObj.addText(event.unicode)
            canvas.refreshScreen(world, canvas.listScreen.getScroll_y(), canvas.inspectorScreen.getScroll_y(), canvas.familyTreeScreen.getScroll_y())

    collectionEvent, pausedPressed = canvas.handleClickOnCollection(event, pausedPressed)

    if collectionEvent:
        canvas.refreshScreen(world, canvas.listScreen.getScroll_y(), canvas.inspectorScreen.getScroll_y(), canvas.familyTreeScreen.getScroll_y())
        return pausedPressed

    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    # Pause from mousclick on Time
    pausedPressed = canvas.pauseHandle(event, pausedPressed)
    canvas.refreshScreen(world, canvas.listScreen.getScroll_y(), canvas.inspectorScreen.getScroll_y(), canvas.familyTreeScreen.getScroll_y())
    return pausedPressed

def callMain (popBreakLimit):
    return main(popBreakLimit)

main()