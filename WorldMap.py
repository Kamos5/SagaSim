

class WorldMap:

    def __init__(self):

        self.width = 200
        self.height = 100

        self.worldMapObj = []

    def generateMap(self):

        for i in range(self.width):
            for j in range(self.height):
                self.worldMapObj.append(((),()))


    def addField(self, borderColor, color=None, x=0, y=0):

        # xCord = len(self.worldMapObj) % self.width
        # yCord = len(self.worldMapObj) // self.width
        if [(x, y), (borderColor, color)] not in self.getWorldMapObj():
            self.worldMapObj.append([(x, y), (borderColor, color)])

    def resetWorldMapObj(self):
        self.worldMapObj = []

    def getWorldMapObj(self):
        return self.worldMapObj

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height