from enum import Enum
import RegionNameGenerator as RNG
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

copyEngList = englishFamilyNames.copy()
copyNorseList = norseFamilyNames.copy()
copySlavList = slavicFamilyNames.copy()
namesPicked = 0

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




def getNewLastNameBasedOnRegion(region):

    if region.getRegionName() in RNG.englishRegionNames:
        lastName = getInitEnglishName()
    elif region.getRegionName() in RNG.norseRegionNames:
        lastName = getInitNorseName()
    elif region.getRegionName() in RNG.slavicRegionNames:
        lastName = getInitSlavicName()
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


def getInitFamilyName():
    global namesPicked
    namesPicked += 1
    if len(initialFamilyNames) > 0:
        choice = random.choice(initialFamilyNames)
        initialFamilyNames.remove(choice)
    else:
        choice = 'Generic Family Name' + str(namesPicked)
    return choice


