import random

settlementsNames = [

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


def randomEnglishSettlementsName ():

    if len(settlementsNames) > 0:
        choice = random.choice(settlementsNames)
        settlementsNames.remove(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomSlavicSettlementsName ():

    if len(settlementsNames) > 0:
        choice = random.choice(settlementsNames)
        settlementsNames.remove(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomMusslimSettlementsName():

    if len(settlementsNames) > 0:
        choice = random.choice(settlementsNames)
        settlementsNames.remove(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomRomanSettlementsName():

    if len(settlementsNames) > 0:
        choice = random.choice(settlementsNames)
        settlementsNames.remove(choice)
    else:
        choice = 'Generic Village Name'
    return choice

def randomAfricanSettlementsName():

    if len(settlementsNames) > 0:
        choice = random.choice(settlementsNames)
        settlementsNames.remove(choice)
    else:
        choice = 'Generic Village Name'
    return choice
