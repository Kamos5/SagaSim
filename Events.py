import time
from statistics import mean

import numpy as np

import Enums
import FamilyFunctions as FF
import HouseFunctions
import SettlementLifeEventsHistory
import WorldFunctions
from Enums import LifeStatus, MaritalStatus, CauseOfDeath, Sexes, Settlements, Traits
import Utils
from Family import Family as Family
import InfectionsFunctions
import Parameters
import FamilyNameGenerator as FNG
import PeopleFunctions as PF
import PersonLifeEventsHistory as PLEH
from Enums import MaritalStatus as MS
import SettlementsFunctions as SF
import SettlementFeatures as SFeat
from SettlementLifeEventsHistory import spoiledFood


def increaseAge (world):

    enumDead = LifeStatus.DEAD
    enumHealty = Enums.GeneralHealth.HEALTHY

    for person in world.getAlivePeople():
        if person.getLifeStatus() is not enumDead:  #must be sometimes people die in between years and getAlive is not updated yet

            if person.getMonthOfBirth() == world.getMonth() and person.getDayOfBirth() == world.getDay():
                person.increaseAge()

                if len(person.getFriends()) > 0:
                    PLEH.celebratedBirthsday(person, world)
                    for friend in person.getFriends():
                        person.increaseHappiness(1)
                        friend.increaseHappiness(1)
                        PLEH.wentToSMBBirthsday(friend, person, world)

                if person.age < 15:
                    person.increaseHeight()

                    #for accelerating growth in children
                    if Parameters.growthSpeed > 0:
                        for growthAccelerator in range(Parameters.growthSpeed-1):
                            person.increaseAge()

                    if person.age > 15:
                        person.age = 15

                if person.age == 15:
                    person.height = person.heightGen
                    person.familyObjRef.moveChildToAdultMembers(person)
                    person.changeMaritalStatus(MS.SINGLE)
                    PLEH.adulthoodReached(person, world)

                if person.age > 50:
                    PF.retirement(person, world)

                if person.modifiedLifespan - person.getAge() <= 5 and person.getHealthFromAge() is enumHealty:
                    person.setHealthFromAge(Enums.GeneralHealth.WEAKEN)

            if deathChanceFromAge(person) or person.age >= person.modifiedLifespan:
                PF.deathProcedures(person, world)
                continue

            if person.getSettlement().getFreeFood() <= 0:
                chanceForStarvation = Utils.randomRange(1, 100)
                person.increaseHappiness(-1)
                if chanceForStarvation <= 1:
                    person.causeOfDeath = CauseOfDeath.STARVATION
                    PF.deathProcedures(person, world)
                    continue


def infectionsSpread (world):

    timeAllPeopleArray = []
    time1Array = []
    time2Array = []
    time3Array = []
    infectionsPerDay = 0
    # 1) infect with new diseases
    # 2) infect others (in house and workplace)
    # 2) move infection to sick phase
    # 3) process infection
    start0 = time.perf_counter()

    for region in world.getRegions():
        if -5 <= region.getCurrentTemperature() <= 15:
            for province in region.getProvinces():
                for settlement in province.getSettlements():
                    for person in settlement.getResidents():
                        if person.lifeStatus == LifeStatus.ALIVE:

                            start1 = time.perf_counter()
                            # 1)
                            chanceForContractDisease = Utils.randomRange(1, 100_000)  # 1 in 1.000.000 / per day
                            contractDiseaseThreshold = 1

                            contractDiseaseThreshold = (contractDiseaseThreshold * person.getGeneralHealth().value[0]) + 2

                            if chanceForContractDisease <= contractDiseaseThreshold:
                                randomInfection = Utils.randomFromCollection(world.diseases)[1]
                                if len(person.getImmunityTo()) > 0:
                                    isImmune = False
                                    for immunityTo in person.getImmunityTo():
                                        if randomInfection == immunityTo[0][0]:
                                            isImmune = True
                                            break
                                    if not isImmune:
                                        if InfectionsFunctions.checkIfInfected(person, randomInfection):
                                            infectionsPerDay = InfectionsFunctions.addInfectionToPerson(person, randomInfection, world)
                                            break
                                else:
                                    if InfectionsFunctions.checkIfInfected(person, randomInfection):
                                        infectionsPerDay = InfectionsFunctions.addInfectionToPerson(person, randomInfection, world)
                            end1 = time.perf_counter()
                            start2 = time.perf_counter()
                            if len(person.getInfections()) > 0:
                                for infection in person.getInfections()[0]:
                                    if type(infection) is dict and infection['contagious']:

                                        # 2a)
                                        infectionsPerDay = InfectionsFunctions.tryToInfectPeopleFromList(person, person.getAccommodation().getHouseResidents(), infection, world)

                                        # 2b)
                                        if person.getOccupation() is not None and len(person.getCurrentDiseases()) > 0:  # ONLY IF NOT SICK AKA CURRENT DISEASES > 0
                                            infectionsPerDay = InfectionsFunctions.tryToInfectPeopleFromList(person, person.getOccupation().getWorkerList(), infection, world)
                            end2 = time.perf_counter()
                            start3 = time.perf_counter()
                            # 3)
                            if len(person.getInfections()) > 0:
                                infections, infDate = zip(*person.getInfections())
                                for (infection, infDate) in zip(infections, infDate):
                                    if infDate + infection['incubation'] <= world.getDayOfTheYear():
                                        if len(person.getCurrentDiseases()) > 0:
                                            diseases, disDates, disImmunity = zip(*person.getCurrentDiseases())
                                            if infection not in diseases:
                                                person.addCurrentDiseases([infection, world.getDayOfTheYear(), 0])
                                                person.increaseHappiness(-5)
                                                PLEH.showingSymptomsOf(person, infection, world)
                                                if InfectionsFunctions.offsetHealth(person, infection, world):
                                                    break

                                        else:
                                            person.addCurrentDiseases([infection, world.getDayOfTheYear(), 0])
                                            person.increaseHappiness(-5)
                                            PLEH.showingSymptomsOf(person, infection, world)
                                            if InfectionsFunctions.offsetHealth(person, infection, world):
                                                break


                            end3 = time.perf_counter()

                    #         time1Array.append(end1-start1)
                    #         time2Array.append(end2-start2)
                    #         time3Array.append(end3-start3)
                    # end0 = time.perf_counter()
                    # print("Time0:" + str(end0-start0))
                    # print("Time1:" + str(mean(time1Array)))
                    # print("Time2:" + str(mean(time2Array)))
                    # print("Time3:" + str(mean(time3Array)))
    infectionsPerPop = round(infectionsPerDay / len(world.getAlivePeople()), 2)
    print("Infections Per Day:" + str(infectionsPerDay))
    print("Infections Per Pop:" + str(infectionsPerPop))

