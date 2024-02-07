numero = int(input("Ingrese un número: "))
diccionario = {}

for i in range(1, numero + 1):
    diccionario[i] = i ** 2

print(diccionario)
