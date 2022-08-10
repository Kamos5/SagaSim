import random


maleNameList = [
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

femaleNameList = [
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

def randomMName ():

    return random.choice(maleNameList)


def randomFName():
    return random.choice(femaleNameList)

#def nameFromFamilyHistory (family, people)
