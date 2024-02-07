'''Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.'''

# Solicitar al usuario un número
numeros =[1,2,3,4,5]

# Imprimir la tabla de multiplicar
for numero in numeros:
    print(f"\nTabla de multiplicar del {numero}:\n")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
