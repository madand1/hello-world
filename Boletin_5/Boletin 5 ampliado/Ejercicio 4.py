alumnos = '''Juan,19
Pepe,17
María,20
Luis,12'''

# Separar la cadena en líneas y luego cada línea en nombre y edad
lineas = alumnos.split('\n')

# Listas para almacenar la información
nombres_edades = []
mayores_de_edad = []
edades = []

for linea in lineas:
    if linea:
        nombre, edad = linea.split(',')
        edad = int(edad)

        # Almacenar nombre y edad en la lista
        nombres_edades.append(f"{nombre}: {edad} años")

        # Almacenar nombres de los mayores de edad en la lista
        if edad >= 18:
            mayores_de_edad.append(nombre)

        # Almacenar edades en la lista
        edades.append(edad)

# Mostrar la lista de nombres y edades
print("Lista de nombres y edades:")
for item in nombres_edades:
    print(item)

# Mostrar la lista de mayores de edad
print("\nNombres de mayores de edad:")
for nombre in mayores_de_edad:
    print(nombre)

# Mostrar la lista de edades
print("\nLista de edades:")
print(edades)

# Encontrar la edad máxima
if edades:
    max_edad = max(edades)

    # Mostrar nombres de los alumnos con la edad máxima
    nombres_max_edad = [linea.split(',')[0] for linea in lineas if linea and int(linea.split(',')[1]) == max_edad]
    print(f"\nAlumnos con la edad máxima ({max_edad} años): {', '.join(nombres_max_edad)}")
else:
    print("\nNo hay datos válidos en la cadena.")