def terrytoryManagement(world):

    regionsTerritories = []
    marginColor = (0, 0, 0)

    # for region in world.getRegions():
    #     regionsTerritories.extend(region.getRegionTerritories())
    #
    # for region in world.getRegions():
    #
    #     regionColor = region.getRegionColor()
    #     possibleExpansion = WorldFunctions.caltulatePossibleTerritoryExpansions(region, world, regionsTerritories)
    #
    #     if len(possibleExpansion) > 0:
    #
    #         expandToX, expandToY = Utils.randomFromCollection(possibleExpansion)
    #         region.addRegionTerritory((expandToX, expandToY))
    #         regionsTerritories.append((expandToX, expandToY))
    #         world.getWorldMap().addField(regionColor, x=expandToX, y=expandToY)
    #         possibleExpansion.remove((expandToX, expandToY))    # TODO consequence: can't expand to bordering pixel that was not in possibleExpansion list if snakeLength > 1.
    #         possibleExpansion.extend(WorldFunctions.caltulatePossibleTerritoryExpansionsForSinglePoint(region, world, regionsTerritories, (expandToX, expandToY)))
    #
    #         #possibleExpansion = WorldFunctions.caltulatePossibleTerritoryExpansions(region, world, regionsTerritories)
    #
    #     # for pEX, pEY in possibleExpansion:
    #     #     world.getWorldMap().addField(regionColor, marginColor, x=pEX, y=pEY)
    #
    # print(len(world.getWorldMap().getWorldMapObj()))

def diseasesProgress(world):

    for person in world.getAlivePeople():
        if person.getLifeStatus() == Enums.LifeStatus.ALIVE:
            person.setCurrentDiseases([disease for disease in person.getCurrentDiseases() if not InfectionsFunctions.toRemoveDisease(person, disease, world)])
            if person.getGeneralHealth().value[0] > 0:
                if len(person.getCurrentDiseases()) > 1:
                    chanceToDieFromPoorHealth = Utils.randomRange(1, 1000)
                    if chanceToDieFromPoorHealth < 10 * 1 * 2 ** (person.getGeneralHealth().value[0]-2):
                        person.causeOfDeath = CauseOfDeath.SICKNESS
                        PF.deathProcedures(person, world)
                        continue
            person.setCurrentInjuries([injury for injury in person.getCurrentInjuries() if not InfectionsFunctions.toRemoveInjury(person, injury, world)])
            if person.getGeneralHealth().value[0] > 1:
                if len(person.getCurrentInjuries()) > 0:
                    chanceToDieFromPoorHealth = Utils.randomRange(1, 1000)
                    if chanceToDieFromPoorHealth < 10 * 1 * 2 ** (person.getGeneralHealth().value[0]-2):
                        person.causeOfDeath = CauseOfDeath.INJURY
                        PF.deathProcedures(person, world)

def loveMaking (world):

    for person in world.getAlivePeople():
        if person.sex == Sexes.FEMALE and 15 <= person.age and (person.spouse is not None or len(person.getLovers()) > 0) and person.lifeStatus == LifeStatus.ALIVE and not person.isPregnant:

            lovemakingWithSpouse = 90       #90
            lovemakingWithLovers = 10     #10

            if (Traits.LUSTFUL in person.getTraits() or Traits.DECEITFUL in person.getTraits() or Traits.CYNICAL in person.getTraits()) and len(person.getLovers()) > 0:
                lovemakingWithSpouse = 25
                lovemakingWithLovers = 75

                if person.getSpouse() is None:
                    lovemakingWithSpouse = 0
                    lovemakingWithLovers = 100

            if (Traits.LUSTFUL not in person.getTraits() and Traits.DECEITFUL not in person.getTraits() and Traits.CYNICAL not in person.getTraits()) and len(person.getLovers()) > 0:
                lovemakingWithSpouse = 50
                lovemakingWithLovers = 50

                if person.getSpouse() is None:
                    lovemakingWithSpouse = 0
                    lovemakingWithLovers = 100

            if Traits.CHASTE in person.getTraits():
                lovemakingWithSpouse = 10
                lovemakingWithLovers = 10

            if len(person.getLovers()) == 0:
                lovemakingWithSpouse = 100
                lovemakingWithLovers = 0


            changeForLovemaking = Utils.randomRange(1, 100)

            if changeForLovemaking < lovemakingWithSpouse and person.getSpouseRelation() > 0:
                chanceOfPregnancy = Utils.randomRange(1, 100)
                if person.getAge() > 45:
                    chanceOfPregnancy = 101
                if chanceOfPregnancy < min(person.fertility, person.getSpouse().fertility) * person.getSpouse().getSettlement().getBaseFertility() * person.getSpouse().getSettlement().getFertilityModifier() * person.getPersonalSexualModifier() * person.getSpouse().getPersonalSexualModifier():
                    person.setIsPregnant(True)
                    person.setPregnancyFather(person.getSpouse())
                    person.setPregnancyTrueFather(person.getSpouse())
                    person.setImpregnationMonth(world.getMonth())
                    person.setLaborDay(world.getMonth())
            elif changeForLovemaking < lovemakingWithLovers:
                if len(person.getLovers()) > 0:
                    lover = Utils.randomFromCollection(person.getLovers())
                    chanceOfPregnancy = Utils.randomRange(1, 100)
                    if person.getAge() > 45 or lover.getSex() == Enums.Sexes.FEMALE:
                        chanceOfPregnancy = 101
                    if chanceOfPregnancy < min(person.fertility, lover.fertility) * person.getSettlement().getBaseFertility() * person.getSettlement().getFertilityModifier() * person.getPersonalSexualModifier() * lover.getPersonalSexualModifier():
                        person.setIsPregnant(True)
                        person.setPregnancyTrueFather(lover)
                        if person.getSpouse() is not None:
                            person.setPregnancyFather(person.getSpouse())
                        person.setImpregnationMonth(world.getMonth())
                        person.setLaborDay(world.getMonth())


