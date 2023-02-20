def tipo_palabra():

    a=input('Por favor, escriba una palabra: ')

    if chr(225) in a or chr(233) in a or chr(237) in a or chr(243) in a or chr(250) in a:

        for i in a[-2:]:
            if chr(225) in i or chr(233) in i or chr(237) in i or chr(243) in i or chr(250) in i:
                return('Aguda')
            else:
                continue

        for i in a[-4:-2]:
            if chr(225) in i or chr(233) in i or chr(237) in i or chr(243) in i or chr(250) in i:
                return('Grave')
            else:
                continue

        for i in a[-7:-4]:
            if chr(225) in i or chr(233) in i or chr(237) in i or chr(243) in i or chr(250) in i:
                return('Esdrujula')
            else:
                continue

        for i in a[:-7]:
            if chr(225) in i or chr(233) in i or chr(237) in i or chr(243) in i or chr(250) in i:
                return('Sobreesdujula')

    else:
        return('esta palabra no tiene tilde')

print(tipo_palabra())