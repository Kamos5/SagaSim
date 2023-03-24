import time
from statistics import mean

import Enums
import FamilyFunctions as FF
import HouseFunctions
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

def increaseAge (world):

    for person in world.getAlivePeople():
        if person.lifeStatus != LifeStatus.DEAD:  #must be sometimes people die in between years and getAlive is not updated yet

            if person.getDayOfBirth() == world.getDay() and person.getMonthOfBirth() == world.getMonth():
                person.increaseAge()

                if person.age < 15:
                    person.increaseHeight()

                    #for accelerating groth in children
                    if Parameters.growthSpeed > 0:
                        for grothAccelerator in range(Parameters.growthSpeed-1):
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

                if person.getHealthFromAge() == Enums.GeneralHealth.HEALTHY and person.modifiedLifespan - person.getAge() <= 5:
                    person.setHealthFromAge(Enums.GeneralHealth.WEAKEN)

            if deathChanceFromAge(person) or person.age >= person.modifiedLifespan:
                PF.deathProcedures(person, world)
                continue

            if person.getSettlement().getFreeFood() <= 0:
                chanceForStarvation = Utils.randomRange(1, 100)
                if chanceForStarvation <= 2:
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
    for person in world.getAlivePeople():
        if person.lifeStatus == LifeStatus.ALIVE:

            start1 = time.perf_counter()
            # 1)
            chanceForContractDisease = Utils.randomRange(1, 10_000_000)  # 1 in 1.000.000 / per day
            contractDiseaseThreshold = 1

            contractDiseaseThreshold = (contractDiseaseThreshold * person.getGeneralHealth().value[0]) + 2

            if chanceForContractDisease <= contractDiseaseThreshold:
                randomInfection = Utils.randomFromCollection(list(world.diseases.items()))[1]
                if len(person.getImmunityTo()) > 0:
                    isImmune = False
                    for immunityTo in person.getImmunityTo():
                        if not randomInfection == immunityTo[0][0]:
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
                                PLEH.showingSymptomsOf(person, infection, world)
                                offsetHealth = person.getGeneralHealth().value[0] + infection['effectOnHealth'] + person.getHealthFromAge().value[0]
                                if offsetHealth >= len(Enums.getGeneralHealthArray()):
                                    offsetHealth = len(Enums.getGeneralHealthArray()) - 1
                                person.setGeneralHelth(Enums.getGeneralHealthArray()[offsetHealth])
                                if person.getGeneralHealth() == Enums.GeneralHealth.DEATH:
                                    person.causeOfDeath = CauseOfDeath.SICKNESS
                                    PF.deathProcedures(person, world)
                                    break
                        else:
                            person.addCurrentDiseases([infection, world.getDayOfTheYear(), 0])
                            PLEH.showingSymptomsOf(person, infection, world)
                            offsetHealth = person.getGeneralHealth().value[0] + infection['effectOnHealth'] + person.getHealthFromAge().value[0]
                            if offsetHealth > len(Enums.getGeneralHealthArray()):
                                offsetHealth = len(Enums.getGeneralHealthArray()) - 1
                            person.setGeneralHelth(Enums.getGeneralHealthArray()[offsetHealth])
                            if person.getGeneralHealth() == Enums.GeneralHealth.DEATH:
                                person.causeOfDeath = CauseOfDeath.SICKNESS
                                PF.deathProcedures(person, world)
                                break

            end3 = time.perf_counter()

            time1Array.append(end1-start1)
            time2Array.append(end2-start2)
            time3Array.append(end3-start3)
    end0 = time.perf_counter()
    print("Time0:" + str(end0-start0))
    print("Time1:" + str(mean(time1Array)))
    print("Time2:" + str(mean(time2Array)))
    print("Time3:" + str(mean(time3Array)))
    infectionsPerPop = round(infectionsPerDay / len(world.getAlivePeople()), 2)
    print("Infections Per Day:" + str(infectionsPerDay))
    print("Infections Per Pop:" + str(infectionsPerPop))

