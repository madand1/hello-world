'''Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ 
en caso contrario, el programa termina cuando se introduce un espacio.
'''

caracter = input("Introduce un caracter (presiona espacio para salir): ")

while caracter != ' ':
    if caracter.lower() in 'aeiou':
        print("VOCAL")
    else:
        print("NO VOCAL")

    caracter = input("Introduce un caracter (presiona espacio para salir): ")
