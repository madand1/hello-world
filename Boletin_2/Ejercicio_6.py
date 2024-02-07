#ejercicio 6
'''Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.'''
cadena_introducida = input ('introduce una cadena por teclado')

if len(cadena_introducida) == 1 and cadena_introducida.isalpha1() and cadena_introducida.isupper:
    print ('la cadena es una letra mayuscula')
else:
    print('la cadena es una letra minuscula')