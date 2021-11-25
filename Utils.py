import uuid
import random

def createUUID():

    return str(uuid.uuid4())

def randomRange(min, max):

    returnVal = random.randint(min, max)
    return returnVal

def randomFromCollection(collection):

    return random.choice(collection)


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