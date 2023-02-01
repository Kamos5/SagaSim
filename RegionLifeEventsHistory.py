import Enums

def weatherEvent(region, world):

    if region.getWeather() != Enums.weatherStatus.NORMAL:
        region.events.append(str(region.getRegionName()) + " was strucked by " + str(region.getWeather().value[1]) + " in the year " + str(world.getYear()))


