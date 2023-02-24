def division(num1, num2):
    assert num2 != 0, "No se puede dividir entre cero" #La condicion valida si el numero es 0, si no se cumple aparece el error
    return num1 / num2

try: #Bloque para intentar ejecutar la funcion y tomar la excepcion que se genera
    rta = division(10, 0)
except AssertionError as excepcion: #Si se produce la excepcion se almacena en la variable excepcion
    print("Ocurrio un error: ",excepcion)
else: #Si no se da una excepcion se ejecuta la condicion else
    print("El resultado es: ",rta)

var = 1
print(type(var))