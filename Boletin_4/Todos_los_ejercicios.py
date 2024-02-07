# Ejercicio 1
cadena = input("Ejercicio 1: Introduce una cadena: ")
for caracter in cadena:
    print(caracter)

# Ejercicio 2
cadena = input("Ejercicio 2: Introduce una cadena: ")
subcadena = input("Introduce una subcadena para comprobar si la cadena comienza con ella: ")
if cadena.startswith(subcadena):
    print("La cadena comienza con la subcadena.")
else:
    print("La cadena no comienza con la subcadena.")

# Ejercicio 3
cadena = input("Ejercicio 3: Introduce una cadena: ")
caracter = input("Introduce un carácter para contar en la cadena: ")
if len(caracter) == 1:
    veces = cadena.count(caracter)
    print(f"El carácter '{caracter}' aparece {veces} veces en la cadena.")
else:
    print("Por favor, introduce un único carácter.")

# Ejercicio 4
cadena = input("Ejercicio 4: Introduce una cadena con palabras separadas por espacios: ")
palabras = cadena.split()
cantidad_palabras = len(palabras)
print(f"La cadena tiene {cantidad_palabras} palabra(s).")

# Ejercicio 5
cadena = input("Ejercicio 5: Introduce una cadena con nombre y apellidos: ")
iniciales = ''.join([nombre[0].upper() for nombre in cadena.split()])
print(f"Las iniciales en mayúsculas son: {iniciales}")

# Ejercicio 6
cadena = input("Ejercicio 6: Introduce una cadena de caracteres: ")
cadena_invertida = cadena[::-1]
print(f"La cadena invertida es: {cadena_invertida}")

# Ejercicio 7
cadena = input("Ejercicio 7: Introduce una cadena: ")
caracter1 = input("Introduce el primer carácter a ser reemplazado: ")
caracter2 = input("Introduce el segundo carácter de reemplazo: ")
if len(caracter1) == 1 and len(caracter2) == 1:
    cadena_modificada = cadena.replace(caracter1, caracter2, 1)
    print(f"La cadena modificada es: {cadena_modificada}")
else:
    print("Por favor, introduce caracteres individuales.")

# Ejercicio 8
cadena = input("Ejercicio 8: Introduce una cadena: ")
cadena_transformada = ''.join([c.upper() if c.islower() else c.lower() for c in cadena])
print(f"La cadena transformada es: {cadena_transformada}")

# Ejercicio 9
cadena = input("Ejercicio 9: Introduce una cadena: ")
subcadena = input("Introduce una subcadena para comprobar si está en la cadena: ")
if subcadena in cadena:
    print("La cadena contiene la subcadena.")
else:
    print("La cadena no contiene la subcadena.")

# Ejercicio 10
cadena = input("Ejercicio 10: Introduce una cadena para verificar si es un palíndromo: ")
cadena_sin_espacios = ''.join(c.lower() for c in cadena if c.isalnum())
es_palindromo = cadena_sin_espacios == cadena_sin_espacios[::-1]
if es_palindromo:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
