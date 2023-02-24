def try_syntax(numerator, denominator): #Definimos una funcion con dos parametros
    try: #Dentro del try se verifica un bloque de codigo para saber si contiene un error
        print(f'In the try block: {numerator}/{denominator}') #Nos permite imprimir combinando cadena con variables que se encuentran dentro de las llaves, en este caso se imprimiran los parametros que se le den a a funcion.
        #quiero ver el resultado de la operacion en el print
        result = numerator / denominator #Variable en la que se quiere dividir entre los parametros que se le dan a la funcion
    except ZeroDivisionError as zde: #Verificamos si se da el error especificado 'ZeroDivisionError' y guardar este error en la nueva variable llamada 'zde'
        print(zde) #En caso tal de que se de el error, se imprime la variable en la que se guarda el error 'zde'
    else: #En caso de no darse el error se cumpliria esta condicion
        print('The result is:', result) #Si no se cumple error entonces imprime la cadena y el resultado de la operacion en la variable 'result'
        return result #Retorna el valor de la variable 'result'
    finally: #Sirve para finalizar un bloque try y las excepciones
        print('Exiting') #Al finalizarlo indicamos que queremos imprimir la cadena que especificamos
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 5)) #Imprime la funcion y le pasamos los valores de los parametros