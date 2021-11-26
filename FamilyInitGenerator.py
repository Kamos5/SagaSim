from Family import Family as FamilyObj
import FamilyNameGenerator

def Init(world):

    initFamilityNumber = 1
    var = 0
    families = []
    while var < 1:

        familyName = FamilyNameGenerator.getInitFamilyName(var)
        family = FamilyObj(familyName)
        family.foundingYear = world.getYear()
        families.append(family)
        var += 1

    return families

