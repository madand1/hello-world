'''Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

'''

# Solicitar al usuario un número
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

# Imprimir la tabla de multiplicar
print(f"\nTabla de multiplicar del {numero}:\n")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
