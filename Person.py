from Family import Family as FamilyObj
import Utils
import NameGenerator
from FamilyTreeNode import BinaryTreeNode
from Enums import LifeStatus, MaritalStatus, HairColor, CauseOfDeath, Sexes, EyeColor



class Person:

    def __init__(self):
        self.personUUID = Utils.createUUID()
        self.title = ''
        self.firstName = ''
        self.secondName = ''
        self.lastName = ''
        self.familyName = ''
        self.originFamilyObjRef = ''
        self.familyObjRef = ''
        self.homeRegion = ''
        self.region = ''
        self.homeSettlement = ''
        self.settlement = ''
        self.yearOfBirth = ''
        self.age = 0
        self.lifespan = 0
        self.modifiedLifespan = 0
        self.sex = Sexes.FEMALE
        # treated as always X chromosome + health : 0 always healthy
        self.sexGen1 = [Sexes.FEMALE, 0]
        # treated as X or Y chromosome : [sex,health]
        self.sexGen2 = [Sexes.FEMALE, 0]
        self.sexuality = 'hetero'
        self.fertility = 0
        self.numberOfChildren = 0
        self.mother = ''
        self.father = ''
        self.trueMother = ''
        self.trueFather = ''
        self.likeTraits = []
        self.dislikeTraits = []
        self.likeAtributes = []
        self.dislikeAtributes = []
        self.lover = ''
        self.spouse = None
        self.spouseRelation = 0
        self.spouseNumberOfLikedTraits = 0
        self.spouseNumberOfDislikedTraits = 0
        self.maritalStatus = MaritalStatus.SINGLE
        self.deadSpouses = []
        self.lifeStatus = LifeStatus.ALIVE
        self.causeOfDeath = CauseOfDeath.NULL
        self.hairColor = HairColor.GRAY
        self.heightGen = 0
        self.height = 0
        #TODO implement hairstyle
        self.hairStyle = ''
        # hair color gen + type : [haircolor, type] 0 - straight 1 - wavy 2 - curly 3 - coiled
        self.hairColorGen1 = [HairColor.GRAY, 0]
        self.hairColorGen2 = self.hairColorGen1
        self.eyeColor = EyeColor.GRAY
        self.eyeColorGen1 = [EyeColor.GRAY, 0]
        self.eyeColorGen2 = self.eyeColorGen1
        self.traits = []
        self.allChildren = []
        self.aliveChildren = []
        self.deadChildren = []
        self.lifeEvents = []
        self.occupation = None
        self.occupationName = ''
        self.freeWealth = 0
        self.familyTree = None
        self.yearOfDeath = ""
        self.happiness = 0
        self.personalSexualityModifier = 1
        pass

    def setInitValues(self, familyName, yearOfBirth, age, randomLifespan, sex, hairColor, hairColorGen1, hairColorGen2, eyeColor, eyeColorGen1, eyeColorGen2, familyObj):

        if sex == Sexes.MALE:
            self.firstName = NameGenerator.getRandomMNameForRegion(familyObj.getOriginRegion())
        else:
            self.firstName = NameGenerator.getRandomMNameForRegion(familyObj.getOriginRegion())

        self.familyName = familyName
        self.lastName = familyObj.familyName
        self.yearOfBirth = yearOfBirth-age
        self.age = age
        self.lifespan = randomLifespan
        self.modifiedLifespan = self.lifespan
        self.sex = sex
        if sex == Sexes.MALE:
            self.sexGen1 = [Sexes.FEMALE, 0]
            self.sexGen2 = [Sexes.MALE, 0]
        else:
            self.sexGen1 = [Sexes.FEMALE, 0]
            self.sexGen2 = [Sexes.FEMALE, 0]

        self.fertility = 50
        self.heightGen = Utils.randomRange(155, 165)
        self.height = self.heightGen
        self.hairColor = hairColor
        self.hairColorGen1 = hairColorGen1
        self.hairColorGen2 = hairColorGen2
        self.eyeColor = eyeColor
        self.eyeColorGen1 = eyeColorGen1
        self.eyeColorGen2 = eyeColorGen2
        self.familyObjRef = familyObj
        self.originFamilyObjRef = familyObj
        self.homeRegion = familyObj.getOriginRegion()
        self.region = self.homeRegion
        self.homeSettlement = familyObj.getOriginSettlement()
        self.settlement = self.homeSettlement
        self.personalSexualityModifier = 1

    def birthNewPerson(self, firstName, lastName, familyName, yearOfBirth, lifespan, sex, sexGen1, sexGen2, sexuality, fertility, height, hairColor, hairColorGen1, hairColorGen2, eyeColor, eyeColorGen1, eyeColorGen2, mother, father, trueMother, trueFather, familyObj):

        self.firstName = firstName
        self.lastName = lastName
        self.familyName = familyName
        self.yearOfBirth = yearOfBirth
        self.lifespan = lifespan
        self.modifiedLifespan = lifespan
        self.sex = sex
        self.sexGen1 = sexGen1
        self.sexGen2 = sexGen2
        self.sexuality = sexuality
        self.fertility = fertility
        self.heightGen = height
        self.hairColor = hairColor
        self.hairColorGen1 = hairColorGen1
        self.hairColorGen2 = hairColorGen2
        self.eyeColor = eyeColor
        self.eyeColorGen1 = eyeColorGen1
        self.eyeColorGen2 = eyeColorGen2
        self.mother = mother
        self.father = father
        self.trueMother = trueMother
        self.trueFather = trueFather
        self.originFamilyObjRef = familyObj
        self.familyObjRef = familyObj
        self.homeRegion = father.getRegion()
        self.homeSettlement = father.getSettlement()
        self.region = self.homeRegion
        self.settlement = self.homeSettlement



    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getFamilyName(self):
        return self.familyName

    def getYearOfBirth(self):
        return self.yearOfBirth

    def getYearOfDeath(self):
        return self.yearOfDeath

    def getSex(self):
        return self.sex

    def getAge(self):
        return self.age

    def getLifeStatus(self):
        return self.lifeStatus

    def increaseAge(self):
        self.age += 1

    def getFather(self):
        return self.father

    def getMother(self):
        return self.mother

    def getSpouse(self):
        return self.spouse

    def setSpouse(self, newSpouse):
        self.spouse = newSpouse

    def getHairColor(self):
        return self.hairColor

    def getHeight(self):
        return self.height

    def getEyeColor(self):
        return self.eyeColor

    def getLifeEvent(self):
        return self.lifeEvents

    def getAliveChildrenList(self):
        return self.aliveChildren

    def appendAliveChildrenList(self, newChild):
        self.allChildren.append(newChild)
        self.aliveChildren.append(newChild)

    def getAllChildren(self):
        return self.allChildren

    def getDeadChildrens(self):
        return self.deadChildren

    def appendDeadChildrenList(self, child):
        self.deadChildren.append(child)

    def getFamilyObjectRef(self):
        return self.familyObjRef

    def getOriginFamilyObjectRef(self):
        return self.originFamilyObjRef

    def setOriginFamilyObjectRef(self, newFamily):
        self.originFamilyObjRef = newFamily

    def changeLifeStatus(self, newLifeStatus):
        self.lifeStatus = newLifeStatus

    def getMaritialStatus(self):
        return self.maritalStatus

    def changeMaritalStatus(self, newMaritalStatus):
        self.maritalStatus = newMaritalStatus

    def getRegion(self):
        return self.region

    def setRegion(self, newRegion):
        self.region = newRegion

    def getSettlement(self):
        return self.settlement

    def setSettlement(self, newSettlement):
        self.settlement = newSettlement

    def increaseHeight(self):
        self.height = int(((-0.8 / self.age) + 1) * self.heightGen)

    def getTraits(self):
        return self.traits

    def addTrait(self, trait):
        if len(self.traits) < 3:
            self.traits.append(trait)

    def getLikedTraits(self):
        return self.likeTraits

    def addLikedTraits(self, trait):
        if len(self.likeTraits) < 3:
            self.likeTraits.append(trait)

    def getDislikedTraits(self):
        return self.dislikeTraits

    def addDislikedTraits(self, trait):
        if len(self.dislikeTraits) < 3:
            self.dislikeTraits.append(trait)

    def getSpouseNumberOfLikedTraits(self):
        return self.spouseNumberOfLikedTraits

    def setSpouseNumberOfLikedTraits(self, number):
        self.spouseNumberOfLikedTraits = number

    def changeSpouseNumberOfLikedTraits(self, number):
        self.spouseNumberOfLikedTraits += number

    def getSpouseNumberOfDislikedTraits(self):
        return self.spouseNumberOfDislikedTraits

    def setSpouseNumberOfDislikedTraits(self, number):
        self.spouseNumberOfDislikedTraits = number

    def changeSpouseNumberOfDislikedTraits(self, number):
        self.spouseNumberOfDislikedTraits += number

    def getOccupation(self):
        return self.occupation

    def setOccupation(self, occupation):
        self.occupation = occupation

    def getOccupationName(self):
        return self.occupationName

    def setOccupationName(self, occupationName):
        self.occupationName = occupationName

    def getFreeWealth(self):
        return self.freeWealth

    def setFreeWealth(self, newValue):
        self.freeWealth = round(newValue, 2)

    def changeFreeWealth(self, modifier):
        self.freeWealth += modifier
        self.freeWealth = round(self.freeWealth, 2)

    def getSpouseRelation(self):
        return self.spouseRelation

    def setSpouseRelation(self, newValue):
        self.spouseRelation = newValue

    def changeSpouseRelation(self, newValue):
        if self.spouseRelation + newValue > 300:
            self.spouseRelation = 300
        else:
            self.spouseRelation += newValue

    def getHappiness(self):
        return self.happiness

    def changeHappiness(self, newValue):
        self.happiness = newValue

    def getPersonalSexualModifier(self):
        return self.personalSexualityModifier

    def changeMultPersonalSexualModifier(self, newValue):
        self.personalSexualityModifier *= newValue

    def initGenDownFamilyTree(self):

        return self.generateDownFamilyTree(BinaryTreeNode(self))

    def initGenUpFamilyTree(self):

        return self.generateUpFamilyTree(BinaryTreeNode(self))

    def getAncestralFamilies(self):

        ancestorsFamiles = []
        tree = self.generateUpFamilyTree(BinaryTreeNode(self))

        ancestorsFamiles = self.getAncestralFamiliesAsListFromTree(tree, ancestorsFamiles)

        return ancestorsFamiles

    def getAncestralFamiliesAsListFromTree(self, tree, ancestorsFamiles = None, fatherSide = True, motherSide = True):

        if ancestorsFamiles is None:
            ancestorsFamiles = []

        father = ''
        mother = ''
        if fatherSide:
            father = tree.getRoot().getFather()
        if motherSide:
            mother = tree.getRoot().getMother()

        if fatherSide and father != '':
            if father.getOriginFamilyObjectRef() not in ancestorsFamiles:
                ancestorsFamiles.append(father.getOriginFamilyObjectRef())
            father.getAncestralFamiliesAsListFromTree(BinaryTreeNode(father), ancestorsFamiles)

        if motherSide and mother != '':
            if mother.getOriginFamilyObjectRef() not in ancestorsFamiles:
                ancestorsFamiles.append(mother.getOriginFamilyObjectRef())
            mother.getAncestralFamiliesAsListFromTree(BinaryTreeNode(mother), ancestorsFamiles)

        return ancestorsFamiles


    def generateDownFamilyTree(self, treeroot):

        for child in self.getAllChildren():
            treeroot.children.append(child.generateDownFamilyTree(BinaryTreeNode(child)))

        return treeroot

    def generateUpFamilyTree(self, treeroot):

        father = treeroot.getRoot().getFather()
        mother = treeroot.getRoot().getMother()
        if father != '':
            for fatherChild in father.getAllChildren():
                if fatherChild != treeroot.getRoot():
                    treeroot.siblings.append(fatherChild)
            treeroot.father = father.generateUpFamilyTree(BinaryTreeNode(father))

        if mother != '':
            for motherChild in mother.getAllChildren():
                if motherChild != treeroot.getRoot() and motherChild not in treeroot.siblings:
                        treeroot.siblings.append(motherChild)
            treeroot.mother = mother.generateUpFamilyTree(BinaryTreeNode(mother))

        return treeroot

