minutos = float(input ("Ingrese el número de minutos: "))
costo_minuto = 0.50
if minutos < 3:
    #dcto = 0
    #minutos_adicionales = 0
    pago_final = minutos * costo_minuto
else:
    dcto = 0.10
    minutos_adicionales = minutos - 3
    pago_final= (3 * costo_minuto) + (minutos_adicionales *dcto)

print ("El pago a realizar es: ", pago_final)



