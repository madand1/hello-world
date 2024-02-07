'''Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.'''

# Definir la tarifa por hora
tarifa_por_hora = float(input("Introduce la tarifa por hora: "))

# Inicializar variables
total_horas_trabajadas = 0

# Solicitar las horas trabajadas diariamente durante la semana
for dia in range(1, 7):
    horas_diarias = float(input(f"Introduce las horas trabajadas en el día {dia}: "))
    total_horas_trabajadas += horas_diarias

# Calcular el sueldo
sueldo = total_horas_trabajadas * tarifa_por_hora

# Imprimir resultados
print(f"\nTotal de horas trabajadas en la semana: {total_horas_trabajadas} horas")
print(f"Sueldo correspondiente: ${sueldo}")
