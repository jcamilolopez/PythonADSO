from re import X

x = int(input("Digite el valor de la base: "))
y = int(input("Digite el valor del exponente: "))

i=1
poten = x

while(i<y):
    i+=1
    poten*=x
if y<=0:
    poten=1
print(poten)
