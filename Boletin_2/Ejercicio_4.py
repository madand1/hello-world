#ejercicio 4
'''Crea un programa que pida al usuario dos números y 
muestre su división si el segundo no es cero,
 o un mensaje de aviso en caso contrario.'''

a = float(input('dame un numero'))
b = float(input('dame un numero'))
resultado = a /b
if b != 0:
    
    print ('La division de {a} entre {b} es : {resultado}')
else :
    print ('no se puede dividir por cero, por favor ingrese un segundo numeoro')