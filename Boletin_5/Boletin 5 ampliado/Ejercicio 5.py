import os 
alumnos = "" 
archivo = 'edades'

if not os.path.exists(archivo):
    print(f"El archivo {archivo} no existe.")
else:
# Leer información desde el archivo
    with open('archivo', 'r') as file:
     alumnos = file.read()

# Separar la cadena en líneas y luego cada línea en nombre y edad
lineas = alumnos.split('\n')
for linea in lineas:
    if linea:
        nombre, edad = linea.split(',')
        edad = int(edad)

        # Mostrar nombre y edad
        print(f"{nombre}: {edad} años")

        # Mostrar nombre de los mayores de edad
        if edad >= 18:
            print(f"{nombre} es mayor de edad")

# Encontrar la edad máxima
edades = [int(linea.split(',')[1]) for linea in lineas if linea]
if edades:
    max_edad = max(edades)

    # Mostrar nombres de los alumnos con la edad máxima
    nombres_max_edad = [linea.split(',')[0] for linea in lineas if linea and int(linea.split(',')[1]) == max_edad]
    print(f"Alumnos con la edad máxima ({max_edad} años): {', '.join(nombres_max_edad)}")
else:
    print("No hay datos válidos en el archivo.")
