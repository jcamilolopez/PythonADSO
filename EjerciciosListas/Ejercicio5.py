import random

vector=[]
rango=random.randint(10,25)
cont=0
posicion=" "
for i in range(rango):
	vector.append(round(random.random()*100))
print(vector)
numero = int(input("Digite un numero: "))
for i in range(rango):
	if numero==vector[i]:
		posicion+=str(i)+" "
		cont+=1
if cont==0:
	vector.append(numero)
	print("El numero se ha agregado al final de la lista")
	print(vector)
else:
	if cont==1:
		print("El numero de la lista",numero,"esta una vez y se encuentra en la posicion",posicion)
	else:
		print("El numero de la lista",numero,"esta",cont,"veces y esta en las posiciones",posicion)