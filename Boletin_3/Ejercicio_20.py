'''Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.'''
# Solicitar al usuario la cantidad de números primos que desea mostrar
n = int(input("Introduce la cantidad de números primos que quieres mostrar: "))

# Mostrar los primeros N números primos
numeros_primos = []
numero_actual = 2

while len(numeros_primos) < n:
    es_primo = True
    i = 2

    while i <= int(numero_actual**0.5) and es_primo:
        if numero_actual % i == 0:
            es_primo = False
        i += 1

    if es_primo:
        numeros_primos.append(numero_actual)
    
    numero_actual += 1

print(f"\nLos primeros {n} números primos son: {numeros_primos}")
