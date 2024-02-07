'''Crea una aplicación que permita adivinar un número.
La aplicación genera un número aleatorio del 1 al 100. 
A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,
a demás de los intentos que te quedan (tienes 10 intentos para acertarlo).
 El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado),
   si se llega al limite de intentos te muestra el número que había generado.'''

import random

numero_a_adivinar = random.randint(1, 100)
intentos_disponibles = 10

print("¡Bienvenido al juego de adivinanza de números!")
print("Intenta adivinar el número entre 1 y 100.")

while intentos_disponibles > 0:
    intento_usuario = int(input("Ingresa tu número: "))

    if intento_usuario == numero_a_adivinar:
        print(f"¡Felicidades! ¡Has adivinado el número {numero_a_adivinar} en {11 - intentos_disponibles} intentos!")
        break
    elif intento_usuario < numero_a_adivinar:
        print("El número es mayor. ¡Inténtalo de nuevo!")
    else:
        print("El número es menor. ¡Inténtalo de nuevo!")

    intentos_disponibles -= 1
    print(f"Te quedan {intentos_disponibles} intentos.")

if intentos_disponibles == 0:
    print(f"¡Oh no! Has agotado tus intentos. El número correcto era {numero_a_adivinar}.")
