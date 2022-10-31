for n in range(1,1000):
    i=1
    cont=0
    while(n > i):
        if n%i ==0:
            cont+=i
        i+=1
    if n == cont:
        print("El numero",n," es un numero perfecto")
