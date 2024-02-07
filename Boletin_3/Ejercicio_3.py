'''Algoritmo que pida números hasta que se introduzca un cero.
 Debe imprimir la suma y la media de todos los números introducidos.'''

suma = 0
contador = 0

while True:
    numero = float(input("Introduce un número (introduce 0 para salir): "))
    
    if numero == 0:
        break

    suma += numero
    contador += 1

if contador == 0:
    print("No se introdujeron números.")
else:
    media = suma / contador
    print(f"Suma: {suma}")
    print(f"Media: {media}")
