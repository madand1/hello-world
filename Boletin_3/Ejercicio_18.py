'''Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.
'''
import time

# Solicitar al usuario la duración en segundos del cronómetro
duracion_total = int(input("Introduce la duración en segundos del cronómetro: "))

while duracion_total > 0:
    horas, minutos = divmod(duracion_total, 3600)
    minutos, segundos = divmod(minutos, 60)
    print(f"{horas:02d}:{minutos:02d}:{segundos:02d}", end="\r")
    time.sleep(1)
    duracion_total -= 1

print("\n¡Tiempo finalizado!")


