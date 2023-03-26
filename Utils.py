import math
import time
from random import randint, choice

import Enums

def randomRange(min, max):

    returnVal = randint(min, max)
    return returnVal


def randomFromCollection(collection):

    return choice(collection)

def randomFromCollectionWithWeight(collection):

    weightSum = 0

    for element in collection:
        weightSum += element.value.getUpgrWeightValue()

    randValue = randint(1, weightSum)

    for element in collection:
        if randValue <= element.value.getUpgrWeightValue():
            return element
        randValue -= element.value.getUpgrWeightValue()

    return element

def randomFromFoundationDictionaryWithWeight(collection):

    weightSum = 0

    for key, value in collection.items():
        weightSum += value['chanceWeightModifier']

    randValue = randint(1, weightSum)

    for key, value in collection.items():
        if randValue <= value['chanceWeightModifier']:
            return collection[key]
        randValue -= value['chanceWeightModifier']

    return None


def randomFromEnumCollection(collection):

    return choice(list(collection))

def randomFromEnumCollectionWithWeights(collection):

    returnVal = randint(1, 100)

    for element in collection:
        if returnVal <= element.value.chanceWeightModifier:
            return element


def geneticRandomFromValues(val1, val2):

    if val1 <= val2:
        returnValue = randomRange(val1, val2)
    else:
        returnValue = randomRange(val2, val1)

    randomChance = randomRange(1, 100)
    if randomChance < 20:
        returnValue = int(returnValue*95/100)
    if randomChance >= 80:
        returnValue = int(returnValue*105/100)

    return returnValue


def geneticRandomFromValuesForHeight(val1, val2):

    if val1 <= val2:
        returnValue = randomRange(val1, val2)
    else:
        returnValue = randomRange(val2, val1)

    randomChance = randomRange(1, 100)
    if randomChance < 10:
        returnValue = int(returnValue*99/100)
    if randomChance >= 90:
        returnValue = int(returnValue*105/100)

    return returnValue

def inheretTraits(person, parent1, parent2, trueParent1, trueParent2):

    randomChanceForTrait1 = randomRange(1, 100)
    randomChanceForTrait2 = randomRange(1, 100)
    randomChanceForTrait3 = randomRange(1, 100)

    if randomChanceForTrait1 <= 20: #random
        trait1 = randomTrait(person)
        person.addTrait(trait1)
    if randomChanceForTrait1 <= 65 and randomChanceForTrait1 > 20: #from parents
        trait1 = traitsFromParerts(person, parent1, parent2)
        person.addTrait(trait1)
    if randomChanceForTrait1 > 65: #from trueParents
        trait1 = traitsFromParerts(person, trueParent1, trueParent2)
        person.addTrait(trait1)

    if randomChanceForTrait2 <= 20: #random
        trait2 = randomTrait(person)
        person.addTrait(trait2)
    if randomChanceForTrait2 <= 65 and randomChanceForTrait2 > 20: #from parents
        trait2 = traitsFromParerts(person, parent1, parent2)
        person.addTrait(trait2)
    if randomChanceForTrait2 > 65: #from trueParents
        trait2 = traitsFromParerts(person, trueParent1, trueParent2)
        person.addTrait(trait2)

    if randomChanceForTrait3 <= 20: #random
        trait3 = randomTrait(person)
        person.addTrait(trait3)
    if randomChanceForTrait3 <= 65 and randomChanceForTrait3 > 20: #from parents
        trait3 = traitsFromParerts(person, parent1, parent2)
        person.addTrait(trait3)
    if randomChanceForTrait3 > 65: #from trueParents
        trait3 = traitsFromParerts(person, trueParent1, trueParent2)
        person.addTrait(trait3)

    likedTrait1 = randomLikedTrait(person)
    person.addLikedTraits(likedTrait1)
    likedTrait2 = randomLikedTrait(person)
    person.addLikedTraits(likedTrait2)
    likedTrait3 = randomLikedTrait(person)
    person.addLikedTraits(likedTrait3)

    dislikedTrait1 = randomDislikedTrait(person)
    person.addDislikedTraits(dislikedTrait1)
    dislikedTrait2 = randomDislikedTrait(person)
    person.addDislikedTraits(dislikedTrait2)
    dislikedTrait3 = randomDislikedTrait(person)
    person.addDislikedTraits(dislikedTrait3)

    if Enums.Traits.CHASTE == person.getTraits():
        person.changeMultPersonalSexualModifier(0.5)
    if Enums.Traits.LUSTFUL == person.getTraits():
        person.changeMultPersonalSexualModifier(1.5)

    if person.sexuality == 'homo':
        if person.getSex() == Enums.Sexes.MALE:
            person.changeMultPersonalSexualModifier(0.8)
        else:
            person.changeMultPersonalSexualModifier(0.4)

