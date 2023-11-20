
def spoiledFood(settlement, world):

    settlement.events.append(str(settlement.getSettlementName()) + " had lost some stockpiled food due to spoilage after winter on the " + str(world.getDay()) + "/" + str(world.getMonth().value[1]) + "/" + str(world.getYear()))

def raided(settlement, target, ammount, world):

    settlement.events.append(str(settlement.getSettlementName()) + " had raided " + str(target.getSettlementName()) + " and had stolen " + str(ammount) + " units of food on the  " + str(world.getDay()) + "/" + str(world.getMonth().value[1]) + "/" + str(world.getYear()))


