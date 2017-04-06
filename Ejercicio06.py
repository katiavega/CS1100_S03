nota = float(input("Ingrese nota de sustentación: "))
print("Condición de titulado: ")
if nota >= 18 and nota <=20:
     print ("Excelencia")
elif nota >= 15 and nota <=17:
     print ("Distinción")
elif nota >= 12 and nota <=14:
     print ("Aprobado")
elif nota <= 11:
     print ("Desaprobado")
else:
    print("Nota va de 0 a 20")

