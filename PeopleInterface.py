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
