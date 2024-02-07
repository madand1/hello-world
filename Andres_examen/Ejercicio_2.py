



cadena = input("Ingrese una cadena de caracteres: ")
caracter = input("Ingrese un carácter alfanumérico: ")


if len(caracter) == 1 and caracter.isalnum():
    
    palabras = cadena.split()
    numero_palabras = len(palabras)
    
    
    posiciones = [i for i, char in enumerate(cadena) if char == caracter]
    
    
    numero_apariciones = cadena.count(caracter)
    
   
    empieza_por_caracter = cadena.startswith(caracter)
    
    # Lo que quiero que me muestre por pantalla
    print(f"Número de palabras en la cadena: {numero_palabras}")
    print(f"Posiciones en las que el carácter '{caracter}' se encuentra en la cadena: {posiciones}")
    print(f"Número de veces que el carácter '{caracter}' aparece en la cadena: {numero_apariciones}")
    print(f"La cadena empieza por el carácter '{caracter}': {empieza_por_caracter}")
else:
    print("Error: Ingrese un carácter alfanumérico válido.")
