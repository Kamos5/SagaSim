class GameState:

    def __init__(self):
        # MENU 0
        # SIMULATION 100


        self.state = 0


    def changeToInit(self):
        self.state = 100

    def changeToSimulation(self):
        self.state = 101

    def isMenuState(self):
        return 0 <= self.state < 100

    def isSimulationState(self):
        return self.state > 100

    def isInitState(self):
        return self.state == 100