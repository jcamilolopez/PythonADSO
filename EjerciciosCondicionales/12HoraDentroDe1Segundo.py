hora=int(input("Digite la hora: "))
min=int(input("Digite los numeros: "))
seg=int(input("Digite los segundos: "))+1
if seg<61 and min<60 and hora<13:
    if seg>=60:
        seg=0
        min += 1
    if min>=60:
        min=0
        hora+=1
    if hora>12:
        hora=1
    print("La hora es",hora,":",min,":",seg)
else:
    print("El valor es erroneo. Digite un valor valido")