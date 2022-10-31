n1=int(input("Digite el primer numero: "))
n2=int(input("Digite el segundo numero: "))
while not(n2==0):
	a=n1
	b=n2
	if n1<0:
		n1=-a
		n2=b
	if n2<0:
		n1=a
		n2=-b
	else:
		n1=b
		n2=a%b
print(n1)
