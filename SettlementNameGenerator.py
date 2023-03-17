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

copyEnglishList = englishSettlementsNames.copy()
copyNorseList = norseSettlementsNames.copy()
copySlavicList = slavicSettlementsNames.copy()
copyMusslimList = englishSettlementsNames.copy()
copyRomanList = englishSettlementsNames.copy()
copyAfricanList = englishSettlementsNames.copy()

def randomEnglishSettlementsName (rebuildOldSettlement = False):

    if len(copyEnglishList) > 0:
        listToChooseFrom = copyEnglishList
        if rebuildOldSettlement:
            listToChooseFrom = abandonedSettlements
        choice = randomChoice(listToChooseFrom)
        copyEnglishList.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomNorseSettlementsName (rebuildOldSettlement = False):

    if len(copyNorseList) > 0:
        listToChooseFrom = copyNorseList
        if rebuildOldSettlement:
            listToChooseFrom = abandonedSettlements
        choice = randomChoice(listToChooseFrom)
        copyNorseList.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomSlavicSettlementsName (rebuildOldSettlement = False):

    if len(copySlavicList) > 0:
        listToChooseFrom = copySlavicList
        if rebuildOldSettlement:
            listToChooseFrom = abandonedSettlements
        choice = randomChoice(listToChooseFrom)
        copySlavicList.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomMusslimSettlementsName(rebuildOldSettlement = False):

    if len(copyMusslimList) > 0:
        listToChooseFrom = copyMusslimList
        if rebuildOldSettlement:
            listToChooseFrom = abandonedSettlements
        choice = randomChoice(listToChooseFrom)
        copyMusslimList.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomRomanSettlementsName(rebuildOldSettlement = False):

    if len(copyRomanList) > 0:
        listToChooseFrom = copyRomanList
        if rebuildOldSettlement:
            listToChooseFrom = abandonedSettlements
        choice = randomChoice(listToChooseFrom)
        copyRomanList.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomAfricanSettlementsName(rebuildOldSettlement = False):

    if len(copyAfricanList) > 0:
        listToChooseFrom = copyAfricanList
        if rebuildOldSettlement:
            listToChooseFrom = abandonedSettlements
        choice = randomChoice(listToChooseFrom)
        copyAfricanList.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Village Name'
    return choice
