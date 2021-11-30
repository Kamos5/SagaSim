from Enums import LifeStatus

class World:

    __initYear = 500

    def __init__(self, startYear=__initYear):
        self.__initYear = startYear
        self.__year = self.__initYear
        self.regions = []

    def getYear(self):
        return self.__year

    def increaseYear(self):
        self.__year += 1

    def getAllAliveMembersNames(self, family, people):

        aliveMembersNames = []
        for person in people:
            if person in family.getAliveAllMembersUUIDs() and person.lifeStatus == LifeStatus.ALIVE:
                aliveMembersNames.append(person.firstName)
        return aliveMembersNames
