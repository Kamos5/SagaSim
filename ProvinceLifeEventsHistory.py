import Enums

def weatherEvent(province, world):

    if province.getWeather() != Enums.weatherStatus.NORMAL:
        province.events.append(str(province.getName()) + " was strucked by " + str(province.getWeather().value[0]) + " on the " + str(world.getDay()) + "/" + str(world.getMonth().value[1]) + "/" + str(world.getYear()))
