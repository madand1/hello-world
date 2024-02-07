#EJercicio 15

'''
Dadas dos variables numéricas A y B,
que el usuario debe teclear,
se pide realizar un algoritmo que 
intercambie los valores de ambas 
variables y muestre cuanto
valen al final las dos variables.
'''


variable_a = float (input("Dame la primera variable :"))

variable_b = float (input ("Dame la segunda variable :"))
#Metemos el valor de la primera variable en la segunda variable , con una varibale temporal (temp), para almacenar el valor de a antes de realizar el cambio. Asigno el valor de a= b y el valor de la variable temp a B.
temp = variable_a

variable_a = variable_b

variable_b = temp

print ("Aqui tienes las variable a  :", variable_a)

print ("Aqui tienes la variable b :", variable_b)