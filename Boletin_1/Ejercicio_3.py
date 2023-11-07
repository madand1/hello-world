# Ejercicio 3
## Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

#para usar la raiz cuadrada es hay que importar la libreria math, tal que asi
import math

# Le pido al usuario los datos 
cateto_1 = float (input("Dame la medida del primer cateto"))
cateto_2 = float (input("Dame la medida del segundop cateto"))

hipotenusa = math.sqrt((cateto_1)**2 * (cateto_2)**2)

print ("Aqui tiene la medida de la hipotenusa :" , hipotenusa)