def birthPeopleNew (world):

    for person in world.getAlivePeople():

        if person.getLifeStatus() != LifeStatus.DEAD:
            if person.getSpouse() is not None:
                # change spouseRelation based on liked/disliked traits
                changeRelationToFromSpouse(person)

            #TIME for labour aka 9m pregnancy
            if person.sex == Sexes.FEMALE and person.isPregnant:

                chanceForMiscarriage = Utils.randomRange(1, 10000)

                if chanceForMiscarriage <= 5:
                    person.setIsPregnant(False)
                    person.setImpregnationMonth(None)
                    person.setPregnancyFather("")
                    person.setPregnancyTrueFather("")
                    person.increaseHappiness(-50)
                    if person.getSpouse() is not None:
                        person.getSpouse().increaseHappiness(-50)
                    PLEH.miscarriage(person, world)
                    continue

                # if (world.getMonth().value[0] > person.getImpregnationMonth().value[0] and world.getMonth().value[0]-person.getImpregnationMonth().value[0] == 9) or (world.getMonth().value[0] < person.getImpregnationMonth().value[0] and person.getImpregnationMonth().value[0] - world.getMonth().value[0] == 3):
                if world.getMonth() == person.getLaborMonth() and world.getDay() == person.getLaborDay():

                    person.setLaborMonth(None)
                    person.setLaborDay(None)

                    chanceOfBirth = Utils.randomRange(1, 100)

                    if chanceOfBirth <= 95:
                        # CHILD object
                        if person.getSpouse() is not None:
                            person.changeSpouseRelation(25)
                            person.getSpouse().changeSpouseRelation(25)
                        childObj = PF.birthChild(world, person, person.getSpouse(), person, person.getPregnancyTrueFather())
                        for child in childObj:
                        # add child to proper family
                            child.familyObjRef.addNewMember(child)
                            world.addPerson(child)
                            world.addAlivePerson(child)
                            PLEH.beenBorn(child, world)

                        person.setIsPregnant(False)
                        person.setImpregnationMonth(None)
                        person.setPregnancyFather("")
                        person.setPregnancyTrueFather("")

                        willMotherDie = False
                        for child in childObj:
                            person.numberOfChildren += 1
                            if person.getSpouse() is not None:
                                person.getSpouse().numberOfChildren += 1

                            if person.modifiedLifespan-person.age > 1:
                                if Utils.randomRange(1, 2) == 1:
                                    person.modifiedLifespan -= 1
                            person.appendAliveChildrenList(child)
                            if person.getSpouse() is not None:
                                person.getSpouse().appendAliveChildrenList(child)
                            child.changeMaritalStatus(MS.CHILD)
                            person.getAccommodation().addHouseResident(child)

                            child.setSettlement(child.getTrueMother().getSettlement())
                            child.getSettlement().increasePopulation()
                            child.getSettlement().addResident(child)

                            world.increaseBirthsPerYearTemp()
                            world.increaseBirthsPerDayTemp()

                            # change of dying from childbirth (mother and child)
                            motherDeath, childdeath = deathChangeFromGivingBirth(person, child)
                            willMotherDie = willMotherDie & motherDeath
                            if childdeath:
                                #parameters: child
                                PF.deathProcedures(child, world)

                        if willMotherDie:
                            PF.deathProcedures(person, world)

                    else:
                        person.setIsPregnant(False)
                        person.setImpregnationMonth(None)
                        person.setPregnancyFather(None)
                        person.increaseHappiness(-50)
                        if person.getSpouse() is not None:
                            person.getSpouse().increaseHappiness(-50)
                        PLEH.stillborn(person, world)
                        continue


def changeRelationToFromSpouse(person):

    if person.sexuality == 'homo':
        person.setSpouseRelation(Parameters.spouseHomoSexualityMod)
    if person.getSpouse().sexuality == 'homo':
        person.getSpouse().setSpouseRelation(Parameters.spouseHomoSexualityMod)

    person.changeSpouseRelation(person.getSpouseNumberOfLikedTraits() * Parameters.spouseLikedTraitsMod)
    person.changeSpouseRelation(person.getSpouseNumberOfDislikedTraits() * Parameters.spouseDislikedTraitsMod)
    person.getSpouse().changeSpouseRelation(person.getSpouse().getSpouseNumberOfLikedTraits() * Parameters.spouseLikedTraitsMod)
    person.getSpouse().changeSpouseRelation(person.getSpouse().getSpouseNumberOfDislikedTraits() * Parameters.spouseDislikedTraitsMod)

def changeRelationFromLovemaking(person, lover):


    #TODO dorobić zmianę relacji
    return

def settlementsPopulationManagement (world):

    timeArray = []

    for region in world.getRegions():
        regionTimeArray = []
        for province in region.getProvinces():
            for settlement in province.getSettlements():
                if world.getDay() == settlement.getMigrationDay() and len(settlement.getResidents()) > 50:
                    start1 = time.perf_counter()

                    villagesList = SF.getVillages(province.getSettlements())
                    townList = SF.getCities(province.getSettlements())

                    unemployedList = settlement.getUnemployedResidentsList()
                    employedList = settlement.getEmployedResidentsList()

                    chanceForMigragion = Parameters.chanceForMigration
                    #Treshhold to create migration wave
                    if ((len(employedList) + len(unemployedList)) > 0 and round(len(unemployedList) / (len(employedList) + len(unemployedList)) * 100) > 15) or (len(settlement.getResidents()) > 300 and settlement.getFreeFood() < 1000):
                        chanceForMigragion *= 2
                    else:
                    # if settlement.getPopulation() >= int(settlement.getMaxPopulation() * Parameters.percentagePopulationThresholdForMigration):
                        chanceOfMigration = Utils.randomRange(1, 100)
                        #Chance of migration happening
                        if chanceOfMigration <= chanceForMigragion:

                            possibleProvincesMigration = []
                            for neighbour in settlement.getProvince().getNeighbours():
                                if neighbour.getType() != 'SEA':
                                    possibleProvincesMigration.append(neighbour)
                            for provinceInRegion in settlement.getRegion().getProvinces():
                                if provinceInRegion not in possibleProvincesMigration:
                                    possibleProvincesMigration.append(provinceInRegion)

                            if len(province.getSettlements()) != province.provinceSize:
                                newSettlement = province.addSettlement(world)
                                if newSettlement is None:
                                    continue
                                newSettlement.setRegion(settlement.getRegion())
                                newSettlement.setMaxPopulation = Parameters.baseVillageSize
                                newTargetSettlement = newSettlement

                            else:
                                newTargerProvince = Utils.randomFromCollection(possibleProvincesMigration)
                                if len(newTargerProvince.getSettlements()) != newTargerProvince.provinceSize:
                                    newSettlement = newTargerProvince.addSettlement(world)
                                    if newSettlement is None:
                                        continue
                                    newSettlement.setRegion(newTargerProvince.getRegion())
                                    newSettlement.setMaxPopulation = Parameters.baseVillageSize
                                    newTargetSettlement = newSettlement
                                else:
                                    newTargetSettlement = Utils.randomFromCollection(newTargerProvince.getSettlements())

                            #
                            # #Check for max size of region
                            # if len(province.getSettlements()) == province.provinceSize:
                            #     newTargetSettlement = Utils.randomFromCollection(province.getSettlements())
                            #
                            # else:
                            #     # # TODO FIX PEOPLE CAN MOVE TO THE SAME VILLAGE
                            #     # #Take lowest population as dest
                            #     # lowestSettlementInRegion = region.getLowestPopulatedSettlement()
                            #     # newTargetSettlement = lowestSettlementInRegion
                            #     # #If lowest pop > lowest max pop * modifier create new setttlement
                            #     # if lowestSettlementInRegion.getPopulation() > int(lowestSettlementInRegion.getMaxPopulation() * Parameters.percentageVillagePopulationThresholdForCreatingNewVillage):
                            #         newSettlement = province.addSettlement(world)
                            #         if newSettlement is None:
                            #             continue
                            #         newSettlement.setRegion(settlement.getRegion())
                            #         newSettlement.setMaxPopulation = Parameters.baseVillageSize
                            #         newTargetSettlement = newSettlement

                            #Migration Wave
                            complexRandomMigrantsList = SF.prepareMigration(settlement, newTargetSettlement, world)
                            SF.iniciateMigration(complexRandomMigrantsList, newTargetSettlement, world)
                            SF.splitFamiliesInMigration(world, region, province, newTargetSettlement, complexRandomMigrantsList)
                    end1 = time.perf_counter()
                    start2 = time.perf_counter()
                    #Upgrading from Village to City
                    if len(villagesList) >= (len(townList)+1) * (Parameters.villageToTownMultiplier + 1) - len(townList):
                        randomVillage = Utils.randomFromCollection(villagesList)
                        if randomVillage.getPopulation() > int(randomVillage.getMaxPopulation() * Parameters.percentageVillagePopulationThresholdForUpgradeToTown):
                            chanceOfUpgradingToCity = Utils.randomRange(1, 100)
                            if chanceOfUpgradingToCity < Parameters.chancePerYearToUpgradeVillageToTown:
                                randomVillage.changeSettlementType(Settlements.TOWN)
                                Utils.randomFromCollection(randomVillage.getProvince().getVillagesExProvisionToThisTown(randomVillage)).setProvision(randomVillage)
                                Utils.randomFromCollection(randomVillage.getProvince().getVillagesExProvisionToThisTown(randomVillage)).setProvision(randomVillage)
                                Utils.randomFromCollection(randomVillage.getProvince().getVillagesExProvisionToThisTown(randomVillage)).setProvision(randomVillage)
                    end2 = time.perf_counter()
                    regionTimeArray.append(0)
                    regionTimeArray.append(end1-start1)
                    regionTimeArray.append(end2-start2)
        timeArray.append(regionTimeArray)

    # print(timeArray)
    # sum = 0
    # for timeRegions in timeArray:
    #     for timeSet in timeRegions:
    #         sum += timeSet
    #
    # print(sum)

