import Enums


class Skill:

    def __init__(self, skillName = '', skillXp = 0, skillLevel = Enums.skillLevels.NONE):
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
        self.skillXp = round(self.skillXp + moreXp, 3)

    def getSkillLevel(self):
        return self.skillLevel

    def changeSkillLevel(self, newLevel):
        self.skillLevel = newLevel