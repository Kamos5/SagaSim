from enum import Enum


class HouseType():

    def __init__(self, name, description, happinessModifier, cost, maintenance):
        self.name = name
        self.description = description
        self.happinessModifier = happinessModifier
        self.cost = cost
        self.accomodations = []
        self.maintenance = maintenance


class HouseEnums(Enum):

    TENT = HouseType("Tent", "Most simple out of all housing", -20, 0, 0)
    SHACK = HouseType("Shack", "A step forward. Better than nothing", -10, 100, 2)
    WOODENHOUSE = HouseType("Wooden house", "Easy to build, hard to resist a fire", 0, 300, 6)
    STONEHOUSE = HouseType("Stone house", "Big bad wolf is not going to blow it away", 10, 500, 10)
    BRICKHOUSE = HouseType("Brick house", "Starting to feel cozy.", 20, 750, 15)
    MANOR = HouseType("Manor", "Living like elite.", 30, 1000, 20)
    PALACE = HouseType("Palace", "Dream of others is your dwelling.", 50, 2000, 40)

