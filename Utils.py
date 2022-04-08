import time
import uuid
import random

import pygame

import Enums
import PeopleInterface as PI

def createUUID():

    return str(uuid.uuid4())


def randomRange(min, max):

    returnVal = random.randint(min, max)
    return returnVal


def randomFromCollection(collection):

    return random.choice(collection)


def randomFromEnumCollection(collection):

    return random.choice(list(collection))


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

    notClear = True

    if len(person.getDislikedTraits()) == 0:
        randomTrait = randomFromEnumCollection(Enums.Traits)
        return randomTrait
    else:
        randomTrait = randomFromEnumCollection(Enums.Traits)
        while notClear:
            for trait in person.getDislikedTraits():
                for trait2 in person.getLikedTraits():
                    if trait == randomTrait and trait2 == randomTrait and trait == trait2:
                        notClear = True
                        randomTrait = randomFromEnumCollection(Enums.Traits)
                    else:
                        notClear = False
            return randomTrait

def randomLikedTrait (person):

    notClear = True

    if len(person.getLikedTraits()) == 0:
        randomTrait = randomFromEnumCollection(Enums.Traits)
        return randomTrait
    else:
        randomTrait = randomFromEnumCollection(Enums.Traits)
        while notClear:
            for trait in person.getLikedTraits():
                if trait == randomTrait:
                    notClear = True
                    randomTrait = randomFromEnumCollection(Enums.Traits)
                else:
                    notClear = False
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
        childHairColorGen1 = [randomFromEnumCollection(Enums.HairColor), 0]

    if mutationGene == 2 and mutationChance <= 5:
        childHairColorGen2 = [randomFromEnumCollection(Enums.HairColor), 0]

    childHairColor = hairColorMap(childHairColorGen1, childHairColorGen2)[0]

    return childHairColor, childHairColorGen1, childHairColorGen2

def geneticEyeColor(trueParent1, trueParent2):


    mutationChance = randomRange(1, 1000)
    mutationGene = randomRange(1, 2)

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
        childEyeColorGen1 = [randomFromEnumCollection(Enums.EyeColor), 0]

    if mutationGene == 2 and mutationChance <= 5:
        childEyeColorGen2 = [randomFromEnumCollection(Enums.EyeColor), 0]

    childEyeColor = eyeColorMap(childEyeColorGen1, childEyeColorGen2)[0]

    return childEyeColor, childEyeColorGen1, childEyeColorGen2


def triangularNumber(n):
    deathChance = 0
    for i in range(n):  # range(3) is a generator for [0, 1, 2]
        deathChance += i
    return deathChance