def diseasesProgress(world):

    for person in world.getAlivePeople():
        if person.getLifeStatus() == Enums.LifeStatus.ALIVE:
            person.setCurrentDiseases([disease for disease in person.getCurrentDiseases() if not toRemoveDisease(person, disease, world)])
            if person.getGeneralHealth().value[0] > 1:
                chanceToDieFromPoorHealth = Utils.randomRange(1, 100)
                if chanceToDieFromPoorHealth < 2 * 2 ** (person.getGeneralHealth().value[0]-2):
                    person.causeOfDeath = CauseOfDeath.SICKNESS
                    PF.deathProcedures(person, world)

def toRemoveDisease(person, disease, world):

    if disease[2] < 100:
        disease[2] += round(100 / disease[0]["daysToCure"])
        if disease[2] >= 100:
            disease[2] = 100  ######TO COS JEST NIE TAK -> rozkminic te tablice
            person.setInfections([infection for infection in person.getInfections() if not infection[0] == disease[0]])
            person.setGeneralHelth(Enums.getGeneralHealthArray()[person.getGeneralHealth().value[0] - disease[0]['effectOnHealth'] + person.getHealthFromAge().value[0]])
            person.addImmunityTo([disease, world.getDayOfTheYear()])
            PLEH.gotImmunityTo(person, disease[0], world)
            return disease


def loveMaking (world):

    for person in world.getAlivePeople():
        if person.sex == Sexes.FEMALE and 15 <= person.age and (person.spouse is not None or len(person.getLovers()) > 0) and person.lifeStatus == LifeStatus.ALIVE and not person.isPregnant:

            lovemakingWithSpouse = 99
            lovemakingWithLovers = 1

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

        #TIME for labour aka 9m pregnancy
        if person.sex == Sexes.FEMALE and person.isPregnant and person.getLifeStatus() != LifeStatus.DEAD:

            if person.getSpouse() is not None:
                # change spouseRelation based on liked/disliked traits
                changeRelationToFromSpouse(person)

            chanceForMiscarriage = Utils.randomRange(1, 10000)

            if chanceForMiscarriage <= 5:
                person.setIsPregnant(False)
                person.setImpregnationMonth(None)
                person.setPregnancyFather("")
                person.setPregnancyTrueFather("")
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
                    childObj = PF.birthChild(world, person, person.getSpouse(), person, person.getPregnancyFather())
                    # add child to proper family
                    childObj.familyObjRef.addNewMember(childObj)
                    world.addPerson(childObj)
                    world.addAlivePerson(childObj)
                    PLEH.beenBorn(childObj, world)

                    person.setIsPregnant(False)
                    person.setImpregnationMonth(None)
                    person.setPregnancyFather("")
                    person.setPregnancyTrueFather("")

                    person.numberOfChildren += 1
                    if person.getSpouse() is not None:
                        person.getSpouse().numberOfChildren += 1

                    if person.modifiedLifespan-person.age > 1:
                        if Utils.randomRange(1, 2) == 1:
                            person.modifiedLifespan -= 1
                    person.appendAliveChildrenList(childObj)
                    if person.getSpouse() is not None:
                        person.getSpouse().appendAliveChildrenList(childObj)
                    childObj.changeMaritalStatus(MS.CHILD)
                    person.getAccommodation().addHouseResident(childObj)

                    childObj.setSettlement(childObj.getTrueMother().getSettlement())
                    childObj.getSettlement().increasePopulation()
                    childObj.getSettlement().addResident(childObj)

                    world.increaseBirthsPerYearTemp()

                    # change of dying from childbirth (mother and child)
                    motherDeath, childdeath = deathChangeFromGivingBirth(person, childObj)

                    if motherDeath:
                        PF.deathProcedures(person, world)

                    if childdeath:
                        #parameters: child
                        PF.deathProcedures(childObj, world)

                else:
                    person.setIsPregnant(False)
                    person.setImpregnationMonth(None)
                    person.setPregnancyFather(None)
                    PLEH.stillborn(person, world)
                    continue


