
class House():

    def __init__(self):
        self.region = None
        self.settlement = None
        self.houseType = None
        self.firstOwner = None
        self.secondOwner = None
        self.residents = []
        self.durability = 100

    def getHouseRegion(self):
        return self.region

    def setHouseRegion(self, newRegion):
        self.region = newRegion

    def getHouseSettlement(self):
        return self.settlement

    def setHouseSettlement(self, newSettlement):
        self.settlement = newSettlement

    def getHouseHouseType(self):
        return self.houseType

    def setHouseHouseType(self, houseType):
        self.houseType = houseType

    def getHouseFirstOwner(self):
        return self.firstOwner

    def setHouseFirstOwner(self, newFirstOwner):
        self.firstOwner = newFirstOwner

    def getHouseSecondOwner(self):
        return self.secondOwner

    def setHouseSecondOwner(self, newSecondOwner):
        self.secondOwner = newSecondOwner

    def getHouseResidents(self):
        return self.residents

    def setHouseResidents(self, residents):
        self.residents = residents

    def addHouseResident(self, newResident):
        self.residents.append(newResident)

    def getHouseDurability(self):
        return self.durability

    def setHouseDurability(self, durability):
        self.durability = durability

    def changeHouseDurability(self, value):
        self.durability += value
