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
    KILLED = 'killed'
    SICKNESS = 'sickness'
    UNKNOWN = 'unknown'
    NULL = ''


class HairColor(Enum):
    BLACK = 5, 'black'
    BROWN = 4, 'brown'
    RED = 3, 'red'
    YELLOW = 2, 'yellow'
    WHITE = 1, 'white'
    UNDEFINED = -1, 'undefined'

class EyeColor(Enum):
    BLACK = 7, 'black'
    BROWN = 6, 'brown'
    AMBER = 5, 'amber'
    HAZEL = 4, 'hazel'
    GREEN = 3, 'green'
    BLUE = 2, 'yellow'
    GRAY = 1, 'gray'
    ALBINO = 0, 'albino'
    UNDEFINED = -1, 'undefined'


class SkinColor(Enum):
    BLACK = 4, 'black'
    BROWN = 3, 'brown'
    YELLOW = 2, 'yellow'
    WHITE = 1, 'white'
    ALBINO = 0, 'albino'
    UNDEFINED = -1, 'undefined'
