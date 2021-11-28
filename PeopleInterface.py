def findOneFirstName (people, UUID):

    if (UUID != ''):
        try:
            index = [x.personUUID for x in people].index(UUID)
        except ValueError:
            index = -1
        if (index >= 0):
            return people[index].firstName
        else:
            return ''
    else:
        return ''

def findOneFamilyName (people, UUID):

    if (UUID != ''):
        try:
            index = [x.personUUID for x in people].index(UUID)
        except ValueError:
            index = -1
        if (index >= 0):
            return people[index].familyName
        else:
            return ''
    else:
        return ''

def findOneLifeSpan (people, UUID):

    if (UUID != ''):
        try:
            index = [x.personUUID for x in people].index(UUID)
        except ValueError:
            index = -1
        if (index >= 0):
            return people[index].lifespan
        else:
            return ''
    else:
        return ''

def findOneFertility (people, UUID):

    if (UUID != ''):
        try:
            index = [x.personUUID for x in people].index(UUID)
        except ValueError:
            index = -1
        if (index >= 0):
            return people[index].fertility
        else:
            return ''
    else:
        return ''

def findOneHairColor (people, UUID):

    if (UUID != ''):
        try:
            index = [x.personUUID for x in people].index(UUID)
        except ValueError:
            index = -1
        if (index >= 0):
            return people[index].hairColor
        else:
            return ''
    else:
        return ''

def findOneHairColorGen1 (people, UUID):

    if (UUID != ''):
        try:
            index = [x.personUUID for x in people].index(UUID)
        except ValueError:
            index = -1
        if (index >= 0):
            return people[index].hairColorGen1
        else:
            return ''
    else:
        return ''

def findOneHairColorGen2 (people, UUID):

    if (UUID != ''):
        try:
            index = [x.personUUID for x in people].index(UUID)
        except ValueError:
            index = -1
        if (index >= 0):
            return people[index].hairColorGen2
        else:
            return ''
    else:
        return ''

def findOneFamilyName (people, UUID):

    if (UUID != ''):
        try:
            index = [x.personUUID for x in people].index(UUID)
        except ValueError:
            index = -1
        if (index >= 0):
            return people[index].familyName
        else:
            return ''
    else:
        return ''

def findOnePersonObj (people, UUID):

    if (UUID != ''):
        try:
            index = [x.personUUID for x in people].index(UUID)
        except ValueError:
            index = -1
        if (index >= 0):
            return people[index]
        else:
            return ''
    else:
        return ''

def findParentsDeadChildrensList(people, UUID):

    fatherList = []
    foundFather = 0
    motherList = []
    foundMother = 0
    for x in people:
        if (x.personUUID == UUID.father):
            fatherList = x.deadChildrens
            foundFather = 1
        if (x.personUUID == UUID.mother):
            motherList = x.deadChildrens
            foundMother = 1
        if foundFather == 1 and foundMother == 1:
            return fatherList, motherList
    return fatherList, motherList
