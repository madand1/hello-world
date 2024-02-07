'''pida un número y calcule su factorial'''

numero = int(input('numero que quieres factorizar'))

factores = []

divisor = 2
while numero > 1:
    while numero % divisor == 0:
        factores.append(divisor) 
        numero /= divisor
    divisor +=1

print(f"los factores de {numero} son {factores}")