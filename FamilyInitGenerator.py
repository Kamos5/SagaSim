import NameGenerator
from Family import Family
import Parameters
import FamilyNameGenerator

def Init(world, chosenName):

    startingSettlements = Parameters.startingSettlementsPerProvince
    families = []

    regionCounter = 1
    for region in world.getRegions():
        familyCounter = 1
        for familyNumber in range(Parameters.startingNumberOfFamiliesPerRegion):
            if (regionCounter == 1 and familyCounter == 1):
                familyName = FamilyNameGenerator.getNewLastNameBasedOnCulture(culture=region.getOriginalCulture(), world=world, chosenName = chosenName)
            else:
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
            familyCounter += 1
        regionCounter += 1

    return families

