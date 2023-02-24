def operacion(a,b):#se nombra una funcion y dentro de su parentesis se le añade dos parametros
    try:##try anlizara el codigo que se ingrese y si encuentra algun error comenzara a ejecutarse sus excepciones
        resultado=a**b#en esta variable se encuentra la operacion
    except OverflowError:#se llama el tipo de excepcion que es overflower
        print("overflower: no se puede realizar la operacion")##imprime este texto si se encuentra esta excepcion
    else:# si no se encuentra el error 
        print(f"el resultado es: {resultado}")#imprime la variable en donde se encuentra la operacion
operacion(25.6,2)#se llama la funcion y se le ponen sus parametros