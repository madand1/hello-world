'''Una persona adquirió un producto para pagar en 20 meses. 
El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. 
Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.'''

# Inicializar variables
total_pagado = 0
pago_mensual = 10  # Primer pago

# Calcular los pagos mensuales y el total pagado después de 20 meses
for mes in range(1, 21):
    print(f"Mes {mes}: Pago mensual = {pago_mensual} €")
    total_pagado += pago_mensual
    pago_mensual *= 2  # El pago se duplica cada mes

# Imprimir el total pagado después de 20 meses
print(f"\nTotal pagado después de 20 meses: {total_pagado} €")
