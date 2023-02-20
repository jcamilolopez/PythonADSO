#Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez
def cadena():
    cadena = "aaabcdefghijklmnñopqrstuvxyz"
    caracteres = len(cadena)
    print(caracteres)
#cadena()

def repetidas():
        print("aaabcdefghijklmnñopqrstuvxyz".count("a"))
#repetidas()

#pida una cadena por teclado y diga cual es su valor al sumar sus codigos
"""def cadena():
    cadena = input("Ingrse el nombre que le quiere dar a la cadena: ")
for caracter in cadena:
    suma_codigos = 0
    suma_codigos += ord(caracter)
    print("La suma de los codigos de caracteres de la cadena es:", suma_codigos)"""
#cadena()

#Cual es el valor numerico de acuerdo a los códigos del alfabeto
def valor_letra(letra):
    if letra.isupper():
        valor = ord(letra) - ord('A') + 1
    elif letra.islower():
        valor = ord(letra) - ord('a') + 1
    else:
        valor = None
    return valor

def valornumerico():
    valor = "a"
    valor2 = "b"
    print(ord(valor))
    print(ord(valor2))
#valornumerico()

#Solicite cadena e imprimala en todas las formas posibles en cuanto a mayusculas y minusculas

def cadena():
    cadena = input("Ingrese una palabra o frase: ")
    print("La cadena en mayusculas es", cadena.upper())
    print("La cadena en minusculas es", cadena.lower())
    print("Cadena en forma de titulo", cadena.title())
#cadena()

# cuantas veces se repite un caracter dado
def cadena(letra):
    cadena = "mamá"  
caracter = "a"
contador = 0
for letra in cadena:
        if letra == caracter:
            contador += 1
#print(f"El carácter '{caracter}' aparece {contador} veces en la cadena '{cadena}'.")
