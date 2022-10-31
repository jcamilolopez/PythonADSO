n = 0
cont = 0
while(n>=0):
    n = int(input("Ingrese los numeros positivos: \n"))
    if n>=0:
        cont+=1
    else:
        print("Se contaron la siguiente cantidad de numeros positivos",cont)