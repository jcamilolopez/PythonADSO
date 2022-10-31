#Determinar si un número es o no es perfecto.

x = int(input("Digite el numero: ")) #Lectura del valor

y = 1 #Inicia desde uno, porque una division entre cero es erronea

acumu = 0

while(y<x):
    if x%y==0: #Si el residuo es cero, 'y' es un divisor propio del numero
        acumu = acumu+y #El numero 'y' se va sumando en el acumulador
    y = y+1 #Contador para que no sea un ciclo infinito
    
if acumu==x: 
    print("El numero es perfecto")
else:
    print("El numero no es perfecto")
