def lecturaDeFrase(frase):

    vocalConTildes = 'áéíóú'

    vocal = 0
    tildes = 0
    consonante = 0
    especial = 0

    for letras in frase:
        if letras.isalpha(): #isalpha() mira si una cadena solo contiene letras
            if letras in 'aeiou':
                vocal += 1
            elif letras in vocalConTildes:
                vocal += 1
                tildes += 1
            else:
                consonante += 1
        else:
            especial += 1

    print("La frase que ingreso "+frase+":"+" Tiene "+str(vocal)+" vocales, "+str(consonante)+" consonantes, "+str(tildes)," vocales con tilde,\n "+str(especial)," caracteres especiales")

lecturaDeFrase("Hola")