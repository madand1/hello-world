# Ejercicio 11

'''
Pide al usuario dos números y 
muestra la “distancia” entre ellos
 (el valor absoluto de su diferencia,
 de modo que el resultado sea 
 siempre positivo).
 '''


numero1 = float (input('Dame el primer numero'))
numero2 = float (input('Dame el segundo numero'))

### abs es que me de el resultado en valor absoluto
distancia = abs(numero1 - numero2)

print ('La distancia es ......:' , distancia)