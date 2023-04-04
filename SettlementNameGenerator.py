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

egyptianSettlementsNames = [
    'Men-nefer',
    'Khem',
    'Yamu',
    'Raqote',
    'Khito',
    'Ptkheka',
    'Zau',
    'Per-Wadjet',
    'Khasut',
    'Timinhor',
    'Piemro',
    'Thonis',
    'Menouthis',
    'Pikuat',
    'Per-Atum',
    'Djedu',
    'Hut-hery-ib',
    'Taremu',
    'Abdju',
    'Abu',
    'Akhetaten',
    'Behdet',
    'Berenice',
    'Buhen',
    'Chenem-Waset',
    'Djanet',
    'Djedet',
    'Djerty',
    'Gebtu',
    'Gesy',
    'Hebenu',
    'Henen-nesut',
    'Herwer',
    'Hut-Repyt',
    'Hut-waret',
    'Iken',
    'Ipu',
    'Iunet',
    'Iunu',
    'Iuny',
    'Iushenshen',
    'Khemenu',
    'Madu',
    'Nekheb',
    'Nekhen',
    'Nubt',
    'Nubt',
    'Pachnamu´nis',
    'Per-Amun',
    'Per-Bast',
    'Per-Hathor',
    'Per-Imen-mat-khent',
    'Per-Medjed',
    'Per-Nemty',
    'Per-Ramessu',
    'Per-Sopdu',
    'Qis',
    'Saka',
    'Semabehdet',
    'Seshesh',
    'Šetennu',
    'Shashotep',
    'Shedet',
    'Sumenu',
    'Swenett',
    'Tamiat',
    'Tao',
    'Ta-senet',
    'Tayu-djayet',
    'Tepihu',
    'Tjaru',
    'Tjebnutjer',
    'Tjebu',
    'Tjenu',
    'Waset',
    'Weprehwy',
    'Zawty'

]

activeNames = []
abandonedSettlements = []

copyEnglishList = englishSettlementsNames.copy()
copyNorseList = norseSettlementsNames.copy()
copySlavicList = slavicSettlementsNames.copy()
copyMusslimList = englishSettlementsNames.copy()
copyRomanList = englishSettlementsNames.copy()
copyAfricanList = englishSettlementsNames.copy()
copyEgyptianList = egyptianSettlementsNames.copy()

settlementsNamesStr = 'SettlementsNames'
settlementsNamesStrLowerFirst = settlementsNamesStr[0].lower() + settlementsNamesStr[1:]

copySettlementsNamesList = []

def makeListsForSettlementsNames(world):

    for cultureName in world.allNames:
        cultureSettlementsNames = f'{cultureName}{settlementsNamesStr}'
        copySettlementsNamesList.append(list(world.allNames[cultureName][cultureSettlementsNames][settlementsNamesStrLowerFirst]))

def randomSettlementsName (regionNumber =0, rebuildOldSettlement = False):

    namesList = copySettlementsNamesList[regionNumber]
    choice = ''

    if namesList is None:
        if regionNumber == 0:
            choice = copyEnglishList
        elif regionNumber == 1:
            choice = copyNorseList
        elif regionNumber == 2:
            choice = copySlavicList
        elif regionNumber == 3:
            choice = copyEgyptianList
    else:
        if len(namesList) > 0:
            choice = randomChoice(namesList)
            namesList.remove(choice)
        else:
            global namesPicked
            namesPicked += 1
            choice = f'Generic Settlement Name {namesPicked}'

    return choice

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

def randomEgyptSettlementsName(rebuildOldSettlement = False):

    if len(copyEgyptianList) > 0:
        listToChooseFrom = copyEgyptianList
        if rebuildOldSettlement:
            listToChooseFrom = abandonedSettlements
        choice = randomChoice(listToChooseFrom)
        copyEgyptianList.remove(choice)
        activeNames.append(choice)
    else:
        choice = 'Generic Egyptian Village Name'
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
