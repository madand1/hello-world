#Ejercicio 19

'''
Escribir un algoritmo para calcular la nota final de un estudiante, 
considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. 
Imprime el resultado obtenido por el estudiante.
'''
correctas = int (input('Dime las respuestas correctas del examen'))

incorrectas = int (input('Dime las respuestas correctas del examen'))  
                   
sin_respuesta = int (input('Dime cuantas respuestas en blanco del examen'))

nota_final = correctas * 5 + incorrectas * -1 + sin_respuesta * 0

print(nota_final)



