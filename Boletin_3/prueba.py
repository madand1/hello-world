'''Escribe un programa que diga si un número introducido por teclado es o no primo. 
Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.'''


n = int(input("Ingrese un número: "))

for i in range(2, n + 1):
    if n % i != 0:
        print(n, "no es primo")
        

    else:
        print(n, "es primo")
        



