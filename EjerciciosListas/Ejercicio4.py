import random

vector=[]
rango=random.randint(10,25)
for i in range(rango):
	vector.append(round(random.random()*100))
print("La lista sin ordenar es:",vector)
cambio=True
while cambio:
	cambio=False
	for i in range(len(vector)-1):
		if vector[i]>vector[i+1]:
			vector[i],vector[i+1]=vector[i+1],vector[i]
			cambio=True

print("La lista ordenada es: ",vector)