def traitsFromParerts (person, parent1, parent2):

    notClear = True

    if len(person.getTraits()) == 0:
        randomTrait = randomFromEnumCollection(parent1.getTraits() + parent2.getTraits())
        return randomTrait
    else:
        randomTrait = randomFromEnumCollection(parent1.getTraits() + parent2.getTraits())
        while notClear:
            for trait in person.getTraits():
                if trait.value[0] + randomTrait.value[0] == 0 or trait == randomTrait:
                    notClear = True
                    randomTrait = randomFromEnumCollection(parent1.getTraits() + parent2.getTraits())
                else:
                    notClear = False

        return randomTrait

def timeFunction(timerFlag, function, params=None):

    if timerFlag:
        start = time.perf_counter()
        if params is not None:
            function(params)
        else:
            function()
        end = time.perf_counter()
        return end - start
    else:
#        function() TODO TEMP
        return 0


def randomTrait (person):

    notClear = True

    if len(person.getTraits()) == 0:
        randomTrait = randomFromEnumCollection(Enums.Traits)
        return randomTrait
    else:
        randomTrait = randomFromEnumCollection(Enums.Traits)
        while notClear:
            for trait in person.getTraits():
                if trait.value[0] + randomTrait.value[0] == 0 or trait == randomTrait:
                    notClear = True
                    randomTrait = randomFromEnumCollection(Enums.Traits)
                else:
                    notClear = False
        return randomTrait

def randomDislikedTrait (person):

    clear0 = True
    clear = True

    if len(person.getDislikedTraits()) == 0:

        randomTrait = randomFromEnumCollection(Enums.Traits)
        while clear0:
            randomTrait = randomFromEnumCollection(Enums.Traits)
            for trait2 in person.getLikedTraits():
                clear0 = clear0 and randomTrait != trait2
            if clear0:
                return randomTrait
            else:
                clear0 = not clear0

    else:
        randomTrait = randomFromEnumCollection(Enums.Traits)
        while clear:
            randomTrait = randomFromEnumCollection(Enums.Traits)
            for trait in person.getDislikedTraits():
                for trait2 in person.getLikedTraits():
                        clear = clear and randomTrait != trait2 and randomTrait != trait
            if clear:
                return randomTrait
            else:
                clear = not clear

def randomLikedTrait (person):

    notClear = True

    if len(person.getLikedTraits()) == 0:
        randomTrait = randomFromEnumCollection(Enums.Traits)
        return randomTrait
    else:
        randomTrait = randomFromEnumCollection(Enums.Traits)
        while notClear:
            randomTrait = randomFromEnumCollection(Enums.Traits)
            for trait in person.getLikedTraits():
                if trait != randomTrait:
                    notClear = False
                else:
                    notClear = True
        return randomTrait


def geneticSex (parent1, parent2):

    mutationChance = randomRange(1, 1000)
    mutationGene = randomRange(1, 2)
    gen1 = randomRange(1, 2)
    gen2 = randomRange(1, 2)
    sexGen1 = parent1.sexGen1
    sexGen2 = parent1.sexGen2

    if gen1 == 1 and gen2 == 1:
        sexGen1 = parent1.sexGen1
        sexGen2 = parent2.sexGen1
    if gen1 == 1 and gen2 == 2:
        sexGen1 = parent1.sexGen1
        sexGen2 = parent2.sexGen2
    if gen1 == 2 and gen2 == 1:
        sexGen1 = parent1.sexGen2
        sexGen2 = parent2.sexGen1
    if gen1 == 2 and gen2 == 2:
        sexGen1 = parent1.sexGen2
        sexGen2 = parent2.sexGen2

    if mutationGene == 1 and mutationChance <= 5:
        sexGen1 = [sexGen1[0], 1]

    if mutationGene == 2 and mutationChance <= 5:
        sexGen2 = [sexGen1[0], 1]

    if sexGen1[0] == Enums.Sexes.MALE or sexGen2[0] == Enums.Sexes.MALE:

        return Enums.Sexes.MALE, sexGen1, sexGen2
    else:
        return Enums.Sexes.FEMALE, sexGen1, sexGen2

