def mi_funcion(num1,num2):#se nombra una funcion y dentro de su parentesis se le añade dos parametros
    try:##try anlizara el codigo que se ingrese y si encuentra algun error comenzara a ejecutarse sus excepciones
        respueta=num1+num2#en esta variable se encuentra la operacion
    except TypeError:#se llama el tipo de excepcion que es TypeError    
        print("el valor debe ser un numero ")#imprime este texto si se encuentra esta excepcion
    else:# si no se encuentra el error 
        print("si se nombre la funcion que la imprima")#imprime este texto si no se encuentra esta excepcion
        print(respueta)#imprime la variable en donde se encuentra la operacion
mi_funcion(4,0.9)#se llama la funcion y se le ponen sus parametros