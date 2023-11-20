#ejercicio 3
'''scribe un programa que lea un número e indique si es par o impar.'''

a = int (input('ingresa un numero'))

if a %2 == 0: ##aqui lo que pasa es que calcula el resto.
    print ('El numero es par')
else:
    print('el numero es impar')           