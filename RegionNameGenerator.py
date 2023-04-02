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

egyptRegionNames = [
    'Nubia',
    'Kemet',
    'Deshret',
    'Tawy',
    'Kush'
]



activeNames = []

def getRandomRegionName():

    Utils.randomFromCollection(getRegionNameList())

def getRegionNameList():

    englishRegionName = randomRegionName()


    regionsName = [
        englishRegionName,

    ]

    return regionsName

def randomRegionName (namesList = None, mode = 0):
    choice = 'Generic Region Name'
    if namesList is None:
        if mode == 0:
            if len(englishRegionNames) > 0:
                listToChooseFrom = englishRegionNames
                choice = randomChoice(listToChooseFrom)
        elif mode == 1:
            if len(norseRegionNames) > 0:
                listToChooseFrom = norseRegionNames
                choice = randomChoice(listToChooseFrom)
        elif mode == 2:
            if len(slavicRegionNames) > 0:
                listToChooseFrom = slavicRegionNames
                choice = randomChoice(listToChooseFrom)
        elif mode == 3:
            if len(egyptRegionNames) > 0:
                listToChooseFrom = egyptRegionNames
                choice = randomChoice(listToChooseFrom)
    else:
        choice = randomChoice(namesList)
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
