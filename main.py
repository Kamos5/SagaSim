import time
import Events
import FamilyFunctions as FF
import FamilyInitGenerator as FIG
import MembersInitGenerator as MIG
import Parameters
import pygame
import sys

import Utils
from Family import Family
from FamilyTreeNode import BinaryTreeNode
from Region import Region
from Settlements import Settlements
from UI import Canvas
from UI.Utils.TextField import TextField
from Person import Person
from World import World as World

world = World()

def initFamilies():

    families = FIG.Init(world)

    return families

def initPeople(families):

    people = MIG.Init(families, world)

    for family in families:
        MIG.initInitMarrieges(family)

    return people

def running (world, manualOverride):

    start = time.perf_counter()
    print(world.getYear())
    timers = True

    # isAliveFlag = False
    # personUUIDFLAG = False
    # personFirstNameFLAG = False
    # personLastNameFLAG = False
    # personSexFLAG = False
    # personSexGen1FLAG = False
    # personSexGen2FLAG = False
    # personAgeFLAG = False
    # personLifeSpanFLAG = False
    # personModLifeSpanFLAG = False
    # personLifeStatFLAG = False
    # fatherFLAG = False
    # fatherIDFLAG = False
    # motherFLAG = False
    # motherIDFLAG = False
    # spouseFLAG = False
    # causeOfDeathFLAG = False
    # hairColorFLAG = False
    # personHairColorGensFLAG = False
    # deadChildrenListFLAG = False
    #
    # blackCount = 0
    # brownCount = 0
    # yellowCount = 0
    # redCount = 0
    # whiteCount = 0
    # grayCount = 0
    # for person in people:
    #
    #     printString = ''
    #     if (person.lifeStatus == Enums.LifeStatus.ALIVE or not isAliveFlag):
    #         if (personUUIDFLAG):
    #             printString += "UUID: " + person.personUUID + " "
    #         if (personFirstNameFLAG):
    #             printString += "FirstName: " + person.firstName + " "
    #         if (personLastNameFLAG):
    #             printString += "LastName: " + person.lastName + " "
    #         if (personSexFLAG):
    #             printString += "Sex: " + str(person.sex.value[1]) + " "
    #         if (personSexGen1FLAG):
    #             printString += "SexGen1: " + str(person.sexGen1[0].value[1]) + " "
    #         if (personSexGen2FLAG):
    #             printString += "SexGen2: " + str(person.sexGen2[0].value[1]) + " "
    #         if personAgeFLAG:
    #             printString += "Age: " + str(person.age) + " "
    #         if (personLifeSpanFLAG):
    #             printString += "Lifespan: " + str(person.lifespan) + " "
    #         if (personModLifeSpanFLAG):
    #             printString += "ModLifespan: " + str(person.modifiedLifespan) + " "
    #         if (personLifeStatFLAG):
    #             printString += "Status: " + person.lifeStatus.value + " "
    #         if (fatherFLAG):
    #             printString += "Father: " + PIF.findOneFirstName(people, person.father) + " "
    #         if (fatherIDFLAG):
    #             printString += "Father-id: " + person.father + " "
    #         if (motherFLAG):
    #             printString += "Mother: " + PIF.findOneFirstName(people, person.mother) + " "
    #         if (motherIDFLAG):
    #             printString += "Mother-id: " + person.mother + " "
    #         if (spouseFLAG):
    #             printString += "Spouse: " + PIF.findOneFirstName(people, person.spouse) + " "
    #         if (causeOfDeathFLAG):
    #             printString += "Status: " + person.causeOfDeath.value + " "
    #         if (hairColorFLAG):
    #             printString += "HairColor: " + str(person.hairColor) + " "
    #             if (person.hairColor == Enums.HairColor.BLACK):
    #                 blackCount += 1
    #             if (person.hairColor == Enums.HairColor.BROWN):
    #                 brownCount += 1
    #             if (person.hairColor == Enums.HairColor.RED):
    #                 redCount += 1
    #             if (person.hairColor == Enums.HairColor.YELLOW):
    #                 yellowCount += 1
    #             if (person.hairColor == Enums.HairColor.WHITE):
    #                 whiteCount += 1
    #             if (person.hairColor == Enums.HairColor.GRAY):
    #                 grayCount += 1
    #         if (personHairColorGensFLAG):
    #             printString += "HairColorGen1: " + str(person.hairColorGen1) + " "
    #             printString += "HairColorGen2: " + str(person.hairColorGen2) + " "
    #         if (deadChildrenListFLAG):
    #             printString += "DeadChildrenList: " + str(person.deadChildrens) + " "
        #if len(printString) > 0:
        #  print(printString)

    # print("Black count: " + str(blackCount))
    # print("Brown count: " + str(brownCount))
    # print("Yellow count: " + str(yellowCount))
    # print("Red count: " + str(redCount))
    # print("White count: " + str(whiteCount))
    # print("Gray count: " + str(grayCount))
    # print("Sum: " + str(blackCount + brownCount + yellowCount + redCount + whiteCount + grayCount))

    isAlive = 0
    isDead = 0
    malePop = 0
    femalePop = 0

    if manualOverride:
        input()

    if timers:
        start1 = time.perf_counter()
    world.increaseYear()
    if timers:
        end1 = time.perf_counter()
        worldtime = end1 - start1
        start1 = time.perf_counter()
    Events.increaseAge(world)
    if timers:
        end1 = time.perf_counter()
        incAgeTime = end1 - start1
        start1 = time.perf_counter()
    Events.birthPeople(world)
    if timers:
        end1 = time.perf_counter()
        birthtime = end1 - start1
        start1 = time.perf_counter()
    FF.SpouseMatchmaking(world)
    if timers:
        end1 = time.perf_counter()
        spouseMMTime = end1 - start1
        start1 = time.perf_counter()
    FF.Divorces(world)
    if timers:
        end1 = time.perf_counter()
        divorcesTime = end1 - start1
        start1 = time.perf_counter()
    Events.settlementsPopulationManagement(world)
    if timers:
        end1 = time.perf_counter()
        breakSettlementsPopTime = end1 - start1
        start1 = time.perf_counter()
    Events.settlementWorkersManagement(world)
    if timers:
        end1 = time.perf_counter()
        workersManagementTime = end1 - start1
        start1 = time.perf_counter()
    Events.crime(world)
    if timers:
        end1 = time.perf_counter()
        crimeTime = end1 - start1
        start1 = time.perf_counter()
    Events.settlementGoodsProduction(world)
    if timers:
        end1 = time.perf_counter()
        settlementGoodsProdTime = end1 - start1
        end = time.perf_counter()
        fullTime = end-start
        if fullTime > 0.0:
            print("WorldTime: " + str(worldtime) + " %: " + str(round(worldtime/fullTime, 2)))
            print("IncAgeTime: " + str(incAgeTime) + " %: " + str(round(incAgeTime/fullTime, 2)))
            print("BirthTime: " + str(birthtime) + " %: " + str(round(birthtime/fullTime, 2)))
            print("SpouseMMTime: " + str(spouseMMTime) + " %: " + str(round(spouseMMTime/fullTime, 2)))
            print("DivorcesTime: " + str(divorcesTime) + " %: " + str(round(divorcesTime / fullTime, 2)))
            print("BreakSettlementsPopTime: " + str(breakSettlementsPopTime) + " %: " + str(round(breakSettlementsPopTime/fullTime, 2)))
            print("WorkersManagementTime: " + str(workersManagementTime) + " %: " + str(round(workersManagementTime / fullTime, 2)))
            print("WorkersManagementTime: " + str(crimeTime) + " %: " + str(round(crimeTime / fullTime, 2)))
            print("SettlementGoodsProdTime: " + str(settlementGoodsProdTime) + " %: " + str(round(settlementGoodsProdTime / fullTime, 2)))
        print(fullTime)

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
    print("Divorces: " + str(world.getDivorcesNumber()))
    # print("Crimes: " + str(world.getCrimesPerYear()))


