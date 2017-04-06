print ("Ingrese fecha de nacimiento:")
dia  = int(input("Ingrese dia:"))
mes  = int(input("Ingrese mes:"))
anio = int(input("Ingrese año:"))

if anio % 2 == 0:   # Es año PAR 
    if mes>=1 and mes<=3: # Ene,Feb ó Mar 
        if dia % 2 ==0: #Día PAR 
            print("Tu piedra preciosa es: ", "Rubí")
        else:           #Día IMPAR 
            print("Tu piedra preciosa es: ", "Zafiro")
    elif mes>=4 and mes<=6:
        # Abr, May, Jun 
        if dia % 2 ==0: #Día PAR 
            print("Tu piedra preciosa es: ", "Diamante")
        else: # Día IMPAR 
            print("Tu piedra preciosa es: Turmalina")
    elif mes>=7 and mes<=9:# Jul, Ago, Set 
        if dia % 2 == 0: #Día PAR 
            print("Tu piedra preciosa es: ", "Turquesa")
        else:           #Día IMPAR 
            print("Tu piedra preciosa es: ", "Hematita")
    elif mes>=10 and mes<=12: # Oct, Nov, Dic 
        if dia % 2 ==0: #Día PAR 
            print("Tu piedra preciosa es: ", "Esmeralda")
        else: #Día IMPAR 
            print("Tu piedra preciosa es: ", "Opalo")
else:               # Es año IMPAR  
    if mes>=1 and mes<=3: # Ene,Feb ó Mar 
        if dia % 2 ==0: #Día PAR 
            print("Tu piedra preciosa es: ", "Lapizlázuri")
        else: #Día IMPAR 
            print("Tu piedra preciosa es: ", "Topacio")
    elif mes>=4 and mes<=6: # Abr, May, Jun 
        if dia % 2 ==0: #Día PAR 
            print("Tu piedra preciosa es: ", "Aguamarina")
        else:          #Día IMPAR 
            print("Tu piedra preciosa es: ", "Rodocrosita")
    elif mes>=7 and mes<=9: # Jul, Ago, Set 
        if dia % 2 ==0: #Día PAR 
            print("Tu piedra preciosa es: ", "Amatista")
        else:           #Día IMPAR 
            print("Tu piedra preciosa es: ", "Peridoto")
    elif mes>=10 and mes<=12: # Oct, Nov, Dic 
        if dia % 2 ==0: #Día PAR 
            print("Tu piedra preciosa es: ", "Ambar")
        else:           #Día IMPAR 
            print("Tu piedra preciosa es: ", "Jade")
print("...Fin del Programa...")
