

class Button:

    def __init__(self, buttonName, buttonName2='', buttonCategory = ''):

        #First identifier mostly object sometimes string where no object (look for buttons in plotscreen)
        self.buttonName = buttonName
        #Second idenrifier only string  in object + string where same object is shown
        self.buttonName2 = buttonName2
        self.buttonCategory = buttonCategory
        self.buttonObject = None
        self.active = False
        self.onHover = False
        self.highlight = False

    def getButtonName(self):
        return self.buttonName

    def getButtonName2(self):
        return self.buttonName2

    def getButtonCategory(self):
        return self.buttonCategory

    def getButtonObject(self):
        return self.buttonObject

    def setButtonObject(self, newObj):
        self.buttonObject = newObj

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

    def setHighlight(self):
        self.highlight = True

    def switchHighlight(self):
        self.highlight = not self.highlight

    def getHighlight(self):
        return self.highlight

    def resetHighlight(self):
        self.highlight = False