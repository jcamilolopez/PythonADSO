#Determinar si un numero es o no es primo

x = int(input("Digite el numero: ")) #Lectura del numero
y = 1
z = 0

while y <= x: #Ciclo mientras la condicion se cumpla 
    if x%y == 0: #Condicion determina si el resultado de la dividision da como residuo cero
        z = z + 1 #Se cuentan las divisiones que dan residuo cero
    y = y + 1 #Aumento de la variable para dar movimiento al ciclo y no sea infinito
if z == 2: 
    print("El numero",x,", es un numero primo")
else: #Si el numero no tiene dos divisores, no es primo
    print("El numero",x,", no es un numero primo")
