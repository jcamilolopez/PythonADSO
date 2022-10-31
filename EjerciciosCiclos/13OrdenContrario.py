x=0
num=int(input('Digite el numero: '))

while num != 0:
    c=num%10
    x=x*10+c
    num //= 10
    
print(x)