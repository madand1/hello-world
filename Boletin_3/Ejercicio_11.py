#Ejercicio 11

'''Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre él mismo y la unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.'''

import math

# Solicitar al usuario un número
numero = int(input("Introduce un número para verificar si es primo: "))

# Verificar si el número es primo
es_primo = True

# No hay necesidad de verificar números mayores que la raíz cuadrada del número
limite_superior = int(math.sqrt(numero)) + 1

# Un número primo solo es divisible por él mismo y la unidad
divisor = 2
while divisor < limite_superior:
    if numero % divisor == 0:
        es_primo = False
    divisor += 1

# Imprimir el resultado
if es_primo and numero > 1:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")




        
    