def birthPeople (world):

    births = 0
    for person in world.getAlivePeople():

        # person here is MOTHER
        # only Females can give birth between 15 and 45y old + must be alive and have spouse
        if person.sex == Sexes.FEMALE and 15 <= person.age <= 45 and person.spouse is not None and person.lifeStatus == LifeStatus.ALIVE:

            # change spouseRelation based on liked/disliked traits
            changeRelationToFromSpouse(person)
            # is spouse alive
            if person.getSpouse().lifeStatus == LifeStatus.ALIVE:
                chanceOfBirth = Utils.randomRange(1, 100)

                if person.sexuality == 'homo':
                    person.setSpouseRelation(-5)
                if person.getSpouse().sexuality == 'homo':
                    person.getSpouse().setSpouseRelation(-5)

                if (chanceOfBirth <= min(person.fertility, person.getSpouse().fertility) * person.getSpouse().getSettlement().getBaseFertility() * person.getSpouse().getSettlement().getFertilityModifier() * person.getPersonalSexualModifier() * person.getSpouse().getPersonalSexualModifier()) and person.getSpouseRelation() > 0:
                    # CHILD object
                    person.changeSpouseRelation(25)
                    person.getSpouse().changeSpouseRelation(25)
                    childObj = PF.birthChild(world, person, person.getSpouse())
                    # add child to proper family
                    childObj.familyObjRef.addNewMember(childObj)
                    world.addPerson(childObj)
                    world.addAlivePerson(childObj)
                    PLEH.beenBorn(childObj, world)
                    person.numberOfChildren += 1
                    person.getSpouse().numberOfChildren += 1
                    if person.modifiedLifespan-person.age > 1:
                        if Utils.randomRange(1, 2) == 1:
                            person.modifiedLifespan -= 1
                    person.appendAliveChildrenList(childObj)
                    person.getSpouse().appendAliveChildrenList(childObj)
                    childObj.changeMaritalStatus(MS.CHILD)
                    person.getAccommodation().addHouseResident(childObj)

                    childObj.setSettlement(childObj.getFather().getSettlement())
                    childObj.getSettlement().increasePopulation()
                    childObj.getSettlement().addResident(childObj)

                    # change of dying from childbirth (mother and child)
                    motherDeath, childdeath = deathChangeFromGivingBirth(person, childObj)

                    if motherDeath:
                        PF.deathProcedures(person, world)

                    if childdeath:
                        #parameters: child
                        PF.deathProcedures(childObj, world)

                    births += 1

    world.appendBirthsPerYear(births)


    return

def changeRelationToFromSpouse(person):

    if person.sexuality == 'homo':
        person.setSpouseRelation(Parameters.spouseHomoSexualityMod)
    if person.getSpouse().sexuality == 'homo':
        person.getSpouse().setSpouseRelation(Parameters.spouseHomoSexualityMod)

    person.changeSpouseRelation(person.getSpouseNumberOfLikedTraits() * Parameters.spouseLikedTraitsMod)
    person.changeSpouseRelation(-person.getSpouseNumberOfDislikedTraits() * Parameters.spouseDislikedTraitsMod)
    person.getSpouse().changeSpouseRelation(person.getSpouse().getSpouseNumberOfLikedTraits() * Parameters.spouseLikedTraitsMod)
    person.getSpouse().changeSpouseRelation(-person.getSpouse().getSpouseNumberOfDislikedTraits() * Parameters.spouseDislikedTraitsMod)

def changeRelationFromLovemaking(person, lover):


    #TODO dorobić zmianę relacji
    return

