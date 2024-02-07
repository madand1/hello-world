agenda = {}

while True:
    print("\nMenú:")
    print("1. Añadir/Modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción: ")

    if opcion == '1':
        nombre = input("Ingrese un nombre: ")
        if nombre in agenda:
            print(f"Teléfono: {agenda[nombre]}")
            modificar = input("¿Desea modificar el teléfono? (s/n): ").lower()
            if modificar == 's':
                telefono = input("Ingrese el nuevo teléfono: ")
                agenda[nombre] = telefono
        else:
            telefono = input("Ingrese el teléfono: ")
            agenda[nombre] = telefono

    elif opcion == '2':
        cadena = input("Ingrese una cadena de caracteres: ")
        coincidencias = [contacto for contacto in agenda.keys() if contacto.startswith(cadena)]
        print("Contactos que coinciden:")
        for contacto in coincidencias:
            print(f"{contacto}: {agenda[contacto]}")

    elif opcion == '3':
        nombre = input("Ingrese el nombre a borrar: ")
        if nombre in agenda:
            confirmar = input(f"¿Está seguro que desea borrar a {nombre}? (s/n): ").lower()
            if confirmar == 's':
                del agenda[nombre]
                print(f"{nombre} ha sido borrado de la agenda.")
        else:
            print("Error: Nombre no encontrado en la agenda.")

    elif opcion == '4':
        print("Lista de contactos:")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")

    elif opcion == '5':
        break

    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
