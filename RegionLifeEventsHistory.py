import Enums

def weatherEvent(region, world):

    if region.getWeather() != Enums.weatherStatus.NORMAL:
        region.events.append(str(region.getRegionName()) + " was strucked by " + str(region.getWeather().value[0]) + " on the " + str(world.getDay()) + "/" + str(world.getMonth().value[1]) + "/" + str(world.getYear()))


