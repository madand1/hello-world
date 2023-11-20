#ejercicio 5

'''Escribe un programa que pida un nombre de usuario y una contraseña y
 si se ha introducido “pepe” y “asdasd” 
se indica “Has entrado al sistema”, sino se da un error.'''

nombre_usuaario = input('ingrese un nombre de usuario')
contraseña = input('ingrese la contraseña')

if nombre_usuaario == 'pepe' and contraseña =='asdasd' :
    print('Has entrado camarada')

else :
    print('No has entrado en el sistema weon')