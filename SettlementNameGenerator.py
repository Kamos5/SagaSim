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

norseSettlementsNames = [

    'Aebeltoft',
    'Kalbaek',
    'Breiðhatóftir',
    'Laugarbrekka',
    'Búðir',
    'Ravndal',
    'Djúpidalur',
    'Essetofte',
    'Fulby',
    'Aeblegården',
    'Hulgade',
    'Højtoft',
    'Innrihólmur',
    'Holbaek',
    'Stenhus',
    'Kallekot',
    'Kirkeby',
    'Klibo',
    'Langatóftir',
    'Lund',
    'Akranes',
    'Sandvik',
    'Stenhus',
    'Haraldssun',
    'Thornby',
    'Torp',
    'Bregentved',
    'Tóftir',
    'Ebeltoft',
    'Kvívi'

]

slavicSettlementsNames = [

    'Kalisz',
    'Stobi',
    'Zadar',
    'Plovdiv',
    'Ptuj',
    'Kerch',
    'Beograd',
    'Nitra',
    'Plzeň',
    'Praha',
    'Polotsk',
    'Budva',
    'Tomislavgrad',
    'Derbent',
    'Kraków',
    'Ohrid',
    'Vis',
    'Sozopol',
    'Kiev',
    'Trenčin',
    'Vitebsk',
    'Kotor',
    'Stolac',
    'Novgorod'

]
activeNames = []
abandonedSettlements = []

def randomEnglishSettlementsName (rebuildOldSettlement = False):

    copyList = englishSettlementsNames.copy()
    if len(copyList) > 0:
        listToChooseFrom = copyList
        if rebuildOldSettlement:
            listToChooseFrom = abandonedSettlements
        choice = randomChoice(listToChooseFrom)
        copyList.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomNorseSettlementsName (rebuildOldSettlement = False):

    copyList = norseSettlementsNames.copy()
    if len(copyList) > 0:
        listToChooseFrom = copyList
        if rebuildOldSettlement:
            listToChooseFrom = abandonedSettlements
        choice = randomChoice(listToChooseFrom)
        copyList.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomSlavicSettlementsName (rebuildOldSettlement = False):

    copyList = slavicSettlementsNames.copy()
    if len(copyList) > 0:
        listToChooseFrom = copyList
        if rebuildOldSettlement:
            listToChooseFrom = abandonedSettlements
        choice = randomChoice(listToChooseFrom)
        copyList.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomMusslimSettlementsName(rebuildOldSettlement = False):

    copyList = englishSettlementsNames.copy()
    if len(copyList) > 0:
        listToChooseFrom = copyList
        if rebuildOldSettlement:
            listToChooseFrom = abandonedSettlements
        choice = randomChoice(listToChooseFrom)
        copyList.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomRomanSettlementsName(rebuildOldSettlement = False):

    copyList = englishSettlementsNames.copy()
    if len(copyList) > 0:
        listToChooseFrom = copyList
        if rebuildOldSettlement:
            listToChooseFrom = abandonedSettlements
        choice = randomChoice(listToChooseFrom)
        copyList.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomAfricanSettlementsName(rebuildOldSettlement = False):

    copyList = englishSettlementsNames.copy()
    if len(copyList) > 0:
        listToChooseFrom = copyList
        if rebuildOldSettlement:
            listToChooseFrom = abandonedSettlements
        choice = randomChoice(listToChooseFrom)
        copyList.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice
