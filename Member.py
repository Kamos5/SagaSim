from Family import Family as FamilyObj
import Utils
import NameGenerator
from Enums import LifeStatus, MaritalStatus, HairColor, CauseOfDeath, Sexes


class Person(FamilyObj):

    def __init__(self):
        self.personUUID = Utils.createUUID()
        self.title = ''
        self.firstName = ''
        self.secondName = ''
        self.lastName = ''
        self.yearOfBirth = ''
        self.age = 0
        self.lifespan = 0
        self.modifiedLifespan = 0
        self.sex = Sexes.FEMALE
        # treated as always X chromosome + health : 0 always healty
        self.sexGen1 = [Sexes.FEMALE, 0]
        # treated as X or Y chromosome
        self.sexGen2 = [Sexes.FEMALE, 0]
        self.fertility = 0
        self.numberOfChildren = 0
        self.mother = ''
        self.father = ''
        self.trueMother = ''
        self.trueFather = ''
        self.lover = ''
        self.spouse = ''
        self.maritalStatus = MaritalStatus.SINGLE
        self.deadSpouses = []
        self.lifeStatus = LifeStatus.ALIVE
        self.causeOfDeath = CauseOfDeath.NULL
        self.hairColor = HairColor.UNDEFINED
        self.traits = []
        self.childrens = []
        self.deadChildrens = []
        pass

    def setInitValues(self, yearOfBirth, age, randomLifespan, sex, hairColor, familyName):

        if sex == Sexes.MALE:
            self.firstName = NameGenerator.randomMName()
        else:
            self.firstName = NameGenerator.randomFName()

        super().__init__(familyName)
        self.lastName = familyName
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

        self.fertility = 80
        self.hairColor = hairColor

    def addNewPerson(self, firstName, lastName, familyName, yearOfBirth, lifespan, sex, sexGen1, sexGen2, fertility, hairdColor, mother, father, trueMother, trueFather):

        self.firstName = firstName
        self.lastName = lastName
        super().__init__(familyName)
        self.yearOfBirth = yearOfBirth
        self.lifespan = lifespan
        self.modifiedLifespan = lifespan
        self.sex = sex
        self.sexGen1 = sexGen1
        self.sexGen2 = sexGen2
        self.fertility = fertility
        self.hairColor = hairdColor
        self.mother = mother
        self.father = father
        self.trueMother = trueMother
        self.trueFather = trueFather


    def addFemalesCount(self):
        super().increaseFemaleNumber()

    def addMalesCount(self):
        super().increaseMaleNumber()

    def setSpouse(self, personUUID):
        self.spouse = personUUID
        self.maritalStatus = MaritalStatus.MARRIED

    def increaseAge(self):
        self.age += 1

    def changeLifeStatus(self, newLifeStatus):
        self.lifeStatus = newLifeStatus

