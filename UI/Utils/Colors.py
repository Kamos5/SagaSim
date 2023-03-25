import Enums


def getColorBasedOnParam(params):

    if params in Enums.GeneralHealth:
        if params == Enums.GeneralHealth.HEALTHY:
            return 10, 120, 10
        elif params == Enums.GeneralHealth.WEAKEN:
            return 200, 200, 10
        elif params == Enums.GeneralHealth.POOR:
            return 250, 100, 10
        elif params == Enums.GeneralHealth.CRIPPLING:
            return 250, 10, 10
        elif params == Enums.GeneralHealth.DEATH:
            return 100, 100, 100

        return 0, 0, 0