def settlementsPopulationManagement (world):

    timeArray = []

    for region in world.getRegions():
        regionTimeArray = []
        for settlement in region.getSettlements():
            if world.getDay() == settlement.getMigrationDay() and world.getMonth() == settlement.getMigrationMonth():
                start1 = time.perf_counter()

                villagesList = SF.getVillages(region.getSettlements())
                townList = SF.getCities(region.getSettlements())

                #Treshhold to create migration wave
                if (len(settlement.getEmployedResidentsList()) + len(settlement.getUnemployedResidentsList())) > 0 and round(len(settlement.getUnemployedResidentsList()) / (len(settlement.getEmployedResidentsList()) + len(settlement.getUnemployedResidentsList())) * 100) > 15:
                # if settlement.getPopulation() >= int(settlement.getMaxPopulation() * Parameters.percentagePopulationThresholdForMigration):
                    chanceOfMigration = Utils.randomRange(1, 100)
                    #Chance of migration happening
                    if chanceOfMigration <= Parameters.chanceForMigration:
                        #Check for max size of region
                        if len(region.getSettlements()) == region.regionSize:
                            newTargetSettlement = Utils.randomFromCollection(region.getSettlements())

                        else:
                            # # TODO FIX PEOPLE CAN MOVE TO THE SAME VILLAGE
                            # #Take lowest population as dest
                            # lowestSettlementInRegion = region.getLowestPopulatedSettlement()
                            # newTargetSettlement = lowestSettlementInRegion
                            # #If lowest pop > lowest max pop * modifier create new setttlement
                            # if lowestSettlementInRegion.getPopulation() > int(lowestSettlementInRegion.getMaxPopulation() * Parameters.percentageVillagePopulationThresholdForCreatingNewVillage):
                                newSettlement = region.addSettlement(world)
                                newSettlement.setRegion(settlement.getRegion())
                                newSettlement.setMaxPopulation = Parameters.baseVillageSize
                                newTargetSettlement = newSettlement

                        #Migration Wave
                        complexRandomMigrantsList = prepareMigration(settlement, newTargetSettlement, world)
                        iniciateMigration(complexRandomMigrantsList, newTargetSettlement, world)
                        splitFamiliesInMigration(world, region, newTargetSettlement, complexRandomMigrantsList)
                end1 = time.perf_counter()
                start2 = time.perf_counter()
                #Upgrading from Village to City
                if len(villagesList) >= (len(townList)+1) * (Parameters.villageToTownMultiplier + 1) - len(townList):
                    randomVillage = Utils.randomFromCollection(villagesList)
                    if randomVillage.getPopulation() > int(randomVillage.getMaxPopulation() * Parameters.percentageVillagePopulationThresholdForUpgradeToTown):
                        chanceOfUpgradingToCity = Utils.randomRange(1, 100)
                        if chanceOfUpgradingToCity < Parameters.chancePerYearToUpgradeVillageToTown:
                            randomVillage.changeSettlementType(Settlements.TOWN)
                            Utils.randomFromCollection(randomVillage.getRegion().getVillagesExProvisionToThisTown(randomVillage)).setProvision(randomVillage)
                            Utils.randomFromCollection(randomVillage.getRegion().getVillagesExProvisionToThisTown(randomVillage)).setProvision(randomVillage)
                            Utils.randomFromCollection(randomVillage.getRegion().getVillagesExProvisionToThisTown(randomVillage)).setProvision(randomVillage)
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

    if world.dayOfWeekFlag == 1:  # Only on Monday produce goods
        for region in world.getRegions():

            for settlement in region.getSettlements():

                mayorModifier = 1


                ## ADMIN PROD
                if len(settlement.getAdminFeatures()[0].getWorkerList()) > 0:

                    # flat bonus 5% if mayor
                    mayorModifier = 1.05
                    mayor = settlement.getAdminFeatures()[0].getWorkerList()[0]

                    if Traits.LAZY in mayor.getTraits():
                        mayorModifier = 0.8
                    if Traits.DILIGENT in mayor.getTraits():
                        mayorModifier = 1.2
                    if Traits.GREEDY in mayor.getTraits():
                        mayorModifier = 0.9
                    if Traits.GREGARIOUS in mayor.getTraits():
                        mayorModifier = 1.1
                    if Traits.IMPATIENT in mayor.getTraits():
                        mayorModifier = 0.9
                    if Traits.PATIENT in mayor.getTraits():
                        mayorModifier = 1.1

                    flatRate = 3
                    if settlement.getAdminFeatures()[0].getName() == SFeat.getTownHall().getName():
                        flatRate = 5
                    mayor.changeFreeWealth(flatRate)
                    settlement.changeFreeWealth(-flatRate)

                ##  FOOD PRODUCTION
                foodProd0 = settlement.getSettlementFoodProduced()
                for foodTile in settlement.getFoodFeatures():

                    foodProd = foodTile.prodYield * foodTile.foundationType.value.yieldModifier * mayorModifier / 100 * foodTile.getWorkersNumber()

                    if settlement.getProvision() is not None:
                        settlement.getProvision().increaseSettlementFoodProduced(foodProd*Parameters.socage)
                        settlement.increaseSettlementFoodProduced(foodProd*(1-Parameters.socage))
                    else:
                        settlement.increaseSettlementFoodProduced(foodProd)

                    for worker in foodTile.getWorkerList():
                        if worker.getGeneralHealth().value[0] <= 1:  # Only Healthy or weaken can work
                            workerModifier = 0
                            if Traits.LAZY in worker.getTraits():
                                workerModifier = -10
                            if Traits.DILIGENT in worker.getTraits():
                                workerModifier = 10
                            if worker.getGeneralHealth().value[1] == 1:  # weaken workers work less
                                workerModifier = round(workerModifier / 2)
                            goodProduced = foodTile.prodYield * (foodTile.foundationType.value.yieldModifier + workerModifier) / 100
                            worker.changeFreeWealth(goodProduced * (100 - settlement.getLocalIncomeTax()) / 100)
                            settlement.changeFreeWealth(goodProduced * (settlement.getLocalIncomeTax()) / 100)

                foodProd1 = settlement.getSettlementFoodProduced()
                settlement.setSettlementFoodProducedLastYear(foodProd1-foodProd0)

                foodConsumed = 0
                for resident in settlement.getResidents():
                    if resident.getAge() < 10:
                        foodConsumed += 0.5
                        settlement.increaseSettlementFoodConsumed(0.5)
                    elif 10 <= resident.getAge() < 15:
                        foodConsumed += 0.75
                        settlement.increaseSettlementFoodConsumed(0.75)
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

                    prodProd = prodTile.prodYield * prodTile.foundationType.value.yieldModifier * mayorModifier / 100 * prodTile.getWorkersNumber()

                    if settlement.getProvision() is not None:
                        settlement.getProvision().increaseSettlementProdProduced(prodProd*Parameters.socage)
                        settlement.increaseSettlementProdProduced(prodProd*(1-Parameters.socage))
                    else:
                        settlement.increaseSettlementProdProduced(prodProd)
                    for worker in prodTile.getWorkerList():
                        if worker.getGeneralHealth().value[0] <= 1:
                            workerModifier = 0
                            if Traits.LAZY in worker.getTraits():
                                workerModifier = -10
                            if Traits.DILIGENT in worker.getTraits():
                                workerModifier = 10
                            if worker.getGeneralHealth().value[1] == 1:  # weaken workers work less
                                workerModifier = round(workerModifier / 2)
                            goodProduced = prodTile.prodYield * (prodTile.foundationType.value.yieldModifier + workerModifier) / 100
                            worker.changeFreeWealth(goodProduced * (100-settlement.getLocalIncomeTax())/100)
                            settlement.changeFreeWealth(goodProduced * (settlement.getLocalIncomeTax())/100)

                prodProd1 = settlement.getSettlementProdProduced()
                settlement.changeFreeProd(prodProd1 - prodProd0)
                settlement.setSettlementProdProducedLastYear(prodProd1 - prodProd0)


                #UPGRADING FEATURES

                if float(settlement.getFreeProd()) > 0:
    #                if settlement.getSettlementFoodProducedLastYear() - settlement.getSettlementFoodConsumedLastYear() < int(round(len(settlement.getResidents())/2)):
                        for tile in settlement.getFoodFeatures():
                            if len(SFeat.getPotencialUpgradesForZone(tile.getName())) > 0:
                                upgradable = Utils.randomFromCollectionWithWeight(SFeat.getPotencialUpgradesForZone(tile.getName()))
                                #for upgradable in (SFeat.getPotencialUpgradesForZone(tile.getName())):
                                if float(settlement.getFreeProd()) >= float(upgradable.value.getUpgradeCost()):
                                    settlement.changeFreeProd(-upgradable.value.getUpgradeCost())
                                    newFeature = SFeat.createZones()[SFeat.getFeatureIndexFromName(upgradable.value.getName())]
                                    settlement.upgradeTile(tile, newFeature, world)
                                    return

                        for tile in settlement.getProdFeatures():
                            if len(SFeat.getPotencialUpgradesForZone(tile.getName())) > 0:
                                upgradable = Utils.randomFromCollectionWithWeight(SFeat.getPotencialUpgradesForZone(tile.getName()))
        #                        for upgradable in (SFeat.getPotencialUpgradesForZone(tile.getName())):
                                if float(settlement.getFreeProd()) >= float(upgradable.value.getUpgradeCost()):
                                    settlement.changeFreeProd(-upgradable.value.getUpgradeCost())
                                    newFeature = SFeat.createZones()[SFeat.getFeatureIndexFromName(upgradable.value.getName())]
                                    settlement.upgradeTile(tile, newFeature, world)
                                    return


