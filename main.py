import time
import Events
import FamilyFunctions as FF
import FamilyInitGenerator as FIG
import MembersInitGenerator as MIG
import Parameters
import pygame
from UI import Canvas
from UI.Utils.TextField import TextField
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

def running (world, families, people, manualOverride):

    start = time.perf_counter()
    print(world.getYear())

    isAliveFlag = False
    personUUIDFLAG = False
    personFirstNameFLAG = False
    personLastNameFLAG = False
    personSexFLAG = False
    personSexGen1FLAG = False
    personSexGen2FLAG = False
    personAgeFLAG = False
    personLifeSpanFLAG = False
    personModLifeSpanFLAG = False
    personLifeStatFLAG = False
    fatherFLAG = False
    fatherIDFLAG = False
    motherFLAG = False
    motherIDFLAG = False
    spouseFLAG = False
    causeOfDeathFLAG = False
    hairColorFLAG = False
    personHairColorGensFLAG = False
    deadChildrenListFLAG = False

    blackCount = 0
    brownCount = 0
    yellowCount = 0
    redCount = 0
    whiteCount = 0
    grayCount = 0
    timers = True

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

    if manualOverride:
        input()

    if timers:
        start1 = time.perf_counter()
    world.increaseYear()
    if timers:
        end1 = time.perf_counter()
        worldtime = end1 - start1
        start1 = time.perf_counter()
    Events.increaseAge(people, world)
    if timers:
        end1 = time.perf_counter()
        incAgeTime = end1 - start1
        start1 = time.perf_counter()
    Events.birthPeople(world, people)
    if timers:
        end1 = time.perf_counter()
        birthtime = end1 - start1
        start1 = time.perf_counter()
    FF.SpouseMatchmaking(families, people, world)
    if timers:
        end1 = time.perf_counter()
        spouseMMTime = end1 - start1
        start1 = time.perf_counter()
    Events.settlementsPopulationManagement(world, families)
    if timers:
        end1 = time.perf_counter()
        breakSettlementsPopTime = end1 - start1
        end = time.perf_counter()
        fullTime = end-start
        if fullTime > 0.0:
            print("WorldTime: " + str(worldtime) + " %: " + str(worldtime/fullTime))
            print("IncAgeTime: " + str(incAgeTime) + " %: " + str(incAgeTime/fullTime))
            print("BirthTime: " + str(birthtime) + " %: " + str(birthtime/fullTime))
            print("SpouseMMTime: " + str(spouseMMTime) + " %: " + str(spouseMMTime/fullTime))
            print("breakSettlementsPopTime: " + str(breakSettlementsPopTime) + " %: " + str(breakSettlementsPopTime/fullTime))
        print(fullTime)

    for family in families:
        isAlive += family.getAliveMemberNumber()
        isDead += family.getDeadMemberNumber()

    print("PeopleOBJNUMBER: " + str(len(people)))
    print("Population alive: " + str(isAlive))
    print("Population dead: " + str(isDead))
    print("Population sum: " + str(isAlive+isDead))



def main():

    world.generateRegions(Parameters.startingNumberOfRegions)
    world.generateSettlements()
    families = initFamilies()
    people = initPeople(families)

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

        canvas.drawStuff(world, families)

        #GameLogic
        tickCurrentTime = time.time() * 1000.0
        if tickCurrentTime - tickStartTime >= pTime:
            running(world, families, people, manualOverride)
            tickStartTime = time.time() * 1000.0


        pygame.display.update()

        for event in pygame.event.get():

            pausedPressed = pygameEvents(event, canvas, families, pausedPressed)
            while pausedPressed:  #For Pausing and resuming
                for event in pygame.event.get():
                    pausedPressed = pygameEvents(event, canvas, families, pausedPressed)


        pygame.display.update()  # Call this only once per loop
        clock.tick(fps)

        if world.getYear() == 1200:

            return

def pygameEvents(event, canvas, families, pausedPressed):

    #scrolling logic
    if event.type == pygame.MOUSEBUTTONDOWN:
        #scroll up
        if event.button == 4:
            pos = pygame.mouse.get_pos()
            if canvas.listScreenObj.collidepoint(pos):
                scroll_y = min(canvas.listScreen.getScroll_y() + 50, 0)
                canvas.refreshScreen(world, families, scroll_y, canvas.inspectorScreen.getScroll_y())
            elif canvas.detailsScreenObj.collidepoint(pos):
                scroll_y = min(canvas.inspectorScreen.getScroll_y() + 50, 0)
                canvas.refreshScreen(world, families, canvas.listScreen.getScroll_y(), scroll_y)
        # scroll down
        if event.button == 5:
            pos = pygame.mouse.get_pos()
            if canvas.listScreenObj.collidepoint(pos):
                if canvas.listScreen.lineHeight*canvas.listScreen.writeLine > canvas.listScreen.height/2:
                    scroll_y = max(canvas.listScreen.getScroll_y() - 50, -int(canvas.listScreen.lineHeight*canvas.listScreen.writeLine) + canvas.listScreen.height/2)
                else:
                    scroll_y = 0
                canvas.refreshScreen(world, families, scroll_y, canvas.inspectorScreen.getScroll_y())
            elif canvas.detailsScreenObj.collidepoint(pos):
                if canvas.inspectorScreen.lineHeight*canvas.inspectorScreen.writeLine > canvas.inspectorScreen.height/2:
                    scroll_y = max(canvas.inspectorScreen.getScroll_y() - 50, -int(canvas.inspectorScreen.lineHeight*canvas.inspectorScreen.writeLine) + canvas.inspectorScreen.height/2)
                else:
                    scroll_y = 0
                canvas.refreshScreen(world, families, canvas.listScreen.getScroll_y(), scroll_y)


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
        if event.key == pygame.K_LEFT:
            if len(canvas.focusObj) > 0:
                canvas.focusObj.pop(len(canvas.focusObj)-1)
                canvas.refreshScreen(world, families, canvas.listScreen.getScroll_y(), canvas.inspectorScreen.getScroll_y())
        if isinstance(canvas.lastFocusObj, TextField):

            # Check for backspace
            if event.key == pygame.K_BACKSPACE:

                # get text input from 0 to -1 i.e. end.
                canvas.lastFocusObj.setText(canvas.lastFocusObj.getText()[:-1])

            # Unicode standard is used for string
            # formation
            else:
                canvas.lastFocusObj.addText(event.unicode)
            canvas.refreshScreen(world, families, canvas.listScreen.getScroll_y(), canvas.inspectorScreen.getScroll_y())

    if canvas.handleClickOnCollection(event):
        canvas.refreshScreen(world, families, canvas.listScreen.getScroll_y(), canvas.inspectorScreen.getScroll_y())

    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    # Pause from mousclick on Time
    pausedPressed = canvas.pauseHandle(event, pausedPressed)
    canvas.refreshScreen(world, families, canvas.listScreen.getScroll_y(), canvas.inspectorScreen.getScroll_y())

    return pausedPressed

main()