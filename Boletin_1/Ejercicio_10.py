# Ejercicio 10 

'''

Un alumno desea 
saber cual será su calificación 
final en la materia de Algoritmos. 
Dicha calificación se compone de los siguientes porcentajes:

55% del promedio de sus tres calificaciones parciales.
30% de la calificación del examen final.
15% de la calificación de un trabajo final.
'''

parcial_1 = float (input('Dame la nota del parcial 1'))

parcial_2 = float (input('Dame la nta del parcial 2'))

parcial_3 = float (input ('Dame la nota del parcial 3'))

examen_final = float (input('Dame la nota de tu examen final'))

trabajo_final = float (input('Dame la nota de tu trabajo final'))

promedio_parciales = (parcial_1 + parcial_2 + parcial_3)/3

porcentaje_parciales = promedio_parciales * 0.55

promedio_final = examen_final * 0.3

promedio_trabajo_final = trabajo_final *0.15

calificacion_final = promedio_final+ porcentaje_parciales + promedio_trabajo_final

print ('Tu calificacion final sera....:', calificacion_final)