'''La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida'''

tipo_uva = input("Ingrese el tipo de uva (A o B): ")
tamano_uva = int(input("Ingrese el tamaño de uva (1 o 2): "))

# Solicitar al usuario que ingrese el precio inicial por kilo de uva.
precio_inicial = float(input("Ingrese el precio inicial por kilo de uva en céntimos: "))

# Inicializar la ganancia.
ganancia = 0

# Calcular la ganancia según las condiciones dadas.
if tipo_uva == 'A':
    if tamano_uva == 1:
        ganancia = precio_inicial + 20
    elif tamano_uva == 2:
        ganancia = precio_inicial + 30
elif tipo_uva == 'B':
    if tamano_uva == 1:
        ganancia = precio_inicial - 30
    elif tamano_uva == 2:
        ganancia = precio_inicial - 50

# Mostrar la ganancia obtenida.
print(f"La ganancia obtenida por el productor es de {ganancia} céntimos por kilo de uva.")