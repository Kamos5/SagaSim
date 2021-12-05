import random
from Person import Person as PersonObj
import FamilyNameGenerator as FNG
from Enums import MaritalStatus, HairColor, Sexes, EyeColor
import Utils

people = []

def Init(families, world):

    random.seed(random.SystemRandom().random())

    for family in families:
        randomNumber = random.randint(4, 4)

        for number in range(randomNumber):
            member = PersonObj()
            sex = InitRandomSex(family, number)
            randomAge = Utils.randomRange(15, 20)
            randomLifespan = Utils.randomRange(50, 60)
            hairColor = setUpHairColorsToFamilies(family)
            hairColorGen1 = [hairColor, 0]
            hairColorGen2 = [hairColor, 0]
            eyeColor = setUpEyeColorsToFamilies(family)
            eyeColorGen1 = [eyeColor, 0]
            eyeColorGen2 = [eyeColor, 0]


            member.setInitValues(family.familyName, world.getYear(), randomAge, randomLifespan, sex, hairColor, hairColorGen1, hairColorGen2, eyeColor, eyeColorGen1, eyeColorGen2, family)
            if family.getFemaleNumber() == 0 and family.getMaleNumber() == 0:
                family.setFoundedBy(member)
            family.addNewMember(member)
            people.append(member)

    return people


def addNewPerson (person):

    people.append(person)


def setUpHairColorsToFamilies (family):

    #TODO REWRITE IT BECAUSE IT MAKES ISSUES WHERE THERE IS NOT ENOUGH FAMILIES (FAMILIES PER REGION*REGIONS NOW MUST BE +5 FOR WORKING CORRECTLY)
    hairColor = HairColor.GRAY

    if family.familyName == FNG.initialFamilyNames[0]:
        hairColor = HairColor.BLACK
    elif family.familyName == FNG.initialFamilyNames[1]:
        hairColor = HairColor.BROWN
    elif family.familyName == FNG.initialFamilyNames[2]:
        hairColor = HairColor.RED
    elif family.familyName == FNG.initialFamilyNames[3]:
        hairColor = HairColor.YELLOW
    elif family.familyName == FNG.initialFamilyNames[4]:
        hairColor = HairColor.WHITE
    else:
        hairColor = HairColor.BROWN

    return hairColor

def setUpEyeColorsToFamilies (family):


    eyeColor = Utils.randomFromEnumCollection(EyeColor)


    return eyeColor


def initInitMarrieges(family):

    while family.getUnmarriedFemaleNumber() > 0 and family.getUnmarriedMaleNumber() > 0:

            pip1 = random.choice(family.getUnmarriedMalesList())
            pip2 = random.choice(family.getUnmarriedFemalesList())
            InitMarriegies(pip1, pip2)
            family.addMarriedMember(pip1)
            family.addMarriedMember(pip2)
            family.removeUnmarriedMember(pip1)
            family.removeUnmarriedMember(pip2)

    return

def InitMarriegies (husband, wife):

    husband.maritalStatus = MaritalStatus.MARRIED
    husband.spouse = wife

    wife.maritalStatus = MaritalStatus.MARRIED
    wife.spouse = husband

    return

def InitRandomSex(family, initPeopleNumber):

    if family.getAllMembersNumber() < 1:
        return Utils.randomFromEnumCollection(Sexes)
    elif initPeopleNumber == 1:
        if family.getFemaleNumber() == 1:
            return Sexes.MALE
        else:
            return Sexes.FEMALE
    else:
        return Utils.randomFromEnumCollection(Sexes)
