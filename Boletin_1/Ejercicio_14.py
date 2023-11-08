# Ejercicio 14

'''
Dado un número de dos cifras, 
diseñe un algoritmo 
que permita obtener el número invertido. 
Ejemplo,
si se introduce 23 que muestre 32.'''
#Primero devere peirme un numero por consola
num = int (input ('Dame un número '))
#Creamos la cadena de cararacteres invertida, para eso convertimos el numero 
#a una cadena de texto, invertimos y la convertimos en un numero-

'''En este código, el usuario será solicitado a ingresar un número entero.
 Luego, convertimos ese número a una cadena de texto usando str(), 
 lo invertimos usando el slicing
 y luego lo convertimos de nuevo a un entero usando int().'''
numero_invertido = int(str (num)[::-1])


#Imprimo la cadena de caracteres invertida.

print("Aqui tienes la cadena de caracteres invertida : ", numero_invertido)
        
