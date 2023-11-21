import Enums


class Skill:

    def __init__(self, skillName = '', skillXp = 0, skillLevel = Enums.SkillsLevels.NONE):
        self.skillName = skillName
        self.skillXp = skillXp
        self.skillLevel = skillLevel

    def getSkillName(self):
        return self.skillName

    def getSkillXp(self):
        return self.skillXp

    def changeSkillXp(self, newXp):
        self.skillXp = newXp

    def increaseSkillXp(self, moreXp):
        didGetBetter = False
        self.skillXp = round(self.skillXp + moreXp, 2)
        for skillLevels in Enums.SkillsLevels:
            if self.skillXp >= skillLevels.value[3] and self.getSkillLevel().value[0] + 1 == skillLevels.value[0]:
                self.skillLevel = skillLevels
                didGetBetter = self.getSkillLevel()

        return didGetBetter

    def getSkillLevel(self):
        return self.skillLevel

    def changeSkillLevel(self, newLevel):
        self.skillLevel = newLevel