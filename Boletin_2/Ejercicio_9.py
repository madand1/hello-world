#ejercicio 9

'''Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);'''

a = float (input ('INgresa un numero por pantalla'))

b = float (input ('INgresa un numero por pantalla'))

c = float (input ('INgresa un numero por pantalla'))

 #Comparar y ordenar los números de mayor a menor.
if a >= b and a >= c:
    if b >= c:
        print("Números ordenados de mayor a menor:", a, b , c)
    else:
        print("Números ordenados de mayor a menor:", a, b, c)
elif b >= a and b >= c:
    if a >= c:
        print("Números ordenados de mayor a menor:", a, b, c)
    else:
        print("Números ordenados de mayor a menor:", a, b, c)
else:
    if a >= b:
        print("Números ordenados de mayor a menor:", a, b, c)
    else:
        print("Números ordenados de mayor a menor:", a, b, c)