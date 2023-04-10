from random import choice

import Utils
from RegionNameGenerator import englishRegionNames, norseRegionNames, slavicRegionNames, egyptRegionNames

maleEnglishNameList = [
    'Adam',
    'Alvin',
    'Balthazar',
    'Berkeley',
    'Brandon',
    'Chriss',
    'Colton',
    'Dorian',
    'Darrel',
    'Evan',
    'Elmar',
    'Felix',
    'Fleming',
    'Gregorius',
    'Garrick',
    'Hector',
    'Harold',
    'Isaac',
    'Jacob',
    'Jarvis',
    'Kaleb',
    'Lewis',
    'Max',
    'Nathaniel',
    'Olin',
    'Palmer',
    'Ramsey',
    'Shaw',
    'Thane',
    'Wallace',
    'York'
]

maleNorseNameList = [

    'Arne',
    'Birger',
    'Bjørn',
    'Bo',
    'Erik',
    'Frode',
    'Gorm',
    'Halfdan',
    'Harald',
    'Knud',
    'Kåre',
    'Leif',
    'Njal',
    'Roar',
    'Rune',
    'Sten',
    'Skarde',
    'Sune',
    'Svend',
    'Troels',
    'Toke',
    'Torsten',
    'Trygve',
    'Ulf',
    'Ødger',
    'Åge'
]


femaleEnglishNameList = [
    'Abigail',
    'Alodie',
    'Bella',
    'Bliss',
    'Caroline',
    'Capri',
    'Diana',
    'Darlene',
    'Elizabeth',
    'Edda',
    'Fiona',
    'Fleta',
    'Gabriela',
    'Gytha',
    'Helena',
    'Haylee',
    'Iris',
    'Ida',
    'Juliette',
    'Katherine',
    'Lydia',
    'Maria',
    'Natalie',

]

femaleNorseNameList = [

    'Astrid',
    'Bodil',
    'Frida',
    'Gertrud',
    'Gro',
    'Estrid',
    'Hilda',
    'Gudrun',
    'Gunhild',
    'Helga',
    'Inga',
    'Liv',
    'Randi',
    'Signe',
    'Sigrid',
    'Revna',
    'Sif',
    'Tora',
    'Tove',
    'Thyra',
    'Thurid',
    'Yrsa',
    'Ulfhild',
    'Åse'

]

maleSlavicNameList = [

    'Aleksandru',
    'Athanasi',
    'Berislav',
    'Blazh',
    'Bogdan',
    'Bogumir',
    'Boleslav',
    'Borislav',
    'Borivoi',
    'Bozhidar',
    'Bozho',
    'Bratomil',
    'Bratoslav',
    'Bronislav',
    'Chedomir',
    'Chestibor',
    'Chestimir',
    'Chestislav',
    'Dalibor',
    'Desislav',
    'Dmitrei',
    'Dobrogost',
    'Dobromil',
    'Dobroslav',
    'Dragomir',
    'Dragoslav',
    'Drazhan',
    'Gostislav',
    'Grigorii',
    'Kazimir',
    'Kresimir',
    'Kyrilu',
    'Ludovit',
    'Lyudmil',
    'Mieczysław',
    'Miloš',
    'Miloslav',
    'Miroslav',
    'Mstislav',
    'Premislav',
    'Radomil',
    'Radoslav',
    'Sławomir',
    'Stanislav',
    'Tomislav',
    'Vlad',
    'Yaroslav',
    'Zbigniew'
]


femaleSlavicNameList = [

    'Bogdana',
    'Bozhena',
    'Desislava',
    'Dragoslava',
    'Elena',
    'Lyudmila',
    'Miloslava',
    'Miroslava',
    'Olga',
    'Radoslava',
    'Inga',
    'Stanislava',
    'Tomislava',
    'Yaroslava'

]

malesEgyptianNameList = [

    'Asim',
    'Chisisi',
    'Gyasi',
    'Khons',
    'Omari',
    'Sadiki',
    'Ur',
    'Abanoub',
    'Abasi',
    'Abayomi',
    'Abdelrahman',
    'Abrax',
    'Abraxas',
    'Abubakar',
    'Bassel',
    'Bast',
    'Bes',
    'Bithiah',
    'Braheem',
    'Shabaka',
    'Shakir',
    'Taafeef',
    'Thutmose',
    'Ur-Atum',
    'Uthman',
    'Waaiz',
    'Yahya',
    'Zahur',
    'Zosar',
    'Zuberi',
    'Moishe',
    'Moisis',
    'Moke',
    'Montu',
    'Mosiah',
    'Mostafa',
    'Moswen',
    'Masud',
    'Masuda',
    'Masudah',
    'Masudi',
    'Menefer',
    'Menes',
    'Mido'

]

