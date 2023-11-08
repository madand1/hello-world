#Ejercicio 17

'''Un ciclista parte de una ciudad A a las 
HH horas, MM minutos y SS segundos. 
El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
Escribir un algoritmo que determine la hora de llegada a la ciudad B.'''

a = int (input ('Ingrese la hora de partida del ciclista'))
b = int (input ('Ingrese los minutos de partida del ciclista'))
c = int (input ('Ingrese los segundos de partida deñ ciclista')) 

tiempo_llegada = int (input ('Tiempo de llegada en segundos'))

hora_salida = a + (b/60) + (c/3600)

tiempo_que_se_tarda = (tiempo_llegada/3600) 

tiempo_correspondido = ( hora_salida - tiempo_que_se_tarda) 

print ('Lo que ha tardado el ciclista : ' ,tiempo_correspondido)
