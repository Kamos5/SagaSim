import random


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


def randomMName ():

    return random.choice(maleEnglishNameList)


def randomFName():
    return random.choice(femaleEnglishNameList)

#def nameFromFamilyHistory (family, people)
