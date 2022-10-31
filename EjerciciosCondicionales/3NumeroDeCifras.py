#3. Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el número
#exceda los límites emita un mensaje y finalice el programa

x = int(input("Ingrese el numero: "))

if(x<0 or x>99999):
      print("El numero digitado es erroneo")
else:
    if(x<10):
        print("El numero cuenta con 1 cifra")
    elif(x<100):
        print("El numero cuenta con 2 cifras")
    elif(x<1000):
        print("El numero cuenta con 3 cifras")
    elif(x<10000):
        print("El numero cuenta con 4 cifras")
    elif(x<100000):
        print("El numero cuenta con 5 cifras")