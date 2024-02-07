# Programa que verifica si un año es bisiesto.

# Solicitar al usuario que ingrese un año.
anio = int(input("Ingrese un año: "))

# Verificar si el año es bisiesto.
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")