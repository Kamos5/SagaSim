import random

import Utils

englishRegionNames = [

    'Englaland',
    'Britannia',
    'Albion',
    'Blighty'

]

slavicRegionNames = [

    'Carantania',
    'Wends',
    'Antes',
    'Sclaveni'

]

middleEastRegionNames = [

    'Assyria',
    'Babylon',
    'Mitanii',
    'Hittite'
]

scandinavianRegionNames = [

    'Midgard',
    'Nidavellir',
    'Alfheim',
    'Svartalfheim',
    'Muspelheim',
    'Saami'
]

egiptRegionNames = [

]



activeNames = []

def getRandomRegionName():

    Utils.randomFromCollection(getRegionNameList())

def getRegionNameList():

    englishRegionName = randomEnglishRegionName()
    norseRegionName = randomNorseRegionName()
    slavicRegionName = randomSlavicRegionName()

    regionsName = [
        englishRegionName,
        norseRegionName
    ]

    return regionsName

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

def randomNorseRegionName():

    if len(englishRegionNames) > 0:
        listToChooseFrom = englishRegionNames
        choice = random.choice(listToChooseFrom)
        englishRegionNames.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice
