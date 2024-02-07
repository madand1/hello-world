# Ejercicio 12

'''
Pide al usuario dos pares 
de números x1,y2 y x2,y2, 
que representen dos puntos en el plano.
Calcula y muestra la 
distancia entre ellos.'''

import math

x1 = float ('Dame el primer numero ')
x2 = float ('dame el segundo numero')
y1 = float ('Dame el tercer numero')
y2 = float ('Dsame el cuarto numero')

distancia = math.sqrt (((x2 - x1 )+ (y2 -y1))**2)

print ('La distancia es.......:' , distancia)