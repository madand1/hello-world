# Ejercicio 8

'''Un vendedor recibe un sueldo base mas un 
un 10% extra por comision de sus ventas
, el vendedor desea saber cuanto dinero
obtendra por concepto de comisiones por las
tres ventas que realiza en el mes y el 
total que recibira en el mes tomando en cuenta
su sueldo base y comisiones'''

sueldo_base = float (input("Dame el sueldo base"))

venta1 = float (input ("Dame el dinero de la venta 1"))
venta2 = float (input ("Dame el dinero de la venta 2"))
venta3 = float (input ("Dame el dinero de la venta 3"))

Comision1 = (venta1 * 0.10)

Comision2 = (venta2 * 0.10)

Comision3 = (venta3 * 0.10)

total = sueldo_base + Comision1 + Comision2 + Comision3

print ("El sueldo total de este mes seria : ", total)

