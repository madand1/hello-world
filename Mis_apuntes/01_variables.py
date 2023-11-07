# Variables en python 

my_string_variable = "My String variable"

print ( my_string_variable ) 

my_int_variable = 5

print (my_int_variable)

my_int_to_str_variable = str (my_int_variable)
print (my_int_to_str_variable)
print (type (my_int_to_str_variable))

my_bool_variable = False    

print ( my_bool_variable)

# Concatenación de variables en print 
print (my_string_variable, str (my_int_variable), my_bool_variable)
print ("Este es el valor de:" , my_bool_variable)

# Algunas funciones del sistema

print (len(my_string_variable))

# Variables en una sola línea AUNQUE SE PUEDE HACER ES MUY MALA PRÁCTICA
name, surname, alias, age = "Andy", "Gonzalez", "MadAndy", 29

print ("Me llamo:" , name, surname,".My alias es:", alias,".Y mi edad es:" ,age)

# Imputs

name = input('What is your name? ')

age = input("¿Que edad tienes? ")

print (name)

print (age)

# Cambiamos su tipo 
name = 35 
age ="Andy"
print (name)
print (age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address  = 32
print (type (address))