def hairColorMap (hairColorGen1, hairColorGen2):

    randomNumber = randomRange(1, 100)

    #sum must equal 100
    threshold1 = 90
    threshold2 = 10

    if hairColorGen1[0].value[0] >= hairColorGen2[0].value[0]:
        if randomNumber <= threshold1:
            return hairColorGen1
        else:
            return hairColorGen2
    else:
        if randomNumber <= threshold1:
            return hairColorGen2
        else:
            return hairColorGen1

def eyeColorMap (eyeColorGen1, eyeColorGen2):

    randomNumber = randomRange(1, 100)

    #sum must equal 100
    threshold1 = 66
    threshold2 = 33

    if eyeColorGen1[0].value[0] >= eyeColorGen2[0].value[0]:
        if randomNumber <= threshold1:
            return eyeColorGen1
        else:
            return eyeColorGen2
    else:
        if randomNumber <= threshold1:
            return eyeColorGen2
        else:
            return eyeColorGen1

def geneticHairColor(trueParent1, trueParent2):


    mutationChance = randomRange(1, 1000)
    mutationGene = randomRange(1, 2)

    damagedGene = 0

    damagedGeneChange = randomRange(1, 100)

    if damagedGeneChange < 5:
        damagedGene = 1

    personParent1HairColorGen1 = trueParent1.hairColorGen1
    personParent1HairColorGen2 = trueParent1.hairColorGen2
    personParent2HairColorGen1 = trueParent2.hairColorGen1
    personParent2HairColorGen2 = trueParent2.hairColorGen2

    randomGen1 = randomRange(1, 2)
    randomGen2 = randomRange(1, 2)

    childHairColorGen1 = personParent1HairColorGen1
    childHairColorGen2 = personParent1HairColorGen2

    if randomGen1 == 1 and randomGen2 == 1:
        childHairColorGen1 = personParent1HairColorGen1
        childHairColorGen2 = personParent2HairColorGen1

    if randomGen1 == 1 and randomGen2 == 2:
        childHairColorGen1 = personParent1HairColorGen1
        childHairColorGen2 = personParent2HairColorGen2

    if randomGen1 == 2 and randomGen2 == 1:
        childHairColorGen1 = personParent2HairColorGen2
        childHairColorGen2 = personParent1HairColorGen1

    if randomGen1 == 2 and randomGen2 == 2:
        childHairColorGen1 = personParent2HairColorGen2
        childHairColorGen2 = personParent2HairColorGen2

    if mutationGene == 1 and mutationChance <= 5:
        childHairColorGen1 = [randomFromEnumCollection(Enums.HairColor), damagedGene]

    if mutationGene == 2 and mutationChance <= 5:
        childHairColorGen2 = [randomFromEnumCollection(Enums.HairColor), damagedGene]

    childHairColor = hairColorMap(childHairColorGen1, childHairColorGen2)[0]

    return childHairColor, childHairColorGen1, childHairColorGen2

def geneticEyeColor(trueParent1, trueParent2):


    mutationChance = randomRange(1, 1000)
    mutationGene = randomRange(1, 2)

    damagedGene = 0

    damagedGeneChange = randomRange(1, 100)

    if damagedGeneChange < 5:
        damagedGene = 1

    personParent1EyeColorGen1 = trueParent1.eyeColorGen1
    personParent1EyeColorGen2 = trueParent1.eyeColorGen2
    personParent2EyeColorGen1 = trueParent2.eyeColorGen1
    personParent2EyeColorGen2 = trueParent2.eyeColorGen2

    randomGen1 = randomRange(1, 2)
    randomGen2 = randomRange(1, 2)

    childEyeColorGen1 = personParent1EyeColorGen1
    childEyeColorGen2 = personParent1EyeColorGen2

    if randomGen1 == 1 and randomGen2 == 1:
        childEyeColorGen1 = personParent1EyeColorGen1
        childEyeColorGen2 = personParent2EyeColorGen1

    if randomGen1 == 1 and randomGen2 == 2:
        childEyeColorGen1 = personParent1EyeColorGen1
        childEyeColorGen2 = personParent2EyeColorGen2

    if randomGen1 == 2 and randomGen2 == 1:
        childEyeColorGen1 = personParent2EyeColorGen2
        childEyeColorGen2 = personParent1EyeColorGen1

    if randomGen1 == 2 and randomGen2 == 2:
        childEyeColorGen1 = personParent2EyeColorGen2
        childEyeColorGen2 = personParent2EyeColorGen2

    if mutationGene == 1 and mutationChance <= 5:
        childEyeColorGen1 = [randomFromEnumCollection(Enums.EyeColor), damagedGene]

    if mutationGene == 2 and mutationChance <= 5:
        childEyeColorGen2 = [randomFromEnumCollection(Enums.EyeColor), damagedGene]

    childEyeColor = eyeColorMap(childEyeColorGen1, childEyeColorGen2)[0]

    return childEyeColor, childEyeColorGen1, childEyeColorGen2


