import Enums
from Skill import Skill


class Skills:

    def __init__(self):
        self.skills = []
        self.skills.append(Skill(Enums.SkillNames.LABOR, 0, Enums.SkillsLevels.NONE))
        self.skills.append(Skill(Enums.SkillNames.ADMIN, 0, Enums.SkillsLevels.NONE))
        self.skills.append(Skill(Enums.SkillNames.FIGHTER, 0, Enums.SkillsLevels.NONE))

    def getSkills(self):
        return self.skills

    def getLaborSkill(self):
        for skill in self.skills:
            if skill.skillName == Enums.SkillNames.LABOR:
                return skill

    def getAdminSkill(self):
        for skill in self.skills:
            if skill.skillName == Enums.SkillNames.ADMIN:
                return skill

    def getFighterSkill(self):
        for skill in self.skills:
            if skill.skillName == Enums.SkillNames.FIGHTER:
                return skill

