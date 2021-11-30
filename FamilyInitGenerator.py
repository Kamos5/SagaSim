from Family import Family
import FamilyNameGenerator

def Init(world):

    initFamilityNumber = 1
    var = 0
    families = []
    while var < 5:

        familyName = FamilyNameGenerator.getInitFamilyName(var)
        family = Family(familyName)
        family.setFoundingYar(world.getYear())
        families.append(family)
        var += 1

    return families

