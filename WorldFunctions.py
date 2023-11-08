import pickle


def caltulatePossibleTerritoryExpansions(region, world, regionsTerritories):

    possibleExpansion = set()
    setRegionTerritories = set(region.getRegionTerritories())
    setRegionsTerritories = set(regionsTerritories)
    impassibleTerrain = world.getWorldMap().getImpassibleTerrain()
    setDouble = setRegionsTerritories.union(impassibleTerrain)

    x0 = 0
    y0 = 0
    maxX = world.getWorldMap().getWidth() - 1
    maxY = world.getWorldMap().getHeight() - 1

    for terrytoryX, terrytoryY in setRegionTerritories:

        # LEFT
        left = (terrytoryX - 1, terrytoryY)
        if left not in setDouble and not terrytoryX == x0:
            possibleExpansion.add((terrytoryX - 1, terrytoryY))
        # RIGHT
        right = (terrytoryX + 1, terrytoryY)
        if right not in setDouble and not terrytoryX == maxX:
            possibleExpansion.add((terrytoryX + 1, terrytoryY))
        # UP
        up = (terrytoryX, terrytoryY - 1)
        if up not in setDouble and not terrytoryY == y0:
            possibleExpansion.add((terrytoryX, terrytoryY - 1))
        # DOWN
        down = (terrytoryX, terrytoryY + 1)
        if down not in setDouble and not terrytoryY == maxY:
            possibleExpansion.add((terrytoryX, terrytoryY + 1))

    return list(possibleExpansion)

def caltulatePossibleTerritoryExpansionsForSinglePoint(region, world, regionsTerritories, point):

    possibleExpansion = set()
    setRegionTerritories = set(region.getRegionTerritories())
    setRegionsTerritories = set(regionsTerritories)

    setDouble = setRegionTerritories & setRegionsTerritories

    x0 = 0
    y0 = 0
    maxX = world.getWorldMap().getWidth() - 1
    maxY = world.getWorldMap().getHeight() - 1


    terrytoryX, terrytoryY = point

    # LEFT
    left = (terrytoryX - 1, terrytoryY)
    if left not in setDouble and not terrytoryX == x0:
        possibleExpansion.add((terrytoryX - 1, terrytoryY))
    # RIGHT
    right = (terrytoryX + 1, terrytoryY)
    if right not in setDouble and not terrytoryX == maxX:
        possibleExpansion.add((terrytoryX + 1, terrytoryY))
    # UP
    up = (terrytoryX, terrytoryY - 1)
    if up not in setDouble and not terrytoryY == y0:
        possibleExpansion.add((terrytoryX, terrytoryY - 1))
    # DOWN
    down = (terrytoryX, terrytoryY + 1)
    if down not in setDouble and not terrytoryY == maxY:
        possibleExpansion.add((terrytoryX, terrytoryY + 1))

    return list(possibleExpansion)


def saveWorld(world):
    print("save")
    with open('save.txt', 'wb') as outp:  # Overwrites any existing file.
        pickle.dump(world, outp, pickle.HIGHEST_PROTOCOL)

def loadWorld(world):
    print('load')
    return pickle.load(open("save.txt", "rb"))