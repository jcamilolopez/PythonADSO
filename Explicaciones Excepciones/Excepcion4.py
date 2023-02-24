def edad(): #Definimos una funcion llamada 'edad'
    try: #Dentro del try colocamos el bloque de codigo que queremos verificar si tiene un error
        tuedad=int(input("introduce tu edad")) #En la variable pedimos que se ingrese desde teclado un numero entero
        print(f'tu edad es  {tuedad}') #Imprime combinando la cadena con la variable 'tuedad' que esta entre llaves 
        #print('Tu edad es ',tuedad)
    except ValueError as e: #Verificamos si se da el error que especificamos 'ValueError' y guarda el error dentro de la nueva variable 'e'
        print(e) #Si se da el error imprime la variable 'e', que es donde se guardo el error
        print("La edad debe ser un valor numerico...") #Imprimimos la cadena que especificamos
        edad() #Se hace llamado de la funcion dentro de la funcion para que sea recursiva. Con esto se seguira ejecutando la funcion hasta que se de un valor valido
    
edad() #Llamado de la funcion