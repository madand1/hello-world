#ejercicio 10
'''Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y las clasifique en uno de estos estados:

exteriores
tangentes exteriores
secantes
tangentes interiores
interiores
concéntricas'''

import math

# Solicitar al usuario que ingrese los puntos centrales y radios de las dos circunferencias.
x1 = float(input("Ingrese la coordenada x del centro de la primera circunferencia: "))
y1 = float(input("Ingrese la coordenada y del centro de la primera circunferencia: "))
r1 = float(input("Ingrese el radio de la primera circunferencia: "))

x2 = float(input("Ingrese la coordenada x del centro de la segunda circunferencia: "))
y2 = float(input("Ingrese la coordenada y del centro de la segunda circunferencia: "))
r2 = float(input("Ingrese el radio de la segunda circunferencia: "))

# Calcular la distancia entre los dos puntos centrales.
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calcular la suma y la diferencia de los radios.
suma_radios = r1 + r2
resta_radios = abs(r1 - r2)

# Clasificar las circunferencias según su posición relativa.
if distancia > suma_radios:
    print("Circunferencias exteriores")
elif distancia == suma_radios:
    print("Circunferencias tangentes exteriores")
elif distancia > resta_radios and distancia < suma_radios:
    print("Circunferencias secantes")
elif distancia == resta_radios:
    print("Circunferencias tangentes interiores")
elif distancia < resta_radios:
    print("Circunferencias interiores")
elif x1 == x2 and y1 == y2 and r1 == r2:
    print("Circunferencias concéntricas")