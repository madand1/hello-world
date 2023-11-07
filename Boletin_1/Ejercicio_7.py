 # Ejercicio 7

'''
Realiza un programa que reciba
una cantidad de minutos y muestre 
por pantalla
a cuantas horas
y minutos corresponde
'''

minutos_recibidos = int (input("Dame los minutos para el conversor"))

horas = minutos_recibidos / 60

minutos_finales = minutos_recibidos % 60

print ("Minutos finales:" , minutos_finales , "Horas que corresponde... :" , horas , "Minutos finales que tiene en ...: ", minutos_finales)
