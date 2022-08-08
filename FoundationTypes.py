from enum import Enum


class FoundationType():

    def __init__(self, name, description, yieldModifier):
        self.name = name
        self.description = description
        self.yieldModifier = yieldModifier


class FoundationEnums(Enum):

    POOR = FoundationType("Poor", "Foundation here is poor", 80)
    MEDIUM = FoundationType("Medium", "Foundation here is medium.", 100)
    GOOD = FoundationType("Good", "Foundation here is good.", 120)

