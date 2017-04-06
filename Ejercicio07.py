cantidad = int(input ("Ingrese cantidad de artículos a comprar: "))
precio   = float(input("Ingrese precio producto: "))
if cantidad >=100:
    dcto = 0.40
elif cantidad >=25 and cantidad <100:
    dcto = 0.20
elif cantidad >=10 and cantidad <25:
    dcto = 0.10
elif cantidad <10:
    dcto = 0
monto = (cantidad * precio)
pago = monto - (monto *dcto)
print ("Ud. pagará: ", pago, " soles")




