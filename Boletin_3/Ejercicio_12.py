'''Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes.'''

# Solicitar al usuario el monto inicial y los depósitos mensuales
monto_inicial = float(input("Introduce el monto inicial: "))
dep_mensuales = []

for mes in range(1, 13):
    deposito = float(input(f"Introduce el depósito del mes {mes}: "))
    dep_mensuales.append(deposito)

# Calcular el ahorro total al final de cada mes y durante el año
ahorro_total = monto_inicial
for mes, deposito in enumerate(dep_mensuales, start=1):
    ahorro_total += deposito
    print(f"Mes {mes}: Ahorro acumulado = {ahorro_total}")

# Imprimir el ahorro total al final del año
print(f"\nAhorro total al final del año: {ahorro_total}")
