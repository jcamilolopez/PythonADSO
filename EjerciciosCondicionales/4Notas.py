#4. Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien,
#etc. Use la escala que prefiera, pero cerciórese que tiene 5 valores

valor_nota = int(input("Ingrese el valor de la nota: "))

if(valor_nota >= 0 and valor_nota < 2):
    print("El valor de su nota es: Insuficiente")
elif(valor_nota >= 2 and valor_nota < 4):
    print("El valor de su nota es: Suficiente")
elif(valor_nota >= 4 and valor_nota < 6):
    print("El valor de su nota es: Bien")
elif(valor_nota >= 6 and valor_nota < 8):
    print("El valor de su nota es: Sobresaliente")
elif(valor_nota >= 8 and valor_nota < 10):
    print("El valor de su nota es: Perfecta")
else:
    print("Dato ingresado es erroneo")