from enum import Enum

import random
initialFamilyNames = [
    'Alfarius',
    'Betarius',
    'Gammarius',
    'Deltius',
    'Eplsilonius',
    'Zetius',
    'Etius',
    'Thetius',
    'Iotius',
    'Kappius',
    'Lambdius',
    'Mius',
    'Nius',
    'Xius',
    'Omnicronius',
    'Pius',
    'Sigmius',
    'Tauius',
    'Upsilorius',
    'Phius',
    'Chius',
    'Psius',
    'Omegius',
    '24',
    '25',
    '26',
    '27',
    '28',
    '29',
    '30',
    '31',
    '32',
    '33',
    '34',
    '35'

]

class FamilyNamesBasedOnProfessions(Enum):

    SMITH = 'Smith',
    ARCHER = 'Archer',
    FISHER = 'Fisher',
    BAKER = 'Baker',
    FARMER = 'Farmer',
    MILLER = 'Miller',
    POTTER = 'Potter',
    SHEPPARD = 'Sheppard',
    TAYLOR = 'Taylor',
    COLEMAN = 'Coleman',


def getNewRandomLastName():

    if len(initialFamilyNames) > 0:
        choice = random.choice(initialFamilyNames)
        initialFamilyNames.remove(choice)
    else:
        choice = 'Generic Family Name'
    return choice

def getInitFamilyName():

    if len(initialFamilyNames) > 0:
        choice = random.choice(initialFamilyNames)
        initialFamilyNames.remove(choice)
    else:
        choice = 'Generic Family Name'
    return choice


