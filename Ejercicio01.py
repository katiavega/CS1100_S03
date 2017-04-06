cat1="Strong acid"
cat2="Weak acid"
cat3="Neutral"
cat4="Weak base"
cat5="Strong base"
cat6="desconocida"

ph =int(input("Ingrese el pH: "))

if  ph>=0 and ph <=4:
    print("El tipo de solución es: ", cat1)
elif ph>=5 and ph <=6:\
    print("El tipo de solución es: ", cat2)
elif ph==7:
    print("El tipo de solución es: ", cat3)
elif ph>=8 and ph <=9:
    print("El tipo de solución es: ", cat4)
elif ph>=10 and ph <=14:
    print("El tipo de solución es: ", cat5)
else:
    print("El tipo de solución es : ", cat6)
    print("...Fin del programa...")
