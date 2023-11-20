
'''
Escribe un programa en python que nos pida dos cadenas de caracteres (validando que
sólo contengan caracteres alfabéticos (letras)) y nos devuelva: 
• La cadena con mayor número de caracteres y su número de caracteres
• Si alguna de las cadenas está contenida en la otra y si es así cuántas veces lo esta
'''

# Solicitar al usuario dos cadenas de caracteres
cadena1 = input("Ingrese la primera cadena de caracteres: ")
cadena2 = input("Ingrese la segunda cadena de caracteres: ")

# Validar que las cadenas solo contengan letras
if cadena1.isalpha() and cadena2.isalpha():
    # Comparar las longitudes de las cadenas
    if len(cadena1) > len(cadena2):
        print(f"Cadena más larga: {cadena1}, Número de caracteres: {len(cadena1)}")
    elif len(cadena2) > len(cadena1):
        print(f"Cadena más larga: {cadena2}, Número de caracteres: {len(cadena2)}")
    else:
        print("Las cadenas tienen la misma longitud.")

    # Verificar si una cadena está contenida en la otra
    if cadena1 in cadena2:
        veces_contenida = cadena2.count(cadena1)
        print(f"{cadena1} está contenida en {cadena2} {veces_contenida} veces.")
    elif cadena2 in cadena1:
        veces_contenida = cadena1.count(cadena2)
        print(f"{cadena2} está contenida en {cadena1} {veces_contenida} veces.")
    else:
        print("Las cadenas no están contenidas entre sí.")
else:
    print("Error: Ingresa cadenas válidas que solo contengan letras.")


