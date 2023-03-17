from random import choice

from RegionNameGenerator import englishRegionNames, norseRegionNames, slavicRegionNames

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


def getRandomMNameForRegion(region):

    if region.getRegionName() in englishRegionNames:
        return randomEnglishMName()
    elif region.getRegionName() in norseRegionNames:
        return randomNorseMName()
    elif region.getRegionName() in slavicRegionNames:
        return randomSlavicMName()
    else:
        return randomEnglishMName()

def getRandomFNameForRegion(region):

    if region.getRegionName() in englishRegionNames:
        return randomEnglishFName()
    elif region.getRegionName() in norseRegionNames:
        return randomNorseFName()
    elif region.getRegionName() in slavicRegionNames:
        return randomSlavicFName()
    else:
        return randomEnglishMName()
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


#def nameFromFamilyHistory (family, people)
