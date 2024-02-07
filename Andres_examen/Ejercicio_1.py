


cantidad_temperaturas = 0
temperatura_mas_alta = float('-inf')
suma_temperaturas = 0
temperaturas_por_encima_de_cero = 0
temperaturas_por_debajo_de_cero = 0
temperatura_igual_a_cero = False


cantidad_temperaturas_valida = False
while not cantidad_temperaturas_valida:
    cantidad_temperaturas_str = input("Ingrese cuántas temperaturas va a introducir: ")
    if cantidad_temperaturas_str.isdigit() and int(cantidad_temperaturas_str) > 0:
        cantidad_temperaturas = int(cantidad_temperaturas_str)
        cantidad_temperaturas_valida = True
    else:
        print("Error: Ingrese un número entero positivo.")


for i in range(cantidad_temperaturas):
    temperatura_valida = False
    while not temperatura_valida:
        temperatura_str = input(f"Ingrese la temperatura {i + 1}: ")
        if temperatura_str.replace('.', '', 1).isdigit():
            temperatura = float(temperatura_str)
            temperatura_valida = True
        else:
            print("Error: Ingrese una temperatura válida.")

    
    if temperatura > temperatura_mas_alta:
        temperatura_mas_alta = temperatura

    
    suma_temperaturas += temperatura

   
    if temperatura > 0:
        temperaturas_por_encima_de_cero += 1
    elif temperatura < 0:
        temperaturas_por_debajo_de_cero += 1
    else:
        temperatura_igual_a_cero = True


temperatura_media = suma_temperaturas / cantidad_temperaturas


print(f"\nTemperatura más alta: {temperatura_mas_alta}")
print(f"Temperatura media: {temperatura_media}")
print(f"Temperaturas por encima de 0: {temperaturas_por_encima_de_cero}")
print(f"Temperaturas por debajo de 0: {temperaturas_por_debajo_de_cero}")
if temperatura_igual_a_cero:
    print("Se ha introducido una temperatura igual a 0.")
