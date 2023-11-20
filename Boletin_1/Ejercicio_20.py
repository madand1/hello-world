#Ejercicio 20

'''Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) 
después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).'''

monedas_2 = int (input('De estas monedas cuantas son de 2 €'))

monedas_1 = int (input('De estas monedas cuantas son de 1 €'))

monedas_50 = int (input('De estas monedas cuantas son de 50 céntimos'))

monedas_20 = int (input('De estas monedas cuantas son de 20 céntimos'))

monedas_10 = int (input('De estas monedas cuantas son de 10 céntimos'))

dinero_total = monedas_2 * 2 + monedas_1 * 1 + monedas_50 * 0.5 + monedas_20 * 0.2 + monedas_10 * 0.10 

print('el dinero toatl seria:' ,dinero_total , '€')





