from Family import Family
from Region import Region
import FamilyNameGenerator
from Settlements import Settlements

def Init(world):

    initFamilityNumber = 1
    var = 0
    families = []
    settlement = Settlements()
    settlement2 = Settlements()
    region = Region("Eden")
    while var < 5:

        if var > 2:
            settlement = settlement2
        familyName = FamilyNameGenerator.getInitFamilyName(var)
        family = Family(familyName)
        family.setFoundingYear(world.getYear())
        family.setOriginRegion(region)
        family.setOriginSettlement(settlement)
        families.append(family)
        var += 1

    return families

