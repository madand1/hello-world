#ejercicio_1
import random

# Inicializar lista con 10 valores aleatorios entre 1 y 10
lista = [random.randint(1, 10) for _ in range(10)]

# Mostrar cada elemento, su cuadrado y su cubo
for elemento in lista:
    print(f"Elemento: {elemento}, Cuadrado: {elemento**2}, Cubo: {elemento**3}")

#ejercicio2
# Crear lista con 5 cadenas leídas por teclado
lista_cadenas = [input("Ingrese cadena: ") for _ in range(5)]

# Copiar elementos en otra lista en orden inverso
lista_inversa = lista_cadenas[::-1]

# Mostrar elementos de la lista inversa
print("Lista Inversa:", lista_inversa)

#ejercicio3
# Leer 5 notas por teclado
notas = [float(input(f"Ingrese nota {i + 1}: ")) for i in range(5)]

# Mostrar todas las notas
print("Notas:", notas)

# Calcular y mostrar nota media
nota_media = sum(notas) / len(notas)
print("Nota Media:", nota_media)

# Mostrar nota más alta y menor
print("Nota Más Alta:", max(notas))
print("Nota Menor:", min(notas))

#ejercicio4
# Declarar lista
vector = []

# Llenar la lista con números hasta que se ingrese un número negativo
while True:
    numero = int(input("Ingrese un número (negativo para terminar): "))
    if numero < 0:
        break
    vector.append(numero)

# Imprimir la lista
print("Vector:", vector)

#ejercicio5
# Inicializar lista con 10 valores aleatorios
numeros = [random.randint(1, 100) for _ in range(10)]

# Ordenar la lista de menor a mayor
numeros.sort()

# Mostrar la lista ordenada
print("Lista Ordenada:", numeros)

#ejercicio6
# Lista de días por mes
dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
nombre_mes = [
    "",
    "enero", "febrero", "marzo", "abril",
    "mayo", "junio", "julio", "agosto",
    "septiembre", "octubre", "noviembre", "diciembre"
]
# Pedir número de mes al usuario
num_mes = int(input("Ingrese un número de mes (1-12): "))

# Mostrar días y nombre del mes
print(f"El mes {num_mes} tiene {dias_por_mes[num_mes]} días y es {nombre_mes[num_mes]}.")

#ejericico7
# Declarar tres listas
lista1 = []
lista2 = []
lista3 = []

# Pedir valores para lista1 y lista2
for i in range(5):
    lista1.append(int(input(f"Ingrese valor para lista1[{i}]: ")))
    lista2.append(int(input(f"Ingrese valor para lista2[{i}]: ")))

# Calcular lista3 = lista1 + lista2
lista3 = [a + b for a, b in zip(lista1, lista2)]

# Mostrar lista3
print("Lista3:", lista3)

#ejericico8
# Declarar listas para nombres y edades
nombres = []
edades = []

# Leer nombre y edad de cada alumno hasta ingresar '*'
while True:
    nombre = input("Ingrese el nombre del alumno (o '*' para terminar): ")
    if nombre == '*':
        break
    edad = int(input("Ingrese la edad del alumno: "))
    nombres.append(nombre)
    edades.append(edad)

# Mostrar alumnos mayores de edad
print("Alumnos mayores de edad:")
for i in range(len(nombres)):
    if edades[i] >= 18:
        print(f"{nombres[i]} - Edad: {edades[i]}")

# Mostrar alumnos mayores
mayor_edad = max(edades)
print("Alumnos mayores:")
for i in range(len(nombres)):
    if edades[i] == mayor_edad:
        print(f"{nombres[i]} - Edad: {edades[i]}")

#ejercicio9
# Declarar lista de temperaturas
temperaturas = []

# Leer temperaturas de 5 días
for i in range(5):
    temperatura = float(input(f"Ingrese temperatura para el día {i + 1}: "))
    temperaturas.append(temperatura)

# Calcular temperatura media de cada día
media_por_dia = [sum(temperaturas) / 5 for _ in range(5)]
print("Temperatura media de cada día:", media_por_dia)

# Encontrar días con menos temperatura
min_temperatura = min(temperaturas)
dias_menos_temperatura = [i + 1 for i in range(5) if temperaturas[i] == min_temperatura]
print("Días con menos temperatura:", dias_menos_temperatura)