def settlementGoodsProduction(world):

    if world.getDayOfTheYear() == 90:
        for region in world.getRegions():
            for province in region.getProvinces():
                for settlement in province.getSettlements():
                    if settlement.getFreeFood() > 0:
                        settlement.changeFreeFood(-(settlement.getFreeFood() - settlement.getFreeFood() * 0.9))
                        spoiledFood(settlement, world)

    if world.dayOfWeekFlag == 1:  # Only on Monday produce goods
        for region in world.getRegions():
            for province in region.getProvinces():
                for settlement in province.getSettlements():

                    mayorModifier = 1


                    ## ADMIN PROD
                    #village center
                    if len(settlement.getAdminFeatures()[0].getWorkerList()) > 0:

                        # flat bonus 5% if mayor
                        mayorModifier = 1.05
                        mayor = settlement.getAdminFeatures()[0].getWorkerList()[0]

                        if Traits.LAZY in mayor.getTraits():
                            mayorModifier *= 0.8
                        if Traits.DILIGENT in mayor.getTraits():
                            mayorModifier *= 1.2
                        if Traits.GREEDY in mayor.getTraits():
                            mayorModifier *= 0.9
                        if Traits.GREGARIOUS in mayor.getTraits():
                            mayorModifier *= 1.1
                        if Traits.IMPATIENT in mayor.getTraits():
                            mayorModifier *= 0.9
                        if Traits.PATIENT in mayor.getTraits():
                            mayorModifier *= 1.1

                        mayorModifier = mayorModifier * mayor.getSkills().getAdminSkill().getSkillLevel().value[4]

                        earnSkillXp(mayor, settlement.getAdminFeatures()[0], (mayorModifier * 100 - 100), world)
                        flatRate = 3
                        if settlement.getAdminFeatures()[0].getName() == SFeat.getVillageHall().getName():
                            flatRate = 5
                        if settlement.getAdminFeatures()[0].getName() == SFeat.getTownHall().getName():
                            flatRate = 7

                        if settlement.getRegion().getOriginalCulture().getTechnologiesInProgress()[0] == Enums.TechnologiesEnums.UNITY:
                            settlement.getRegion().getOriginalCulture().increaseTechnologiesInProgress(mayorModifier * 7)
                        mayor.changeFreeWealth(flatRate)
                        settlement.changeFreeWealth(-flatRate)

                    #shrine
                    if len(settlement.getAdminFeatures()[1].getWorkerList()) > 0:
                        flatRate = 3
                        priest = settlement.getAdminFeatures()[1].getWorkerList()[0]
                        priestModifier = 1

                        if Traits.LAZY in priest.getTraits():
                            priestModifier *= 0.8
                        if Traits.DILIGENT in priest.getTraits():
                            priestModifier *= 1.2
                        if Traits.GREEDY in priest.getTraits():
                            priestModifier *= 0.9
                        if Traits.GREGARIOUS in priest.getTraits():
                            priestModifier *= 1.1
                        if Traits.IMPATIENT in priest.getTraits():
                            priestModifier *= 0.9
                        if Traits.PATIENT in priest.getTraits():
                            priestModifier *= 1.1

                        earnSkillXp(priest, settlement.getAdminFeatures()[0], (priestModifier * 100 - 100), world)
                        priest.changeFreeWealth(flatRate)
                        settlement.changeFreeWealth(-flatRate)

                        if settlement.getRegion().getOriginalCulture().getTechnologiesInProgress()[0] == Enums.TechnologiesEnums.UNITY:
                            settlement.getRegion().getOriginalCulture().increaseTechnologiesInProgress(priestModifier * 7)

                    ## SERVICES
                    if len(settlement.getServicesFeatures()[0].getWorkerList()) > 0:
                        for specialist in settlement.getServicesFeatures()[0].getWorkerList():
                            rate = specialist.getSkills().getLaborSkill().getSkillLevel().value[0]
                            # for settlement.getSick()

                    ## MILITARY
                    if len(settlement.getMilitaryFeatures()[0].getWorkerList()) > 0:
                        flatRate = 3
                        for soldier in settlement.getMilitaryFeatures()[0].getWorkerList():
                            soldierModifier = 1

                            if Traits.LAZY in soldier.getTraits():
                                soldierModifier *= 0.8
                            if Traits.DILIGENT in soldier.getTraits():
                                soldierModifier *= 1.2
                            if Traits.GREEDY in soldier.getTraits():
                                soldierModifier *= 0.9
                            if Traits.GREGARIOUS in soldier.getTraits():
                                soldierModifier *= 1.1
                            if Traits.IMPATIENT in soldier.getTraits():
                                soldierModifier *= 0.9
                            if Traits.PATIENT in soldier.getTraits():
                                soldierModifier *= 1.1

                            earnSkillXp(soldier, settlement.getMilitaryFeatures()[0], (soldierModifier * 100 - 100), world)
                            soldier.changeFreeWealth(flatRate)
                            settlement.changeFreeWealth(-flatRate)


                    ##  FOOD PRODUCTION
                    foodProd0 = settlement.getSettlementFoodProduced()
                    for foodTile in settlement.getFoodFeatures():

                        for worker in foodTile.getWorkerList():
                            if worker.getGeneralHealth().value[0] <= 1:  # Only Healthy or weaken can work
                                workerModifier = 0
                                if Traits.LAZY in worker.getTraits():
                                    workerModifier += -10
                                if Traits.DILIGENT in worker.getTraits():
                                    workerModifier += 10
                                if worker.getGeneralHealth().value[1] == 1:  # weaken workers work less
                                    workerModifier = round(workerModifier / 2)

                                foodProd = foodTile.prodYield * worker.getSkills().getLaborSkill().getSkillLevel().value[4] * (foodTile.foundationType['yieldModifier'] + workerModifier) * mayorModifier / 100

                                if settlement.getProvision() is not None:
                                    settlement.getProvision().increaseSettlementFoodProduced(foodProd * Parameters.socage)
                                    settlement.increaseSettlementFoodProduced(foodProd * (1 - Parameters.socage))
                                else:
                                    settlement.increaseSettlementFoodProduced(foodProd)

                                earnSkillXp(worker, foodTile, workerModifier, world)
                                goodProduced = foodTile.prodYield * worker.getSkills().getLaborSkill().getSkillLevel().value[4] * (foodTile.foundationType['yieldModifier'] + workerModifier) / 100
                                worker.changeFreeWealth(goodProduced * (100 - settlement.getLocalIncomeTax()) / 100)
                                settlement.changeFreeWealth(goodProduced * (settlement.getLocalIncomeTax()) / 100)

                    foodProd1 = settlement.getSettlementFoodProduced()
                    settlement.setSettlementFoodProducedLastYear(foodProd1-foodProd0)

                    foodConsumed = 0
                    for resident in settlement.getResidents():
                        if resident.getAge() < 10:
                            foodConsumed += 0.3
                            settlement.increaseSettlementFoodConsumed(0.3)
                        elif 10 <= resident.getAge() < 15:
                            foodConsumed += 0.6
                            settlement.increaseSettlementFoodConsumed(0.6)
                        else:
                            if Enums.Traits.GREGARIOUS in resident.getTraits():
                                foodConsumed += 0.9
                            if Enums.Traits.GREEDY in resident.getTraits():
                                foodConsumed += 1.1
                            else:
                                foodConsumed += 1
                            settlement.increaseSettlementFoodConsumed(1)
                    settlement.setSettlementFoodConsumedLastYear(foodConsumed)
                    if settlement.getFreeFood() + (foodProd1 - foodProd0) - foodConsumed < 0:
                        settlement.setFreeFood(0)
                    else:
                        settlement.changeFreeFood(foodProd1 - foodProd0 - foodConsumed)

                    settlement.setNetFoodLastYear(foodProd1-foodProd0-foodConsumed)

                    ##PRODUCTION PRODUCTION
                    prodProd0 = settlement.getSettlementProdProduced()

                    for prodTile in settlement.getProdFeatures():

                        for worker in prodTile.getWorkerList():
                            if worker.getGeneralHealth().value[0] <= 1:
                                workerModifier = 0
                                if Traits.LAZY in worker.getTraits():
                                    workerModifier = -10
                                if Traits.DILIGENT in worker.getTraits():
                                    workerModifier = 10
                                if worker.getGeneralHealth().value[1] == 1:  # weaken workers work less
                                    workerModifier = round(workerModifier / 2)

                                prodProd = prodTile.prodYield * worker.getSkills().getLaborSkill().getSkillLevel().value[4] * (prodTile.foundationType['yieldModifier'] + workerModifier) * mayorModifier / 100

                                if settlement.getProvision() is not None:
                                    settlement.getProvision().increaseSettlementProdProduced(prodProd * Parameters.socage)
                                    settlement.increaseSettlementProdProduced(prodProd * (1 - Parameters.socage))
                                else:
                                    settlement.increaseSettlementProdProduced(prodProd)

                                earnSkillXp(worker, prodTile, workerModifier, world)
                                goodProduced = prodTile.prodYield * worker.getSkills().getLaborSkill().getSkillLevel().value[4] * (prodTile.foundationType['yieldModifier'] + workerModifier) / 100
                                worker.changeFreeWealth(goodProduced * (100-settlement.getLocalIncomeTax())/100)
                                settlement.changeFreeWealth(goodProduced * (settlement.getLocalIncomeTax())/100)

                    prodProd1 = settlement.getSettlementProdProduced()
                    settlement.changeFreeProd(prodProd1 - prodProd0)
                    settlement.setSettlementProdProducedLastYear(prodProd1 - prodProd0)


                    #UPGRADING FEATURES

                    if float(settlement.getFreeProd()) > 0:
        #                if settlement.getSettlementFoodProducedLastYear() - settlement.getSettlementFoodConsumedLastYear() < int(round(len(settlement.getResidents())/2)):
                            SF.checkForTileUpgrades(settlement, settlement.getFoodFeatures(), world)
                            SF.checkForTileUpgrades(settlement, settlement.getProdFeatures(), world)

