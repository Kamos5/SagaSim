from random import choice as randomChoice

import Utils

englishRegionNames = [

    'Englaland',
    'Britannia',
    'Albion',
    'Blighty',

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

norseRegionNames = [

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
        norseRegionName,
        slavicRegionName
    ]

    return regionsName

def randomEnglishRegionName ():

    if len(englishRegionNames) > 0:
        listToChooseFrom = englishRegionNames
        choice = randomChoice(listToChooseFrom)
        activeNames.append(choice)
    else:
        choice = 'Generic British Region Name'
    return choice

def randomSlavicRegionName ():

    if len(slavicRegionNames) > 0:
        listToChooseFrom = slavicRegionNames
        choice = randomChoice(listToChooseFrom)
        activeNames.append(choice)
    else:
        choice = 'Generic Slavic Region Name'
    return choice

def randomMusslimRegionName():

    if len(englishRegionNames) > 0:
        listToChooseFrom = englishRegionNames
        choice = randomChoice(listToChooseFrom)
        activeNames.append(choice)
    else:
        choice = 'Generic Region Name'
    return choice

def randomRomanRegionName():

    if len(englishRegionNames) > 0:
        listToChooseFrom = englishRegionNames
        choice = randomChoice(listToChooseFrom)
        activeNames.append(choice)
    else:
        choice = 'Generic Region Name'
    return choice

def randomAfricanRegionName():

    if len(englishRegionNames) > 0:
        listToChooseFrom = englishRegionNames
        choice = randomChoice(listToChooseFrom)
        activeNames.append(choice)
    else:
        choice = 'Generic Region Name'
    return choice

def randomNorseRegionName():

    if len(englishRegionNames) > 0:
        listToChooseFrom = norseRegionNames
        choice = randomChoice(listToChooseFrom)
        activeNames.append(choice)
    else:
        choice = 'Generic Region Name'
    return choice
