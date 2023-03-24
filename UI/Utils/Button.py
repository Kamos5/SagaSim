

class Button:

    def __init__(self, buttonName, buttonCategory = ''):

        self.buttonName = buttonName
        self.buttonCategory = buttonCategory
        self.active = False

    def getButtonName(self):
        return self.buttonName

    def getButtonCategory(self):
        return self.buttonCategory

    def getButtonFlag(self):
        return self.active

    def changeActiveStatus(self):
        self.active = not self.active

    def getIsActive(self):
        return self.active