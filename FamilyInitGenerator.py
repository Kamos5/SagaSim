from Family import Family
from Region import Region
import FamilyNameGenerator
from Settlements import Settlements

def Init(world):

    initFamilityNumber = 1
    var = 0
    families = []
    while var < 5:
        familyName = FamilyNameGenerator.getInitFamilyName(var)
        family = Family(familyName)
        family.setFoundingYear(world.getYear())
        family.setOriginRegion(world.getRegionFromIndex(0)) #TODO FOR NOW ONLY 1 REGION
        family.setOriginSettlement(world.getRegionFromIndex(0).getSettlementFromIndex(var % 2))
        families.append(family)
        var += 1

    return families