def accommodationManagment(world):

    if world.dayOfWeekFlag == 1:  # Only on Monday produce goods

        for region in world.getRegions():

            for settlement in region.getSettlements():

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

        for settlement in region.getSettlements():

            for employee in settlement.getEmployedResidentsList():

                for employeeSecond in settlement.getEmployedResidentsList():

                    if employeeSecond not in employee.getKnownAssociates() or employee != employeeSecond:

                        employee.addKnownAssociates(employeeSecond, 0)
                        employeeSecond.addKnownAssociates(employee, 0)



def settlementWorkersManagement(world):

    for region in world.getRegions():

        for settlement in region.getSettlements():

                basicAdminJobWeight = 5
                basicFoodJobWeight = 1
                basicProdJobWeight = 1

                unemployedWorkerList = settlement.getUnemployedResidentsList()
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
                    if basicAdminJobWeight + basicFoodJobWeight + basicProdJobWeight > 0:

                        for freeWorkPlace in range(numberOfFreeWorkplaces):
                            if len(unemployedWorkerList) == 0:
                                break
                            randomJobSite = Utils.randomRange(1, weightedAdminJobs + weightedFoodJobs + weightedProdJobs)
                            if len(adminFreeWorkplacesSpots) > 0 and randomJobSite <= weightedAdminJobs:
                                newWorker = Utils.randomFromCollection(unemployedWorkerList)
                                randomJob = Utils.randomRange(0, len(adminFreeWorkplacesSpots)-1)
                                hireEmployee(newWorker, adminFreeWorkplacesSpots[randomJob][0], world)
                                numberOfFreeWorkplaces -=1
                                unemployedWorkerList.remove(newWorker)
                                del adminFreeWorkplacesSpots[randomJob-1]
                            elif len(foodFreeWorkplacesSpots) > 0 and randomJobSite <= weightedAdminJobs + weightedFoodJobs:
                                newWorker = Utils.randomFromCollection(unemployedWorkerList)
                                randomJob = Utils.randomRange(0, len(foodFreeWorkplacesSpots)-1)
                                hireEmployee(newWorker, foodFreeWorkplacesSpots[randomJob][0], world)
                                numberOfFreeWorkplaces -= 1
                                unemployedWorkerList.remove(newWorker)
                                del foodFreeWorkplacesSpots[randomJob-1]
                            elif len(prodFreeWorkplacesSpots) > 0 and randomJobSite <= weightedAdminJobs + weightedFoodJobs + weightedProdJobs:
                                newWorker = Utils.randomFromCollection(unemployedWorkerList)
                                randomJob = Utils.randomRange(0, len(prodFreeWorkplacesSpots)-1)
                                hireEmployee(newWorker, prodFreeWorkplacesSpots[randomJob][0], world)
                                numberOfFreeWorkplaces -= 1
                                unemployedWorkerList.remove(newWorker)
                                del prodFreeWorkplacesSpots[randomJob-1]

                if settlement.getSettlementFoodProducedLastYear() <= 0:
                    fireAllEmployees(settlement.getAdminFeatures()[0], world)
                    fireAllEmployees(settlement.getProdFeatures()[0], world)