def triangularNumber(n):
    deathChance = 0
    for i in range(n):  # range(3) is a generator for [0, 1, 2]
        deathChance += i
    return deathChance


def printDownFamilyTree(tree, level=0, prefix=""):

    if tree.getRoot().getFather() is not None and tree.getRoot().getMother() is not None:
        print(prefix + "-" + tree.getRoot().getFirstName() + tree.getRoot().getLastName() + " (" + str(tree.getRoot().getYearOfBirth()) + "-" + str(tree.getRoot().getYearOfDeath()) + ")" + " <" + tree.getRoot().getFather().getFirstName() + " " + tree.getRoot().getFather().getLastName() + " + " + tree.getRoot().getMother().getFirstName() + " " + tree.getRoot().getMother().getFamilyName() + ">")

    else:
        print(prefix + "-" + tree.getRoot().getFirstName() + " " + tree.getRoot().getLastName() + " (" + str(tree.getRoot().getYearOfBirth()) + "-" + str(tree.getRoot().getYearOfDeath()) + ")")

    if len(tree.getChildren()) > 0:
        for branch in tree.getChildren():
            printDownFamilyTree(branch, level + 1, prefix + " ")

def printUpFamilyTree(tree, level=0, prefix=""):

    sexPrefix = ""

    if len(tree.getRoot().getAllChildren()) > 0:
        if tree.getRoot().getSex() == Enums.Sexes.MALE:
            sexPrefix = "Father: "
        else:
            sexPrefix = "Mother: "

    rootString = prefix + sexPrefix + tree.getRoot().getFirstName() + " " + tree.getRoot().getLastName() + " (" + str(tree.getRoot().getYearOfBirth()) + "-" + str(tree.getRoot().getYearOfDeath()) + ")"
    siblingString = ""

    if len(tree.getSiblings()) > 0:
        siblingString += " Siblings:"
        for sibling in tree.getSiblings():
            siblingString += " (" + sibling.getFirstName() + " " + sibling.getLastName() + ")"

    print(rootString + siblingString)
    if tree.getRoot().getFather() is not None:
        printUpFamilyTree(tree.getFather(), level + 1, prefix + " ")

    if tree.getRoot().getMother() is not None:
        printUpFamilyTree(tree.getMother(), level + 1, prefix + " ")

def checkForLikedTraisInPerson2(person, person2):

    likedTraites = 0
    for trait in person2.getTraits():
        if trait in person.getLikedTraits():
            likedTraites += 1

    return likedTraites

def checkForDislikedTraisInPerson2(person, person2):

    dislikedTraites = 0
    for trait in person2.getTraits():
        if trait in person.getDislikedTraits():
            dislikedTraites += 1

    return dislikedTraites

def getTemperatureBasedOnDay(day):

    daysInYear = 365

    offSetForStartingDay = 112

    basicMinTemperature = -10
    basicMaxTemperature = 30

    noiseLevel = 3

    dayInRads = (day-offSetForStartingDay) * 360 / daysInYear

    rawResult = math.sin(math.radians(dayInRads))  # <-1;1>

    rawResultNormalized = (rawResult + 1) / 2  # <0;1>
    basicMaxTemperatureNormalized = basicMaxTemperature - basicMinTemperature  # <40>

    properTemperatureNormalized = rawResultNormalized * basicMaxTemperatureNormalized   # <0;40>

    idealTemperature = properTemperatureNormalized + basicMinTemperature  # <-10;30>

    noiseOffset = randomRange(-noiseLevel, noiseLevel)  # <-3;3>

    endTemperature = round(idealTemperature + noiseOffset)  # <-13;33>

    return endTemperature


