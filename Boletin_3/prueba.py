'''Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre él mismo y la unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.'''

numero = int(input("Introduce un número: "))

for i in range(2, numero): 
    
    if numero % i == 0:
        print(numero, "no es primo")
        break
    
    if i == numero - 1:
        print(numero, "es primo")

        