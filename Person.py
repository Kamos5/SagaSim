import Enums
import Skills
import Utils
import NameGenerator
from FamilyTreeNode import BinaryTreeNode
from Enums import LifeStatus, MaritalStatus, HairColor, CauseOfDeath, Sexes, EyeColor, GeneralHealth, SkinColor
from House import House


class Person:

    def __init__(self):
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
        self.isPregnant = None
        self.impregnationMonth = None
        self.laborDay = 1
        self.laborMonth = None
        self.pregnancyFather = None
        self.pregnancyTrueFather = None
        self.lastBirthMonth = Enums.Months.JANUARY
        self.mother = None
        self.father = None
        self.trueMother = None
        self.trueFather = None
        self.likeTraits = []
        self.dislikeTraits = []
        self.likeAtributes = []
        self.dislikeAtributes = []
        self.lovers = []
        self.knownAssociates = []
        self.friends = []
        self.rivals = []
        self.spouse = None
        self.spouseRelation = 0
        self.spouseNumberOfLikedTraits = 0
        self.spouseNumberOfDislikedTraits = 0
        self.maritalStatus = MaritalStatus.SINGLE
        self.deadSpouses = []
        self.exSpouses = []
        self.lifeStatus = LifeStatus.ALIVE
        self.generalHealth = GeneralHealth.HEALTHY
        self.healthFromAge = GeneralHealth.HEALTHY
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
        self.skinColor = SkinColor.ALBIN
        self.skinColorGen1 = [SkinColor.ALBIN, 0]
        self.skinColorGen2 = self.skinColorGen1
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
        self.happinessLevel = Enums.HappinessLevel.CONTENT
        self.personalSexualityModifier = 1
        self.accommodation = None
        self.realEstate = []
        self.iqGen = 0
        self.iq = 0
        self.immunityTo = []
        self.currentDiseases = []
        self.currentInjuries = []
        self.infections = []
        self.skills = Skills.Skills()
        pass

    def setInitValues(self, familyName, yearOfBirth, age, randomLifespan, sex, hairColor, hairColorGen1, hairColorGen2, eyeColor, eyeColorGen1, eyeColorGen2, skinColor, skinColorGen1, skinColorGen2, familyObj):

        if sex == Sexes.MALE:
            self.firstName = NameGenerator.getRandomMNameForRegion(familyObj.getOriginRegion().getRegionNumber())
        else:
            self.firstName = NameGenerator.getRandomFNameForRegion(familyObj.getOriginRegion().getRegionNumber())

        self.familyName = familyName
        self.lastName = familyObj.familyName
        self.yearOfBirth = yearOfBirth-age
        self.monthOfBirth = Utils.randomFromEnumCollection(Enums.Months)
        self.dayOfBirth = Utils.randomRange(1, self.getMonthOfBirth().value[2])
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
            self.isPregnant = False

        self.fertility = 50
        if sex == Sexes.MALE:
            self.heightGen = Utils.randomRange(150, 160)
        else:
            self.heightGen = Utils.randomRange(140, 150)
        self.height = self.heightGen
        self.hairColor = hairColor
        self.hairColorGen1 = hairColorGen1
        self.hairColorGen2 = hairColorGen2
        self.eyeColor = eyeColor
        self.eyeColorGen1 = eyeColorGen1
        self.eyeColorGen2 = eyeColorGen2
        self.skinColor = skinColor
        self.skinColorGen1 = skinColorGen1
        self.skinColorGen2 = skinColorGen2
        self.familyObjRef = familyObj
        self.originFamilyObjRef = familyObj
        self.homeRegion = familyObj.getOriginRegion()
        self.region = self.homeRegion
        self.homeSettlement = familyObj.getOriginSettlement()
        self.settlement = self.homeSettlement
        self.settlement.increasePopulation()
        self.settlement.addResident(self)
        self.personalSexualityModifier = 1
        self.accommodation = House()

    def birthNewPerson(self, firstName, lastName, familyName, dayOfBirth, monthOfBirth, yearOfBirth, lifespan, sex, sexGen1, sexGen2, sexuality, fertility, height, hairColor, hairColorGen1, hairColorGen2, eyeColor, eyeColorGen1, eyeColorGen2, skinColor, skinColorGen1, skinColorGen2, mother, father, trueMother, trueFather, familyObj, immunities):

        self.firstName = firstName
        self.lastName = lastName
        self.familyName = familyName
        self.yearOfBirth = yearOfBirth
        self.monthOfBirth = monthOfBirth
        self.dayOfBirth = dayOfBirth
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
        self.skinColor = skinColor
        self.skinColorGen1 = skinColorGen1
        self.skinColorGen2 = skinColorGen2
        self.mother = mother
        self.father = father
        self.trueMother = trueMother
        self.trueFather = trueFather
        self.originFamilyObjRef = familyObj
        self.familyObjRef = familyObj
        if father is not None:
            self.homeRegion = father.getRegion()
            self.homeSettlement = father.getSettlement()
        else:
            self.homeRegion = mother.getRegion()
            self.homeSettlement = mother.getSettlement()
        self.region = self.homeRegion
        self.settlement = self.homeSettlement
        self.setAccommodation(trueMother.getAccommodation())
        self.immunityTo = immunities


    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getFamilyName(self):
        return self.familyName

    def getMonthOfBirth(self):
        return self.monthOfBirth

    def getDayOfBirth(self):
        return self.dayOfBirth

    def getYearOfBirth(self):
        return self.yearOfBirth

    def getYearOfDeath(self):
        return self.yearOfDeath

    def getSex(self):
        return self.sex

    def getSexGen1(self):
        return self.sexGen1

    def getSexGen2(self):
        return self.sexGen2

    def getSexuality(self):
        return self.sexuality

    def getAge(self):
        return self.age

    def getLifeStatus(self):
        return self.lifeStatus

    def getGeneralHealth(self):
        return self.generalHealth

    def setGeneralHelth(self, newHealth):
        self.generalHealth = newHealth

    def getHealthFromAge(self):
        return self.healthFromAge

    def setHealthFromAge(self, newHealth):
        self.healthFromAge = newHealth


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

    def getSkinColor(self):
        return self.skinColor

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

    def getDeadSpouses(self):
        return self.deadSpouses

    def addDeadSpouse(self, deadSpouse):
        self.deadSpouses.append(deadSpouse)

    def getExSpouses(self):
        return self.exSpouses

    def addExSpouse(self, ex):
        self.exSpouses.append(ex)

    def getLovers(self):
        return self.lovers

    def getKnownAssociates(self):
        return self.knownAssociates

    def addKnownAssociates(self, newAssociate):
        self.knownAssociates.append(newAssociate)

    def getLovers(self):
        return self.lovers

    def addLover(self, lover):
        self.lovers.append(lover)

    def removeLover(self, lover):
        self.lovers.remove(lover)

    def getFriends(self):
        return self.friends

    def addFriends(self, newFriend):
        self.friends.append(newFriend)

    def removeFriend(self, friend):
        self.friends.remove(friend)

    def getRivals(self):
        return self.rivals

    def addRivals(self, newRivals):
        self.rivals.append(newRivals)

    def removeRival(self, rival):
        self.rivals.remove(rival)

    def getImpregnationMonth(self):
        return self.impregnationMonth

    def setImpregnationMonth(self, month):
        self.impregnationMonth = month

    def getLaborDay(self):
        return self.laborDay

    def getLaborMonth(self):
        return self.laborMonth

    def setLaborMonth(self, month):
        self.laborMonth = month

    def setLaborDay(self, impregnationMonth):

        if impregnationMonth == Enums.Months.JANUARY:
            self.laborDay = Utils.randomRange(1, 31)
            self.setLaborMonth(Enums.Months.OCTOBER)
        if impregnationMonth == Enums.Months.FEBRUARY:
            self.laborDay = Utils.randomRange(1, 30)
            self.setLaborMonth(Enums.Months.NOVEMBER)
        if impregnationMonth == Enums.Months.MARCH:
            self.laborDay = Utils.randomRange(1, 31)
            self.setLaborMonth(Enums.Months.DECEMBER)
        if impregnationMonth == Enums.Months.APRIL:
            self.laborDay = Utils.randomRange(1, 31)
            self.setLaborMonth(Enums.Months.JANUARY)
        if impregnationMonth == Enums.Months.MAY:
            self.laborDay = Utils.randomRange(1, 28)
            self.setLaborMonth(Enums.Months.FEBRUARY)
        if impregnationMonth == Enums.Months.JUNE:
            self.laborDay = Utils.randomRange(1, 31)
            self.setLaborMonth(Enums.Months.MARCH)
        if impregnationMonth == Enums.Months.JULY:
            self.laborDay = Utils.randomRange(1, 30)
            self.setLaborMonth(Enums.Months.APRIL)
        if impregnationMonth == Enums.Months.AUGUST:
            self.laborDay = Utils.randomRange(1, 31)
            self.setLaborMonth(Enums.Months.MAY)
        if impregnationMonth == Enums.Months.SEPTEMBER:
            self.laborDay = Utils.randomRange(1, 30)
            self.setLaborMonth(Enums.Months.JUNE)
        if impregnationMonth == Enums.Months.OCTOBER:
            self.laborDay = Utils.randomRange(1, 31)
            self.setLaborMonth(Enums.Months.JULY)
        if impregnationMonth == Enums.Months.NOVEMBER:
            self.laborDay = Utils.randomRange(1, 31)
            self.setLaborMonth(Enums.Months.AUGUST)
        if impregnationMonth == Enums.Months.DECEMBER:
            self.laborDay = Utils.randomRange(1, 30)
            self.setLaborMonth(Enums.Months.SEPTEMBER)

    def getPregnancyFather(self):
        return self.pregnancyFather

    def setPregnancyFather(self, father):
        self.pregnancyFather = father

    def getPregnancyTrueFather(self):
        return self.pregnancyTrueFather

    def setPregnancyTrueFather(self, trueFather):
        self.pregnancyTrueFather = trueFather

    def getTrueMother(self):
        return self.trueMother

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
        if self.spouseRelation + newValue > 10000:
            self.spouseRelation = 10000
        else:
            self.spouseRelation += newValue

    def getHappiness(self):
        return self.happiness

    def setHappiness(self, newValue):
        self.happiness = newValue

    def increaseHappiness(self, newValue):
        self.happiness += newValue
        if self.happiness > 300:
            self.happiness = 300
        if self.happiness < -300:
            self.happiness = -300
        for happinessLevel in Enums.HappinessLevel:
            if happinessLevel.value[0] <= self.happiness <= happinessLevel.value[1]:
                self.setHappinessLevel(happinessLevel)

    def getHappinessLevel(self):
        return self.happinessLevel

    def setHappinessLevel(self, newValue):
        self.happinessLevel = newValue

    def getImmunityTo(self):
        return self.immunityTo

    def addImmunityTo(self, disease):
        self.immunityTo.append(disease)

    def getCurrentDiseases(self):
        return self.currentDiseases

    def addCurrentDiseases(self, newDisease):
        self.currentDiseases.append(newDisease)

    def setCurrentDiseases(self, diseases):
        self.currentDiseases = diseases

    def removeCurrentDiseases(self, disease):
        self.currentDiseases.remove(disease)

    def getCurrentInjuries(self):
        return self.currentInjuries

    def addCurrentInjuries(self, newInjuries):
        self.currentInjuries.append(newInjuries)

    def setCurrentInjuries(self, injuries):
        self.currentInjuries = injuries

    def removeCurrentInjuries(self, injuries):
        self.currentInjuries.remove(injuries)

    def getInfections(self):
        return self.infections

    def addInfection(self, infection):
        self.infections.append(infection)

    def removeInfection(self, infection):
        self.infections.remove(infection)

    def setInfections(self, infections):
        self.infections = infections

    def getAccommodation(self):
        return self.accommodation

    def setAccommodation(self, newAccommodation):
        self.accommodation = newAccommodation

    def getPersonalSexualModifier(self):
        return self.personalSexualityModifier

    def changeMultPersonalSexualModifier(self, newValue):
        self.personalSexualityModifier *= newValue

    def initGenDownFamilyTree(self):

        return self.generateDownFamilyTree(BinaryTreeNode(self))

    def initGenUpFamilyTree(self):

        return self.generateUpFamilyTree(BinaryTreeNode(self))

    def getLastBirthMonth(self):
        return self.lastBirthMonth

    def setLastBirthMonth(self, newMonth):
        self.lastBirthMonth = newMonth

    def getIsPregnant(self):
        return self.isPregnant

    def setIsPregnant(self, newIsPregnant):
        self.isPregnant = newIsPregnant

    def getRealEstate (self):
        return self.realEstate

    def addRealEstate(self, newEstate):
        self.realEstate.append(newEstate)

    def removeRealEstate(self, estate):
        self.realEstate.remove(estate)

    def getSkills(self):
        return self.skills

    def getAncestralFamilies(self):

        ancestorsFamiles = []
        tree = self.generateUpFamilyTree(BinaryTreeNode(self))

        ancestorsFamiles = self.getAncestralFamiliesAsListFromTree(tree, ancestorsFamiles)

        return ancestorsFamiles

    def getAncestralFamiliesAsListFromTree(self, tree, ancestorsFamiles = None, fatherSide = True, motherSide = True):

        if ancestorsFamiles is None:
            ancestorsFamiles = []

        father = None
        mother = None
        if fatherSide:
            father = tree.getRoot().getFather()
        if motherSide:
            mother = tree.getRoot().getMother()

        if fatherSide and father is not None:
            if father.getOriginFamilyObjectRef() not in ancestorsFamiles:
                ancestorsFamiles.append(father.getOriginFamilyObjectRef())
            father.getAncestralFamiliesAsListFromTree(BinaryTreeNode(father), ancestorsFamiles)

        if motherSide and mother is not None:
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
        if father is not None:
            for fatherChild in father.getAllChildren():
                if fatherChild != treeroot.getRoot():
                    treeroot.siblings.append(fatherChild)
            treeroot.father = father.generateUpFamilyTree(BinaryTreeNode(father))

        if mother is not None:
            for motherChild in mother.getAllChildren():
                if motherChild != treeroot.getRoot() and motherChild not in treeroot.siblings:
                        treeroot.siblings.append(motherChild)
            treeroot.mother = mother.generateUpFamilyTree(BinaryTreeNode(mother))

        return treeroot

