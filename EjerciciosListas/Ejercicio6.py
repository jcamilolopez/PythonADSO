import random

vector=[]
aux=True
a=0
b=1
c=1
while aux:
	rango=int(input("Ingrese la cantidad de elementos a usar en la serie de Fibonacci: "))
	if rango>=5 and rango<=20:
		aux=False
	else:
		print("Deben ser minimo 5 elementos y maximo 20 elementos")
for i in range(rango):
	c=a+b
	a=b
	b=c
	vector.append(c)
print("La lista con los valores de Fibonacci hasta la posicion insertada es: ",vector)