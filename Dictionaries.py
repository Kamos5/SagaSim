import random


class AssosiateRelation (dict):

    def __init__(self):
        super().__init__()
        self['assosiate'] = None
        self['relation'] = 0




class Person:

    def __init__(self):
        self.ass = []

    def addAss(self, newAss):
        self.ass.append(newAss)

    def getAss(self):
        return self.ass

    def removeAss(self, oldAss):
        for ass in self.ass:
            if ass['assosiate'] == oldAss:
                self.ass.remove(ass)


persons = []
others = []
for i in range(5):
    persons.append(Person())

for i in range(3):
    others.append(Person())

for person in persons:
    for other in others:
        ar = AssosiateRelation()
        ar['assosiate'] = other
        ar['relation'] = random.randint(1, 10)
        person.addAss(ar)

print(persons)

for person in persons:
    for other in others:
        for singleAss in person.ass:
            if other == singleAss['assosiate']:
                person.removeAss(other)

print(persons)

list2 = [["a",0],["b",2],["c",3],['d',4]]


somelist = [x for x in list2 if not x[0]=='b']

print(somelist)

