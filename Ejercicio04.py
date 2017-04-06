X = float(input("Ingrese coordenada X: "))
Y = float(input("Ingrese coordenada Y: "))

if X>0 and Y>0:
    print ("Este punto pertenece al cuadrante: ", "I")
elif X>0 and Y<0:
    print ("Este punto pertenece al cuadrante: ", "II")
elif X<0 and Y>0:
    print ("Este punto pertenece al cuadrante: ", "IV")
elif X<0 and Y<0:
    print ("Este punto pertenece al cuadrante: ", "III")
else:
    print ("0,0 se encuentra en el centro del Plano Cartesiano")
print("...Fin del Programa...")
