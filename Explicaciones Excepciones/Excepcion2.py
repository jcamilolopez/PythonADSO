values = (1, 0) #Tupla con dos valores
#x,y=10,12
#print(divmod(10,3))
try: #Dentro del bloque try colocamos el codigo que queremos verificar si tiene un error
    q, r = divmod(*values) #Dos variables a que se les asigna el valor de la variable values y con el * le agregamos vamos valores de la tupla, de acuerdo a la posicion. Con la funcion divmod, nos devuelve en tupla el divisor y el residuo de la division de las variables q y r
    #print('valor de q=',q)
    print(f'q={q}') #Esta forma de imprimir nos permite combinar cadenas con variables, colocando la variable q entre llaves
    print(f'r={r}') #Esta forma de imprimir nos permite combinar cadenas con variables, colocando la variable r entre llaves
except (ZeroDivisionError, TypeError) as e: #Verificar si se da alguno de los errores que especificamos dnetro de los parentesis y luego de darse alguno de los dos errores se guarda en a nueva variable que nombramos 'e'
    print(type(e), e) #Imprime el tipo de error en la variable 'e' con la funcion type(), y ademas imprime el error especifico que se dio 
