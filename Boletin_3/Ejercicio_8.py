'''Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir. A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:

La suma de los números que están dentro del intervalo (intervalo abierto).
Cuantos números están fuera del intervalo.
He informa si hemos introducido algún número igual a los límites del intervalo.'''

# Solicitar al usuario el límite inferior y superior
while True:
    limite_inferior = int(input("Introduce el límite inferior del intervalo: "))
    limite_superior = int(input("Introduce el límite superior del intervalo: "))

    if limite_inferior <= limite_superior:
        break
    else:
        print("Error: El límite inferior no puede ser mayor que el límite superior. Inténtalo de nuevo.")

# Inicializar variables
suma_dentro_intervalo = 0
numeros_fuera_intervalo = 0
numero_igual_limites = False

# Solicitar números hasta que se introduce 0
while True:
    numero = int(input("Introduce un número (presiona 0 para salir): "))

    if numero == 0:
        break

    if limite_inferior < numero < limite_superior:
        suma_dentro_intervalo += numero
    else:
        numeros_fuera_intervalo += 1

    if numero == limite_inferior or numero == limite_superior:
        numero_igual_limites = True

# Imprimir resultados
print("\nResultados:")
print(f"Suma de los números dentro del intervalo: {suma_dentro_intervalo}")
print(f"Números fuera del intervalo: {numeros_fuera_intervalo}")
print(f"¿Se introdujo algún número igual a los límites del intervalo?: {'Sí' if numero_igual_limites else 'No'}")
