# Ejercicio 9

'''
Una tienda ofrece un descuento del 15% 
sobre el total de la compra y un cliente 
desea saber cuanto deberá 
pagar finalmente por su compra.'''

total_compra = float (input ("Dame el ticket de compra"))

descuento = (total_compra * 0.15)

pago_final = (total_compra - descuento)
print ("Aqui tienesel recibo que debera : ", pago_final)