def hireEmployee(employee, tile, world):

    tile.addWorker(employee)
    employee.setOccupation(tile)
    employee.setOccupationName(tile.getOccupationName())
    PLEH.foundEmpoyment(employee, world)

    return

def fireAllEmployees(tile, world):

    for worker in tile.getWorkerList():
        worker.getOccupation().removeWorker(worker)
        worker.setOccupation(None)
        PLEH.lostEmpoyment(worker, world)

    return

def prepareMigration(settlement, newTargetSettlement, world):

    migrantFamilies = 0
    if settlement.getSettlementType() == Settlements.TOWN:
        mirgrationWave = Parameters.migrationWaveForTown
    else:
        mirgrationWave = Parameters.migrationWaveForVillage

    randomMigrantsList = []
    complexRandomMigrantList = []
    # random x people with their alive children move to new Village
    for migrantFamilies in range(mirgrationWave):
        randomPerson = Utils.randomFromCollection(settlement.getResidents())
        if randomPerson not in randomMigrantsList:
            # for MINOR
            if randomPerson.age < 15:
                getRandomMigrantListForSingleRandomPerson(randomPerson, "Father", randomMigrantsList, settlement, world)
                getRandomMigrantListForSingleRandomPerson(randomPerson, "Mother", randomMigrantsList, settlement, world)
            else:
                # for Adult
                getRandomMigrantListForSingleRandomPerson(randomPerson, "Adult", randomMigrantsList, settlement, world)
            if len(randomMigrantsList) > 0:
                complexRandomMigrantList.append(randomMigrantsList)
                migrantFamilies += 1
                randomMigrantsList = []


    return complexRandomMigrantList

