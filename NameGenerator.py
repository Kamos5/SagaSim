from random import choice

from RegionNameGenerator import englishRegionNames, norseRegionNames

maleEnglishNameList = [
    'Adam',
    'Alvin',
    'Balthazar',
    'Berkeley',
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

def getRandomMNameForRegion(region):

    try:
        if region.getRegionName() in englishRegionNames:
            return randomEnglishMName()
        if region.getRegionName() in norseRegionNames:
            return randomNorseMName()
    except:
        print("Aaaa")

def getRandomFNameForRegion(region):

    if region.getRegionName() in englishRegionNames:
        return randomEnglishFName()
    if region.getRegionName() in norseRegionNames:
        return randomNorseFName()

def randomEnglishMName():

    return choice(maleEnglishNameList)

def randomEnglishFName():
    return choice(femaleEnglishNameList)

def randomNorseMName():
    return choice(maleNorseNameList)

def randomNorseFName():
    return choice(femaleNorseNameList)

#def nameFromFamilyHistory (family, people)
