'''Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.

'''

while True:
    # Mostrar el menú
    print("\nMenú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

    # Solicitar al usuario que elija una opción
    opcion = input("Selecciona una opción (1-4): ")

    # Procesar la opción seleccionada
    if opcion == '1':
        print("Has seleccionado la Opción 1.")
        # Agrega aquí el código para la Opción 1

    elif opcion == '2':
        print("Has seleccionado la Opción 2.")
        # Agrega aquí el código para la Opción 2

    elif opcion == '3':
        print("Has seleccionado la Opción 3.")
        # Agrega aquí el código para la Opción 3

    elif opcion == '4':
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, elige una opción válida.")
