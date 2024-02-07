'''Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.'''

# Solicitar al usuario dos números
inicio = int(input("Introduce el primer número: "))
fin = int(input("Introduce el segundo número: "))

# Asegurarse de que el primer número sea menor o igual al segundo
if inicio > fin:
    inicio, fin = fin, inicio

# Imprimir todos los números pares entre los dos números
print(f"\nNúmeros pares entre {inicio} y {fin}:")
for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        print(numero)

