import random

englishRegionNames = [

    'Englaland',
    'Britannia',
    'Albion',
    'Blighty'

]

activeNames = []

def randomEnglishRegionName ():

    if len(englishRegionNames) > 0:
        listToChooseFrom = englishRegionNames
        choice = random.choice(listToChooseFrom)
        englishRegionNames.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic British Region Name'
    return choice

def randomSlavicRegionName ():

    if len(englishRegionNames) > 0:
        listToChooseFrom = englishRegionNames
        choice = random.choice(listToChooseFrom)
        englishRegionNames.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomMusslimRegionName():

    if len(englishRegionNames) > 0:
        listToChooseFrom = englishRegionNames
        choice = random.choice(listToChooseFrom)
        englishRegionNames.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomRomanRegionName():

    if len(englishRegionNames) > 0:
        listToChooseFrom = englishRegionNames
        choice = random.choice(listToChooseFrom)
        englishRegionNames.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomAfricanRegionName():

    if len(englishRegionNames) > 0:
        listToChooseFrom = englishRegionNames
        choice = random.choice(listToChooseFrom)
        englishRegionNames.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice
