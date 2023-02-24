def cifrar(mensaje):
    alfabeto_original = "abcdefghijklmnopqrstuvwxyz" 
    alfabeto_cifrado = "defghijklmnopqrstuvwxyzabc" 
    
    mensaje_cifrado = "" #Variable en la que se almacena el mensaje cifrado
    
    for letra in mensaje:
        
        if letra.isalpha(): #Condicion que verifica si la letra es letra xd
            indice = alfabeto_original.find(letra.lower()) #find para conseguir el indice de la letra del alfabeto. Lower para convertir en minuscula las letras de la frase
            nueva_letra = alfabeto_cifrado[indice] #Del indice del codigo anterior, obtenemos la letra correspondiente el alfabeto cifrado
            
            if letra.isupper(): #Si la letra del alfabeto comun es mayuscula
                nueva_letra = nueva_letra.upper() #Convertimos la letra del cifrado en mayuscula
        else:
            nueva_letra = letra #Si el caracter no es letra lo dejamos tal cual en el mensaje cifrado
        mensaje_cifrado += nueva_letra #Agregamos la letra cifrada a la frase cifrada
    
    return mensaje_cifrado

mensaje_original = input("Ingrese aqui una frase: ")
print()
mensaje_cifrado = cifrar(mensaje_original)
print()
print("Mensaje cifrado:", mensaje_cifrado)
print()
print("Mensaje original:", mensaje_original)
