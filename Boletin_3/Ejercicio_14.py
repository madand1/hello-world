'''Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra en el km 150, los coches tienen sentido opuesto y tienen la misma velocidad. Realizar un programa para determinar en qué kilómetro de esa carretera se encontrarán.'''

# Solicitar al usuario las posiciones iniciales y las velocidades de los coches
posicion_coche1 = int(input("Introduce la posición inicial del primer coche en kilómetros: "))
posicion_coche2 = int(input("Introduce la posición inicial del segundo coche en kilómetros: "))
velocidad_coche = float(input("Introduce la velocidad de ambos coches en kilómetros por hora: "))

# Calcular la distancia relativa entre los coches
distancia_relativa = abs(posicion_coche1 - posicion_coche2)

# Calcular el tiempo hasta el encuentro
tiempo_encuentro = distancia_relativa / (2 * velocidad_coche)

# Calcular la posición de encuentro
posicion_encuentro = posicion_coche1 + velocidad_coche * tiempo_encuentro

# Imprimir el resultado
print(f"\nLos coches se encontrarán en el kilómetro {posicion_encuentro:.2f}.")
