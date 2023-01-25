from random import choice, seed, SystemRandom

import HouseFunctions
from Person import Person as PersonObj
from Enums import MaritalStatus, HairColor, Sexes, EyeColor
import Utils

people = []

def Init(families, world):

    seed(SystemRandom().random())

    for family in families:
        randomNumber = Utils.randomRange(4, 4)

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

            member.addTrait(Utils.randomTrait(member))
            member.addTrait(Utils.randomTrait(member))
            member.addTrait(Utils.randomTrait(member))

            member.addLikedTraits(Utils.randomLikedTrait(member))
            member.addLikedTraits(Utils.randomLikedTrait(member))
            member.addLikedTraits(Utils.randomLikedTrait(member))

            member.addDislikedTraits(Utils.randomDislikedTrait(member))
            member.addDislikedTraits(Utils.randomDislikedTrait(member))
            member.addDislikedTraits(Utils.randomDislikedTrait(member))

            newHouse = HouseFunctions.getNewHouse()
            member.getSettlement().buildNewHouse(newHouse)
            HouseFunctions.setNewHouseToPerson(member, newHouse)
            HouseFunctions.setHouseDurability(newHouse, Utils.randomRange(60, 90))
            newHouse.addHouseResident(member)

            if family.getFemaleNumber() == 0 and family.getMaleNumber() == 0:
                family.setFoundedBy(member)
            family.addNewMember(member)
            people.append(member)

    return people


def addNewPerson (person):

    people.append(person)


def setUpHairColorsToFamilies (family):

    hairColor = Utils.randomFromEnumCollection(HairColor)

    return hairColor

def setUpEyeColorsToFamilies (family):


    eyeColor = Utils.randomFromEnumCollection(EyeColor)


    return eyeColor


def initInitMarrieges(family):

    while family.getUnmarriedFemaleNumber() > 0 and family.getUnmarriedMaleNumber() > 0:

            pip1 = choice(family.getUnmarriedMalesList())
            pip2 = choice(family.getUnmarriedFemalesList())
            InitMarriegies(pip1, pip2)
            family.addMarriedMember(pip1)
            family.addMarriedMember(pip2)
            family.removeUnmarriedMember(pip1)
            family.removeUnmarriedMember(pip2)
            pip2.getAccommodation().removeHouseResident(pip2)
            pip2.setAccommodation(pip1.getAccommodation())
            pip2.getAccommodation().addHouseResident(pip2)

    return

def InitMarriegies (husband, wife):

    husband.maritalStatus = MaritalStatus.MARRIED
    husband.spouse = wife
    husband.spouse.setSpouseRelation(50)

    wife.maritalStatus = MaritalStatus.MARRIED
    wife.spouse = husband
    wife.spouse.setSpouseRelation(50)

    wife.getAccommodation().removeHouseResident(wife)
    wife.setAccommodation(husband.getAccommodation())
    wife.getAccommodation().addHouseResident(wife)

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
