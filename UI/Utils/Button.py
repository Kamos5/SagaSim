

class Button:

    def __init__(self, buttonName, buttonCategory = ''):

        self.buttonName = buttonName
        self.buttonCategory = buttonCategory
        self.active = False
        self.onHover = False

    def getButtonName(self):
        return self.buttonName

    def getButtonCategory(self):
        return self.buttonCategory

    def getButtonFlag(self):
        return self.active

    def changeActiveStatus(self):
        self.active = not self.active

    def setActiveStatus(self):
        self.active = True

    def resetActiveStatus(self):
        self.active = False

    def getIsActive(self):
        return self.active

    def getOnHover(self):
        return self.onHover

    def setOnHover(self):
        self.onHover = True

    def resetOnHover(self):
        self.onHover = False
