from Family import Family
from Culture import Culture
import Parameters
import FamilyNameGenerator

def Init(world):

    var = 0
    startingSettlements = Parameters.startingSettlementsPerRegion
    families = []
    culture1 = Culture("Culture1")
    culture2 = Culture("Culture2")
    culture3 = Culture("Culture3")
    culture4 = Culture("Culture4")
    culture5 = Culture("Culture5")
    cultures = [culture1, culture2, culture3, culture4, culture5]
    #var = familie number
    for region in range(Parameters.startingNumberOfRegions):
        for familyNumber in range(Parameters.startingNumberOfFamiliesPerRegion):
            familyName = FamilyNameGenerator.getInitEnglishName()
            family = Family(familyName)
            family.setFoundingYear(world.getYear())
            family.setOriginRegion(world.getRegionFromIndex(region))
            world.getRegionFromIndex(region).setActiveSettlements(startingSettlements)
            family.setOriginSettlement(world.getRegionFromIndex(region).getSettlementFromIndex(familyNumber % startingSettlements))
            family.setOriginCulture(cultures[region])
            families.append(family)

    return families

