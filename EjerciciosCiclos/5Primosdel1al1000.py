n = 1 #Iniciamos variable en 1
while n <=100:
    cont =1 
    x=0 
    while cont <= n:
        if n % cont == 0: #Si el residuo es cero, se contabilizara
            x=x+1 #Incremento de variable
        cont = cont +1 #Incrementar la variable
    if x==2: #Si se cumple el numero es primo
        print(n)

    n = n + 1