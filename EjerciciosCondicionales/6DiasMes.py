dia_año = int(input("Ingrese el dia del año: "))

if(dia_año >= 1 and dia_año <=31):
    print("El dia",dia_año,"del año, es del mes de enero")
elif(dia_año >= 32 and dia_año <=59):
    print("El dia",dia_año,"del año, es del mes de febrero")
elif(dia_año >= 60 and dia_año <=90): #Este mes tiene 31 dias
    print("El dia",dia_año,"del año, es del mes de marzo")
elif(dia_año >= 91 and dia_año <=120): #Este mes tiene 30 dias
    print("El dia",dia_año,"del año, es del mes de abril")
elif(dia_año >= 121 and dia_año <=151): #Este mes tiene 31 dias
    print("El dia",dia_año,"del año, es del mes de mayo")
elif(dia_año >= 152 and dia_año <=181): #Este mes tiene 30 dias
    print("El dia",dia_año,"del año, es del mes de junio")
elif(dia_año >= 182 and dia_año <=212):
    print("El dia",dia_año,"del año, es del mes de julio")
elif(dia_año >= 213 and dia_año <=243):
    print("El dia",dia_año,"del año, es del mes de agosto")
elif(dia_año >= 244 and dia_año <=273):
    print("El dia",dia_año,"del año, es del mes de septiembre")
elif(dia_año >= 274 and dia_año <=304):
    print("El dia",dia_año,"del año, es del mes de octubre")
elif(dia_año >= 305 and dia_año <=334):
    print("El dia",dia_año,"del año, es del mes de noviembre")
elif(dia_año >= 335 and dia_año <=365):
    print("El dia",dia_año,"del año, es del mes de diciembre")
else:
    print("El valor ingresado es erroneo")
