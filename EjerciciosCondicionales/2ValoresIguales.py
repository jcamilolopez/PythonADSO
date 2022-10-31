#2. Escribe un programa que pida tres números y que escriba si son los tres
#iguales, si hay dos iguales o si son los tres distintos

x = int(input("Agregue el primer numero: "))
y = int(input("Agregue el segundo numero: "))
z = int(input("Agregue el tercer numero: "))

if x==y==z:
    print("Los tres numeros son del mismo valor")
elif x==y or x==z or y==z:
    print("Hay dos valores del mismo valor")
else:
    print("Todos los valores son diferentes")