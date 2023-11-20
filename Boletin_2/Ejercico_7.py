#Ejercicio 7
'''Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:

El exponente sea positivo, sólo tienes que imprimir la potencia.
El exponente sea 0, el resultado es 1.
El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.'''

exponente = int(input('mete el exponente por pantalla:  '))
base = float(input('Mete la base por pantalla: '))

if exponente > 1 :
    resulatdo = base ** exponente
    print ('Aqui tienes el resulatdo : ', resulatdo   )
elif exponente == 0 :
    print ('El resulatdo = 1')

else :
    resultado = 1/ base ** abs(exponente)
    print(f'La potencia de {base} elevado a {exponente} (con exponente negativo) es: {resultado}')