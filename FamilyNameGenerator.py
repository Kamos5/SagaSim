from enum import Enum
import RegionNameGenerator as RNG
import random
from random import choice as randomChoice

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

norseFamilyNames = [

    'Aland',
    'Asketill',
    'Bielke',
    'Borg',
    'Brando',
    'Christensen',
    'Adal',
    'Wulf',
    'Ellingboe',
    'Erling',
    'Eskildsen',
    'Frisk',


]

slavicFamilyNames = [
    'Adamić',
    'Antić',
    'Babić',
    'Bogdanić',
    'Broz',
    'Crnčević',
    'Dragović',
    'Dragović',
    'Franić',
    'Franjić',
    'Grbić',
    'Adamík',
    'Aksamit',
    'Andrysiak',
    'Archaki',
    'Barno',
    'Bárta',
    'Bartosz',
    'Beneš',
    'Beran',
    'Bilyk',
    'Bomba',
    'Bosko',
    'Čech',
    'Čermák',
    'Černý',
    'Chalupník',
    'Cherkasskiy',
    'Chernenko',
    'Cherneski',
    'Chmela',
    'Chvátal',
    'Datsyuk',
    'Doležal',
    'Doubek',
    'Dubanowski',
    'Dziedzic',
    'Fiala',
    'Ganus',
    'Gogol',
    'Gomółka',
    'Grbić',
    'Grgić',
    'Gutnik',
    'Holub',
    'Horáček',
    'Horvat',
    'Hrubý',
    'Hruška',
    'Ilić',
    'Ivanova',
    'Ivanović',
    'Janković',
    'Jedlička',
    'Jehlička',
    'Jelen',
    'Kalashnik',
    'Kamiński',
    'Kazan',
    'Kocur',
    'Kovačić',
    'Kudrna',
    'Kyselý',
    'Lomachenko',
    'Lončar',
    'Malaya',
    'Marković',
    'Máselník',
    'Mlynář',
    'Molchan',
    'Navrátil',
    'Nedbálek',
    'Nikolić',
    'Novak',
    'Panchenko',
    'Perko',
    'Petrić',
    'Podsedník',
    'Pokorný',
    'Polák',
    'Poroshenko',
    'Řezník',
    'Rosya',
    'Ružička',
    'Ryba',
    'Skála',
    'Slavík',
    'Soroka',
    'Stankić',
    'Stjepanić',
    'Stojanović',
    'Ślusarski',
    'Tesař',
    'Tomić',
    'Vengerov',
    'Veselý',
    'Vinković',
    'Vlahović',
    'Zbirak',
    'Žitnik',
    'Zorić'

]

genericFamilyNames = [
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

egyptianFamilyNames = [

    'Adom',
    'Akhenaton',
    'Akhethetep',
    'Akhom',
    'Akil',
    'Amenemhat',
    'Amenemope',
    'Anen',
    'Anum',
    'Aper-el',
    'Badru',
    'Baketmut',
    'Beketaten',
    'Chisisi',
    'Darwish',
    'Hamidi',
    'Hanbal',
    'Kamuzu',
    'Khaldun',
    'Khnumhotep',
    'Manu',
    'Nakhtmin',
    'Nebamun',
    'Nizam',
    'Nuru',
    'Rahotep',
    'Ramose'

]

copyEngList = englishFamilyNames.copy()
copyNorseList = norseFamilyNames.copy()
copySlavList = slavicFamilyNames.copy()
copyEgyptList = egyptianFamilyNames.copy()
namesPicked = 0

familyNamesStr = 'FamilyNames'
familyNamesStrLowerFirst = familyNamesStr[0].lower() + familyNamesStr[1:]

copyNamesList = []



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

def makeListsForLastNames(world):

    for cultureName in world.allNames:
        cultureFamilyNames = f'{cultureName}{familyNamesStr}'
        copyNamesList.append(list(world.allNames[cultureName][cultureFamilyNames][familyNamesStrLowerFirst]))

def getNewLastNameBasedOnCulture(regionNumber = 0):

    namesList = copyNamesList[regionNumber]
    choice = ''

    if namesList is None:
        if regionNumber == 0:
            choice = getInitEnglishName()
        elif regionNumber == 1:
            choice = getInitNorseName()
        elif regionNumber == 2:
            choice = getInitSlavicName()
        elif regionNumber == 3:
            choice = getInitEgyptName()
    else:
        if len(namesList) > 0:
            choice = randomChoice(namesList)
            namesList.remove(choice)
        else:
            global namesPicked
            namesPicked += 1
            choice = f'Generic Family Name {namesPicked}'

    return choice


def getNewLastNameBasedOnRegion(region):

    if region.getRegionName() in RNG.englishRegionNames:
        lastName = getInitEnglishName()
    elif region.getRegionName() in RNG.norseRegionNames:
        lastName = getInitNorseName()
    elif region.getRegionName() in RNG.slavicRegionNames:
        lastName = getInitSlavicName()
    elif region.getRegionName() in RNG.egyptRegionNames:
        lastName = getInitEgyptName()
    else:
        lastName = getInitEnglishName()

    return lastName

def getNewRandomLastName():

    global namesPicked
    namesPicked += 1
    if len(copyEngList) > 0:
        choice = random.choice(copyEngList)
        copyEngList.remove(choice)
    else:
        choice = 'Generic Family Name' + str(namesPicked)
    return choice

def getInitEnglishName():
    global namesPicked
    namesPicked += 1
    if len(copyEngList) > 0:
        choice = random.choice(copyEngList)
        copyEngList.remove(choice)
    else:
        choice = 'Generic Family Name' + str(namesPicked)
    return choice

def getInitNorseName():
    global namesPicked
    namesPicked += 1
    if len(copyNorseList) > 0:
        choice = random.choice(copyNorseList)
        copyNorseList.remove(choice)
    else:
        choice = 'Generic Family Norse Name' + str(namesPicked)
    return choice

def getInitSlavicName():
    global namesPicked
    namesPicked += 1
    if len(copySlavList) > 0:
        choice = random.choice(copySlavList)
        copySlavList.remove(choice)
        namesPicked +=1
    else:
        choice = 'Generic Family Slavic Name' + str(namesPicked)
    return choice

def getInitEgyptName():
    global namesPicked
    namesPicked += 1
    if len(copyEgyptList) > 0:
        choice = random.choice(copyEgyptList)
        copyEgyptList.remove(choice)
        namesPicked +=1
    else:
        choice = 'Generic Family Egyptian Name' + str(namesPicked)
    return choice

def getInitFamilyName():
    global namesPicked
    namesPicked += 1
    if len(genericFamilyNames) > 0:
        choice = random.choice(genericFamilyNames)
        genericFamilyNames.remove(choice)
    else:
        choice = 'Generic Family Name' + str(namesPicked)
    return choice