def main():

    world.generateRegions(Parameters.startingNumberOfRegions)
    world.generateSettlements()
    world.setFamilies(initFamilies())
    world.setPeople(initPeople(world.getFamilies()))

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

    while sun:

        pCount = world.getGameSpeed()

        pTime = 1000 / pCount

        # VisualLogic
        canvas.clearCanvas()
        canvas.navBarScreen.addHelp()
        canvas.navBarScreen.addDateTimer(world)

        canvas.drawStuff(world)

        #GameLogic
        tickCurrentTime = time.time() * 1000.0
        if tickCurrentTime - tickStartTime >= pTime:
            running(world, manualOverride)
            tickStartTime = time.time() * 1000.0


        pygame.display.update()

        for event in pygame.event.get():

            pausedPressed = pygameEvents(event, canvas, pausedPressed)
            while pausedPressed:  #For Pausing and resuming
                for event in pygame.event.get():
                    pausedPressed = pygameEvents(event, canvas, pausedPressed)


        pygame.display.update()  # Call this only once per loop
        clock.tick(fps)

        # FAMILY TREE UP (from child to parents)
        # if world.getYear() == 600:
        #     temp = world.getPeople()[len(world.getPeople())-1].generateUpFamilyTree(BinaryTreeNode(world.getPeople()[len(world.getPeople())-1]))
        #     Utils.printUpFamilyTree(temp)
        #     return
        # FAMILY TREE DOWN (parents to child)
        # if world.getYear() == 600:
        #     temp = world.getPeople()[0].generateDownFamilyTree(BinaryTreeNode(world.getPeople()[0]))
        #     Utils.printDownFamilyTree(temp)
        #     return
        if world.getYear() == 1200:

            return

