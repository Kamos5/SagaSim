from random import choice as randomChoice

englishSettlementsNames = [

    'Amesbury',
    'Bedford',
    'Chesterfield',
    'Darlington',
    'Edenbridge',
    'Framlingham',
    'Grassington',
    'Hastings',
    'Ilford',
    'Jarrow',
    'Keswick',
    'Ledbury',
    'Maltby',
    'Newmarket',
    'Oldham',
    'Plymouth',
    'Queenborough',
    'Reading',
    'Stotfold',
    'Thornaby'

]

activeNames = []
abandonedSettlements = []

def randomEnglishSettlementsName (rebuildOldSettlement = False):

    if len(englishSettlementsNames) > 0:
        listToChooseFrom = englishSettlementsNames
        if rebuildOldSettlement:
            listToChooseFrom = abandonedSettlements
        choice = randomChoice(listToChooseFrom)
        englishSettlementsNames.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomSlavicSettlementsName (rebuildOldSettlement = False):

    if len(englishSettlementsNames) > 0:
        listToChooseFrom = englishSettlementsNames
        if rebuildOldSettlement:
            listToChooseFrom = abandonedSettlements
        choice = randomChoice(listToChooseFrom)
        englishSettlementsNames.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomMusslimSettlementsName(rebuildOldSettlement = False):

    if len(englishSettlementsNames) > 0:
        listToChooseFrom = englishSettlementsNames
        if rebuildOldSettlement:
            listToChooseFrom = abandonedSettlements
        choice = randomChoice(listToChooseFrom)
        englishSettlementsNames.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomRomanSettlementsName(rebuildOldSettlement = False):

    if len(englishSettlementsNames) > 0:
        listToChooseFrom = englishSettlementsNames
        if rebuildOldSettlement:
            listToChooseFrom = abandonedSettlements
        choice = randomChoice(listToChooseFrom)
        englishSettlementsNames.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomAfricanSettlementsName(rebuildOldSettlement = False):

    if len(englishSettlementsNames) > 0:
        listToChooseFrom = englishSettlementsNames
        if rebuildOldSettlement:
            listToChooseFrom = abandonedSettlements
        choice = randomChoice(listToChooseFrom)
        englishSettlementsNames.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice
