from enum import Enum

import random
englishFamilyNames = [
    'Parkin',
    'Rodgers',
    'Blackburn',
    'Chadwick',
    'Webber',
    'Cassidy',
    'Thorne',
    'Sanderson',
    'McKay',
    'Gallagher',
    'Shah',
    'Cunningham',
    'Gibbs',
    'Boyd',
    'Thorpe',
    'McCann',
    'Hogg',
    'Humphries',
    'McGrath',
    'McLeod',
    'Cummings',
    'Firth',
    'Reeve',
    'McCormick',
    'McAllister',
    'Drake',
    'Boulton',
    'Langford',
    'Ayres',
    'Craven',
]





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
    'Omegius'

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

def getInitEnglishName():
    if len(englishFamilyNames) > 0:
        choice = random.choice(englishFamilyNames)
        englishFamilyNames.remove(choice)
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