# Leer temperatura y mostrar días con temperatura máxima coincidente
temperatura_max = float(input("Ingrese temperatura máxima: "))
dias_max_temperatura = [i + 1 for i in range(5) if temperaturas[i] == temperatura_max]
if dias_max_temperatura:
    print("Días con temperatura máxima coincidente:", dias_max_temperatura)
else:
    print("No hay días con temperatura máxima coincidente.")

#ejercicio10

# Crear tabla de 5x5 enteros
tabla = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]

# Sumar elementos de cada fila y mostrar resultados
for i, fila in enumerate(tabla):
    suma_fila = sum(fila)
    print(f"Suma de elementos en la fila {i + 1}: {suma_fila}")

# Sumar elementos de cada columna y mostrar resultados
for j in range(5):
    suma_columna = sum(tabla[i][j] for i in range(5))
    print(f"Suma de elementos en la columna {j + 1}: {suma_columna}")

#ejercicio11
# Crear tabla diagonal de 5x5
diagonal = [[1 if i == j else 0 for j in range(5)] for i in range(5)]

# Mostrar contenido de la tabla
for fila in diagonal:
    print(fila)

#ejercicio11

# Crear tabla diagonal de 5x5
diagonal = [[1 if i == j else 0 for j in range(5)] for i in range(5)]

# Mostrar contenido de la tabla
for fila in diagonal:
    print(fila)

#ejercicio12
# Crear tabla marco de 5x15
marco = [[1 if i == 0 or i == 4 or j == 0 or j == 14 else 0 for j in range(15)] for i in range(5)]

# Mostrar contenido de la tabla
for fila in marco:
    print(''.join(map(str, fila)))

#eje13
# Declarar listas para nombres de conductores y kilómetros
nombres = []
kms = []

# Leer nombres y kilómetros
for _ in range(5):
    nombre = input("Ingrese nombre del conductor: ")
    kms_dia = [int(input(f"Ingrese kilómetros para el día {i + 1}: ")) for i in range(7)]
    nombres.append(nombre)
    kms.append(kms_dia)

# Generar lista total_kms con los kilómetros totales de cada conductor
total_kms = [sum(dia) for dia in kms]

# Mostrar lista con nombres y kilómetros totales
for i in range(5):
    print(f"{nombres[i]} - Kilómetros totales: {total_kms[i]}")

#ejer14
# # Declarar listas para precios y cantidades
precios = []
cantidades = []

# Leer precios y cantidades de 5 artículos en 4 sucursales
for i in range(5):
    precio = float(input(f"Ingrese precio del artículo {i + 1}: "))
    cantidades_sucursal = [int(input(f"Ingrese cantidad vendida en sucursal {j + 1}: ")) for j in range(4)]
    precios.append(precio)
    cantidades.append(cantidades_sucursal)

# Calcular cantidades totales de cada artículo
cantidades_totales = [sum(cantidades[i]) for i in range(5)]
print("Cantidades totales de cada artículo:", cantidades_totales)

# Mostrar cantidad del artículo 3 en sucursal 1
print("Cantidad del artículo 3 en sucursal 1:", cantidades[2][0])

# Calcular recaudación total de cada sucursal
recaudacion_sucursal = [sum(cantidades[i][j] * precios[i] for i in range(5)) for j in range(4)]
print("Recaudación total de cada sucursal:", recaudacion_sucursal)

# Calcular recaudación total de la empresa
recaudacion_total = sum(recaudacion_sucursal)
print("Recaudación total de la empresa:", recaudacion_total)

# Encontrar sucursal de mayor recaudación
sucursal_mayor_recaudacion = recaudacion_sucursal.index(max(recaudacion_sucursal)) + 1
print("Sucursal de mayor recaudación:", sucursal_mayor_recaudacion)

#eje15
# Declarar listas para equipos y resultados
equipos = []
resultados = []

# Leer nombres de equipos y resultados de 15 partidos
for i in range(15):
    equipo_local = input(f"Ingrese nombre del equipo local para el partido {i + 1}: ")
    equipo_visitante = input(f"Ingrese nombre del equipo visitante para el partido {i + 1}: ")
    goles_local = int(input(f"Ingrese goles del equipo local para el partido {i + 1}: "))
    goles_visitante = int(input(f"Ingrese goles del equipo visitante para el partido {i + 1}: "))
    equipos.extend([equipo_local, equipo_visitante])
    resultados.extend([goles_local, goles_visitante])

