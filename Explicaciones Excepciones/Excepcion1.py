try: #Dentro del bloque try colocamos el codigo que queremos verificar si tiene un error
    #print(1/1)
    raise SyntaxError #Llamamos un error, especificamente el que indicamos, el cual es SyntaxisError
except SyntaxError as e: #Para verificar si existe el error SyntaxisError y le decimos que guarde el error en la nueva variable 'e'
    print(e) #Si existe el error se imprime la variable 'e' donde esta guardado el error
    print('Cierra el parentesis') #Si se da el error nos imprime la cadena que le especificamos
    
try: 
    #raise ZeroDivisionError
    print(1/0) #Tratamos de imprimir una division entre 0
#except (ZeroDivisionError) as e: #Se hizo comentario porque no tiene un codigo especifico que ejecutar si se da el error
except ZeroDivisionError as zde: #Para verificar si se da el error ZeroDivisionError y el error guardarlo en la nueva variable 'zde'
    print(zde) #Imprime el error que se dio dentro del bloque de codigo
    #print('prueba error')