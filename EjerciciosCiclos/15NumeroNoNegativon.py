num=int(input("Digite el numero no negativo n: "))
nu=num+1
if num > 0:
    while nu>0:
        for i in range(1,nu):
            print(i,end='')
        nu-=1
        print()
else:
    print("El valor no se encuentra dentro de nuestros datos")