# Mostrar quiniela de la jornada
for i in range(15):
    print(f"Partido {i + 1}: {equipos[2*i]} vs {equipos[2*i + 1]} - Resultado: {resultados[2*i]}-{resultados[2*i + 1]}")

#ejer16
# Declarar lista vacía
mi_lista = []

while True:
    # Mostrar menú
    print("1. Añadir número a la lista")
    print("2. Añadir número a la lista en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")

    opcion = int(input("Seleccione una opción: "))

    # Añadir número al final de la lista
    if opcion == 1:
        numero = int(input("Ingrese un número: "))
        mi_lista.append(numero)

    # Añadir número en una posición específica
    elif opcion == 2:
        numero = int(input("Ingrese un número: "))
        posicion = int(input("Ingrese la posición: "))
        if 1 <= posicion <= len(mi_lista) + 1:
            mi_lista.insert(posicion - 1, numero)
        else:
            print("Posición no válida.")

    # Mostrar longitud de la lista
    elif opcion == 3:
        print("Longitud de la lista:", len(mi_lista))

    # Mostrar y eliminar el último número
    elif opcion == 4:
        if mi_lista:
            ultimo_numero = mi_lista.pop()
            print("Último número:", ultimo_numero)
        else:
            print("La lista está vacía.")

    # Eliminar un número en una posición específica
    elif opcion == 5:
        posicion = int(input("Ingrese la posición: "))
        if 1 <= posicion <= len(mi_lista):
            numero_eliminado = mi_lista.pop(posicion - 1)
            print(f"Número en la posición {posicion} eliminado: {numero_eliminado}")
        else:
            print("Posición no válida.")

    # Contar ocurrencias de un número
    elif opcion == 6:
        numero = int(input("Ingrese un número: "))
        ocurrencias = mi_lista.count(numero)
        print(f"El número {numero} aparece {ocurrencias} veces en la lista.")

    # Encontrar posiciones de un número
    elif opcion == 7:
        numero = int(input("Ingrese un número: "))
        posiciones = [i + 1 for i in range(len(mi_lista)) if mi_lista[i] == numero]
        if posiciones:
            print(f"Posiciones del número {numero}: {posiciones}")
        else:
            print(f"El número {numero} no está en la lista.")

    # Mostrar números en la lista
    elif opcion == 8:
        print("Números en la lista:", mi_lista)

    # Salir del programa
    elif opcion == 9:
        break
    else:
        print("Opción no válida.")

#ejer17 
# Crear lista hasta que se ingrese un número negativo
lista_original = []
while True:
    numero = int(input("Ingrese un número (negativo para terminar): "))
    if numero < 0:
        break
    lista_original.append(numero)

# Crear lista sin duplicados
lista_sin_duplicados = list(set(lista_original))

# Mostrar lista sin duplicados
print("Lista sin duplicados:", lista_sin_duplicados)

#ejer18
# Crear lista de palabras
lista_palabras = ["hola", "mundo", "python", "programacion", "lista"]

while True:
    # Mostrar opciones
    print("1. Contar")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Mostrar")
    print("5. Terminar")

    opcion = int(input("Seleccione una opción: "))

    # Contar ocurrencias de una cadena
    if opcion == 1:
        cadena = input("Ingrese una cadena: ")
        ocurrencias = lista_palabras.count(cadena)
        print(f"La cadena '{cadena}' aparece {ocurrencias} veces en la lista.")

    # Modificar ocurrencias de una cadena
    elif opcion == 2:
        cadena = input("Ingrese una cadena a modificar: ")
        nueva_cadena = input("Ingrese la nueva cadena: ")
        lista_palabras = [nueva_cadena if palabra == cadena else palabra for palabra in lista_palabras]
        print(f"Cadena modificada. Nueva lista: {lista_palabras}")

    # Eliminar ocurrencias de una cadena
    elif opcion == 3:
        cadena = input("Ingrese una cadena a eliminar: ")
        lista_palabras = [palabra for palabra in lista_palabras if palabra != cadena]
        print(f"Cadena eliminada.")
