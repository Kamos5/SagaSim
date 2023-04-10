from random import choice as randomChoice

namesPicked = 0

provinceNamesStr = 'ProvinceNames'
provinceNamesStrLowerFirst = provinceNamesStr[0].lower() + provinceNamesStr[1:]

provinceSeaNamesStr = 'SeaNames'
provinceSeaNamesStrLowerFirst = provinceSeaNamesStr[0].lower() + provinceSeaNamesStr[1:]

copyProvinceNamesList = []
copyProvinceSeaNamesList = []


def makeListsForProvinceNames(world):

    for cultureName in world.allNames:
        provinceSettlementsNames = f'{cultureName}{provinceNamesStr}'
        copyProvinceNamesList.append(list(world.allNames[cultureName][provinceSettlementsNames][provinceNamesStrLowerFirst]))

        if cultureName == 'generic':
            provinceSeaNames = f'{cultureName}{provinceSeaNamesStr}'
            copyProvinceSeaNamesList.extend(list(world.allNames[cultureName][provinceSeaNames][provinceSeaNamesStrLowerFirst]))



def randomProvinceName (regionNumber =0):

    namesList = copyProvinceNamesList[regionNumber]
    choice = ''
    global namesPicked
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