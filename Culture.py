from Enums import Sexes

class Culture:

    def __init__(self, cname):
        self.cultureName = cname
        self.inheritanceBy = Sexes.MALE


    def getInheritanceBy(self):
        return self.inheritanceBy