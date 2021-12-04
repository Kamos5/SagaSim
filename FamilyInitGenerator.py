from Family import Family
from Region import Region
import FamilyNameGenerator
from Settlements import Settlements

def Init(world):

    initFamilityNumber = 1
    var = 0
    #TODO SOMETHING IS WRONG WITH MORE
    startingSettlements = 2
    families = []
    #var = familie number
    while var < 5:
        familyName = FamilyNameGenerator.getInitFamilyName()
        family = Family(familyName)
        family.setFoundingYear(world.getYear())
        family.setOriginRegion(world.getRegionFromIndex(0)) #TODO FOR NOW ONLY 1 REGION
        world.getRegionFromIndex(0).setActiveSettlements(startingSettlements)
        family.setOriginSettlement(world.getRegionFromIndex(0).getSettlementFromIndex(var % startingSettlements))
        families.append(family)
        var += 1

    return families

