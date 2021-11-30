import random


maleNameList = [
    'Adam',
    'Balthazar',
    'Chriss',
    'Dorian',
    'Evan',
    'Felix',
    'Gregorius',
    'Hector',
    'Isaac',
    'Jacob',
    'Kaleb',
    'Lewis',
    'Max',
    'Nathaniel'
]

femaleNameList = [
    'Abigail',
    'Bella',
    'Caroline',
    'Diana',
    'Elizabeth',
    'Fiona',
    'Gabriela',
    'Helena',
    'Iris',
    'Juliette',
    'Katherine',
    'Lydia',
    'Maria',
    'Natalie'
]

settlementsVillageNames = [

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
    'Ledbury'

]


def randomsettlementsVillageName ():

    if len(settlementsVillageNames) > 0:
        choice = random.choice(settlementsVillageNames)
        settlementsVillageNames.remove(choice)
    else:
        choice = 'Generic Village Name'
    return choice


def randomMName ():

    return random.choice(maleNameList)


def randomFName():
    return random.choice(femaleNameList)

#def nameFromFamilyHistory (family, people)