def earnSkillXp(person, feature, modifier, world):

    #times 7 because for all the week (check is only for monday)
    if feature.getSkillUsed() == Enums.SkillNames.LABOR:
        gotBetter = person.getSkills().getLaborSkill().increaseSkillXp(round((100 + modifier) / 100, 2) * 7)
        if gotBetter:
            person.increaseHappiness(5)
            PLEH.gotBetterSkillLevel(person, Enums.SkillNames.LABOR, gotBetter, world)
    if feature.getSkillUsed() == Enums.SkillNames.ADMIN:
        gotBetter = person.getSkills().getAdminSkill().increaseSkillXp(round((100 + modifier) / 100, 2) * 7)
        if gotBetter:
            person.increaseHappiness(5)
            PLEH.gotBetterSkillLevel(person, Enums.SkillNames.ADMIN, gotBetter, world)
    if feature.getSkillUsed() == Enums.SkillNames.FIGHTER:
        gotBetter = person.getSkills().getFighterSkill().increaseSkillXp(round((100 + modifier) / 100, 2) * 7)
        if gotBetter:
            person.increaseHappiness(5)
            PLEH.gotBetterSkillLevel(person, Enums.SkillNames.FIGHTER, gotBetter, world)

    return

def accommodationManagment(world):

    if world.dayOfWeekFlag == 1:  # Only on Monday produce goods

        for region in world.getRegions():
            for province in region.getProvinces():
                for settlement in province.getSettlements():

                    for house in settlement.getHousing():

                        HouseFunctions.payForUpkeep(house)

                        if house.getHouseDurability() == 0:
                            if len(house.getHouseResidents()) == 0:
                                settlement.removeHouse(house)
                            else:
                                HouseFunctions.downgradeHouse(house)

                        HouseFunctions.payForUpgrade(house)


