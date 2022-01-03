import random


maleNameList = [
    'Adam',
    'Balthazar',
    'Chriss',
    'Dorian',
    'Evan',
    'Felix',
    'Gregorius',
    'Hector',
    'Isaac',
    'Jacob',
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
    'Bella',
    'Caroline',
    'Diana',
    'Elizabeth',
    'Fiona',
    'Gabriela',
    'Helena',
    'Iris',
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
