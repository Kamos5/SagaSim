import NameGenerator
from Family import Family
import Parameters
import FamilyNameGenerator

def Init(world):

    startingSettlements = Parameters.startingSettlementsPerProvince
    families = []

    for region in world.getRegions():
        for familyNumber in range(Parameters.startingNumberOfFamiliesPerRegion):
            familyName = FamilyNameGenerator.getNewLastNameBasedOnCulture(culture=region.getOriginalCulture(), world=world)
            # familyName = FamilyNameGenerator.getNewLastNameBasedOnRegion(world.getRegionFromIndex(region))
            family = Family(familyName)
            family.setFoundingYear(world.getYear())
            family.setOriginRegion(region)
            provinceObj = region.getProvinces()[0]
            family.setOriginProvince(provinceObj)
            family.setOriginSettlement(provinceObj.getSettlementFromIndex(familyNumber % startingSettlements))
            family.setOriginCulture(region.getOriginalCulture())
            families.append(family)

    return families