def associateManagement(world):

    for region in world.getRegions():

        for province in region.getProvinces():

            for settlement in province.getSettlements():

                for employee in settlement.getEmployedResidentsList():

                    for employeeSecond in settlement.getEmployedResidentsList():

                        if employeeSecond not in employee.getKnownAssociates() or employee != employeeSecond:

                            employee.addKnownAssociates(employeeSecond, 0)
                            employeeSecond.addKnownAssociates(employee, 0)



def settlementWorkersManagement(world):

    for region in world.getRegions():

        for province in region.getProvinces():
            for settlement in province.getSettlements():

                    loopBreaker = 0
                    basicAdminJobWeight = 10
                    basicFoodJobWeight = 1
                    basicProdJobWeight = 1

                    #FIRE SICK PEOPLE
                    for milTile in settlement.getMilitaryFeatures():
                        SF.fireEmployeesWithPoorHealth(milTile, world)
                    for adminTile in settlement.getAdminFeatures():
                        SF.fireEmployeesWithPoorHealth(adminTile, world)
                    for foodTile in settlement.getFoodFeatures():
                        SF.fireEmployeesWithPoorHealth(foodTile, world)
                    for prodTile in settlement.getProdFeatures():
                        SF.fireEmployeesWithPoorHealth(prodTile, world)

                    unemployedWorkerList = settlement.getUnemployedResidentsList()

                    #MILITARY
                    if settlement.getEmploymentRate() >= 0.3 and len(unemployedWorkerList) > 0 and settlement.getFreeWealth() > 0:

                        if Utils.randomRange(1, 100) > 0.6:
                            militaryFreeWorkplacesSpots = []
                            for milTile in settlement.getMilitaryFeatures():
                                for occupations in range(milTile.getFreeWorkersSlots()):
                                    militaryFreeWorkplacesSpots.append([milTile, occupations])

                            if len(militaryFreeWorkplacesSpots) > 0:
                                newWorker = Utils.randomFromCollection(unemployedWorkerList)
                                randomJob = Utils.randomRange(0, len(militaryFreeWorkplacesSpots) - 1)

                                if newWorker.getSex() == Sexes.MALE:
                                    SF.hireEmployee(newWorker, militaryFreeWorkplacesSpots[randomJob][0], world)
                                    unemployedWorkerList.remove(newWorker)
                                    del militaryFreeWorkplacesSpots[randomJob]

                    #REST
                    if len(unemployedWorkerList) > 0:
                        if settlement.getSettlementFoodProducedLastYear() <= 0:

                            basicFoodJobWeight *= 20

                        if settlement.getSettlementProdProducedLastYear() == 0:
                            basicProdJobWeight *= 2

                        adminFreeWorkplacesSpots = []
                        for adminTile in settlement.getAdminFeatures():
                            for occupations in range(adminTile.getFreeWorkersSlots()):
                                adminFreeWorkplacesSpots.append([adminTile, occupations])

                        foodFreeWorkplacesSpots = []
                        for foodTile in settlement.getFoodFeatures():
                            for occupations in range(foodTile.getFreeWorkersSlots()):
                                foodFreeWorkplacesSpots.append([foodTile, occupations])

                        prodFreeWorkplacesSpots = []
                        for prodTile in settlement.getProdFeatures():
                            for occupations in range(prodTile.getFreeWorkersSlots()):
                                prodFreeWorkplacesSpots.append([prodTile, occupations])

                        numberOfFreeWorkplaces = len(adminFreeWorkplacesSpots) + len(foodFreeWorkplacesSpots) + len(prodFreeWorkplacesSpots)
                        if len(adminFreeWorkplacesSpots) == 0 or settlement.getFreeWealth() < 0:
                            basicAdminJobWeight = 0
                        if len(foodFreeWorkplacesSpots) == 0:
                            basicFoodJobWeight = 0
                        if len(prodFreeWorkplacesSpots) == 0:
                            basicProdJobWeight = 0

                        weightedAdminJobs = len(adminFreeWorkplacesSpots) * basicAdminJobWeight
                        weightedFoodJobs = len(foodFreeWorkplacesSpots) * basicFoodJobWeight
                        weightedProdJobs = len(prodFreeWorkplacesSpots) * basicProdJobWeight

                        if basicAdminJobWeight + basicFoodJobWeight + basicProdJobWeight > 0 and weightedAdminJobs + weightedFoodJobs + weightedProdJobs > 0:

                            for freeWorkPlace in range(numberOfFreeWorkplaces):
                                if loopBreaker == 10:
                                    break
                                if len(unemployedWorkerList) == 0:
                                    break

                                if weightedAdminJobs + weightedFoodJobs + weightedProdJobs == 0:
                                    break

                                randomJobSite = Utils.randomRange(0, weightedAdminJobs + weightedFoodJobs + weightedProdJobs)

                                if len(adminFreeWorkplacesSpots) > 0 and randomJobSite <= weightedAdminJobs:
                                    newWorker = Utils.randomFromCollection(unemployedWorkerList)
                                    randomJob = Utils.randomRange(0, len(adminFreeWorkplacesSpots)-1)
                                    if adminFreeWorkplacesSpots[randomJob][0].getOccupationName() != 'Priest' or (adminFreeWorkplacesSpots[randomJob][0].getOccupationName() == 'Priest' and newWorker.getSex() == Sexes.MALE and newWorker.getSpouse() is None):
                                        SF.hireEmployee(newWorker, adminFreeWorkplacesSpots[randomJob][0], world)
                                        unemployedWorkerList.remove(newWorker)
                                        del adminFreeWorkplacesSpots[randomJob]
                                        weightedAdminJobs -= basicAdminJobWeight
                                    else:
                                        loopBreaker +=1
                                        continue

                                elif len(foodFreeWorkplacesSpots) > 0 and randomJobSite <= weightedAdminJobs + weightedFoodJobs:
                                    newWorker = Utils.randomFromCollection(unemployedWorkerList)
                                    randomJob = Utils.randomRange(0, len(foodFreeWorkplacesSpots)-1)
                                    SF.hireEmployee(newWorker, foodFreeWorkplacesSpots[randomJob][0], world)
                                    unemployedWorkerList.remove(newWorker)
                                    del foodFreeWorkplacesSpots[randomJob]
                                    weightedFoodJobs -= basicFoodJobWeight

                                elif len(prodFreeWorkplacesSpots) > 0 and randomJobSite <= weightedAdminJobs + weightedFoodJobs + weightedProdJobs:
                                    newWorker = Utils.randomFromCollection(unemployedWorkerList)
                                    randomJob = Utils.randomRange(0, len(prodFreeWorkplacesSpots)-1)
                                    SF.hireEmployee(newWorker, prodFreeWorkplacesSpots[randomJob][0], world)
                                    unemployedWorkerList.remove(newWorker)
                                    del prodFreeWorkplacesSpots[randomJob]
                                    weightedProdJobs -= basicProdJobWeight

                    if settlement.getSettlementFoodProducedLastYear() <= 0:
                        SF.fireAllEmployees(settlement.getAdminFeatures()[0], world)
                        for milFeature in settlement.getMilitaryFeatures():
                            SF.fireAllEmployees(milFeature, world)
                        for prodfeature in settlement.getProdFeatures():
                            SF.fireAllEmployees(prodfeature, world)

