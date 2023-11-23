import Enums
from Enums import Sexes

class Culture:

    def __init__(self, cname):
        self.cultureName = cname
        self.inheritanceBy = Sexes.MALE
        self.united = False
        self.technologiesInProgress = [Enums.TechnologiesEnums.UNITY, 0]
        self.technologiesCompleted = []

    def getInheritanceBy(self):
        return self.inheritanceBy

    def getCultureName(self):
        return self.cultureName

    def getTechnologiesInProgress(self):
        return self.technologiesInProgress

    def addTechnologiesInProgress(self, newTechnology):
        self.technologiesInProgress.append([newTechnology, 0])

    def removeTechnologiesInProgress(self, newTechnology):
        self.technologiesInProgress.remove(newTechnology)

    def increaseTechnologiesInProgress(self, value):
        if self.getPercentOfTechnologyInProgress() < 100:
            self.getTechnologiesInProgress()[1] = round(self.getTechnologiesInProgress()[1] + value, 2)
        else:
            self.addTechnologiesCompleted(self.getTechnologiesInProgress())
            # self.removeTechnologiesInProgress(self.getTechnologiesInProgress()) #TODO TEMPORARY

    def getPercentOfTechnologyInProgress(self):

        return round(self.getTechnologiesInProgress()[1] / self.getTechnologiesInProgress()[0].value[3], 2)

    def getTechnologiesCompleted(self):
        return self.technologiesCompleted

    def addTechnologiesCompleted(self, technologyCompleted):
        self.technologiesCompleted.append(technologyCompleted)