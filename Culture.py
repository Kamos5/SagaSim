from Enums import Sexes

class Culture:

    def __init__(self, cname):
        self.cultureName = cname
        self.inheritanceBy = Sexes.MALE
        self.united = False

    def getInheritanceBy(self):
        return self.inheritanceBy

    def getCultureName(self):
        return self.cultureName