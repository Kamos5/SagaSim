import uuid
import random
import Enums

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


def HairColorMap (randomNumber, color1, color2, color3, color4, color5):

    #sum must equal 100
    threshold1 = 89
    threshold2 = 5
    threshold3 = 3
    threshold4 = 2
    threshold5 = 1

    if randomNumber <= threshold1:
        return color1
    if threshold1 < randomNumber <= threshold1 + threshold2:
        return color2
    if threshold1 + threshold2 < randomNumber <= threshold1 + threshold2 + threshold3:
        return color3
    if threshold1 + threshold2 + threshold3 < randomNumber <= threshold1 + threshold2 + threshold3 + threshold4:
        return color4
    if threshold1 + threshold2 + threshold3 + threshold4 < randomNumber <= threshold1 + threshold2 + threshold3 + threshold4 + threshold5:
        return color5


def geneticHairColor(val1, val2):

    # HAIR1	    HAIR2			                    OUTCOME	LIKELINESS
    # 				                80	         10	        5	        3	        2
    # BLACK	 5   BLACK	5		BLACK	5    BROWN	 4   YELLOW	 3   RED	2    WHITE  1
    # BLACK	 5   BROWN	4		BLACK	5    BROWN	 4   YELLOW	 3   RED	2    WHITE  1
    # BLACK	 5   YELLOW	3		BLACK	5    BROWN	 4   YELLOW	 3   RED	2    WHITE  1
    # BLACK	 5   RED	2		BLACK	5    BROWN	 4   YELLOW	 3   RED	2    WHITE  1
    # BLACK	 5   WHITE	1		BLACK	5    BROWN	 4   YELLOW	 3   RED	2    WHITE  1
    # BROWN	 4   BROWN	4		BROWN	4    BLACK	 5   YELLOW	 3   RED	2    WHITE  1
    # BROWN	 4   YELLOW	3		BROWN	4    BLACK	 5   YELLOW	 3   RED	2    WHITE  1
    # BROWN	 4   RED	2		BROWN	4    BLACK	 5   YELLOW	 3   RED	2    WHITE  1
    # BROWN	 4   WHITE	1		BROWN	4    BLACK	 5   YELLOW	 3   RED	2    WHITE  1
    # YELLOW 3   YELLOW	3		YELLOW	3    BLACK	 5   BROWN	 4   RED	2    WHITE  1
    # YELLOW 3   RED 	2		YELLOW	3    BLACK	 5   BROWN	 4   RED	2    WHITE  1
    # YELLOW 3   WHITE	1		YELLOW	3    BLACK	 5   BROWN	 4   RED	2    WHITE  1
    # RED	 2   RED	2       RED	    2    BLACK	 5   BROWN	 4   YELLOW	3    WHITE  1
    # RED	 2   WHITE	1		RED	    2    BLACK	 5   BROWN	 4   YELLOW	3    WHITE  1
    # WHITE	 1   WHITE	1		WHITE	1    BLACK	 5   BROWN	 4   YELLOW	3    RED    2

    randomNumber = randomRange(1, 100)

    if val1.value[0] == 5 or val2.value[0] == 5:
        return HairColorMap(randomNumber, Enums.HairColor.BLACK, Enums.HairColor.BROWN, Enums.HairColor.YELLOW, Enums.HairColor.RED, Enums.HairColor.WHITE)
    if val1.value[0] == 4 or val2.value[0] == 4:
        return HairColorMap(randomNumber, Enums.HairColor.BROWN, Enums.HairColor.BLACK, Enums.HairColor.YELLOW, Enums.HairColor.RED, Enums.HairColor.WHITE)
    if val1.value[0] == 3 or val2.value[0] == 3:
        return HairColorMap(randomNumber, Enums.HairColor.YELLOW, Enums.HairColor.BLACK, Enums.HairColor.BROWN, Enums.HairColor.RED, Enums.HairColor.WHITE)
    if val1.value[0] == 2 or val2.value[0] == 2:
        return HairColorMap(randomNumber, Enums.HairColor.RED, Enums.HairColor.BLACK, Enums.HairColor.BROWN, Enums.HairColor.YELLOW, Enums.HairColor.WHITE)
    if val1.value[0] == 1 or val2.value[0] == 1:
        return HairColorMap(randomNumber, Enums.HairColor.WHITE, Enums.HairColor.RED, Enums.HairColor.BLACK, Enums.HairColor.BROWN, Enums.HairColor.YELLOW)

