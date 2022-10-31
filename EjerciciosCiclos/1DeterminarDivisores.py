#Determinar los divisores de un numero introducido por teclado.

x = int(input("Digite el numero: ")) #Lectura del numero

cont=0 #Contador iniciado en cero para evitar errores
for i in range (1,x+1): 
    if x%i==0:
        print(i) #Imprime los numeros divisores del numero digitado
        cont=cont+1 #Para contar los divisores
print("Los numeros divisores del",x,"son:",cont,"")