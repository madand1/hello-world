num_alumnos = int(input("Ingrese el número de alumnos: "))
alumnos_notas = {}

for _ in range(num_alumnos):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    
    while True:
        nota = float(input("Ingrese una nota (ingrese un número negativo para terminar): "))
        if nota < 0:
            break
        notas.append(nota)
    
    if nombre in alumnos_notas:
        print("Error: El nombre del alumno ya existe.")
    else:
        alumnos_notas[nombre] = notas

for nombre, notas in alumnos_notas.items():
    media = sum(notas) / len(notas)
    print(f"Alumno: {nombre}, Notas: {notas}, Media: {media}")