def crime(world):

    crimeLevel = 0
    crimeHomicideTemp = 0
    crimeAssaultTemp = 0
    crimeBurglaryTemp = 0
    crimeTheftTemp = 0
    crimeFailedTemp = 0

    for person in world.getAlivePeople():
        randomChanceForCrime = Utils.randomRange(1, 1000)
        if randomChanceForCrime < 3 and (Traits.VENGEFUL in person.getTraits() or Traits.GREEDY in person.getTraits() or Traits.DECEITFUL in person.getTraits() and person.getOccupation() is None) and person.getAge() > 15 and person.getLifeStatus() == LifeStatus.ALIVE and person.getFreeWealth() < person.getSettlement().getAvarageResidentsWealth():
            randomPerson = Utils.randomFromCollection(person.getSettlement().getResidents())
            if randomPerson != person and randomPerson != person.spouse and randomPerson not in person.getAliveChildrenList():
                randomCrime = Utils.randomRange(1, 100)
                #homicide
                if randomCrime < 10:
                    # print("Homicide")
                    PF.deathProcedures(randomPerson, world)
                    offenderIdentified = Utils.randomRange(1, 100)
                    if offenderIdentified > 50:
                        PLEH.killedByDuringCrime(randomPerson, person, world)
                    else:
                        PLEH.killedByDuringCrime(randomPerson, None, world)
                    PLEH.killedSMBDuringCrime(person, randomPerson, world)
                    if randomPerson.getFreeWealth() > 0:
                        loot = randomPerson.getFreeWealth()
                        randomPerson.setFreeWealth(loot / 2)
                        person.changeFreeWealth(loot)
                    crimeLevel += 1
                    crimeHomicideTemp += 1
                    continue
                if randomCrime < 30:
                    # print("Assault")
                    if randomPerson.getFreeWealth() > 0:
                        loot = randomPerson.getFreeWealth()
                        randomPerson.setFreeWealth(loot / 3)
                        person.changeFreeWealth(loot)
                    InfectionsFunctions.injureSomeone(randomPerson, world)
                    crimeLevel += 1
                    crimeAssaultTemp += 1
                    continue
                if randomCrime < 70:
                    # print("Burglary")
                    if randomPerson.getFreeWealth() > 0:
                        loot = randomPerson.getFreeWealth()
                        randomPerson.setFreeWealth(loot / 4)
                        person.changeFreeWealth(loot)
                    crimeLevel += 1
                    crimeBurglaryTemp += 1
                    continue
                if randomCrime < 90:
                    # print("Theft")
                    if randomPerson.getFreeWealth() > 0:
                        loot = randomPerson.getFreeWealth()
                        randomPerson.setFreeWealth(loot / 5)
                        person.changeFreeWealth(loot)
                    crimeLevel += 1
                    crimeTheftTemp += 1
                    continue
                if randomCrime <= 100:
                    # print("Crime failed")
                    crimeLevel += 1
                    crimeFailedTemp += 1
                    continue

    world.appendCrimesPerYear(crimeLevel, [crimeHomicideTemp, crimeAssaultTemp, crimeBurglaryTemp, crimeTheftTemp, crimeFailedTemp])

def moveFoodAndProduction(migrantSize, oldSettlement, newSettlement):

    foodPackages = 2 * migrantSize
    if oldSettlement.getFreeFood() > foodPackages:
        oldSettlement.changeFreeFood(foodPackages)
        newSettlement.changeFreeFood(foodPackages)

def deathFromNegligence(person):

    if person.father is not None and person.mother is not None:
        if person.father.lifeStatus == LifeStatus.DEAD and person.mother.lifeStatus == LifeStatus.DEAD:
            chanceOfDeath = Utils.randomRange(1, 100)
            triangChance = (Utils.triangularNumber(person.age-1))
            if chanceOfDeath < 100 - triangChance:
                person.causeOfDeath = CauseOfDeath.NEGLIGENCE
                return True
    return False


def deathChanceFromAge(person):

    chanceOfDeath = Utils.randomRange(1, 10000)
    dead = False

    age = person.getAge()
    modifiedLifespan = person.modifiedLifespan

    if age == 0:
        if chanceOfDeath <= 5:
            dead = True
            person.causeOfDeath = CauseOfDeath.CHILDSICKNESS
    elif age == 1:
        if chanceOfDeath <= 4:
            person.causeOfDeath = CauseOfDeath.CHILDSICKNESS
            dead = True
    elif age == 2:
        if chanceOfDeath <= 3:
            person.causeOfDeath = CauseOfDeath.CHILDSICKNESS
            dead = True
    elif modifiedLifespan-age <= 5:
        if chanceOfDeath <= 100 - (modifiedLifespan-age) * 4:
            person.causeOfDeath = CauseOfDeath.AGE
            dead = True

    if person.age < 15:
        if deathFromNegligence(person):
            dead = True

    return dead


def deathChangeFromGivingBirth(person, child, modifier=0):

    motherDeath = False
    childDeath = False
    numberOfChildren = person.numberOfChildren
    chanceOfMotherDeath = 0

    if numberOfChildren == 0:
        chanceOfMotherDeath = Utils.randomRange(1, 100)
    elif numberOfChildren == 1:
        chanceOfMotherDeath = Utils.randomRange(1, 98)
    elif numberOfChildren == 2:
        chanceOfMotherDeath = Utils.randomRange(1, 95)
    else:
        chanceOfMotherDeath = Utils.randomRange(1, 90)

    if chanceOfMotherDeath > 88 + modifier:
        person.causeOfDeath = CauseOfDeath.CHILDBIRTH
        motherDeath = True

    chanceOfChildsDeath = Utils.randomRange(1, 100)

    if chanceOfChildsDeath > 90 + modifier:
        child.causeOfDeath = CauseOfDeath.CHILDBIRTH
        childDeath = True

    return motherDeath, childDeath

