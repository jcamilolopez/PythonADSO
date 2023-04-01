from Oscar import *
import csv

listaGanadores = []
with open('C:\\Users\\SENA\\Desktop\\Proces_archivo\\oscars_male.csv') as ganadores:

    csvReader = csv.reader(ganadores)

    for i in csvReader:
        ob = Oscar(i[0],i[1],i[2],i[3],i[4])
        #print(i)
        listaGanadores.append(ob)

print(listaGanadores)

for oscars in listaGanadores:
    print(oscars.getName())

print(listaGanadores[1])


listaGanadoras = []
with open('C:\\Users\\SENA\\Desktop\\Proces_archivo\\oscars_female.csv') as ganadoras:
    csvReader = csv.reader(ganadoras)

    for i in csvReader:
        ob = Oscar(i[0],i[1],i[2],i[3],i[4])
        #print(i)
        listaGanadoras.append(ob)

print(listaGanadores)

for oscars in listaGanadoras:
    print(oscars.getName())
print(listaGanadores[1])
