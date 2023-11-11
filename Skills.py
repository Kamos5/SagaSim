import Enums


class Skills:

    def __init__(self):
        self.skillLaborXp = 0
        self.skillLaborLvl = Enums.skillLevels.NONE
        self.skillPhysical = 0
        self.skillPhysicalLvl = Enums.skillLevels.NONE
        self.skillFishery = 0
        self.skillFisheryLvl = Enums.skillLevels.NONE
        self.skillAdmin = 0
        self.skillAdminLvl = Enums.skillLevels.NONE
        self.skillFighter = 0
        self.skillFighterLvl = Enums.skillLevels.NONE


    def isEnoughXpForLvl(self):
        return True