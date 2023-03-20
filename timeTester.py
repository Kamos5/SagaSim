import main

howManyLoops = 10
population = 2000

f = open("times.txt", "a")
f.write('Population:' + str(population))
f.write('\n')
f.close()

for i in range(howManyLoops):
    f = open("times.txt", "a")
    for data in main.callMain(population):
        f.write(str(data) + '; ')
    f.write('\n')
    f.close()