hora=int(input("Digite la hora:"))
min=int(input("Digite los minutos:"))
seg=int(input("ingrese los segundos:"))+1
if seg<61 and min<60 and hora<24:
    if seg>=59:
        seg=0
        min += 1
    if min>=59:
        min=0
        hora+=1
    if hora>23:
        hora=1
    print("La hora ingresada es",hora,":",min,":",seg)
else:
    print("El valor no es correcto, por favor ingrese un valor correcto")