def splitFamiliesInMigration(world, region, newTargetSettlement, complexRandomMigrantsList):


    for randomMigrantList in complexRandomMigrantsList:
        chanceOfChangingLastName = Utils.randomRange(1, 100)
        #won't change last name if only 1 person will be in migrant list whose culture sex is not to inherite
        if (chanceOfChangingLastName < Parameters.chanceForChangingLastNameDuringMigration and
                len(randomMigrantList) > 1 and
                randomMigrantList[0].familyObjRef.aliveMemberNumber > 1 and
                randomMigrantList[0].familyObjRef.getOriginCulture().getInheritanceBy() != randomMigrantList[0].sex):
            chanceForRevingAncestralFamily = Utils.randomRange(1, 100)

            if chanceForRevingAncestralFamily > 20:
                newFamilyName = FNG.getNewLastNameBasedOnRegion(region)
                family = Family(newFamilyName)
                family.setFoundingYear(world.getYear())
                family.setOriginRegion(region)
                family.setOriginSettlement(newTargetSettlement)
                family.setOriginCulture(randomMigrantList[0].familyObjRef.getOriginCulture())
                family.setFamilyBranchedFrom(randomMigrantList[0].familyObjRef)
                randomMigrantList[0].familyObjRef.addOffspringBranch(family)
                world.addFamily(family)
            else:
                ancestralFamilies = randomMigrantList[0].getAncestralFamilies()
                if len(ancestralFamilies) > 1:
                    ancestralFamilies.pop(0)
                    family = Utils.randomFromCollection(ancestralFamilies)
                    newFamilyName = family.getFamilyName()
                else:
                    newFamilyName = FNG.getNewLastNameBasedOnRegion(region)
                    family = Family(newFamilyName)
                    family.setFoundingYear(world.getYear())
                    family.setOriginRegion(region)
                    family.setOriginSettlement(newTargetSettlement)
                    family.setOriginCulture(randomMigrantList[0].familyObjRef.getOriginCulture())
                    family.setFamilyBranchedFrom(randomMigrantList[0].familyObjRef)
                    randomMigrantList[0].familyObjRef.addOffspringBranch(family)
                    world.addFamily(family)

            newHouse = HouseFunctions.getNewHouse()
            newTargetSettlement.buildNewHouse(newHouse)
            HouseFunctions.setHouseDurability(newHouse, Utils.randomRange(60, 90))

            for person in randomMigrantList:

                person.getAccommodation().removeHouseResident(person)
                HouseFunctions.setNewHouseToPerson(person, newHouse)
                newHouse.addHouseResident(person)

                person.familyObjRef.removeFromFamily(person)
                person.familyName = newFamilyName
                person.lastName = newFamilyName
                person.familyObjRef = family
                person.setOriginFamilyObjectRef(family)
                if family.getFemaleNumber() == 0 and family.getMaleNumber() == 0:
                    family.setFoundedBy(person)
                    #HouseFunctions.addNewOwner(person, newHouse)
                family.addNewMember(person)
                PLEH.changedLastName(person, world, person.getFamilyName())

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
                    loot = randomPerson.getFreeWealth()
                    randomPerson.setFreeWealth(loot / 2)
                    person.changeFreeWealth(loot)
                    crimeLevel += 1
                    crimeHomicideTemp += 1
                    continue
                if randomCrime < 30:
                    # print("Assault")
                    loot = randomPerson.getFreeWealth()
                    randomPerson.setFreeWealth(loot / 3)
                    person.changeFreeWealth(loot)
                    crimeLevel += 1
                    crimeAssaultTemp += 1
                    continue
                if randomCrime < 70:
                    # print("Burglary")
                    loot = randomPerson.getFreeWealth()
                    randomPerson.setFreeWealth(loot / 4)
                    person.changeFreeWealth(loot)
                    crimeLevel += 1
                    crimeBurglaryTemp += 1
                    continue
                if randomCrime < 90:
                    # print("Theft")
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

