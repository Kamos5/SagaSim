
def spoiledFood(settlement, world):

    settlement.events.append(str(settlement.getSettlementName()) + " had lost some stockpiled food due to spoilage after the winter.")

def raided(settlement, target, foodAmmount, wealthAmmount, world):

    settlement.events.append(f'{settlement.getSettlementName()} had raided {target.getSettlementName()} and had stolen {foodAmmount} units of food and {wealthAmmount} units of wealth on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')

def beenRaided(settlement, foodAmmount, wealthAmmount, world):

    settlement.events.append(f'{settlement.getSettlementName()} had been raided and lost {foodAmmount} units of food and {wealthAmmount} units of wealth on the {world.getDay()}/{world.getMonth().value[1]}/{world.getYear()}')


