#1. Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el
#valor del medio es 11. No use operadores lógicos

x = int(input("Ingrese el primer numero: "))
y = int(input("Ingrese el segundo numero: "))
z = int(input("Ingrese el tercer numero: "))

minimo = min(x, y, z)
maximo = max(x, y, z)
valormedio = (x + y + z) - minimo - maximo

print(minimo, valormedio, maximo)
print("El valor medio de los tres numeros es: ", valormedio)
