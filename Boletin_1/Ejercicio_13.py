# Ejercico 13

'''
Realizar un algoritmos
que lea un número y
que muestre su raíz cuadrada
y su raíz cúbica.'''

import math


x1 = float (input ('Dame el primer numero '))
x2 = float (input ('Dame el segundo número'))

raiz_cuadrada = math.sqrt (x1 + x2)**2

raiz_cubica = math.sqrt (x1 + x2)**3

print ('Aqui tienes la raiz cuadrada....;',  raiz_cuadrada)

print ('Aqui tienes la raiz cubica....:', raiz_cubica)