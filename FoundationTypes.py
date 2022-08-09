from enum import Enum


class FoundationType():

    def __init__(self, name, description, yieldModifier, chanceWeightModifier):
        self.name = name
        self.description = description
        self.yieldModifier = yieldModifier
        self.chanceWeightModifier = chanceWeightModifier


class FoundationEnums(Enum):

    BARREN = FoundationType("Barren", "Foundation here is barren", 20, 2)
    EXTREMELYPOOR = FoundationType("Extremely poor", "Foundation here is extremely poor", 40, 5)
    VERYPOOR = FoundationType("Very poor", "Foundation here is very poor", 60, 15)
    POOR = FoundationType("Poor", "Foundation here is poor", 80, 35)
    MEDIUM = FoundationType("Medium", "Foundation here is medium.", 100, 65)
    GOOD = FoundationType("Good", "Foundation here is good.", 120, 85)
    VERYGOOD = FoundationType("Very good", "Foundation here is extremely good", 140, 95)
    EXTREMELYGOOD = FoundationType("Extremely good", "Foundation here is extremely good", 160, 98)
    FECUND = FoundationType("Fecund", "Foundation here is extremely fertile", 180, 100)