femaleEgyptianNameList = [

    'Akila',
    'Bahiti',
    'Dalila',
    'Ife',
    'Khepri',
    'Masika',
    'Naunet',
    'Amunet',
    'Auset',
    'Bastet',
    'Bennu',
    'Berenike',
    'Chione',
    'Cliupatra',
    'Dendera',
    'Ebony',
    'Edrice',
    'Eshe',
    'Farida',
    'Feme',
    'Femi',
    'Fukayna',
    'Gamila',
    'Habibah',
    'Hafsah',
    'Isis',
    'Jomana',
    'Keket',
    'Kissa',
    'Kleopatra',
    'Lapis',
    'Anat',
    'Anippe',
    'Asenath',
    'Ebonee',
    'Eboney',
    'Eboni',
    'Hathor',
    'Heba',
    'Heqet',
    'Masika',
    'Massika',
    'Maye',
    'Midge',
    'Moswen',
    'Nailah',
    'Lateefah',
    'Lotus',
    'Maibe',
    'Mandisa',
    'Mariam'

]

firstNamesStr = 'Names'
firstNamesStrLowerFirst = firstNamesStr[0].lower() + firstNamesStr[1:]
copyNamesMList = []
copyNamesFList = []

def makeListsForFirstNames(world):

    for index, cultureName in enumerate(world.allNames):
        if index < len(world.getRegions()):
            firstNamesStrUpperFirst = cultureName[0].upper() + cultureName[1:]
            cultureFamilyNames = f'male{firstNamesStrUpperFirst}{firstNamesStr}'
            copyNamesMList.append(list(world.allNames[cultureName][cultureFamilyNames][firstNamesStrLowerFirst]))
            firstNamesStrUpperFirst = cultureName[0].upper() + cultureName[1:]
            cultureFamilyNames = f'female{firstNamesStrUpperFirst}{firstNamesStr}'
            copyNamesFList.append(list(world.allNames[cultureName][cultureFamilyNames][firstNamesStrLowerFirst]))

def getRandomMNameForRegion(regionNumber = 0):

    namesList = []
    choice = ''

    if copyNamesMList is None:
        if regionNumber == 0:
            choice = randomEnglishMName()
        elif regionNumber == 1:
            choice = randomNorseMName()
        elif regionNumber == 2:
            choice = randomSlavicMName()
        elif regionNumber == 3:
            choice = randomEgyptianMName()
    else:
        namesList = copyNamesMList[regionNumber]
        if len(namesList) > 0:
            choice = Utils.randomFromCollection(namesList)
        else:
            global namesPicked
            namesPicked += 1
            choice = f'Generic Male Name'

    return choice


def getRandomFNameForRegion(regionNumber = 0):

    namesList = []
    choice = ''

    if copyNamesFList is None:
        if regionNumber == 0:
            choice = randomEnglishFName()
        elif regionNumber == 1:
            choice = randomNorseFName()
        elif regionNumber == 2:
            choice = randomSlavicFName()
        elif regionNumber == 3:
            choice = randomEgyptianFName()
    else:
        namesList = copyNamesFList[regionNumber]
        if len(namesList) > 0:
            choice = Utils.randomFromCollection(namesList)
        else:
            global namesPicked
            namesPicked += 1
            choice = f'Generic Female Name'

    return choice

def randomEnglishMName():

    return choice(maleEnglishNameList)

def randomEnglishFName():
    return choice(femaleEnglishNameList)

def randomNorseMName():
    return choice(maleNorseNameList)

def randomNorseFName():
    return choice(femaleNorseNameList)

def randomSlavicMName():
    return choice(maleSlavicNameList)

def randomSlavicFName():
    return choice(femaleSlavicNameList)

def randomEgyptianMName():
    return choice(malesEgyptianNameList)

def randomEgyptianFName():
    return choice(femaleEgyptianNameList)
#def nameFromFamilyHistory (family, people)
