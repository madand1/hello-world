precios_frutas = {"manzana": 2, "banana": 1.5, "uva": 3}

while True:
    fruta = input("Ingrese el nombre de la fruta (o 'salir' para terminar): ").lower()
    if fruta == 'salir':
        break

    cantidad = int(input("Ingrese la cantidad vendida: "))
    
    if fruta in precios_frutas:
        precio_total = precios_frutas[fruta] * cantidad
        print(f"Precio total de {fruta}: ${precio_total}")
    else:
        print("Error: Fruta no encontrada.")
