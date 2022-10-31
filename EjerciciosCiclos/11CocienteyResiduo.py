n1 = int(input("Digite el primer numero: "))
n2 = int(input("Digite el segundo numero: "))
n3 = n1
cociente=0
if n2>n1:
	n1=n2
	n2=n3
while n1>=n2:
	n1-=n2
	cociente+=1
print("El cociente es el numero",cociente,"y el residuo es",n1)