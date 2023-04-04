import NameGenerator
from Family import Family
import Parameters
import FamilyNameGenerator

def Init(world):

    startingSettlements = Parameters.startingSettlementsPerRegion
    families = []
    FamilyNameGenerator.makeListsForLastNames(world)
    NameGenerator.makeListsForFirstNames(world)

    for region in range(Parameters.startingNumberOfRegions):

        for familyNumber in range(Parameters.startingNumberOfFamiliesPerRegion):
            familyName = FamilyNameGenerator.getNewLastNameBasedOnCulture(regionNumber=region)
            # familyName = FamilyNameGenerator.getNewLastNameBasedOnRegion(world.getRegionFromIndex(region))
            family = Family(familyName)
            family.setFoundingYear(world.getYear())
            family.setOriginRegion(world.getRegionFromIndex(region))
            world.getRegionFromIndex(region).setActiveSettlements(startingSettlements)
            family.setOriginSettlement(world.getRegionFromIndex(region).getSettlementFromIndex(familyNumber % startingSettlements))
            family.setOriginCulture(world.cultures[region])
            families.append(family)

    return families

