from enum import Enum


class HouseType():

    def __init__(self, tier=0, name='', description='', happinessModifier=0, cost=0, maintenance=0, costToUpgrade=0):
        self.tier = tier
        self.name = name
        self.description = description
        self.happinessModifier = happinessModifier
        self.cost = cost
        self.accomodations = []
        self.maintenance = maintenance
        self.costToUpgrade = costToUpgrade

    def getHouseTypeName(self):
        return self.name

    def getHouseUpkeep(self):
        return self.maintenance

    def getTier(self):
        return self.tier

    def getCostToUpgrade(self):
        return self.costToUpgrade

class HouseEnums(Enum):

    NULL = HouseType(0, "NULLNAME", "NULLDESC", 0, 0, 0)
    TENT = HouseType(1, "Tent", "Most simple out of all housing", -20, 0, 0, 100)
    SHACK = HouseType(2, "Shack", "A step forward. Better than nothing", -10, 100, 2, 300)
    WOODENHOUSE = HouseType(3, "Wooden house", "Easy to build, hard to resist a fire", 0, 300, 6, 500)
    STONEHOUSE = HouseType(4, "Stone house", "Big bad wolf is not going to blow it away", 10, 500, 10, 750)
    BRICKHOUSE = HouseType(5, "Brick house", "Starting to feel cozy.", 20, 750, 15, 1000)
    MANOR = HouseType(6, "Manor", "Living like elite.", 30, 1000, 20, 2000)
    PALACE = HouseType(7, "Palace", "Dream of others is your dwelling.", 50, 2000, 40, 100000000000000000000000000000)

