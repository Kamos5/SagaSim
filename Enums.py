from enum import Enum

class LifeStatus(Enum):
    ALIVE = 'alive'
    DEAD = 'dead'
    COMATOSE = 'comatose'

class MaritalStatus(Enum):
    CHILD = 'child'
    SINGLE = 'single'
    MARRIED = 'married'
    WIDOW = 'widow'
    WIDOWER = 'widower'
    DEAD = 'dead'
    DIVORCED = 'divorced'

class CauseOfDeath(Enum):
    AGE = 'age'
    CHILDBIRTH = 'childbirth'
    NEGLIGENCE = 'negligence'
    KILLED = 'killed'
    SICKNESS = 'sickness'
    STARVATION = 'starvation'
    UNKNOWN = 'unknown'
    NULL = ''

class HairColor(Enum):
    BLACK = 5, 'black', (0, 0, 0)
    BROWN = 4, 'brown', (84,38,4)
    YELLOW = 3, 'yellow', (255,215,0)
    RED = 2, 'red', (178,34,34)
    WHITE = 1, 'white', (255,250,240)
    GRAY = 0, 'gray', (166,166,166)


class EyeColor(Enum):
    BLACK = 7, 'black', (0, 0, 0)
    BROWN = 6, 'brown', (84, 38, 4)
    AMBER = 5, 'amber', (163, 100, 5)                    #bursztynowe
    HAZEL = 4, 'hazel', (218, 143, 30)      #piwne
    GREEN = 3, 'green', (51, 102, 0)
    BLUE = 2, 'blue', (0, 0, 153)
    GRAY = 1, 'gray', (166, 166, 166)

class SkinColor(Enum):
    BLACK = 4, 'black'
    BROWN = 3, 'brown'
    YELLOW = 2, 'yellow'
    WHITE = 1, 'white'
    ALBINO = 0, 'albino'
    UNDEFINED = -1, 'undefined'

#0 means healthy gen
class Sexes(Enum):
    MALE = 0, 'M'
    FEMALE = 0, 'F'

class Traits(Enum):
    BRAVE = 1, 'Brave'
    CRAVEN = -1, 'Craven'
    CALM = 2, 'Calm'
    WRATHFUL = -2, 'Wrathful'
    CHASTE = 3, 'Chaste'
    LUSTFUL = -3, 'Lustful'
    CONTENT = 4, 'Content'
    AMBITIOUS = -4, 'Ambitious'
    DILIGENT = 5, 'Diligent'
    LAZY = -5, 'Lazy'
    FICKLE = 6, 'Fickle'
    STUBBORN = -6, 'Stubborn'
    FORGIVING = 7, 'Forgiving'
    VENGEFUL = -7, 'Vengeful'
    GENEROUS = 8, 'Generous'
    GREEDY = -8, 'Greedy'
    GREGARIOUS = 9, 'Gregarious'
    SHY = -9, 'Shy'
    HONEST = 10, 'Honest'
    DECEITFUL = -10, 'Deceitful'
    HUMBLE = 11, 'Humble'
    ARROGANT = -11, 'Arrogant'
    JUST = 12, 'Just'
    ARBITRARY = -12, 'Arbitrary'
    PATIENT = 13, 'Patient'
    IMPATIENT = -13, 'Impatient'
    TEMPERATE = 14, 'Temperate'
    GLUTTONOUS = -14, 'Gluttonous'
    TRUSTING = 15, 'Trusting'
    PARANOID = -15, 'Paranoid'
    ZEALOUS = 16, 'Zealous'
    CYNICAL = -16, 'Cynical'
    COMPASSIONATE = 17, 'Compassionate'
    CALLOUS = -17, 'Callous'


class Settlements(Enum):

    VILLAGE = 'village'
    TOWN = 'town'

class weatherStatus(Enum):

    #weater, intensity, effect
    NORMAL = 'Normal', 'normal weather'

class mildWeatherStatus(Enum):
    MILDFLOOD = 'Mild flood', 'mild cataclysm', 15
    MILDDROUGHT = 'Mild drought', 'mild cataclysm', 15
    MILDWILDFIRE = 'Mild wildfire', 'mild cataclysm', 15
    MILDEARTHQUAKE = 'Mild earth quake', 'mild cataclysm', 15

class mediumWeatherStatus(Enum):
    MEDIUMFLOOD = 'Medium flood', 'medium cataclysm', 30
    MEDIUMDROUGHT = 'Medium drought', 'medium cataclysm', 30
    MEDIUMWILDFIRE = 'Medium wildfire', 'medium cataclysm', 30
    MEDIUMEARTHQUAKE = 'Medium wildfire', 'medium cataclysm', 30

class strongWeatherStatus(Enum):
    STRONGFLOOD = 'Strong flood', 'strong cataclysm', 45
    STRONGDROUGHT = 'Strong drought', 'strong cataclysm', 45
    STRONGWILDFIRE = 'Strong wildfire', 'strong cataclysm', 45
    STRONGEARTHQUAKE = 'Strong wildfire', 'strong cataclysm', 45


class extremeWeatherStatus(Enum):
    EXTREMEFLOOD = 'Extreme flood', 'extreme cataclysm', 60
    EXTREMEDROUGHT = 'Extreme drought', 'extreme cataclysm', 60
    EXTREMEWILDFIRE = 'Extreme wildfire', 'extreme cataclysm', 60
    EXTREMEEARTHQUAKE = 'Extreme wildfire', 'extreme cataclysm', 60


class normalIllnesses(Enum):


    # name, description, time lenght(untreated), [affected object?], [effect in %]
    PNEUMONIA = 'Pneumonia', 'Takes your breath away', 1, ['fertility'], [20]


class geneticIllnesses(Enum):
    # name, description, [source genes], [affected object?], [effect in %]
    WHITEDEATH = 'White death', 'Being too white is a terminal sin.', [EyeColor.GRAY, HairColor.WHITE], ['lifespan', 'fertility'], [50, 25]
    BLACKDEATH = 'Black death', 'Black live does not matter', [EyeColor.GRAY, HairColor.WHITE], ['lifespan', 'fertility'], [25, 50]

