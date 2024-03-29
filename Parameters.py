startingSettlementsPerProvince = 2
startingNumberOfFamiliesPerRegion = 10
startingNumberOfRegions = 5
startingYear = 499
baseCitySize = 1000
baseVillageSize = 300
baseCityFertility = 0.9
baseVillageFertility = 1
percentagePopulationThresholdForMigration = 0.5
percentageVillagePopulationThresholdForCreatingNewVillage = 0.4
percentageVillagePopulationThresholdForUpgradeToTown = 0.75
chancePerYearToUpgradeVillageToTown = 80
chanceForMigration = 5
provincesPerRegion = 5

#growthAccelerationForKidsUpToAdulthood
growthSpeed = 0 #default 0

settlementHighFoodFertilityModifier = 1.2   #default 1.2
settlementNormalFoodFertilityModifier = 1.0 #default 1.0
settlementLowFoodFertilityModifier = 0.33   #default 0.33

# aka how many village per town there must be
villageToTownMultiplier = 3
migrationWaveForTown = 5
migrationWaveForVillage = 7

chanceForChangingLastNameDuringMigration = 25  # aka 5% to chance create new branch family

provinceSizeMin = 4
provinceSizeMax = 4

# socage -> % production to homeTown TODO _ FIXFIXFIX
socage = 0

#spouse relations modifiers
spouseLikedTraitsMod = 1
spouseDislikedTraitsMod = -1
spouseHomoSexualityMod = -1

# Graph data
globalPopulation = ['Global Population', '#eeaaaa']
globalPopulationArray = [globalPopulation]

crime = ['All Crimes', '#000000']
crimeHomicide = ['Homicide', '#ee2222']
crimeAssault = ['Assault', '#A36405']
crimeBurglary = ['Burglary', '#FFD700']
crimeTheft = ['Theft', '#119999']
crimeFailed = ['Crime Failed', '#666666']
crimeColorArray = [crime, crimeHomicide, crimeAssault, crimeBurglary, crimeTheft, crimeFailed]

deadColor = ['Deaths', '#000000']
aliveColor = ['Births', '#336600']
birthsDeathsColorArray = [deadColor, aliveColor]

eyeColorBlack = ['Black', '#000000']
eyeColorBrown = ['Brown', '#542604']
eyeColorAmber = ['Amber', '#A36405']
eyeColorHazel = ['Hazel', '#DA8F1E']
eyeColorGreen = ['Green', '#336600']
eyeColorBlue = ['Blue', '#000099']
eyeColorGray = ['Gray', '#666666']

eyeColorArray = [eyeColorBlack, eyeColorBrown, eyeColorAmber, eyeColorHazel, eyeColorGreen, eyeColorBlue, eyeColorGray]

hairColorBlack = ['Black', '#000000']
hairColorBrown = ['Brown', '#542604']
hairColorYellow = ['Yellow', '#FFD700']
hairColorRed = ['Red', '#B22222']
hairColorWhite = ['White', '#FFFAF0']
hairColorGray = ['Gray', '#666666']

hairColorArray = [hairColorBlack, hairColorBrown, hairColorYellow, hairColorRed, hairColorWhite, hairColorGray]

sexualityHetero = ['Hetero', '#000099']
sexualityHomo = ['Homo', '#666666']
sexualityColorArray = [sexualityHetero, sexualityHomo]

averageHeight = ['Average Height', '#A36405']
averageMHeight = ['Average Male Height', '#000099']
averageFHeight = ['Average Female Height', '#B22222']
averageHeightColorArray = [averageHeight, averageMHeight, averageFHeight]

regionColors0 = ["#009999"]
regionColors1 = ["#990099"]
regionColors2 = ["#999900"]
regionColorArray = [regionColors0, regionColors1, regionColors2]
