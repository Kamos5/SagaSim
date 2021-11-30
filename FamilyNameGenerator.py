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




def getInitFamilyName(variable):

    if len(initialFamilyNames) > 0:
        choice = random.choice(initialFamilyNames)
        initialFamilyNames.remove(choice)
    else:
        choice = 'Generic Family Name'
    return choice


