'''Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Para esto, se registran los días que trabajó y las horas de cada día. Realice un algoritmo para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la empresa por los N empleados.'''
# Solicitar al usuario el número de trabajadores
num_trabajadores = int(input("Introduce el número de trabajadores: "))

# Inicializar variables
total_pagado_empresa = 0

# Calcular el sueldo semanal de cada trabajador y el total pagado por la empresa
for empleado in range(1, num_trabajadores + 1):
    print(f"\nEmpleado {empleado}:")
    horas_trabajadas_semana = 0

    # Calcular las horas trabajadas por día
    for dia in range(1, 8):
        horas_dia = float(input(f"Introduce las horas trabajadas en el día {dia}: "))
        horas_trabajadas_semana += horas_dia

    tarifa_por_hora = float(input(f"Introduce la tarifa por hora del empleado {empleado}: "))

    sueldo_semanal = horas_trabajadas_semana * tarifa_por_hora
    total_pagado_empresa += sueldo_semanal

    print(f"Sueldo semanal del empleado {empleado}: {sueldo_semanal} €")

# Imprimir el total pagado por la empresa
print(f"\nTotal pagado por la empresa por los {num_trabajadores} empleados: {total_pagado_empresa} €")
