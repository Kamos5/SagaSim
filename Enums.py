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
    UNKNOWN = 'unknown'
    NULL = ''


class HairColor(Enum):
    BLACK = 5, 'black'
    BROWN = 4, 'brown'
    YELLOW = 3, 'yellow'
    RED = 2, 'red'
    WHITE = 1, 'white'
    GRAY = 0, 'gray'


class EyeColor(Enum):
    BLACK = 7, 'black'
    BROWN = 6, 'brown'
    AMBER = 5, 'amber'#bursztynowe
    HAZEL = 4, 'hazel'#piwne
    GREEN = 3, 'green'
    BLUE = 2, 'blue'
    GRAY = 1, 'gray'

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