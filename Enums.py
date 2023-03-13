from enum import Enum

class Months (Enum):

    JANUARY = 1, 'January', 31, #31
    FEBRUARY = 2, 'February', 28 #28
    MARCH = 3, 'March', 31 #31
    APRIL = 4, 'April', 30 #30
    MAY = 5, 'May', 31 #31
    JUNE = 6, 'June', 30 #30
    JULY = 7, 'July', 31 #31
    AUGUST = 8, 'August', 31 #31
    SEPTEMBER = 9, 'September', 30 #30
    OCTOBER = 10, 'October', 31 #31
    NOVEMBER = 11, 'November', 30 #30
    DECEMBER = 12, 'December', 31 #31

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

            #weater, intensity, effect, duration(days)
    NORMAL = 'Normal', 'normal weather', 0, 0

class weatherFloods(Enum): #MAR/APR/MAY
    MILD = 'Mild flood', 'mild cataclysm', 15, 7
    MEDIUM = 'Medium flood', 'medium cataclysm', 30, 14
    STRONG = 'Strong flood', 'strong cataclysm', 45, 21
    EXTREME = 'Extreme flood', 'extreme cataclysm', 60, 28

class weatherDroughts(Enum): #JUN/JUL/AUG
    MILD = 'Mild drought', 'mild cataclysm', 15, 14
    MEDIUM = 'Medium drought', 'medium cataclysm', 30, 28
    STRONG = 'Strong drought', 'strong cataclysm', 45, 42
    EXTREME = 'Extreme drought', 'extreme cataclysm', 60, 56

class weatherWildFire(Enum): #SEP/OCT/NOV
    MILD = 'Mild wildfire', 'mild cataclysm', 15, 7
    MEDIUM = 'Medium wildfire', 'medium cataclysm', 30, 14
    STRONG = 'Strong wildfire', 'strong cataclysm', 45, 21
    EXTREME = 'Extreme wildfire', 'extreme cataclysm', 60, 28

class weatherBlizzard(Enum):  #DEC/JAN/FEB
    MILD = 'Mild blizzard', 'mild cataclysm', 15, 7
    MEDIUM = 'Medium blizzard', 'medium cataclysm', 30, 14
    STRONG = 'Strong blizzard', 'strong cataclysm', 45, 21
    EXTREME = 'Extreme blizzard', 'extreme cataclysm', 60, 28

class weatherEarthQuake(Enum):
    MILD = 'Mild earth quake', 'mild cataclysm', 15, 2
    MEDIUM = 'Medium wildfire', 'medium cataclysm', 30, 3
    STRONG = 'Strong wildfire', 'strong cataclysm', 45, 5
    EXTREME = 'Extreme wildfire', 'extreme cataclysm', 60, 7





class mildWeatherStatus(Enum):
    MILDFLOOD = 'Mild flood', 'mild cataclysm', 15, 7
    MILDDROUGHT = 'Mild drought', 'mild cataclysm', 15, 14
    MILDWILDFIRE = 'Mild wildfire', 'mild cataclysm', 15, 7
    MILDEARTHQUAKE = 'Mild earth quake', 'mild cataclysm', 15, 2

class mediumWeatherStatus(Enum):
    MEDIUMFLOOD = 'Medium flood', 'medium cataclysm', 30, 14
    MEDIUMDROUGHT = 'Medium drought', 'medium cataclysm', 30, 28
    MEDIUMWILDFIRE = 'Medium wildfire', 'medium cataclysm', 30, 14
    MEDIUMEARTHQUAKE = 'Medium wildfire', 'medium cataclysm', 30, 3

class strongWeatherStatus(Enum):
    STRONGFLOOD = 'Strong flood', 'strong cataclysm', 45, 21
    STRONGDROUGHT = 'Strong drought', 'strong cataclysm', 45, 42
    STRONGWILDFIRE = 'Strong wildfire', 'strong cataclysm', 45, 21
    STRONGEARTHQUAKE = 'Strong wildfire', 'strong cataclysm', 45, 5


class extremeWeatherStatus(Enum):
    EXTREMEFLOOD = 'Extreme flood', 'extreme cataclysm', 60, 28
    EXTREMEDROUGHT = 'Extreme drought', 'extreme cataclysm', 60, 56
    EXTREMEWILDFIRE = 'Extreme wildfire', 'extreme cataclysm', 60, 28
    EXTREMEEARTHQUAKE = 'Extreme wildfire', 'extreme cataclysm', 60, 7


class normalIllnesses(Enum):


    # name, description, time lenght(untreated), [affected object?], [effect in %]
    PNEUMONIA = 'Pneumonia', 'Takes your breath away', 1, ['fertility'], [20]


class geneticIllnesses(Enum):
    # name, description, [source genes], [affected object?], [effect in %]
    WHITEDEATH = 'White death', 'Being too white is a terminal sin.', [EyeColor.GRAY, HairColor.WHITE], ['lifespan', 'fertility'], [50, 25]
    BLACKDEATH = 'Black death', 'Black live does not matter', [EyeColor.GRAY, HairColor.WHITE], ['lifespan', 'fertility'], [25, 50]