def pygameEvents(event, canvas, pausedPressed):

    #scrolling logic
    if event.type == pygame.MOUSEBUTTONDOWN:
        #scroll up
        if event.button == 4:
            pos = pygame.mouse.get_pos()
            if canvas.listScreenObj.collidepoint(pos) and not canvas.showHelp and not canvas.showFamilyScreen:
                scroll_y = min(canvas.listScreen.getScroll_y() + 50, 0)
                canvas.refreshScreen(world, scroll_y, canvas.inspectorScreen.getScroll_y(), canvas.familyTreeScreen.getScroll_y())
            if canvas.detailsScreenObj.collidepoint(pos) and not canvas.showHelp and not canvas.showFamilyScreen:
                scroll_y = min(canvas.inspectorScreen.getScroll_y() + 50, 0)
                canvas.refreshScreen(world, canvas.listScreen.getScroll_y(), scroll_y, canvas.familyTreeScreen.getScroll_y())

            if canvas.showFamilyScreen:
                if canvas.familyTreeScreenObj.collidepoint(pos):
                    scroll_y = min(canvas.familyTreeScreen.getScroll_y() + 50, 0)
                    canvas.refreshScreen(world, canvas.listScreen.getScroll_y(), canvas.inspectorScreen.getScroll_y(), scroll_y)
        # scroll down
        if event.button == 5:
            pos = pygame.mouse.get_pos()
            if canvas.listScreenObj.collidepoint(pos) and not canvas.showHelp and not canvas.showFamilyScreen:
                if canvas.listScreen.lineHeight*canvas.listScreen.writeLine > canvas.listScreen.height/2:
                    scroll_y = max(canvas.listScreen.getScroll_y() - 50, -int(canvas.listScreen.lineHeight*canvas.listScreen.writeLine) + canvas.listScreen.height/2)
                else:
                    scroll_y = 0
                canvas.refreshScreen(world, scroll_y, canvas.inspectorScreen.getScroll_y(), canvas.familyTreeScreen.getScroll_y())
            if canvas.detailsScreenObj.collidepoint(pos) and not canvas.showHelp and not canvas.showFamilyScreen:
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
        if event.key == pygame.K_KP_PLUS:
            if pCount == 1:
                pCount = 5
            elif pCount == 5:
                pCount = 10
            elif pCount == 10:
                pCount = 50
            elif pCount == 50:
                pCount = 100
            elif pCount == 100:
                pCount = 500
            world.setGameSpeed(pCount)

        if event.key == pygame.K_KP_MINUS:
            if pCount == 500:
                pCount = 100
            elif pCount == 100:
                pCount = 50
            elif pCount == 50:
                pCount = 10
            elif pCount == 10:
                pCount = 5
            elif pCount == 5:
                pCount = 1
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
                        for settlement in region.getSettlements():
                            if settlement == lastFocusedObj and region.getSettlements().index(lastFocusedObj) > 0:
                                lastFocusedObj.setUIExpand(False)
                                canvas.focusObj.append(region.getSettlements()[region.getSettlements().index(lastFocusedObj)-1])
                                return pausedPressed

                            if settlement == lastFocusedObj and region.getSettlements().index(lastFocusedObj) == 0:
                                lastFocusedObj.setUIExpand(False)
                                canvas.focusObj.append(region)
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
                        for settlement in region.getSettlements():
                            if settlement == lastFocusedObj and region.getSettlements().index(lastFocusedObj) < len(region.getSettlements())-1:
                                if not lastFocusedObj.getUIExpand():
                                    canvas.focusObj.append(region.getSettlements()[region.getSettlements().index(lastFocusedObj)+1])
                                    return pausedPressed
                                else:
                                    if len(settlement.getResidents()) > 0:
                                        canvas.focusObj.append(settlement.getResidents()[0])
                                        return pausedPressed
                                    else:
                                        canvas.focusObj.append(region.getSettlements[region.getSettlements().index(lastFocusedObj) + 1])
                                        return pausedPressed

                if isinstance(canvas.focusObj[len(canvas.focusObj) - 1], Region):
                    for region in world.getRegions():
                        if region == lastFocusedObj and world.getRegions().index(lastFocusedObj) < len(world.getRegions())-1:
                            if not lastFocusedObj.getUIExpand():
                                canvas.focusObj.append(world.getRegions()[world.getRegions().index(lastFocusedObj)+1])
                                return pausedPressed
                            else:
                                if len(lastFocusedObj.getSettlements()) > 0:
                                    canvas.focusObj.append(lastFocusedObj.getSettlements()[0])
                                    return pausedPressed
                                else:
                                    canvas.focusObj.append(world.getRegions()[world.getRegions().index(lastFocusedObj)+1])
                                    return pausedPressed

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

    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    # Pause from mousclick on Time
    pausedPressed = canvas.pauseHandle(event, pausedPressed)
    canvas.refreshScreen(world, canvas.listScreen.getScroll_y(), canvas.inspectorScreen.getScroll_y(), canvas.familyTreeScreen.getScroll_y())

    return pausedPressed

main()