def raiding (world):

    for region in world.getRegions():
        for province in region.getProvinces():
            for settlement in province.getSettlements():
                if world.getSeason() == Enums.Seasons.WINTER and world.getDay() == settlement.getRaidDatesPerSeason()[0][0] and world.getMonth() == settlement.getRaidDatesPerSeason()[0][1]:
                    raidingFunctions(settlement, world)
                if world.getSeason() == Enums.Seasons.SPRING and world.getDay() == settlement.getRaidDatesPerSeason()[1][0] and world.getMonth() == settlement.getRaidDatesPerSeason()[1][1]:
                    raidingFunctions(settlement, world)
                if world.getSeason() == Enums.Seasons.SUMMER and world.getDay() == settlement.getRaidDatesPerSeason()[2][0] and world.getMonth() == settlement.getRaidDatesPerSeason()[2][1]:
                    raidingFunctions(settlement, world)
                if world.getSeason() == Enums.Seasons.FALL and world.getDay() == settlement.getRaidDatesPerSeason()[3][0] and world.getMonth() == settlement.getRaidDatesPerSeason()[3][1]:
                    raidingFunctions(settlement, world)
            if world.getDay() == 1 and (world.getMonth() == Enums.Months.DECEMBER or world.getMonth() == Enums.Months.MARCH or world.getMonth() == Enums.Months.JUNE or world.getMonth() == Enums.Months.SEPTEMBER):
                for settlement in province.getSettlements():
                    settlement.resetRaidedFlag()
                    settlement.resetRaidDatesPerSeason()

def raidingFunctions(settlement, world):

    if len(settlement.getMilitary()) > 0:
        randomTarget = findTarget(settlement, world)

        stolenFoodAmount = round(randomTarget.getFreeFood() * 0.4, 2)
        randomTarget.changeFreeFood(-stolenFoodAmount)
        settlement.changeFreeFood(stolenFoodAmount)
        stolenWealthAmount = round(randomTarget.getFreeWealth() * 0.4, 2)
        randomTarget.changeFreeWealth(-stolenWealthAmount)
        settlement.changeFreeWealth(stolenWealthAmount)
        SettlementLifeEventsHistory.raided(settlement, randomTarget, stolenFoodAmount, stolenWealthAmount, world)
        SettlementLifeEventsHistory.beenRaided(randomTarget, stolenFoodAmount, stolenWealthAmount, world)
        settlement.setRaidedFlag()
        if len(randomTarget.getMilitary()) > 0:
            for defSoldier in randomTarget.getMilitary():
                changeToGetWounded = Utils.randomRange(1, 100)
                if changeToGetWounded < 95 - defSoldier.getSkills().getFighterSkill().getSkillLevel().value[0] * 6:
                    InfectionsFunctions.injureSomeone(defSoldier, world)
        for soldier in settlement.getMilitary():
            changeToGetWounded = Utils.randomRange(1, 100)
            if changeToGetWounded < 95 - soldier.getSkills().getFighterSkill().getSkillLevel().value[0] * 6:
                InfectionsFunctions.injureSomeone(soldier, world)
            PLEH.raided(soldier, randomTarget, world)


def caltulateRaidSuccess(settlement, target, world):

    attackingForce = len(settlement.getMilitary())
    defendingForce = len(target.getMilitary())
    if defendingForce == 0:
        return 100

    return

def caltulateRaidCasuaslies():
    return

def findTarget(settlement, world):

    raidList = []
    regions = world.getRegions().copy()
    regions.remove(settlement.getProvince().getRegion())
    for region in regions:
        for province in region.getProvinces():
            raidList += province.getSettlements()

    randomTarget = Utils.randomFromCollection(raidList)

    return randomTarget

def assosiatesFriendsAndFoes(world):
    times1 = 0
    times2 = 0
    start1 = time.perf_counter()
    for region in world.getRegions():
        for province in region.getProvinces():
            for settlement in province.getSettlements():
                for person in settlement.getEmployedResidentsList():
                    for fellowEmployee in person.getOccupation().getWorkerList():
                        if fellowEmployee != person and fellowEmployee not in person.getKnownAssociates():
                            person.addKnownAssociates(fellowEmployee)
                            fellowEmployee.addKnownAssociates(person)
                            person1LikenessIndicatorForPerson2 = Utils.checkForLikedTraisInPerson2(person, fellowEmployee)
                            person2LikenessIndicatorForPerson1 = Utils.checkForLikedTraisInPerson2(fellowEmployee, person)
                            if person1LikenessIndicatorForPerson2 > 0 and person2LikenessIndicatorForPerson1 > 0:
                                if fellowEmployee not in person.getFriends():
                                    person.addFriends(fellowEmployee)
                                    person.increaseHappiness(20)
                                    PLEH.gotFriend(person, fellowEmployee, world)
                                if person not in fellowEmployee.getFriends():
                                    fellowEmployee.addFriends(person)
                                    person.increaseHappiness(20)
                                    PLEH.gotFriend(fellowEmployee, person, world)

                            person1DislikenessIndicatorForPerson2 = Utils.checkForDislikedTraisInPerson2(person, fellowEmployee)
                            person2DislikenessIndicatorForPerson1 = Utils.checkForDislikedTraisInPerson2(fellowEmployee, person)
                            if person1DislikenessIndicatorForPerson2 > 0 and person2DislikenessIndicatorForPerson1 > 0:
                                if fellowEmployee not in person.getFriends():
                                    person.addRivals(fellowEmployee)
                                    person.increaseHappiness(-20)
                                    PLEH.gotRival(person, fellowEmployee, world)
                                if person not in fellowEmployee.getFriends():
                                    fellowEmployee.addRivals(person)
                                    person.increaseHappiness(-20)
                                    PLEH.gotRival(fellowEmployee, person, world)

    end1 = time.perf_counter()
    start2 = time.perf_counter()
    for person in world.getAlivePeople():
        personFriends = person.getFriends()
        if len(personFriends) > 0:
            for friend in personFriends:
                if PF.canBeLover(person, friend):
                    PF.checkAndAddPersonToLovers(person, friend, world)
                friendSpouse = friend.getSpouse()
                if friendSpouse is not None:
                    if PF.canBeLover(person, friendSpouse):
                        PF.checkAndAddPersonToLovers(person, friendSpouse, world)


    end2 = time.perf_counter()
    times1 = end1 - start1
    times2 = end2 - start2

    print("Times1: " + str(times1))
    print("Times2: " + str(times2))
