def errorcito():

    numeritos = [2, 8, 3, 6, 4]

    try:
        posicion = numeritos[10] #Intentando acceder a la posicion 10 de la lista

    except LookupError as excepcion: #Tomamos la excepcion LookupError y guardamos la variable excepcion
        print("Se encontro un error al buscar esta posicion: ",excepcion)
        
    else: #Si la excepcion no se da, se ejecuta la condicion else
        print("El numero en esa posicion es: ",posicion)

errorcito()