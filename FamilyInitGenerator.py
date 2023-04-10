import NameGenerator
from Family import Family
import Parameters
import FamilyNameGenerator

def Init(world):

    startingSettlements = Parameters.startingSettlementsPerProvince
    families = []
    FamilyNameGenerator.makeListsForLastNames(world)
    NameGenerator.makeListsForFirstNames(world)

    for region in range(Parameters.startingNumberOfRegions):
        regionObj = world.getRegionFromIndex(region)
        for familyNumber in range(Parameters.startingNumberOfFamiliesPerRegion):
            familyName = FamilyNameGenerator.getNewLastNameBasedOnCulture(regionNumber=region)
            # familyName = FamilyNameGenerator.getNewLastNameBasedOnRegion(world.getRegionFromIndex(region))
            family = Family(familyName)
            family.setFoundingYear(world.getYear())
            family.setOriginRegion(regionObj)
            provinceObj = regionObj.getProvinces()[0]
            family.setOriginProvince(provinceObj)
            family.setOriginSettlement(provinceObj.getSettlementFromIndex(familyNumber % startingSettlements))
            family.setOriginCulture(world.cultures[region])
            families.append(family)

    return families

