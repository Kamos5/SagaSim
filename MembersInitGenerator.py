import random
from Member import Person as PersonObj
import FamilyNameGenerator as FNG
from Enums import MaritalStatus, HairColor
import Utils

people = []

def Init(families, world):

    random.seed(random.SystemRandom().random())
    sexes = ["M", "F"]


    for family in families:
        randomNumber = random.randint(2, 2)

        for number in range(randomNumber):
            member = PersonObj()
            sex = InitRandomSex(family, sexes, number)
            randomAge = Utils.randomRange(15, 20)
            # if sex == "F":
            #     randomAge = 40
            randomLifespan = Utils.randomRange(40, 50)
            hairColor = setUpHairColorsToFamilies(family)
            member.setInitValues(world.getYear(), randomAge, randomLifespan, sex, hairColor, family.familyName)
            family.addNewMember(member)
            family.addNewUnmarriedMember(member)
            people.append(member)

    return people


def addNewPerson (person):

    people.append(person)


def setUpHairColorsToFamilies (family):


    hairColor = HairColor.UNDEFINED

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


def initInitMarrieges(family, people):

    while len(family.getAllUnmarriedAdultMalesUUIDs()) > 0 and len(family.getAllUnmarriedAdultFemalesUUIDs()) > 0:

            pip1 = random.choice(family.getAllUnmarriedAdultMalesUUIDs())
            pip2 = random.choice(family.getAllUnmarriedAdultFemalesUUIDs())
            InitMarriegies(pip1, pip2, people)
            family.removeFromUnmarriedAdultMalesUUIDsList(pip1)
            family.removeFromUnmarriedAdultFemalesUUIDsList(pip2)

    return

def InitMarriegies (pip1, pip2, people):

    for pips in people:
        if pips.personUUID == pip1:
            pips.maritalStatus = MaritalStatus.MARRIED
            pips.spouse = pip2
        if pips.personUUID == pip2:
            pips.maritalStatus = MaritalStatus.MARRIED
            pips.spouse = pip1

    return

def InitRandomSex(family, sexes, initPeopleNumber):

    if family.getFamilyMembersNumber() < 1:
        return Utils.randomFromCollection(sexes)
    elif initPeopleNumber == 1:
        if family.femaleNumber == 1:
            return sexes[0]
        else:
            return sexes[1]
    else:
        return Utils.randomFromCollection(sexes)
