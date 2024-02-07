'''Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). 
El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
'''

cantidad_numeros = int(input("Introduce la cantidad de números a ingresar: "))

numeros_mayores_cero = 0
numeros_menores_cero = 0
numeros_iguales_cero = 0

for i in range(cantidad_numeros):
    numero = float(input(f"Introduce el número {i + 1}: "))
    
    if numero > 0:
        numeros_mayores_cero += 1
    elif numero < 0:
        numeros_menores_cero += 1
    else:
        numeros_iguales_cero += 1

print(f"\nResultados:")
print(f"Números mayores que 0: {numeros_mayores_cero}")
print(f"Números menores que 0: {numeros_menores_cero}")
print(f"Números iguales a 0: {numeros_iguales_cero}")
                   