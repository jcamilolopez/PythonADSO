maximo=int(input("Digite el valor del dato maximo: "))
x = 0
cont = 0
suma = 0
while(suma<maximo):
    x+=1
    suma=0
    for i in range(0,x+1):
        suma+=1

print(x,"Es el minimo numero natural solicitado para sobre pasar el dato maximo")