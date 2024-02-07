'''Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, calcule cuánto pagó la empresa por los N empleados.'''

# Solicitar al usuario el número de trabajadores
num_trabajadores = int(input("Introduce el número de trabajadores: "))

# Inicializar variables
total_pagado_empresa = 0

# Calcular el sueldo semanal de cada trabajador y el total pagado por la empresa
for empleado in range(1, num_trabajadores + 1):
    horas_trabajadas = float(input(f"Introduce las horas trabajadas por el empleado {empleado}: "))
    tarifa_por_hora = float(input(f"Introduce la tarifa por hora del empleado {empleado}: "))

    sueldo_semanal = horas_trabajadas * tarifa_por_hora
    total_pagado_empresa += sueldo_semanal

    print(f"Sueldo semanal del empleado {empleado}: {sueldo_semanal} €\n")

# Imprimir el total pagado por la empresa
print(f"Total pagado por la empresa por los {num_trabajadores} empleados: {total_pagado_empresa} €")
