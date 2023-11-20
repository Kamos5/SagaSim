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

class GeneralHealth(Enum): #Index, status,
    HEALTHY = 0, 'Healthy'
    WEAKEN = 1, 'Weaken'
    POOR = 2, 'Poor'
    CRIPPLING = 3, 'Crippling'
    TERMINAL = 4, 'Terminal'
    DEATH = 5, 'Death'

def getGeneralHealthArray():
    return [GeneralHealth.HEALTHY, GeneralHealth.WEAKEN, GeneralHealth.POOR, GeneralHealth.CRIPPLING, GeneralHealth.TERMINAL, GeneralHealth.DEATH]

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
    CHILDSICKNESS = 'child sickness'
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
    BLACK = 5, 'black', (63, 40, 24)
    BROWN = 4, 'brown', (148, 97, 60)
    YELLOW = 3, 'yellow', (247, 226, 171)
    RED = 2, 'red', (207, 158, 124)
    WHITE = 1, 'white', (255, 223, 196)
    ALBIN = 0, 'albin', (255, 250, 250)

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

            #weater, intensity, effect, duration(days), tempChange
    NORMAL = 'Normal', 'normal weather', 0, 0, 0

class weatherFloods(Enum): #MAR/APR/MAY
    MILD = 'Mild flood', 'mild cataclysm', 15, 7, -5
    MEDIUM = 'Medium flood', 'medium cataclysm', 30, 14, -6
    STRONG = 'Strong flood', 'strong cataclysm', 45, 21, -7
    EXTREME = 'Extreme flood', 'extreme cataclysm', 60, 28, -8

class weatherDroughts(Enum): #JUN/JUL/AUG
    MILD = 'Mild drought', 'mild cataclysm', 15, 14, 5
    MEDIUM = 'Medium drought', 'medium cataclysm', 30, 28, 6
    STRONG = 'Strong drought', 'strong cataclysm', 45, 42, 7
    EXTREME = 'Extreme drought', 'extreme cataclysm', 60, 56, 8

class weatherWildFire(Enum): #SEP/OCT/NOV
    MILD = 'Mild wildfire', 'mild cataclysm', 15, 7, 7
    MEDIUM = 'Medium wildfire', 'medium cataclysm', 30, 14, 8
    STRONG = 'Strong wildfire', 'strong cataclysm', 45, 21, 9
    EXTREME = 'Extreme wildfire', 'extreme cataclysm', 60, 28, 10

class weatherBlizzard(Enum):  #DEC/JAN/FEB
    MILD = 'Mild blizzard', 'mild cataclysm', 15, 7, -7
    MEDIUM = 'Medium blizzard', 'medium cataclysm', 30, 14, -8
    STRONG = 'Strong blizzard', 'strong cataclysm', 45, 21, -9
    EXTREME = 'Extreme blizzard', 'extreme cataclysm', 60, 28, -10

class weatherEarthQuake(Enum):
    MILD = 'Mild earth quake', 'mild cataclysm', 15, 2, 0
    MEDIUM = 'Medium wildfire', 'medium cataclysm', 30, 3, 0
    STRONG = 'Strong wildfire', 'strong cataclysm', 45, 5, 0
    EXTREME = 'Extreme wildfire', 'extreme cataclysm', 60, 7, 0





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
    BLACKDEATH = 'Black death', 'Black live does not matter', [EyeColor.BLACK, HairColor.BLACK], ['lifespan', 'fertility'], [25, 50]

class ItemType(Enum):
    FOOD = 'food'
    MATERIAL = 'material'
    MISC = 'misc'

class SkillsLevels(Enum):

    # lvl, skill name, description, requiredXp, modifier
    NONE = 0, 'None', 'has no skill whatsoever',                0, 0.5
    NOVICE = 1, 'Novice', 'became novice',                      100, 0.6
    ADEQUATE = 2, 'Adequate', 'became adequate',                200, 0.7
    COMPETENT = 3, 'Competent', 'became competent',             300, 0.8
    SKILLED = 4, 'Skilled', 'became skilled',                   400, 0.9
    PROFICIENT = 5, 'Proficient', 'became proficient',          500, 1
    TALENTED = 6, 'Talented', 'became talented',                600, 1.1
    ADEPT = 7, 'Adept', 'became adept',                         1000, 1.2
    EXPERT = 8, 'Expert', 'became expert',                      2000, 1.3
    PROFESSIONAL = 9, 'Professional', 'became professional',    3000, 1.4
    ACCOMPLISHED = 10, 'Accomplished', 'became accomplished',   5000, 1.5
    GREAT = 11, 'Great', 'became great',                        7000, 1.6
    MASTER = 12, 'Master', 'became master',                     9000, 1.7
    HIGHMASTER = 13, 'High Master', 'became high master',       10000, 1.8
    GRANDMASTER = 14, 'Grand Master', 'became grand master',    11000, 1.9
    LEGENDARY = 15, 'Legendary', 'became legendary',            12000, 2.0


class SkillNames(Enum):
    LABOR = 'Labor'
    ADMIN = 'Administrative'
    FIGHTER = 'Fighter'

class Seasons(Enum):
    WINTER = 'Winter'
    SPRING = 'Spring'
    SUMMER = 'Summer'
    FALL = 'Fall'