from enum import Enum


class LifeStatus(Enum):
    ALIVE = 'alive'
    DEAD = 'dead'
    COMATOSE = 'comatose'


class MaritalStatus(Enum):
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
    AMBER = 5, 'amber'
    HAZEL = 4, 'hazel'
    GREEN = 3, 'green'
    BLUE = 2, 'yellow'
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


class Settlements(Enum):

    VILLAGE = 'village'
    TOWN = 'town'