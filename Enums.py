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