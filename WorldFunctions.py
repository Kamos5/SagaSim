

def caltulatePossibleTerritoryExpansions(region, world,regionsTerritories):
    possibleExpansion = []

    for terrytoryX, terrytoryY, in region.getRegionTerritories():
        # LEFT
        left = (terrytoryX - 1, terrytoryY)
        if not terrytoryX == 0 and left not in region.getRegionTerritories() and left not in possibleExpansion and left not in regionsTerritories:
            possibleExpansion.append((terrytoryX - 1, terrytoryY))
        # RIGHT
        right = (terrytoryX + 1, terrytoryY)
        if not terrytoryX == world.getWorldMap().getWidth() - 1 and right not in region.getRegionTerritories() and right not in possibleExpansion and right not in regionsTerritories:
            possibleExpansion.append((terrytoryX + 1, terrytoryY))
        # UP
        up = (terrytoryX, terrytoryY - 1)
        if not terrytoryY == 0 and up not in region.getRegionTerritories() and up not in possibleExpansion and up not in regionsTerritories:
            possibleExpansion.append((terrytoryX, terrytoryY - 1))
        # DOWN
        down = (terrytoryX, terrytoryY + 1)
        if not terrytoryY == world.getWorldMap().getHeight() - 1 and down not in region.getRegionTerritories() and down not in possibleExpansion and down not in regionsTerritories:
            possibleExpansion.append((terrytoryX, terrytoryY + 1))

    return possibleExpansion