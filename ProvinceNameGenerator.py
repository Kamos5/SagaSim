from random import choice as randomChoice

namesPicked = 0

provinceNamesStr = 'ProvinceNames'
provinceNamesStrLowerFirst = provinceNamesStr[0].lower() + provinceNamesStr[1:]

provinceSeaNamesStr = 'SeaNames'
provinceSeaNamesStrLowerFirst = provinceSeaNamesStr[0].lower() + provinceSeaNamesStr[1:]

copyProvinceNamesList = []
copyProvinceSeaNamesList = []


def makeListsForProvinceNames(world):

    for culture in world.getCultures():
        provinceSettlementsNames = f'{culture.getCultureName()}{provinceNamesStr}'
        copyProvinceNamesList.append(list(world.allNames[culture.getCultureName()][provinceSettlementsNames][provinceNamesStrLowerFirst]))

        if culture.getCultureName() == 'generic':
            provinceSeaNames = f'{culture.getCultureName()}{provinceSeaNamesStr}'
            copyProvinceSeaNamesList.extend(list(world.allNames[culture.getCultureName()][provinceSeaNames][provinceSeaNamesStrLowerFirst]))



def randomProvinceName (regionNumber =0, chosenName = ''):

    namesList = copyProvinceNamesList[regionNumber]
    global namesPicked
    if chosenName != '':
        choice = chosenName
        namesList.remove(choice)
        namesPicked += 1
        return choice
    choice = ''

    if namesList is None:

        namesPicked += 1
        choice = f'Generic province {namesPicked}'
    else:
        if len(namesList) > 0:
            choice = randomChoice(namesList)
            namesList.remove(choice)
        else:
            namesPicked += 1
            choice = f'Generic province {namesPicked}'

    return choice

def randomProvinceSeaName():

    namesList = copyProvinceSeaNamesList
    choice = ''
    global namesPicked
    if namesList is None:

        namesPicked += 1
        choice = f'Generic Sea {namesPicked}'
    else:
        if len(namesList) > 0:
            choice = randomChoice(namesList)
            namesList.remove(choice)
        else:
            namesPicked += 1
            choice = f'Generic Sea {namesPicked}'

    return choice