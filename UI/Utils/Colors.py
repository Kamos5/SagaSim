import Enums


def getColorBasedOnParam(param):

    if param in Enums.GeneralHealth:
        if param == Enums.GeneralHealth.HEALTHY:
            return 10, 120, 10
        elif param == Enums.GeneralHealth.WEAKEN:
            return 200, 200, 10
        elif param == Enums.GeneralHealth.POOR:
            return 250, 100, 10
        elif param == Enums.GeneralHealth.CRIPPLING:
            return 250, 10, 10
        elif param == Enums.GeneralHealth.DEATH:
            return 100, 100, 100

        return 0, 0, 0

    if param in Enums.Sexes:
        if param == Enums.Sexes.FEMALE:
            return 250, 20, 250
        elif param == Enums.Sexes.MALE:
            return 80, 80, 250

    if param in Enums.LifeStatus:
        if param == Enums.LifeStatus.ALIVE:
            return 10, 120, 10
        elif param == Enums.LifeStatus.DEAD:
            return 100, 100, 100

