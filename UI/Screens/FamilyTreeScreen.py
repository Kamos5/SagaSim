import pygame

import Enums
from UI.Utils.Fonts import Fonts
from UI.Utils.Label import Label


class FamilyTreeScreen:

    def __init__(self, width, height, widthOffSet, heightOffSet, screenPosX, screenPosY):
        self.screenColor = 5, 25, 5
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
        self.rightPadding = self.width * 0.05

        self.familyTreeScreenSurface = pygame.Surface([self.width, self.height - self.heightOffSet])
        self.familyTreeScreenSurfaceObjsRect = []

    def getScroll_y(self):

        return self.scroll_y

    def setScroll_y(self, newValue):

        self.scroll_y = newValue

    def getFamilyTreeScreenSurface(self):
        return self.familyTreeScreenSurface

    def cleanScreen(self):

        self.familyTreeScreenSurface.fill(self.screenColor, (0, 0, self.width, self.height))
        self.familyTreeScreenSurfaceObjsRect = []

    def resetWriteLine(self):

        self.writeLine = 1

    def addTree(self, obj, showUpTree, showDownTree):

        localLabelSize = 350

        label = Label("Down Family Tree (from parent to child)", localLabelSize, self.lineHeight, self.textFont, True, showDownTree)
        self.familyTreeScreenSurfaceObjsRect.append([self.familyTreeScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y)), "DownTree"])
        label = Label("Up Family Tree (from child to parent)", localLabelSize, self.lineHeight, self.textFont, True, showUpTree)
        self.familyTreeScreenSurfaceObjsRect.append([self.familyTreeScreenSurface.blit(label.localSurface, (self.width - localLabelSize - self.rightPadding, self.lineHeight * self.writeLine + self.scroll_y)), "UpTree"])
        self.writeLine += 3

        if showUpTree:
            init = obj.initGenUpFamilyTree()
            self.printUpFamilyTree(init)
        if showDownTree:
            init = obj.initGenDownFamilyTree()
            self.printDownFamilyTree(init)

    def printDownFamilyTree(self, tree, level=0, prefix=""):

        screenYPosition = self.lineHeight * self.writeLine + self.scroll_y
        lifeSymbol = ""
        if tree.getRoot().getLifeStatus() == Enums.LifeStatus.DEAD:
            lifeSymbol = "†"

        if level == 0:
            if tree.getRoot().getSpouse() != None:
                labelString = (prefix + "" + tree.getRoot().getFirstName() + " " + lifeSymbol + " " + tree.getRoot().getLastName() + " (" + str(tree.getRoot().getYearOfBirth()) + "-" + str(tree.getRoot().getYearOfDeath()) + ")" + " Spouse:" + tree.getRoot().getSpouse().getFirstName() + " " + tree.getRoot().getSpouse().getFamilyName() + " (" + str(tree.getRoot().getSpouse().getYearOfBirth()) + "-" + str(tree.getRoot().getSpouse().getYearOfDeath()) + ")")
            else:
                labelString = (prefix + "" + tree.getRoot().getFirstName() + " " + lifeSymbol + " " + tree.getRoot().getLastName() + " (" + str(tree.getRoot().getYearOfBirth()) + "-" + str(tree.getRoot().getYearOfDeath()) + ")")
        else:

            if tree.getRoot().getFather() != "" and tree.getRoot().getMother() != "":

                labelString = (prefix + "" + tree.getRoot().getFirstName() + " " + lifeSymbol + " " + tree.getRoot().getLastName() + " (" + str(tree.getRoot().getYearOfBirth()) + "-" + str(tree.getRoot().getYearOfDeath()) + ")" + " <" + tree.getRoot().getFather().getFirstName() + " " + tree.getRoot().getFather().getLastName() + " + " + tree.getRoot().getMother().getFirstName() + " " + tree.getRoot().getMother().getFamilyName() + ">")

            else:
                labelString = (prefix + "" + tree.getRoot().getFirstName() + " " + lifeSymbol + " " + tree.getRoot().getLastName() + " (" + str(tree.getRoot().getYearOfBirth()) + "-" + str(tree.getRoot().getYearOfDeath()) + ")")


        if self.height >= screenYPosition:
        # if level <= maxLevel:
            label = Label(labelString, self.width - self.leftPadding - self.rightPadding, self.lineHeight, self.textFont, False)
            self.familyTreeScreenSurface.blit(label.localSurface, (self.leftPadding, screenYPosition))
            self.writeLine += 1

            if len(tree.getChildren()) > 0:
                for branch in tree.getChildren():
                    self.printDownFamilyTree(branch, level + 1, prefix + "-")


    def printUpFamilyTree(self, tree, level=0, prefix=""):

        maxLevel = 3
        labelString = ""
        sexPrefix = ""
        lifeSymbol = ""
        if tree is not None:
            if tree.getRoot().getLifeStatus() == Enums.LifeStatus.DEAD:
                lifeSymbol = "†"

            if len(tree.getRoot().getAllChildren()) > 0:
                if tree.getRoot().getSex() == Enums.Sexes.MALE:
                    sexPrefix = "Father: "
                else:
                    sexPrefix = "Mother: "

            if level == 0:
                sexPrefix = ""

            rootString = prefix + sexPrefix + tree.getRoot().getFirstName() + " " + lifeSymbol + " " + tree.getRoot().getLastName() + " (" + str(tree.getRoot().getYearOfBirth()) + "-" + str(tree.getRoot().getYearOfDeath()) + ")"
            siblingString = ""

            if len(tree.getSiblings()) > 0:
                siblingString += " Siblings:"
                for sibling in tree.getSiblings():
                    siblingString += " (" + sibling.getFirstName() + " " + sibling.getLastName() + ")"

            labelString = (rootString + siblingString)

            if level <= maxLevel:
                label = Label(labelString, self.width - self.leftPadding - self.rightPadding, self.lineHeight, self.textFont)
                self.familyTreeScreenSurface.blit(label.localSurface, (self.leftPadding, self.lineHeight * self.writeLine + self.scroll_y))
                self.writeLine += 1

                if tree.getRoot().getFather() != "":
                    self.printUpFamilyTree(tree.getFather(), level + 1, prefix + " ")

                if tree.getRoot().getMother() != "":
                    self.printUpFamilyTree(tree.getMother(), level + 1, prefix + " ")