'''Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.'''

# Solicitar al usuario la base y el exponente
base = float(input("Introduce la base (número real): "))
exponente = int(input("Introduce el exponente (número entero positivo): "))

# Verificar que el exponente sea un número entero positivo
if exponente < 0:
    print("Error: El exponente debe ser un número entero positivo.")
else:
    # Calcular la potencia sin utilizar el operador de potencia
    resultado = 1
    for _ in range(exponente):
        resultado *= base

    # Imprimir el resultado
    print(f"{base} elevado a la {exponente} es igual a: {resultado}")
