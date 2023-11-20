'''Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.'''

a = int(input('Dame un numero comprendido entre 1 y 12 '))

if a == 1:
    print('el mes seleccionado sera enero')
elif a == 2:
    print('el mes seleccionado sera Febrero')

elif a == 3:
    print('el mes seleccionado sera Marzo')

elif a == 4:
    print('el mes seleccionado sera Abril')

elif a == 5:
    print('el mes seleccionado es Mayo')

elif a == 6:
    print('el mes seleccionado es junio')

elif a == 7:
    print('julio')

elif a== 8:
    print ('Agosto')


elif a== 9: 
    print ('septiembre')

elif a== 10:
    print ('octubre')
elif a==11:
    print ('Noviembre')

elif a==12:
    print ('diciembre')

else:
    print ('no existe tal mes')