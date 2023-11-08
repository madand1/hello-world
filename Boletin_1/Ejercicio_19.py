#Ejercicio 19

'''Escribir un algoritmo para calcular la nota final de un estudiante, considerando que:
 por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. 
Imprime el resultado obtenido por el estudiante.'''


num = int (input("dame un numerical"))
primo = True

for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
    

if primo:
    print("Es primo")
else:
    print("No es primo")

    