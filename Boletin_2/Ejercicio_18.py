# Programa que muestra el día de la semana correspondiente.

# Solicitar al usuario que ingrese un número del 1 al 7.
numero_dia = int(input("Ingrese un número del 1 al 7: "))

# Determinar el día de la semana correspondiente.
if numero_dia == 1:
    print("Día de la semana: Lunes")
elif numero_dia == 2:
    print("Día de la semana: Martes")
elif numero_dia == 3:
    print("Día de la semana: Miércoles")
elif numero_dia == 4:
    print("Día de la semana: Jueves") 
elif numero_dia == 5:
    print("Día de la semana: Viernes")
elif numero_dia == 6:
    print("Día de la semana: Sábado")
elif numero_dia == 7:
    print("Día de la semana: Domingo")
else:
    print("Error: Ingrese un número válido del 1 al 7.")