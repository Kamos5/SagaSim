

class Button:

    def __init__(self, buttonName):

        self.buttonName = buttonName
        self.active = False

    def getButtonName(self):
        return self.buttonName

    def getButtonFlag(self):
        return self.active

    def changeActiveStatus(self):
        self.active = not self.active