def iniciateMigration(complexMigrantList, settlementTarget, world):

    for migrantList in complexMigrantList:
        for migrant in migrantList:
            PLEH.movedHome(migrant, migrant.getSettlement(), settlementTarget, world)
            migrant.getSettlement().decreasePopulation()
            migrant.getSettlement().removeResident(migrant)
            migrant.setSettlement(settlementTarget)
            settlementTarget.increasePopulation()
            settlementTarget.addResident(migrant)
            FF.fireSingleEmployee(migrant, world)


def getRandomMigrantListForSingleRandomPerson(person, parent, randomMigrantsList, settlement, world):

    getParent = ''
    if person.getFather() is not None and person.getFather() != '' and person.getFather().lifeStatus != LifeStatus.DEAD:
        if parent == "Father":
            getParent = person.getFather()
    if person.getFather() is not None and person.getMother() != '' and person.getMother().lifeStatus != LifeStatus.DEAD:
        if parent == "Mother":
            getParent = person.getMother()
    if parent == "Adult":
        getParent = person

    if getParent != '':
        if getParent not in randomMigrantsList:
            # if newLastName != '':
            #     getParent.lastName = newLastName
            randomMigrantsList.append(getParent)

        parentChildrensList = getParent.getAliveChildrenList()
        for parentChildren in parentChildrensList:
            if parentChildren.age < 15:
                if parentChildren not in randomMigrantsList:
                    randomMigrantsList.append(parentChildren)
                    #PLEH.movedHome(parentChildren, settlement, world)

        if getParent.spouse is not None:
            if getParent.spouse not in randomMigrantsList:
                randomMigrantsList.append(getParent.spouse)
                #PLEH.movedHome(getParent.spouse, settlement, world)
                # if newLastName != '':
                #     getParent.lastName = newLastName

            parentSpouseChildrensList = getParent.spouse.aliveChildren
            for parentSpouseChildren in parentSpouseChildrensList:
                if parentSpouseChildren.age < 15:
                    if parentSpouseChildren not in randomMigrantsList:
                        randomMigrantsList.append(parentSpouseChildren)
                        #PLEH.movedHome(parentSpouseChildren, settlement, world)
                        # if newLastName != '':
                        #     getParent.lastName = newLastName




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

def assosiatesFriendsAndFoes(world):

    for region in world.getRegions():
        for settlement in region.getSettlements():
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
                                PLEH.gotFriend(person, fellowEmployee, world)
                            if person not in fellowEmployee.getFriends():
                                fellowEmployee.addFriends(person)
                                PLEH.gotFriend(fellowEmployee, person, world)

                        person1DislikenessIndicatorForPerson2 = Utils.checkForDislikedTraisInPerson2(person, fellowEmployee)
                        person2DislikenessIndicatorForPerson1 = Utils.checkForDislikedTraisInPerson2(fellowEmployee, person)
                        if person1DislikenessIndicatorForPerson2 > 0 and person2DislikenessIndicatorForPerson1 > 0:
                            if fellowEmployee not in person.getFriends():
                                person.addRivals(fellowEmployee)
                                PLEH.gotRival(person, fellowEmployee, world)
                            if person not in fellowEmployee.getFriends():
                                fellowEmployee.addRivals(person)
                                PLEH.gotRival(fellowEmployee, person, world)




