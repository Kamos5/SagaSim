class GameState:

    def __init__(self):
        # MENU 0
        # SIMULATION 100


        self.state = 0


    def getGameState(self):
        return self.state

    def changeToInit(self):
        self.state = 100

    def changeToSimulation(self):
        self.state = 101

    def changeToMenu(self):
        self.state = 1

    def isMenuState(self):
        return self.getGameState() == 1


    def isMenuState(self):
        return 0 <= self.state < 100

    def isSimulationState(self):
        return self.state > 100

    def isInitState(self):
        return self.state == 100