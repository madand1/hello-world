# Programa que verifica si una fecha es correcta.

# Solicitar al usuario que ingrese el día, mes y año.
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año:"))

# Verificar si la fecha es correcta.
# Consideraremos que febrero tiene 28 días (no consideramos años bisiestos en este ejemplo).

# Verificar la validez del año y del mes.
if 1 <= mes <= 12 and anio >= 0:
    # Verificar la validez del día para un mes específico.
    if (mes in [1, 3, 5, 7, 8, 10, 12] and 1 <= dia <= 31) or \
       (mes in [4, 6, 9, 11] and 1 <= dia <= 30) or \
       (mes == 2 and 1 <= dia <= 28):
        print(f"{dia}/{mes}/{anio} es una fecha válida.")
    else:
        print(f"{dia}/{mes}/{anio} no es una fecha válida.")
else:
    print(f"{dia}/{mes}/{anio} no es una fecha válida.")