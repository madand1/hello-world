#Ejercicio 16
'''
 Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. 
 
 El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para

 
 ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y 

 con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.
'''

velocidad_vehiculo_1 = float (input ("Dame la velocidad del primer vehiculo :"))

velocidad_vehiculo_2 = float (input ("Dame la velocidad del segundo vehiculo :"))

distancia = float (input ("Dame la distancia entre los vehiculos (km) :"))

tiempo = distancia / (velocidad_vehiculo_2 - velocidad_vehiculo_1)

print ("Aqui tienes el tiempo en el que alcanzara el vehiculo más rapido al más lento :", tiempo)

